# ######################=
# ## WowLoader v1.0
# ## For MoonScript
# #######################=
#######################=

import os
import time
import sys

modfolder_path = "mods"
cmd = None
out = False

def autoexec():
    # Checks for mods folder

    if os.path.isdir(modfolder_path):
        pass # Mod folder exists
    else:
        os.system('mkdir mods') # Creates mods folder

    python_file_list = get_python_files_in_folder(modfolder_path)
    modlist = python_file_list

def cmds():
    # Mod loading stuff
    
    if cmd[:4] == "mod ":
        exec(f"from mods import {cmd[4:].translate(str.maketrans("", "", "\""))}\n{cmd[4:].translate(str.maketrans("", "", "\""))}.__modStart()")
    elif cmd[:8] == "wowtools":
        # WoWTools 1.0 Shell
        # To run just open WoWTools.moon
        print("=###############=")
        print("| WoWTools v1.0 |")
        print("=###############=\n")
        print("Booting . . .")
        print("WoWTools Shell\n")
        while True:
            wowsh = input("⟫ ")
            if wowsh == "exit":
                sys.exit()
            elif wowsh[:3] == "rm ":
                os.system(f"del mods\\{wowsh[3:]}.py")
                print("Removed.")
            elif wowsh[:5] == "init ":
                print("Starting...")
                exec(f"from mods import {wowsh[5:].translate(str.maketrans("", "", "\""))}\n{wowsh[5:].translate(str.maketrans("", "", "\""))}.__modStart()")
            elif wowsh == "wowget":
                print("Error: \"Not ready\".") 
                print("Note: WowGet is in the works.")
            else:
                pass
    else:
        out = True
