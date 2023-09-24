import os
import shutil

WORKDIR = os.path.abspath(__file__).replace(os.path.basename(__file__), '')

dirs = os.listdir()
moddirs = []
for x in range(len(dirs)):
    if dirs[x][0] == '@':
        moddirs.append(dirs[x])
for t in range(len(moddirs)):
    keyfile = os.listdir(f"{moddirs[t]}\\Keys")[0]
    if not(os.path.isfile(f"keys\\{keyfile}")):
        print(f"Копирвание ключа {keyfile}")
        shutil.copyfile(f"{moddirs[t]}\\Keys\\{keyfile}", f"keys\\{keyfile}")
modlist = ""
outputstr = ""
for i in range(len(moddirs)):
    modlist = modlist + str(moddirs[i]) + ";"
    outputstr = outputstr + str(moddirs[i]) + " "
command = f'start "" "DayZServer_x64.exe" -config=serverDZ.cfg -cpuCount=4 -port=2302 -profiles=profiles "-mod={modlist}" -dologs -adminlog -netlog -freezecheck "-BEpath={WORKDIR}\\battleye";'
print(command)
os.system(command)