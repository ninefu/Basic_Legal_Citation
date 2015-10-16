
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
    ex_file = urllib.urlopen(filename).read()
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



soup = get_beautiful_file("toc.html")
for a in soup.findAll("a", href=True):
    pseudo_link = remove_non_ascii(a.text)
    pseudo_link = pseudo_link.strip()
    if os.path.isfile(pseudo_link + '.htm'):
        a["href"] = pseudo_link + '.htm'
    else:
        if os.path.isfile(pseudo_link + '.html'):
            a["href"] = pseudo_link + '.html'
        else:
            a["href"] = ''
pretty_html = soup.prettify()
f = open(r'toc.html', "w")
f.write(pretty_html)
f.close()