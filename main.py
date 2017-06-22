'''
    take the url factor out of a html
__author__ = ''

'''

# -*- coding: utf-8 -*-

import urllib
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import re
#from os import listdir
# from os.path import isfile, join,exists
DMMSEARCH = "http://www.dmm.co.jp/search/=/searchstr=TESTTEST/analyze=V1EBCFcEUAU_/" \
            "n1=FgRCTw9VBA4GF1RWR1cK/n2=Aw1fVhQKX0BdC0VZX2kCQQU_/sort=ranking/"

TARGETDIR = "z:\\video\\00_AV"
#http://www.dmm.co.jp/search/=/searchstr=jbs007/analyze=V1EBClcEUQU_/n1=FgRCTw9VBA4GF1RWR1cK/n2=Aw1fVhQKX0BdC0VZX2kCQQU_/sort=ranking/

def readFile(file_name):

    f = open(file_name)
    in_doc = f.read()
    f.close()
    return in_doc

def getURL(in_doc):

    html_doc = in_doc
    soup = BeautifulSoup(html_doc, 'html.parser')

    result = soup.findAll(href=re.compile(".*iff"))
    rtn = []
    try:
        for r in result:
            rtn.append(str(r).split('"')[1])
        return rtn
    except BaseException:
        return ""


def checkAvCode(avCode, i='*'):
    # match the pattern :
    # starts with 3~5 letters and followed by numbers with or without Hyphen in front
    regex = r'\w{2,5}\D*\d{1,5}\.(.*)$'
    if not(re.match(regex, avCode)):
        #print avCode + " matches"

        print ("No." + str(i) + " " + avCode + " not matches!")
        return False
    return True



#def readFileIntoList(path):
    #scratch file name into a list under a certain dir
    #return [f for f in listdir(path) if isfile(join(path,f))]

def transferUrl():
    send_url = "http://www.linkexpander.com/get_url.php"
    short_url = "http://ift.tt/2s5RqG4"
    param = {"url": short_url, }
    page_text = ""
    param = urllib.parse.urlencode(param).encode(encoding='ascii')
    with urllib.request.urlopen(url=send_url, data=param) as page:
        for line in page.readlines():
            page_text = page_text + line.decode('utf-8')
    print(page_text)

    return 0

# print (getURL(readFile('digist_text')))
transferUrl()
# for ele in readFileIntoList(TARGETDIR):
#         if checkAvCode(str(ele)):
#             avCode = str(ele).split(".")[0]
#             coverUrl = getAccurateUrl(avCode)
#             if coverUrl != "":
#                 coverUrl = getCoverImage(coverUrl)
#                 downLoadAs = TARGETDIR + '\\' + avCode + '.jpg'
#                 # if file already exists
#                 if exists(downLoadAs):
#                     print ('Cover for ' + avCode + ' is already exists')
#                 else:
#                     print ('[cc]'+coverUrl)
#                     if coverUrl != "":
#                         data = urllib.request.urlretrieve(coverUrl, downLoadAs)
#                         print ("Cover for " + avCode + " OK!\n")
#                     else:
#                         print ("Cover for " + avCode + " N/A \n")
#             else:
#                 print ("Not found the cover for " + avCode + "\n")
#                 print ("test is not a null is not cally")

