//
//  main.cpp
//  Homebrew Manager
//
//  Created by Jack Bruienne on 1/15/16.
//  Copyright © 2016 MCJack123. All rights reserved.
//

#include "utils.h"
#include "parser.h"
#include "execute.h"

u8 *packagesF;
u32 size2;

int main(int argc, char* argv[]) {
	gfxInitDefault();
	httpcInit(0);
	//Initialize console on top screen. Using NULL as the second argument tells the console library to use the internal console structure as current one
	consoleInit(GFX_TOP, &screen);
	consoleInit(GFX_BOTTOM,&debug);
	consoleSelect(&screen);
	APT_CheckNew3DS(&consoletype);
	printf("Console type: %s\n",consoletype?"New 3DS. Good job!":"Old 3DS. This may be a bit slow.");
	sleep(1);
    debugPrint("Downloading packages file");
        debugPrint("Starting download");
        httpGet("http://raw.githubusercontent.com/MCJack123/HBM-repo/master/Packages", &packagesF, &size2, false);
        debugPrint((const char*)packagesF);
        parsePackagesFile(std::string((char*)packagesF));
        debugPrint("Done.");
    int selection = 0;
    consoleSelect(&screen);
    while (aptMainLoop()) {
        consoleClear();
        printf("\x1b[36mHomebrew Manager for 3DS by JackMacWindows\x1b[37m\nUse the D-pad to navigate, A to select, or start to exit.\nPlease select an option:\n\n %s Install official package\n %s Add/install unofficial repository\n %s Download other zip file\n %s Create package", selection==0?"*":" ", selection==1?"*":" ", selection==2?"*":" ", selection==3?"*":" ");
        hidScanInput();
        u32 kDown = hidKeysDown();
        if (kDown) {
            if (kDown & KEY_DOWN) selection = incIntWithMax(selection, 3);
            else if (kDown & KEY_UP) selection = decIntWithMax(selection, 3);
            else if (kDown & KEY_A) {
                consoleClear();
                printf("\n\nSelected option: ");
                runManager(selection);
				consoleSelect(&screen);
            }
            else if (kDown & KEY_START) goto End;
        }
        gfxFlushBuffers();
        gfxSwapBuffers();
        //Wait for VBlank
        gspWaitForVBlank();
        sleep(.075);
    }
End:
	// Exit services
    httpcExit();
    gfxExit();
	return 0;
}
