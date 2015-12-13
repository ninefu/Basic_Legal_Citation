__author__ = 'DeviSnigdha'
import glob
import re
import shutil
import zipfile
import urllib
import sys
import os.path
#import urlparse
import urllib
import cgi
from bs4 import BeautifulSoup, Tag, Comment
from BeautifulSoup import NavigableString

# get the html file as a BeautifulSoup file
def get_beautiful_file(filename):
    ex_file = open(filename).read()
    ex_soup = BeautifulSoup(ex_file,"html.parser")
    return ex_soup

#Remove ignore-on-convert as a class and add as an attribute
def addIgnoreAttr(soup):

    for div_tag in soup.findAll("div",{"class" : "ignore-on-convert"}):
        div_tag['class'].remove('ignore-on-convert')
        div_tag['ignore-on-convert'] = ''

    for but_tag in soup.findAll("button",{"class" : "ignore-on-convert"}):
        but_tag['class'].remove('ignore-on-convert')
        but_tag.attrs.update({'ignore-on-convert':''})

    return soup

#Main
print "ignoreClass"

dir_path = '*00.html'
files = glob.glob(dir_path)
print(files)
count = 0
modified = 0
for filename in files:
    print("Working on file " + filename)
    count += 1 
    html = filename

    if os.path.isfile(html): #verify if the file exists
        soup = get_beautiful_file(html)

        if len(soup.findAll("div",{"class" : "ignore-on-convert"})) > 0:
            modified += 1
            soup = addIgnoreAttr(soup)

    new_filename = filename[:-4] #remove .html

    folder = "ignoreClassFiles"
    if not os.path.exists(folder):
        os.makedirs(folder)
    new_filename = folder+"/"+ new_filename +"html"
    f = open(new_filename, "w")
    f.write(str(soup.prettify("utf-8")))
    f.close()
print("Total files: " + str(count))
print("Files modified: " + str(modified))

exit()