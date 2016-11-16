#!/usr/bin/env python
import urllib2;
from bs4 import BeautifulSoup
import re
import csv
import time
import StringIO
import gzip

mt_url = 'https://tp.m-team.cc/torrents.php'

f = open('mt.cookie','r')
mt_cookie = f.read().strip('\n') #get cookie from file and remove the enter 
f.close()

mt_header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
    'Cookie' : mt_cookie,
    'Accept-Encoding' : 'gzip'
}
mt_req = urllib2.Request(mt_url,headers=mt_header)
mt_pages = urllib2.urlopen(mt_req)
#print(mt_pages.info().get('Content-Encoding'))

if mt_pages.info().get('Content-Encoding') == 'gzip':
    #print mt_pages.read()
    buf = StringIO.StringIO(mt_pages.read())
    f = gzip.GzipFile(fileobj=buf)
    mt_html = f.read()
else:
    mt_html = mt_pages.read()


print mt_html


mt_soup =  BeautifulSoup(mt_html, "lxml")
mt_fulltable = mt_soup.find("table",{"class" : "torrents"})
td_th = re.compile('t[dh]')

for row in mt_fulltable.find_all("tr",{"class":"sticky_top"},recursive=False):
    #cells = row.find_all("td")
    #if cells[1].find("table",{"class":"torrentname"}):
        #torrent_table = cells[1].find("table",{"class":"torrentname"})
    #torrent_table = cells[1].find("table",{"class":"torrentname"})
    #print torrent_table
    #print cells
    torrent_table = row.find("table",{"class":"torrentname"})
    torrent_other = row.find_all("td",{"class":"rowfollow"})
    size = torrent_other[3].find(text=True)
    print torrent_table
    print size









#rows = mt_fulltable.find_all("tr")
##print rows
#cells0 = BeautifulSoup(rows[1],"lxml").find_all("td")
#torrent_table0 = cells0.find("table",{"class":"torrentname"})
#print torrent_table0
##
##cells1 = rows[1].find_all("td")
##torrent_table1 = cells1.find("table",{"class":"torrentname"})
##print torrent_table1
##cells2 = rows[2].find_all("td")
##torrent_table2 = cells2.find("table",{"class":"torrentname"})
##print torrent_table2
#









