from dataclasses import replace
import os
import shutil

robloxpath = os.path.expandvars(r'%LOCALAPPDATA%/Roblox/Versions')

files = os.listdir(robloxpath)
try: 
    files.remove('RobloxStudioLauncherBeta.exe')
except:
    print("what?")

print(r'%LOCALAPPDATA%/Roblox/Versions')
path = "C:/Users/" + os.getlogin() + "/AppData/Local/Roblox/Versions/" + files[0] + "/content/sounds/ouch.ogg"
print(path)
dir_path = os.path.dirname(os.path.realpath(__file__))

shutil.move(dir_path + "/files/ouch.ogg", path)
#version-9045f70ea522489c\content\sounds\ouch.ogg
#version-9045f70ea522489c/content/sounds/ouch.ogg