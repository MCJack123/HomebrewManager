//
//  parser.h
//  Homebrew Manager
//
//  Created by Homework User on 12/13/16.
//  Copyright © 2016 MCJack123. All rights reserved.
//


#include <vector>
#include <string>
#include <sstream>

typedef std::map<std::string, std::string> Package;
std::map<std::string, Package> packages;
std::vector<std::string> packnames;

struct PackingSlip {
    std::string name;
	std::string p3dsxprefix;
    int type;
    std::vector<std::string> files;
};

std::vector<std::string> doSegment(const std::string& str,
                                      const std::string& delimiter = "\n") {
    std::vector<std::string> strings;

    std::string::size_type pos = 0;
    std::string::size_type prev = 0;
    while ((pos = str.find(delimiter, prev)) != std::string::npos)
    {
        strings.push_back(str.substr(prev, pos - prev));
        prev = pos + 1;
    }

    // To get the last substring (or only, if delimiter is not found)
    strings.push_back(str.substr(prev));

    return strings;
}

Package parsePackage(std::string pack) {
    Package retval;
    std::vector<std::string> packSplit = doSegment(pack);
    for (std::string segment : packSplit) {
		debugPrint("Parsing " + segment);
		if (segment == "") continue;
        retval[segment.substr(0, segment.find(":"))] = segment.substr(segment.find(":") + 1);
    }
    return retval;
}

void parsePackagesFile(std::string file) {
    std::vector<std::string> packs = doSegment(file, "}\n");
    int i = 0;
    for (std::string segment : packs) {
		if (segment == "\n" || segment == "") continue;
		debugPrint("Going " + segment);
        packages[segment.substr(0, segment.find("{"))] = parsePackage(segment.substr(segment.find("{") + 1));
		debugPrint("Writing receipt");
        packnames.push_back(segment.substr(0, segment.find("{")));
        i++;
    }
}

struct PackingSlip parsePackingSlip(char *slip) {
    struct PackingSlip retval;
    std::vector<std::string> lines = doSegment(std::string(slip));
    bool doingFiles = false;
    for (std::string segment : lines) {
        if (doingFiles) {
            if (segment == "}") {doingFiles = false; continue;}
            retval.files.push_back(segment);
        } else {
            if (segment == "\n" || segment == "") continue;
            std::string key, value;
            key = segment.substr(0, segment.find(":"));
            value = segment.substr(segment.find(":") + 1);
            if (key == "name") retval.name = value;
			else if (key == "type") retval.type = std::atoi(value.c_str());
            else if (key == "files") doingFiles = true;
			else if (key == "prefix") retval.p3dsxprefix = value;
        }
    }
    return retval;
}
