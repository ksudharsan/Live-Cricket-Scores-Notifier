import os
import re
import subprocess
from os.path import expanduser

commands=[("sudo rm " + expanduser("~")+"/.config/autostart/cric-notify.desktop","deleting files"),("sudo rm -r /usr/share/cric-notify","deleting files")]

for command,text in commands:
    #print command
    print text
    p=subprocess.Popen(command,shell=True)
    p.wait()
    

print "Module successfully Uninstalled."
print "\n"
print "Please restart."
