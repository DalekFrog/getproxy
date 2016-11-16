#!/usr/bin/env python

import urllib2;
#from BeautifulSoup import BeautifulSoup;
from bs4 import BeautifulSoup
import re
import csv
import time
import StringIO
import gzip

#arr = []
avali_proxy = []
for i in range(10):
    #print i
    requrl = "http://www.kuaidaili.com/free/outha/" + str(i+1)
    # http://cn-proxy.com/
    print requrl
    #h = {'User-Agent': 'Mozilla/5.0'}
    h = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',
        'Referer' : 'http://www.kuaidaili.com/free/outha/20/',
        'Accept-Encoding' : 'gzip'
    }
    #req = urllib2.Request(requrl,headers=h)
    req = urllib2.Request(requrl)
    pages = urllib2.urlopen(req)
    print(pages.info().get('Content-Encoding'))

    if pages.info().get('Content-Encoding') == 'gzip':
        print pages.read()
        buf = StringIO.StringIO(pages.read())
        f = gzip.GzipFile(fileobj=buf)
        html = f.read()

    html = pages.read()
    #compresseddata =  pages.read()
    #compressedstream = StringIO.StringIO(compresseddata)
    #gzipper = gzip.GzipFile(fileobj=compressedstream)
    #html = gzipper.read()
    print html

    soup =  BeautifulSoup(html, "lxml")
    table = soup.find("table",{"class" : "table table-bordered table-striped"})

    #print table
    IP_ADDR = ""
    PORT = ""
    TYPE = ""
    LOCATION = ""
    SPEED = ""
    
    #f = open('proxy.csv', 'w')
    #csv_writer = csv.writer(f)
    td_th = re.compile('t[dh]')
    
    arr = []
    for row in table.findAll("tr"):
        cells = row.findAll(td_th)
        if len(cells) == 7:
            IP_ADDR = cells[0].find(text=True)
            #if not IP_ADDR:
            #    continue
            PORT = cells[1].find(text=True)
            TYPE = cells[3].find(text=True)
            LOCATION = cells[4].find(text=True)
            SPEED = cells[5].find(text=True)
    
            #print("%s:%s" %(IP_ADDR,PORT))
            proxy_addr = IP_ADDR + ":" +  PORT
            print proxy_addr
            arr.append(proxy_addr)
    time.sleep(3)
    avali_proxy.extend(arr[1:])

     
            #csv_writer.writerow([ x.encode('utf-8') for x in [IP_ADDR, PORT, TYPE, LOCATION, SPEED]])
    
print avali_proxy
print len(avali_proxy)

#f.close()







#http://www.jianshu.com/p/2c2781462902
#https://my.oschina.net/jhao104/blog/647308

#def parse_html(text): 
#    soup = BeautifulSoup(text, "lxml", from_encoding="UTF-8")
#    #target = soup.find(id="historyTable").find('table').findAll('tr')
#    target = soup.find(id="list").find('table').findAll('tr')
#    results = []
#    rec = []
#    for tr in target[1:]:
#        tds = tr.findAll('td')
#        build_no = str(tds[1].span.string.strip())
#        patch = str(tds[0].a.string)
#        status_node = tds[2].find('a')
#        status = str(status_node.find('span').string)
#        status_link = '%s/%s'%(TEAMCITY_HOME, status_node.attrs['href'])
#        started = str(tds[5].string.replace(u'\xa0', ' '))
#
#        print '-'*10
#        print '%s\t'%patch,
#        print '%s\t'%build_no,
#        print '%s\t'%status,
#        print '%s\t'%started
#
#parse_html(html)
