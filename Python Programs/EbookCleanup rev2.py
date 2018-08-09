#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

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



def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    print('   ')

    source_directory = '/Volumes/6TB USB 5_18_18/Vuze Downloads 2/'
    pdf_dir = '/Volumes/6TB USB 5_18_18/Cleaned_Ebooks/PDF_Files/'
    epub_dir = '/Volumes/6TB USB 5_18_18/Cleaned_Ebooks/Epub_Files/'
    mobi_dir = '/Volumes/6TB USB 5_18_18/Cleaned_Ebooks/Mobi_Files/'
    zip_dir = '/Volumes/6TB USB 5_18_18/Cleaned_Ebooks/Zip_Files/'
    mp4_dir = '/Volumes/6TB USB 5_18_18/Cleaned_Ebooks/MP4_Files/'
    jpg_dir = '/Volumes/6TB USB 5_18_18/Cleaned_Ebooks/JPG_Files/'
    mp3_dir = '/Volumes/6TB USB 5_18_18/Cleaned_Ebooks/MP3_Files/'
    junk_dir = '/Volumes/6TB USB 5_18_18/Cleaned_Ebooks/Junk_Files/'

   


    for dirName, subdirList, fileList in os.walk(source_directory):
        
        for fname in fileList:
            
            if ".mobi" in fname:
                print("it is a Kindle file " + fname)
                dirstring = dirName
                filestring = (dirstring +"/" + fname)
                destfile = (mobi_dir + "/" + fname)
                shutil.copyfile (filestring, destfile)
            elif ".pdf" in fname:
                print("it is a pdf file " + fname)
                dirstring = dirName
                filestring = (dirstring +"/" + fname)
                destfile = (pdf_dir + "/" + fname)
                shutil.copyfile (filestring, destfile)
            elif ".epub" in fname:
                print("File is an apple book " + fname)
                dirstring = dirName
                filestring = (dirstring +"/" + fname)
                destfile = (epub_dir + "/" + fname)
                shutil.copyfile (filestring, destfile)             
            elif ".zip" in fname:
                print("File is an zip file  " + fname)
                dirstring = dirName
                filestring = (dirstring +"/" + fname)
                destfile = (zip_dir + "/" + fname)
                shutil.copyfile (filestring, destfile)    
            elif ".mp4" in fname:
                print("File is an Video file  " + fname)
                dirstring = dirName
                print(dirstring)
                filestring = (dirstring +"/" + fname)
                destfile = (mp4_dir + "/" + fname)
                shutil.copyfile (filestring, destfile) 
            elif ".jpg" in fname:
                print("File is an jpg file  " + fname)
                dirstring = dirName
                #print(dirstring)
                filestring = (dirstring +"/" + fname)
                destfile = (jpg_dir + "/" + fname)
                shutil.copyfile (filestring, destfile)  
            elif ".mp3" in fname:
                print("File is an mp3 file  " + fname)
                dirstring = dirName
                filestring = (dirstring +"/" + fname)
                destfile = (mp3_dir + "/" + fname)
                shutil.copyfile (filestring, destfile) 
            elif ".txt" in fname:
                print("File is an junk file  " + fname)
                dirstring = dirName
                #print(dirstring)
                filestring = (dirstring +"/" + fname)
                destfile = (junk_dir + "/" +fname)
                shutil.copyfile (filestring, destfile) 
   
   
    print ('  ')
            
    print("!!!!" +  'Done')    

   

if __name__ == '__main__': main()
