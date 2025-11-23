import os
import time
import sys


modfolder_path = "mods"
cmd = None
out = False

modlist = ""

def runMod(mod):
    exec(f"""from mods import {mod}
    {mod}.__modStart()
    """)

def get_python_files_in_folder(folder_path):
    """
    Retrieves a list of Python file names from the specified folder.

    Args:
        folder_path (str): The path to the folder to scan.

    Returns:
        list: A list containing the names of all Python files in the folder.
    """
    python_files = []
    try:
        # List all entries in the given directory
        for item in os.listdir(folder_path):
            # Construct the full path to the item
            full_item_path = os.path.join(folder_path, item)
            # Check if the item is a file and ends with '.py'
            if os.path.isfile(full_item_path) and item.endswith('.py'):
                python_files.append(item)
    except FileNotFoundError:
        print(f"Error: Folder '{folder_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return python_files

# Example usage:  # Replace with the actual path to your folder

# ######################=
# ## WowLoader v1.0
# ## For MoonScript
# #######################=
#######################=

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
