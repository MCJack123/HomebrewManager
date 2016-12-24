//
//  execute.h
//  Homebrew Manager
//
//  Created by Homework User on 12/13/16.
//  Copyright © 2016 MCJack123. All rights reserved.
//

#include <stdio.h>
#include <dirent.h>
#include "Archives.h" //zip functionality used from Lua Player Plus
#include <3ds/applets/swkbd.h>

void run_Official() {
    printf("\x1b[36mInstall official package\x1b[37m\n\nPress A to select a package, X to type a custom name, or B to exit.\nPlease select from the list below:");
	typedef std::map<std::string, Package>::const_iterator MapIterator;
	/*for (MapIterator iter = packages.begin(); iter != packages.end(); iter++) {
		printf("Key: %s\tValues:\n", iter->first.c_str());
		typedef Package::const_iterator MapIterator2;
		for (MapIterator2 iter2 = iter->second.begin(); iter2 != iter->second.end(); iter2++)
			printf("\tKey: %s\tValue: %s\n", iter2->first.c_str(), iter2->second.c_str());
	}*/
	consoleSelect(&debug);
    int selected = 0;
    while (true) {
        consoleClear();
        int i = 0;
        for (MapIterator it = packages.begin(); it != packages.end(); it++) {
            if (selected - i > 30) continue;
			Package namedd = it->second;
			std::string name = namedd["name"];
			if (i == selected) printf("\x1b[47;30m%s\x1b[40;37m\n", name.c_str());
			else printf("%s\n", name.c_str());
			i++;
            if (selected >= 30 && i - 1 == selected) break;
        }
        hidScanInput();
        u32 iDown = hidKeysDown();
        if (iDown) {
            if (iDown & KEY_DOWN)
                selected = decIntWithMax(selected, packages.size() - 1);
            else if (iDown & KEY_UP)
                selected = incIntWithMax(selected, packages.size() - 1);
            else if (iDown & KEY_B)
                return;
            else if (iDown & KEY_A)
                goto Install;
            else if (iDown & KEY_X) {
                SwkbdState keyboard;
                char* buf;
                swkbdInit(&keyboard, SWKBD_TYPE_NORMAL, 2, 32);
                swkbdSetButton(&keyboard, SWKBD_BUTTON_RIGHT, "Search", true);
                swkbdSetButton(&keyboard, SWKBD_BUTTON_LEFT, "Cancel", false);
                if (swkbdInputText(&keyboard, buf, 32) == SWKBD_BUTTON_LEFT) break;
                debugPrint(buf);
                consoleSelect(&debug);
                if (packages.find(std::string(buf)) != packages.end()) {
                    int j = 0;
                    for (auto lines2 : packages) {
                        if (std::get<1>(lines2) == (packages[std::string(buf)])) {selected = j; goto Install;}
                        j++;
                    }
                } else {
                    consoleSelect(&screen);
                    printf("\x1b[31mError: \x1b[37mPackage not found");
                    consoleSelect(&debug);
                }
            }
        }
		sleep(.08);
    }
Install:
	//D72A-0000-02D5-D7E3
    Package selectedPackage = packages[packnames[selected]];
    consoleClear();
    consoleSelect(&screen);
    printf("\n\n\x1b[33mDownloading package...\x1b[37m");
	if (selectedPackage["location"].find("http://") == std::string::npos) selectedPackage["location"] = "https://raw.githubusercontent.com/MCJack123/HBM-repo/master/files/" + selectedPackage["location"];
	debugPrint(selectedPackage["location"]);
	/*u8 *packageF;
	u32 size;
    if (!httpGet(selectedPackage["location"].c_str(), &packageF, &size, true)) {printf("\n\x1b[31mError: Could not download file!\x1b[37m\n"); sleep(3); return;}
	debugPrint((char*)packageF);
	consoleSelect(&screen);
    printf("\t\x1b[32mDownload complete!\n\x1b[33mExtracting files...");
    FILE *file = fopen("/hbm_pack.hbp", "wb");
    fputs((char*)packageF, file);
    fclose(file);*/
    Zip *zipfile = ZipOpen("/hbm_pack.hbp");
    if (zipfile == NULL) {debugPrint("Could not open zip file"); sleep(3); return;}
    ZipFile *packslip = ZipFileRead(zipfile, "PackingSlip", NULL);
	struct PackingSlip slip = parsePackingSlip(reinterpret_cast<char*>(packslip->data));
    std::string installDir;
    if (slip.type == 0) {
        installDir = "/3ds/" + slip.p3dsxprefix + "/";
        mkdir(installDir.c_str(), 0777);
    } else if (slip.type == 1) {
        if (!dirExists("/cia/")) mkdir("/cia/", 0777);
        installDir = "/cia/";
    } else if (slip.type == 2) {
        installDir = "/3ds/";
    } else {
        printf("\n\x1b[31mError: Homebrew type not recognized!\x1b[37m");
        return;
    }
    for (std::string sfile : slip.files) {
        FILE *fout = fopen(std::string(installDir + sfile).c_str(), "wb");
        ZipFile *inn = ZipFileRead(zipfile, sfile.c_str(), NULL);
        fputs(reinterpret_cast<char*>(inn->data), fout);
        fclose(fout);
    }
    if (slip.type == 1) {
        printf("\n\x1b[36mThe CIA has been copied to /cia. Do you want to install it? (Do not install if you do not have CFW.) Press A to install, or any other key to exit.");
        while (true) {
            hidScanInput();
            u32 lDown = hidKeysDown();
            if (lDown) {
                if (lDown & KEY_A) {
                    printf("\n\x1b[33mInstalling CIA to SD card...");
                    amInit();
                    Handle ciaInstall;
                    AM_StartCiaInstall(MEDIATYPE_SD, &ciaInstall);
					ZipFile *fin;
                    for (std::string ssfile : slip.files) {
                        if (ssfile.find(".cia") != std::string::npos) {
                            fin = ZipFileRead(zipfile, ssfile.c_str(), NULL);
							break;
                        }
                    }
                    FSFILE_Write(ciaInstall, NULL, 0, fin->data, fin->size, FS_WRITE_FLUSH);
                    AM_FinishCiaInstall(ciaInstall);
                    printf("\t\x1b[32mFinished!");
                } else break;
            }
        }
    }
    printf("\x1b[32mThe installation finished! Press any key to exit.\x1b[37m");
    while (true) {
        hidScanInput();
        if (hidKeysDown()) break;
    }
    ZipClose(zipfile);
}

void runManager(int selection) {
    if (selection == 0) run_Official();
    //else if (selection == 1) run_Unofficial();
    //else if (selection == 3) run_MakeZip();
    //else run_External();
}
