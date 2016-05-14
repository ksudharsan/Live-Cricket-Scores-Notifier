import os
import re
import subprocess
from os.path import expanduser

commands=[("sudo mkdir /usr/share/cric-notify","creating directory structure"),("sudo mkdir /usr/share/cric-notify/src/","creating directory structure"),("sudo cp src/live-scores.py /usr/share/cric-notify/src/live-scores.py","Copying files"),("sudo cp cric-notify.desktop " + expanduser("~")+"/.config/autostart/cric-notify.desktop","copying files")]

for command,text in commands:
    #print command
    print text
    p=subprocess.Popen(command,shell=True)
    p.wait()
    

print "Module successfully added."
print "Please restart to get notifications."


