import glob
import zipfile
import urllib
import sys
import os.path
#import urlparse
import urllib
import cgi
from bs4 import BeautifulSoup, Tag, Comment
#from BeautifulSoup import BeautifulSoup,Tag, Comment

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
        iframe.replaceWith("")

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
    print("Type the input HTML file: ")
    html = input()
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

def replace_spans (a, span, example, count):
    name = "example" + str(count)
    ul.attrs.append(('ng-show',name))
    ul.attrs.append(('class',"text-level2"))
    li_list = ul.findAll("li", {"class" : "text-level2"})
    for l in li_list:
        l.attrs = [(key,value) for key,value in l.attrs
                   if key != "class" or value != "text-level2"]
        
    #<a href="..." target="..."> remove the target part
    a.attrs = [(key,value) for key,value in a.attrs
               if key !="target"]
    #remove the link from <a href="....">, point it to a null location
    a["href"] = "#"
    a.attrs.append(('ng-model',name))
    a.attrs.append(('onclick',"return false"))
    a.attrs.append(('ng-click',name +" = !" +name ) )
    return;


#main
count = 0
dir_path = 'HTMLFiles\*00.html'
files = glob.glob(dir_path)
for filename in files:
    print("Working on file " + filename)
    html = filename
    if os.path.isfile(html): #verify if the file exists
        soup = get_beautiful_file(html)   # create a soup
        replace_all_iframes(soup)

        for span in soup.findAll("span", {"class": "example_icon"}):
            a = span.find("a")
            example = a["href"]
            if(filename == "6-200.html"):
                print(filename + " href: " + example)
            if os.path.isfile(example):
                print("trying to open ahref target for file: " + filename + " href : " + example)
                example = get_beautiful_file(example)
                ul = example.body.find("ul")
                if ul is not None:
                    #if the example file isn't an ordered list, chances are that it's a very big HTML file
                    #in that case, don't replace with dynamic ng-show command
                    span.append(ul)
                    count += 1
                    replace_spans(a, span, example, count)

    # find all a which are examples and replace them with the standart <span><a></a></span> pattern
        for a in soup.findAll("a", {"class": "example_icon"}):
            span = Tag(soup, "span", [("class","example_icon")])
            soup.insert(0, span)
            #get the value <a href="link.html">, store link.html into example
            example = a["href"]
            a["class"] = ""
            a.replaceWith(span)
            if(filename == "6-200.html"):
                print(filename + " href: " + example)
            #open the target link of <a href="...">
            if os.path.isfile(example):
                print("trying to open ahref target for file: " + filename + " href : " + example)
                example = get_beautiful_file(example)
                ul = example.body.find("ul")            
                span.insert(0, a)
                span.insert(1, ul)
                count += 1
                replace_spans(a, span, example, count)

        new_filename = filename[:-4]
folder = "Parsed"
if not os.path.exists(folder):
    os.makedirs(folder)
    new_filename = folder+"/"+new_filename +"html"
    f = open(new_filename, "w")
    f.write(soup.prettify())
    f.close()
