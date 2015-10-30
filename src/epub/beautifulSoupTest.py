
import zipfile
import urllib
import sys
import os.path
import mimetypes
import time
import urlparse
import cgi
from optparse import OptionParser
from readability.readability import Document
from BeautifulSoup import BeautifulSoup,Tag, Comment



# remove the comments from a BeautifulSoup file
def remove_comments(soup):
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    [comment.extract() for comment in comments]

# get the html file as a BeautifulSoup file
def get_beautiful_file(filename):
    ex_file = urllib.urlopen(filename).read().decode('utf-8', 'ignore')
    ex_soup = BeautifulSoup(ex_file)
    return ex_soup

def replace_all_iframes(soup):
    for iframe in soup.body('iframe'):
        example = iframe["src"]
        ex_soup = get_beautiful_file(example)
        remove_comments(ex_soup)
        p = ex_soup.body
        print p.prettify()

# replace all <li> with <p> if the class is Example or note for epub compatibility
def replace_all_li(soup):
    for li in soup.findAll("li"):
        if li["class"] == "Example" or li["class"] == "note":
            li.name = 'p'

def replace_all_tables(soup):
    for table in soup.findAll("table", {'class': 'text-level1'}):
        for tr in table:
            pass

def create_epub_compatilble_html(html_filename):
    soup = get_beautiful_file(html_filename)

def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i)<128)

# FUNCTION TO CREATE A HTML FILE GETTING ONLY THE CONTENT FROM THE AUTHOR'S PAGE
def get_contents_page():
    print "Type the input HTML file: "
    html = raw_input()
    doc = '''<!DOCTYPE html><html lang="en">'''

    if os.path.isfile(html):
        soup = get_beautiful_file(html)
        head = soup.head
        doc += str(head)
        contents = soup.find("div", {"id": "page-wrapper"})
        #test if we get contents
        doc += '''<body>'''
        doc += str(contents)
        doc += '''</body></html>'''
        new_html = BeautifulSoup(doc)
        pretty_html = new_html.prettify()
        f = open(r'1_1-epub.html', "w")
        f.write(pretty_html)
        f.close()

def create_toc_file():
    html = "1_1.html"
    doc = '''<!DOCTYPE html><html lang="en">'''

    if os.path.isfile(html):
        soup = get_beautiful_file(html)
        head = soup.head
        doc += str(head)
        contents = soup.find("div", {"role": "navigation"})
        #test if we get contents
        doc += '''<body>'''
        doc += str(contents)
        doc += '''</body></html>'''
        new_html = BeautifulSoup(doc)
        pretty_html = new_html.prettify()
        f = open(r'toc.html', "w")
        f.write(pretty_html)
        f.close()

html = "2-100.htm"       # get the file 2-100.htm
if os.path.isfile(html): #verify if the file exists
    soup = get_beautiful_file(html)   # create a soup
    for span in soup.findAll("span", {"class": "example_icon"}):
        a = span.find("a")
        example = a["href"]
        if os.path.isfile(example):
            print "====== ", str(example), " ======"
            example = get_beautiful_file(example)
            print example.body.find("ul").prettify()