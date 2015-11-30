__author__ = 'DeviSnigdha'
import glob
import re
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

def isiframePresent(soup):
	f = soup.findAll('iframe')
	if len(f) > 0:
		return 1
	else:
		return 0

def replace_all_iframes(soup):
	#replace the title of the iframe
	for p in soup.findAll("p", {'class': 'iframe'}):
		span = p.find("span", {'class': 'Examplewindow'})
		text = re.sub(r'\([^)]*\)', '', span.text)
		span.string = text
		
	#replace iframe
	for iframe in soup.findAll("iframe"):
		new_tag = soup.new_tag('div')
		new_tag['name'] = iframe['name']
		new_tag['style'] = "border:1px solid black;display:inline-block;width:24em;text-align:left"
		ex_path = "selectedTemplate.path = '" + iframe['src'] + "'"
		new_tag['data-ng-include'] = ex_path
		soup.iframe.replace_with(new_tag)

	return soup

def replace_spans (a, span, example, count):
    print("a:"+ a + "span:" + span + "example:" + example +"count:"+count)
    exit()
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


def addModalPopUp(soup):
	count = 0
	for span in soup.findAll("span", {"class": "example_icon"}):
            a = span.find("a")
            example = a["href"].decode("utf-8")
            print("example file is" + example)
            
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


	return soup

#Main

print "Start"
dir_path = 'HTMLFiles/*00.html'
files = glob.glob(dir_path)
for filename in files:
    print("Working on file " + filename)
    html = filename
    
    if os.path.isfile(html): #verify if the file exists
        soup = get_beautiful_file(html)
        if isiframePresent(soup) == 1:
        	print("isiframePresent")
        	#Initial example box
        	soup = replace_all_iframes(soup)

        	#Add modal popup
        	soup = addModalPopUp(soup)

        #remove_comments(soup)
    new_filename = filename[:-5] #ignore .html
    filename = re.split('/',new_filename)[1]
    print(filename)
    
    folder = "ParsedHTML"
    if not os.path.exists(folder):
    	os.makedirs(folder)
    new_filename = folder+"/"+ filename +".html"
    f = open(new_filename, "w")
    f.write(str(soup.prettify("utf-8")))
    f.close()