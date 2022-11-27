#!/usr/bin/python3 
#Save easily any directory in a tar archive
import os 
import re
import sys
dir_to_save = input("[>] Which directory do you want to save ?")
if(os.path.exists(dir_to_save)):
    print("[~] Found directory "+dir_to_save)
    if(re.match("(etc)|(root)|(tmp)|(bin)|(proc)|(sbin)/gmi",dir_to_save)):
        print("[!] Your directory name is strange, I will not save it for you")
        sys.exit()
    else:
        saveDir=system("mktemp -d")
        time=system("date +%s")
        print("[~] Saving to "+saveDir)
        os.system("tar cvf "+saveDir+"/save_"+time+".tar "+dir_to_save)
else:
    print("[!] You specified a directory that doesn't exist...")