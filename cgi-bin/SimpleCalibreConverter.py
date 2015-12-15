#!/usr/bin/python -u
print "Content-type: text/html\r\n\r\n"

from subprocess import call, PIPE, Popen
import os.path, shutil
import urllib2, httplib
import sys

#urllib2.urlopen("http://ec2-52-35-183-12.us-west-2.compute.amazonaws.com/data/").read()
'''
    HOW TO USE:
        The computer must have Calibre, BeautifulSoup, Python  installed for the program to work correctly.
        The user needs:
            a TOC (table of contents) file, which is just an html with links to other pages.
            a metadata file with info about the author, publisher, year, etc
            a cover page for the book

    HOW IT WORKS:
        All of the pages are embedded using the links inside the toc file
        Using breadth first search on the toc.html file, Calibre finds the links to all other html files and
        adds them to the .epub
        If you have a file that MUST be in the epub, but you have no link to it (you'll need to include a link somewhere,
        preferably in the TOC.html file)

    OPTIONS:
        -m metadata   --sets the metadata of the ebook
        --insert-metadata
        --cover cover.gif  -- iff cover is not specified in metadata
        --breadth-first    -- analyse the TOC.html in breadth first search order
        --extra-css style.css  --adds an extra css file
        --no-default-epub-cover
        --no-svg-cover   -- to work on iphones correctly
        --preserve-cover-aspect-ratio
'''

def epub_conversion(args, outputFolder):
    output = outputFolder + "/basic-legal-citation.epub"
    args.append(output)

    args.append("--breadth-first")
    args.append("--insert-blank-line-size")
    args.append("5")    

    arg = raw_input("Type the input metadata file (if any): ")
    if os.path.isfile(arg):
        args.append("-m")
        args.append(arg)
        args.append("--insert-metadata")

    arg = raw_input("Type the cover file (if any): ")
    if os.path.isfile(arg):
        args.append("--cover")
        args.append(arg)
        args.append("--preserve-cover-aspect-ratio")
    else:
        args.append("--no-default-epub-cover")


    arg = raw_input("Type a extra css file (if any): ")
    if os.path.isfile(arg):
        args.append("--extra-css")
        args.append(arg)
    return args

def pdf_conversion(args, outputFolder):
    output = outputFolder + "/basic-legal-citation.pdf"
    args.append(output)
    
    args.append("--breadth-first")
    args.append("--margin-bottom")
    args.append("100")
    args.append("--margin-top") 
    args.append("50")
    args.append("--margin-left")
    args.append("80")
    args.append("--margin-right")
    args.append("80")
    args.append("--insert-blank-line-size")
    args.append("5")    

    arg = ""#raw_input("Type the input metadata file (if any): ")
    if os.path.isfile(arg):
        args.append("-m")
        args.append("--insert-metadata")
        args.append(arg)

    arg = "cover.jpeg"#raw_input("Type the cover file (if any): ")
    if os.path.isfile(arg):
        args.append("--cover")
        args.append(arg)
        args.append("--preserve-cover-aspect-ratio")

    arg = "pdf.css"#raw_input("Type a extra css file (if any): ")
    if os.path.isfile(arg):
        args.append("--extra-css")
        args.append(arg)
    args.append("--pdf-page-numbers")
    args.append("--disable-font-rescaling")
    args.append("--smarten-punctuation")
    return args

def deleteFolderContents(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception, e:
            print e

args = []
command = "ebook-convert"
args.append(command)

#arg = "ebook-toc.html"#raw_input("Type the input HTML (Table of Contents) file: ")
arg = "../html/pages/toc.html"#raw_input("Type the input HTML (Table of Contents) file: ")
outputFolder = "/var/www/html/data"
if os.path.isfile(arg):
    print "Starting to convert, please be patient and DON'T reload the page"
    args.append(arg)
    deleteFolderContents(outputFolder)
    args = pdf_conversion(args, outputFolder)
    #retStatus = call(args)
    process = Popen(args, shell=False, stdout=PIPE)

    # Poll process for new output until finished
    while True:
        nextline = process.stdout.readline()
        if nextline == '' and process.poll() != None:
            break
        sys.stdout.write(nextline.replace("\n","<br />\n"))
        sys.stdout.flush()

    #replacer = Popen(['sed', 's/\\n/br/g'], shell=False, stdin=converter.stdout, stdout=PIPE)
    #output = replacer.communicate()
    #output=process.communicate()[0]
    #exitCode = process.returncode
    #print output[0].replace("\n","<br />\n")

    #if(output[1]):
    #if(retStatus):
    #    print("Conversion failed!\n")

    print("Convertion SUCCESSFULL ! \n")
    #converter.stdout.close()
    #converter.wait()
    #redirect

print('<link href="../dist/css/customize.css" rel="stylesheet">')
print('<link href="../dist/css/citation.css" rel="stylesheet">')
print('<link href="../bower_components/bootstrap/dist/css/bootstrap.min.css" rel="stylesheet">')
print('<div class = "conButt btn-lg btn-info "><a href="../data">Converted files </a></div>')

#    httplib.HTTPConnection.debuglevel = 1 
#    request = urllib2.Request('http://www.diveintopython.net/http_web_services/redirects.html')
#    opener = urllib2.build_opener()
#    f = opener.open(request)
