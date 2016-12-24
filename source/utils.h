#ifndef __ASCII3DS_UTILS_H_
#define __ASCII3DS_UTILS_H_
#include <sys/types.h>
#include <sys/stat.h>
#include <cstdio>
#include <cstring>
#include <malloc.h>
#include <fstream>
#include <string>
#include <sstream>
#include <cstdlib>
#include <tuple>
#include <map>
#include <sys/unistd.h>
#ifndef _SYS_UNISTD_H_
#include <unistd.h>
#endif
#include <3ds.h>
#include <3ds/services/csnd.h>
#include "certs/cybertrust.h"
#include "certs/digicert.h"
//#define CHECK(val, msg) if (val != 0) { debugPrint(formatErrMessage(msg, val).c_str()); return false; }
#define __LUA_SOUND_ // is currently unsafe, now used to turn sound off
#define __DEBUG // will enable debugPrint() --v--

void debugPrint(const char * debugText); // this function
#ifndef __LUA_SOUND_
#include "sound.h"
//#else
//#include "luaSound.hpp"
#endif
PrintConsole screen, debug;
bool consoletype;
#ifndef __LUA_SOUND_
themeSound sound1;
themeSound sound2; // backup just in case its needed
#endif

std::map<u32, const char *> httpResponses = {
	{100, "Continue"},
	{101, "Switching Protocols"},
	{102, "Processing"},
	{200, "OK"},
	{201, "Created"},
	{202, "Accepted"},
	{203, "Non-Authoritative Information"},
	{204, "No Content"},
	{205, "Reset Content"},
	{206, "Partial Content"},
	{207, "Multi-Status"},
	{208, "Already Reported"},
	{226, "IM Used"},
	{300, "Multiple Choices"},
	{301, "Moved Permanently"},
	{302, "Found"},
	{303, "See Other"},
	{304, "Not Modified"},
	{305, "Use Proxy"},
	{306, "Switch Proxy"},
	{307, "Temporary Redirect"},
	{308, "Permanent Redirect"},
	{400, "Bad Request"},
	{401, "Unauthorized"},
	{402, "Payment Required"},
	{403, "Forbidden"},
	{404, "Not Found"},
	{405, "Method Not Allowed"},
	{406, "Not Acceptable"},
	{407, "Proxy Authentication Required"},
	{408, "Request Time-out"},
	{409, "Conflict"},
	{410, "Gone"},
	{411, "Length Required"},
	{412, "Precondition Failed"},
	{413, "Payload Too Large"},
	{414, "URI Too Long"},
	{415, "Unsupported Media Type"},
	{416, "Range Not Satisfiable"},
	{417, "Expectation Failed"},
	{418, "I'm a teapot"},
	{421, "Misdirected Request"},
	{422, "Unprocessable Entity"},
	{423, "Locked"},
	{424, "Failed Dependency"},
	{426, "Upgrade Required"},
	{428, "Precondition Required"},
	{429, "Too Many Requests"},
	{431, "Request Header Fields Too Large"},
	{451, "Unavailable For Legal Reasons"},
	{500, "Internal Server Error"},
	{501, "Not Implemented"},
	{502, "Bad Gateway"},
	{503, "Service Unavailable"},
	{504, "Gateway Time-out"},
	{505, "HTTP Version Not Supported"},
	{506, "Variant Also Negotiates"},
	{507, "Insufficient Storage"},
	{508, "Loop Detected"},
	{510, "Not Extended"},
    {511, "Network Authentication Required"}
};

void debugPrint(const char * debugText) { // here
#ifdef __DEBUG
    consoleSelect(&debug);
    printf("%s\n", debugText);
    consoleSelect(&screen);
#endif
}

void debugPrint(std::string debugText) { // here
#ifdef __DEBUG
    consoleSelect(&debug);
    printf("%s\n", debugText.c_str());
    consoleSelect(&screen);
#endif
}

std::string formatErrMessage(const char* msg, const Result& val) {
	std::stringstream os;
	os << msg << "\nRet code: " << val;
	return os.str();
}

static inline bool CHECK(int val, const char * msg) {if (val != 0) { debugPrint(formatErrMessage(msg, val).c_str()); return false; } return true;}

int incIntWithMax(int& addend, int maximum, int minimum = 0) {
    if (addend == maximum) addend = minimum;
    else addend++;
    return addend;
}

int decIntWithMax(int& addend, int maximum, int minimum = 0) {
    if (addend == minimum) addend = maximum;
    else addend--;
    return addend;
}

template <class T>
void sleep(T time) {usleep(time * 1000000);}

inline bool fexists (const std::string& name) {
    return ( access( name.c_str(), F_OK ) != -1 );
}

void clearAll() {
    consoleSelect(&debug);
    consoleClear();
    consoleSelect(&screen);
    consoleClear();
}

bool dirExists(const char *path)
{
    struct stat info;
    
    if(stat( path, &info ) != 0)
        return false;
    else if(info.st_mode & S_IFDIR)
        return true;
    else return false;
}

unsigned int makeUnsigned_i(int unsignee) {
    if (unsignee < 0) return 0;
    else return unsignee;
}

bool httpGet(const char* url, u8** buf, u32* size, const bool verbose) {
	httpcContext context;
	if (!CHECK(httpcOpenContext(&context, HTTPC_METHOD_GET, (char*)url, 0), "Could not open HTTP context")) return false;
	// Add User Agent field (required by Github API calls)
	if (!CHECK(httpcAddRequestHeaderField(&context, (char*)"User-Agent", (char*)"Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7498.US"), "Could not set User Agent")) return false;

	// Add root CA required for Github and AWS URLs
	CHECK(httpcAddTrustedRootCA(&context, cybertrust_cer, cybertrust_cer_len), "Could not add Cybertrust root CA");
	CHECK(httpcAddTrustedRootCA(&context, digicert_cer, digicert_cer_len), "Could not add Digicert root CA");

	if (!CHECK(httpcBeginRequest(&context), "Could not begin request")) return false;

	u32 statuscode = 0;
	if (!CHECK(httpcGetResponseStatusCode(&context, &statuscode), "Could not get status code")) return false;
	if (statuscode != 200) {
		// Handle 3xx codes
		if (statuscode >= 300 && statuscode < 400) {
			char newUrl[1024];
			if (!CHECK(httpcGetResponseHeader(&context, (char*)"Location", newUrl, 1024), "Could not get Location header for 3xx reply")) return false;
			if (!CHECK(httpcCloseContext(&context), "Could not close HTTP context")) return false;
			return httpGet(newUrl, buf, size, verbose);
		}
		debugPrint(formatErrMessage(std::string("Non-200 status code: " + std::string(httpResponses[statuscode])).c_str(), statuscode).c_str());
        return false;
	}

	u32 pos = 0;
	u32 dlstartpos = 0;
	u32 dlpos = 0;
	Result dlret = HTTPC_RESULTCODE_DOWNLOADPENDING;

	if (!CHECK(httpcGetDownloadSizeState(&context, &dlstartpos, size), "Could not get file size")) return false;
	
	*buf = (u8*)std::malloc(*size);
    if (*buf == NULL) {debugPrint(formatErrMessage("Could not allocate enough memory", *size).c_str()); return false;}
	std::memset(*buf, 0, *size);
	printf("%lu ", *size);
	while (pos < *size && dlret == (s32)HTTPC_RESULTCODE_DOWNLOADPENDING)
	{
		u32 sz = *size - pos;
		printf("%lu %lu ", sz, pos);
		dlret = httpcReceiveData(&context, *buf + pos, sz);
		if (!CHECK(httpcGetDownloadSizeState(&context, &dlpos, NULL), "Could not get file size")) return false;
		pos = dlpos - dlstartpos;
		printf("%lu %lu %lu ", dlpos, sz, pos);
		if (verbose) {
            consoleSelect(&debug);
            consoleClear();
			printf("Download progress: %lu / %lu", dlpos, *size);
			gfxFlushBuffers();
		}
	}
	
	if (verbose) {
		printf("\n");
	}

	if (!CHECK(httpcCloseContext(&context), "Could not close HTTP context")) return false;
    return true;
}

/*if (num <= (max - min) / 2) return max - (num - min); else return min + (((max - min) / 2) - num);*/
#define flipInt(n, x, m) (n<=(x-m)/2?x-(n-m):m+(((x-m)/2)-n))
//inline int flipInt(int n, int x, int m = 0) {return (n<=(x-m)/2?x-(n-m):m+(((x-m)/2)-n));}

#endif
