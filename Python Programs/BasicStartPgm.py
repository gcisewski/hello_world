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


def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    print('   ')

    
    url = ('https://realpython.com/blog/')
    content = urllib.request.urlretrieve(url)
    #content = urllib.request._opener.open (url)
    #content = urllib.request.urlopen(url)
    soup = BeautifulSoup(content)
    print (soup.prettify())

    
     
    print ('  ')
            
    print("!!!!" +  'Done')    

   

if __name__ == '__main__': main()
  
