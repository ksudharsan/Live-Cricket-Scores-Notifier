from bs4 import BeautifulSoup
import pynotify
import gtk.gdk
import urllib2 
import time
import socket

REMOTE_SERVER = "www.google.com"
def is_connected():
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(REMOTE_SERVER)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False

def get_scores():

	url = urllib2.urlopen("http://www.espncricinfo.com/ci/engine/match/index.html?view=live")
	content = url.read()
	pynotify.init("CRIC_SCORES")
	soup = BeautifulSoup(content,"lxml")
	data = soup.findAll("section", {"class": "matches-day-block"})

	totdata=""
	count=0
	for match in data:
		
		current=match.findAll("section",{"class": "default-match-block","data-matchstatus": "current"})
		if count == 2: 
			break
		for matches in current:			
			info = matches.findAll("div", {"class": "innings-info-1"})
			for val in info:
				totdata += val.text
			info = matches.findAll("div", {"class": "innings-info-2"})
			for val in info:
				totdata+=val.text
			totdata+= "*************************************"
		count+=1

	return totdata

while True:	
	if is_connected():
		new_val=get_scores()	
		pynotify.Notification("Live Cricket Scores",""+new_val).show()	
		time.sleep(60)

