'''
    take the url factor out of a html
__author__ = ''

'''

# -*- coding: utf-8 -*-
import urllib
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import re
#from os import listdir
# from os.path import isfile, join,exists

TARGETDIR = "digist_text"
FIND_STR = ".*ift\.tt"
LOGERFILE = "dslog.txt"

#http://www.dmm.co.jp/search/=/searchstr=jbs007/analyze=V1EBClcEUQU_/n1=FgRCTw9VBA4GF1RWR1cK/n2=Aw1fVhQKX0BdC0VZX2kCQQU_/sort=ranking/

# write the file name to a log file
def logger(dl_URLs):
    f = open(LOGERFILE,'a')
    f.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\r')
    for dl in dl_URLs:
        f.write(dl+'\r')
    f.write("---------------" +'\r')
    f.close()
    return 0

# clear the src file, with time stamp left
def clearSrcFile():
    f = open(TARGETDIR,'w')
    f.write('import completed @ ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S')+'\r')
    return 0

# read the html code from a certain file
def readSrcFile(file_name):
    f = open(file_name)
    in_doc = f.read()
    f.close()
    return in_doc

# get the download url from src file
def getURL(in_doc):
    soup = BeautifulSoup(in_doc, 'html.parser')
    result = soup.findAll(href=re.compile(FIND_STR))
    rtn = []
    try:
        for r in result:
            rtn.append(str(r).split('"')[1])
        return rtn
    except BaseException:
        return ""

# expand the short URLs to real URLs
def expandLinks(origin_URL):
    SHORT_URL_EXPANDER = "http://www.linkexpander.com/get_url.php"
    rst = []
    for iu in origin_URL:
        #do transfoer
        #iu = 'https://goo.gl/884XZo'
        param = {"url": iu, }
        page_text = ""
        param = urllib.parse.urlencode(param).encode(encoding='ascii')
        print ("linking..."+SHORT_URL_EXPANDER)
        try:
            with urllib.request.urlopen(url=SHORT_URL_EXPANDER, data=param) as page:
                for line in page.readlines():
                    page_text = page_text + line.decode('utf-8')
            #print(page_text)
            ou = page_text.split('<br />')[0]
            rst.append(ou)
            print (iu + " => " + ou + '\r')
        except BaseException:
            rst.append("error")
    return rst

# main
urls_in_file = getURL(readSrcFile(TARGETDIR))
expandLinks(urls_in_file)
#logger(u)
#clearSrcFile()
