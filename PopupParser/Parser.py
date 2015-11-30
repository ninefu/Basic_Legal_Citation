__author__ = 'DeviSnigdha'
import glob
import zipfile
import urllib
import sys
import os.path
#import urlparse
import urllib
import cgi
from bs4 import BeautifulSoup, Tag, Comment

# remove the comments from a BeautifulSoup file
def remove_comments(soup):
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    [comment.extract() for comment in comments]

# get the html file as a BeautifulSoup file
def get_beautiful_file(filename):
    ex_file = open(filename).read()
    ex_soup = BeautifulSoup(ex_file,"html.parser")
    return ex_soup

def replace_all_iframes(soup):
    for iframe in soup.body('iframe'):
        print(iframe)
        print(iframe.name)
        iframe.name = 'div'
        #iframe.atrrs['class'].add("initialExample")
        print(iframe.name)

    return soup

#Main
count = 0
dir_path = 'HTMLFiles\*00.htm'
files = glob.glob(dir_path)
for filename in files:
    print("Working on file " + filename)
    html = filename
    if os.path.isfile(html): #verify if the file exists
        soup = get_beautiful_file(html)
        soup = replace_all_iframes(soup)

        #remove_comments(soup)
    new_filename = filename[:-4]

    folder = "Test.html"
    #if not os.path.exists(folder):
    #os.makedirs(folder)
    #new_filename = folder+"/"+new_filename +"html"
    f = open(folder, "w")
    f.write(str(soup.prettify("utf-8")))
    f.close()