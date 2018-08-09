#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup




def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    print(' Beautiful Soup Web Scrape  ')

    #url = urllib.request.urlopen('http://pythonprogramming.net')
    '''
    url = 'http://pythonprogramming.net'
    values = {'s': 'basic',
                'submit' : 'search'}

    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url,data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    print(respData)
    '''
    
    try:
        url =urllib.request.urlopen('https://www.google.com/search?q=test')
        #url =urllib.request.urlopen('http://pytonprogramming.net')
        #url =urllib.request.urlopen('http://www.envelopwireless.com')
        headers ={}
        headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.1 Safari/605.1.15'
        
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read()

        saveFile = open('noheaders.txt','w')
        saveFile.write(str(respData.read()))
        saveFile.close()

    except Exception as e:
        print(str(e))
        print('buttfuck')


    
    #print(web_page.read())    
    

   
    print ('  ')
            
    print("!!!!" +  'Done')    

   

if __name__ == '__main__': main()
