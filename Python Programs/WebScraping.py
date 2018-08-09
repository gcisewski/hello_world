#
# Example file for working with conditional statements
#
import sys
import fileinput
import filecmp
import io
import tkinter
import fnmatch
import os
import shutil
import glob
import pathlib
from bs4 import BeautifulSoup
import urllib
import requests
import whois

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

         
    print ('  ')
            
    print("!!!!" +  'Done')    

   

if __name__ == '__main__': main()
  
