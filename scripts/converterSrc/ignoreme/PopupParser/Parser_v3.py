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

# remove those navigation headers and footers from every page.
def remove_all_navbars(soup):
    for table in soup.findAll("table"):
        for a in table.findAll('a'):
            if a.text == "Home":
                table.replaceWith("")
    return soup

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

def copyExampleFile(ex_file):
    folder = "../ParsedHTML"
    if not os.path.exists(folder):
        os.makedirs(folder)

    if not os.path.exists(folder+"/"+ex_file):
        shutil.copy(ex_file,folder)
    #new_filename = folder+"/"+ new_filename +"html"


def replace_all_iframes(soup):
	#replace the title of the iframe
    
    for span in soup.findAll("span", {'class': 'Examplewindow'}):
        text = re.sub(r'\(<a .*>restore</a>\)',' ', span.text) 
        span.string = text
        span['class'].append("ExampleBox")
    
        new_div = soup.new_tag('div')
        new_div['style'] = "text-align: center;"
        replace_spans(span,new_div)


    #replace iframe
    iframes = soup.findAll("iframe")
    for iframe in iframes:
        new_tag = soup.new_tag('div')
        new_tag['class'] = "ExampleBox"
        new_tag['name'] = iframe['name']
        new_tag['style'] = "border:1px solid black;display:inline-block;width:24em;text-align:left"
        #ex_path = "selectedTemplate.path = '" + iframe['src'] + "'"
        #new_tag['data-ng-include'] = ex_path
        #copyExampleFile(iframe['src'])
        ex_file = iframe['src']
        example = get_beautiful_file(ex_file)
        ul = example.body.find("ul")
        if ul is not None:
            #if the example file isn't an ordered list, chances are that it's a very big HTML file
            #in that case, don't replace with dynamic ng-show command
            new_tag.append(ul)
        
        new_div = soup.new_tag('div')
        new_div['style'] = "text-align: center;"
        new_div.append(new_tag)
        soup.iframe.replace_with(new_div)

    return soup

def convertToButton(tag):
    new_tag = soup.new_tag('button')
    new_tag['ng-click'] = "toggleModal('Success')"
    new_tag['class'] = "btn btn-default"
    new_tag.string = tag.string

    return new_tag

def replacePopUp(span):
    a = span.find("a")
    example = a["href"].decode("utf-8")
    print("example file is" + example)
    #Replace <<e.g>> icon with a button
    button = convertToButton(a)
    span.a.replace_with(button)
           
    if(filename == "6-200.html"):
        print(filename + " href: " + example)
    if os.path.isfile(example):
        print("trying to open ahref target for file: " + filename + " href : " + example)
        ex_file = example
        example = get_beautiful_file(example)
        ul = example.body.find("ul")
        if ul is not None:
            #if the example file isn't an ordered list, chances are that it's a very big HTML file
            #in that case, don't replace with dynamic ng-show command
            modal = soup.new_tag('modal')
            modal['visible'] = "showModal"
            modal.append(ul)
            span.append(modal)
        else:
            copyExampleFile(ex_file)

    return span

def replace_spans(old_span, new_span):
    contents = old_span.replace_with(new_span)
    new_span.append(contents)


def addModalPopUp(soupHTML):
	count = 0
	for ex_span in soupHTML.findAll("span", {"class": "example_icon"}):
            new_span = replacePopUp(ex_span)
            div = soup.new_tag('div')
            div['ng-controller'] = "dynamicExamplesCtrl"
            div['class'] = "container"
            replace_spans(new_span,div)

        count += 1
	return soupHTML

#Main

print "Start"
dir_path = '*00.htm'
files = glob.glob(dir_path)
print(files)
for filename in files:
    print("Working on file " + filename)
    html = filename
    
    if os.path.isfile(html): #verify if the file exists
        soup = get_beautiful_file(html)
        #Remove header links - home, etc
        soup = remove_all_navbars(soup)
        if isiframePresent(soup) == 1:
            #Initial example box
            soup = replace_all_iframes(soup)

            #Add modal popup
            popup = addModalPopUp(soup)

    new_filename = filename[:-3] #ignore .htm
    #filename = re.split('.',new_filename)[0]
    #print(filename)

    folder = "../ParsedHTML"
    if not os.path.exists(folder):
        os.makedirs(folder)
    new_filename = folder+"/"+ new_filename +"html"
    f = open(new_filename, "w")
    f.write(str(soup.prettify("utf-8")))
    f.close()