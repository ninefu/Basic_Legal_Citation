'''
    HOW TO USE:
        The computer must have Calibre, BeautifulSoup, Python  installed for the program to work correctly.
        The user needs:
            * a TOC (table of contents) file, which is just an html with links to other pages.
            * a metadata file with info about the author, publisher, year, etc
            * a cover page for the book
        For simplicity we have provided both a table of contents in ebook-toc.html and a cover page for the
        conversion. 

    HOW IT WORKS:
        All of the pages are embedded using the links inside the toc file, if you want a page in the
        pdf or epub, input a anchor <a href> </a> in the TOC file. The order of the anchors is maintained
        during conversion. 
        FILES: pdf.css, ebook-toc.html, pdf-toc.html, cover.jpeg, pdf-firstpage.html MUST be inside
        html/pages for the conversion to work smoothly. 

    THE CODE:
        Most of the code is used to linearize the tables created in a few of the HTML. Each table has
        received an id according to how it should be linearized. The linearization is heavily dependant
        upon the structure of the tables. In case the structure is altered, the linearization may not
        work as intended. 

    OPTIONS:
        -m metadata_file                  - sets the metadata of the ebook
        --insert-metadata
        --cover cover.jpeg                - iff cover is not specified in metadata
        --breadth-first                   - analyse the TOC.html in breadth first search order
        --extra-css style.css             - adds an extra css file
        --no-default-epub-cover
        --no-svg-cover                    - to work on iphones correctly
        --preserve-cover-aspect-ratio
        --disable-font-rescaling          - preserve the font size specified in the css
        --expand-css                      - use the full css file
        --smarten-punctuation             - convert the punctuation into its typographic equivalent
        --margin-*                        - set the margin of the book in px
        --pdf-page-numbers                - add page numbers to the pdf
'''

from subprocess import call
import os.path
import glob
import zipfile
import urllib
import sys
import os.path
import urlparse
import cgi
import shutil, errno
from BeautifulSoup import BeautifulSoup,Tag, Comment

# get the html file as a BeautifulSoup file
def get_beautiful_file(filename):
    ex_file = urllib.urlopen(filename).read().decode('utf-8', 'ignore')
    ex_soup = BeautifulSoup(ex_file)
    return ex_soup

# remove those navigation headers and footers from every page.
def remove_all_navbars(soup):
    for table in soup.findAll("table"):
        for a in table.findAll('a'):
            if a.text == "Home":
                table.replaceWith("")

def linearize_cols_1(soup, table):
    if table.get('id') == "linearize-cols-1":
            ul = Tag(soup,"ul")
            ul["class"] = "linearized"
            for td in table.findAll("td"):
                for p in td.findAll("p"):
                    p.name = "span"
                try:
                    text = ''.join(td.findAll(text=True))
                    text = text.strip()
                    if text != '' and text != '&nbsp;':
                        td.name = "li"
                        ul.append(td)
                except:
                    pass
            table.replaceWith(ul)

def linearize_cols_2_bold(soup, table):
    if table.get('id') == "linearize-cols-2-bold":
        ul = Tag(soup,"ul")
        ul["class"] = "linearized"
        for tr in table.findAll("tr"):
            tr.name = "span"
            tr["class"] = "spaced"
            for td in tr.findAll("td"):
                if td["width"] =="22%":
                    td.name = "li"
                    tag = td
                else:
                    tag.append(td)
                    td.name = "ul"
                for p in td.findAll("p", { "class" : "Example"}):
                    p.name = "li"
            ul.append(tr)
        table.replaceWith(ul)

def linearize_states(soup, table):
    if table.get('id') == "linearize-states":
        ul = Tag(soup,"ul")
        ul["class"] = "text-level3"
        tag = None
        for tr in table.findAll("tr"):
            tr.name = "span"
            tr["class"] = "spaced"
            for td in tr.findAll("td"):
                if td["width"] =="40%":
                    td.name = "li"
                    tag = td
                else:
                    tag.append(td)
                    td.name = "ul"
            ul.append(tr)
        table.replaceWith(ul)

def get_first_three(soup, table):
    loop = 0
    first = 1
    enclose = Tag(soup, "div")
    for tr in table.findAll("tr"):
        li = Tag(soup, "li")
        for td in tr.findAll("td"):
            if loop != 3:
                try:
                    text = ''.join(td.findAll(text=True))
                    text = text.strip()
                    if text != '' and text != '&nbsp;':
                        td.name = "span"
                        if first == 1:
                            first = 0
                            enclose.append(td)
                        else:
                            if loop != 2: td.append(' - ')
                            li.append(td)
                except:
                    pass
            else:
                break    
            loop += 1
        loop = 0
        if ''.join(li.findAll(text=True)) != '':
            enclose.append(li)
    title = enclose.find("span")
    enclose.find("span").replaceWith("")
    enclose.name = "ul"
    div = Tag(soup, "div")
    div.append(title)
    div.append(enclose)
    return div

def get_last_three(soup, table):
    loop = 0
    first = 1
    enclose = Tag(soup, "div")
    ul = Tag(soup, "ul")
    for tr in table.findAll("tr"):
        td = tr.findAll("td")
        li = Tag(soup, "li")
        for el in td[3:]:
            if loop != 3:
                try:
                    text = ''.join(el.findAll(text=True))
                    text = text.strip()
                    if text != '' and text != '&nbsp;':
                        el.name = "span"
                        if first == 1:
                            first = 0
                            enclose.append(el)
                        else:
                            if loop != 2: el.append(' - ')
                            li.append(el)
                except:
                    pass
            else:
                break    
            loop += 1
        loop = 0
        if ''.join(li.findAll(text=True)) != '':
            enclose.append(li)
    title = enclose.find("span")
    enclose.find("span").replaceWith("")
    enclose.name = "ul"
    div = Tag(soup, "div")
    div.append(title)
    div.append(enclose)
    return div

def linearize_cols_3_2(soup, table):
    if table.get('id') == "linearize-cols-3-2":
        div = Tag(soup, "div")
        div["class"] = "div-container"
        ul_last = get_last_three(soup, table)
        ul_first = get_first_three(soup, table)        
        div.append(ul_first)
        div.append(ul_last)
        table.replaceWith(div)

def linearize_cols_1_4(soup, table):
    if table.get('id') == "linearize-cols-1-4":
        div = Tag(soup, "ul")
        for i in range(4):
            for tr in table.findAll("tr"):
                td = tr.find("td")
                tr.find("td").replaceWith("")
                div.append(td)
        list_a = div.findAll("a")
        composite_list = [list_a[x:x+4] for x in range(0, len(list_a), 4)]
        ul = Tag(soup, "ul")
        for lista in composite_list:
            li = Tag(soup, "li")
            for a in lista:
                if a == lista[-1]:
                    a = BeautifulSoup(a.prettify())
                else:
                    a = BeautifulSoup(a.prettify() + '<span> | </span>')
                li.append(a)
            ul.append(li)
        table.replaceWith(ul)

def linearize_rows_1(soup, table):
    if table.get('id') == "linearize-rows-1":
        div = Tag(soup, "div")
        div["class"] = "center"
        for tr in table.findAll("tr"):
            lista = tr.findAll("td")
            for td in lista:
                for p in td.findAll("p"):
                    p.name = "span"
                td.name = "span"
                if td == lista[-1]:
                    td = BeautifulSoup(td.prettify())
                else:
                    td = BeautifulSoup(td.prettify() + '<span> | </span>')
                div.append(td)
        table.replaceWith(div)

def linearize_rows_1_cols(soup, table):
    if table.get('id') == "linearize-rows-1-cols":
        div = Tag(soup, "div")
        div["class"] = "center"
        for tr in table.findAll("tr"):
            lista = tr.findAll("td")
            li = Tag(soup, "li")
            for td in lista:
                for p in td.findAll("p"):
                    p.name = "span"
                td.name = "span"
                if td == lista[0]:
                    td = BeautifulSoup('<b>' + td.prettify() + '</b>')
                else:
                    td = BeautifulSoup('<span>[</span>' + td.prettify() + '<span>]</span>')
                li.append(td)
            div.append(li)
        div.name = "ul"
        table.replaceWith(div)

def get_first_two(soup, table):
    loop = 0
    enclose = Tag(soup, "div")
    for tr in table.findAll("tr"):
        li = Tag(soup, "li")
        for td in tr.findAll("td"):
            if loop != 2:
                try:
                    text = ''.join(td.findAll(text=True))
                    text = text.strip()
                    if text != '' and text != '&nbsp;':
                        td.name = "span"
                        if loop != 1: td.append(' - ')
                        li.append(td)
                except:
                    pass
            else:
                break    
            loop += 1
        loop = 0
        if ''.join(li.findAll(text=True)) != '':
            enclose.append(li)
    return enclose

def get_last_two(soup, table):
    loop = 0
    enclose = Tag(soup, "div")
    ul = Tag(soup, "ul")
    for tr in table.findAll("tr"):
        td = tr.findAll("td")
        li = Tag(soup, "li")
        for el in td[2:]:
            if loop != 2:
                try:
                    text = ''.join(el.findAll(text=True))
                    text = text.strip()
                    if text != '' and text != '&nbsp;':
                        el.name = "span"
                        if loop != 1: el.append(' - ')
                        li.append(el)
                except:
                    pass
            else:
                break    
            loop += 1
        loop = 0
        if ''.join(li.findAll(text=True)) != '':
            enclose.append(li)
    return enclose

def linearize_cols_2(soup, table):
    if table.get('id') == "linearize-cols-2":
        ul = Tag(soup, "ul")
        ul["class"] = "ul-container"
        ul_last = get_last_two(soup, table)
        ul_first = get_first_two(soup, table)        
        ul.append(ul_first)
        ul.append(ul_last)
        table.replaceWith(ul)

def get_first_3(soup, table):
    loop = 0
    first = 1
    enclose = Tag(soup, "div")
    for tr in table.findAll("tr"):
        li = Tag(soup, "li")
        for td in tr.findAll("td"):
            if loop != 3:
                try:
                    text = ''.join(td.findAll(text=True))
                    text = text.strip()
                    if text != '' and text != '&nbsp;':
                        td.name = "span"
                        if loop != 2: td.append(' - ')
                        li.append(td)
                except:
                    pass
            else:
                break    
            loop += 1
        loop = 0
        if ''.join(li.findAll(text=True)) != '':
            enclose.append(li)
    return enclose

def get_last_3(soup, table):
    loop = 0
    first = 1
    enclose = Tag(soup, "div")
    ul = Tag(soup, "ul")
    for tr in table.findAll("tr"):
        td = tr.findAll("td")
        li = Tag(soup, "li")
        for el in td[3:]:
            if loop != 3:
                try:
                    text = ''.join(el.findAll(text=True))
                    text = text.strip()
                    if text != '' and text != '&nbsp;':
                        el.name = "span"
                        if loop != 2: el.append(' - ')
                        li.append(el)
                except:
                    pass
            else:
                break    
            loop += 1
        loop = 0
        if ''.join(li.findAll(text=True)) != '':
            enclose.append(li)
    return enclose

def linearize_cols_3(soup, table):
    if table.get('id') == "linearize-cols-3":
        div = Tag(soup, "ul")
        div["class"] = "div-container"
        ul_last = get_last_3(soup, table)
        ul_first = get_first_3(soup, table)        
        div.append(ul_first)
        div.append(ul_last)
        table.replaceWith(div)

def sub_table(soup, subtable):
    ul = Tag(soup, "ul")
    li = Tag(soup, "li")
    string = '<i>The Bluebook: </i>'
    for tr in subtable.findAll("tr"):
        for td in tr.findAll("td"):
            try:
                text = ''.join(td.findAll(text=True))
                text = text.strip()
                if text != '' and text != '&nbsp;':
                    string += ''.join(td.findAll(text=True)) 
                    string.strip()
                    string += ', '
            except:
                pass
        string = string.strip().rstrip(',')
    li.append(BeautifulSoup(string))
    ul.append(li)
    return ul 

def linearize_bb(soup, table):
    if table.get('id') == "linearize-bb":
        div = Tag(soup, "div")
        first = 1
        lista = table.findAll("tr")
        tr1 = lista[0]
        div.append(tr1)
        for tr in lista[1:]:
            ul = Tag(soup, "ul")
            li = Tag(soup, "li")
            for td in tr.findAll("td"):
                for p in td.findAll("p"):
                    p.name = "span"
                try:
                    text = ''.join(td.findAll(text=True))
                    text = text.strip()
                    if text != '' and text != '&nbsp;':
                        if first == 1:
                            li.append(td)
                            first = 0
                        else:
                            td.replaceWith("")
                except:
                    pass
                for subtable in td.findAll("table"):
                    sub = sub_table(soup, subtable)
                    try:
                        text = ''.join(td.findAll(text=True))
                        text = text.strip()
                        if text != '' and text != '&nbsp;': 
                            li.append(sub)
                    except:
                        pass
            first = 1
            if li.contents: ul.append(li)
            div.append(ul)
        table.replaceWith(div)

def sub_table2(soup, subtable):
    ul = Tag(soup, "ul")
    li = Tag(soup, "li")
    string = '<i>ALWD Guide to Legal Citation: </i>'
    for tr in subtable.findAll("tr"):
        for td in tr.findAll("td"):
            try:
                text = ''.join(td.findAll(text=True))
                text = text.strip()
                if text != '' and text != '&nbsp;':
                    string += ''.join(td.findAll(text=True)) 
                    string += ', '
            except:
                pass
        string = string.strip().rstrip(',')
    li.append(BeautifulSoup(string))
    ul.append(li)
    return ul 

def linearize_alwd(soup, table):
    if table.get('id') == "linearize-alwd":
        div = Tag(soup, "div")
        first = 1
        lista = table.findAll("tr")
        tr1 = lista[0]
        div.append(tr1)
        for tr in lista[1:]:
            ul = Tag(soup, "ul")
            li = Tag(soup, "li")
            for td in tr.findAll("td"):
                for p in td.findAll("p"):
                    p.name = "span"
                try:
                    text = ''.join(td.findAll(text=True))
                    text = text.strip()
                    if text != '' and text != '&nbsp;':
                        if first == 1:
                            li.append(td)
                            first = 0
                        else:
                            td.replaceWith("")
                except:
                    pass
                for subtable in td.findAll("table"):
                    sub = sub_table2(soup, subtable)
                    try:
                        text = ''.join(td.findAll(text=True))
                        text = text.strip()
                        if text != '' and text != '&nbsp;':
                            li.append(sub)
                    except:
                        pass
            first = 1
            if li.contents: ul.append(li)
            div.append(ul)
        table.replaceWith(div)

def linearize_tables(soup):
    for table in soup.findAll("table"):
        linearize_cols_1(soup, table)
        linearize_cols_2_bold(soup, table)
        linearize_cols_3_2(soup, table)
        linearize_cols_1_4(soup, table)
        linearize_rows_1(soup, table)
        linearize_cols_2(soup, table)
        linearize_cols_3(soup, table)
        linearize_rows_1_cols(soup, table)
        linearize_bb(soup, table)
        linearize_alwd(soup, table)
        linearize_states(soup, table)

def ignore_on_conversion(soup):
    ignore_list = soup.findAll(lambda tag:[a for a in tag.attrs if a[0].startswith('ignore-')])
    if ignore_list and len(ignore_list) > 0:
        for tag in ignore_list:
            tag.replaceWith("")

def epub_conversion(folder, args):
    output = "basic-legal-citation.epub"
    args.append(output)

    args.append("--breadth-first")
    args.append("--insert-blank-line-size")
    args.append("5")   

    arg = ""#raw_input("Type the input metadata file (if any): ")
    if os.path.isfile(arg):
        args.append("-m")
        args.append(arg)
        args.append("--insert-metadata")

    arg = folder + "cover.jpeg"#raw_input("Type the cover file (if any): ")
    if os.path.isfile(arg):
        args.append("--cover")
        args.append(arg)
        args.append("--preserve-cover-aspect-ratio")
    else:
        args.append("--no-default-epub-cover")


    arg = folder + "pdf.css"#raw_input("Type a extra css file (if any): ")
    if os.path.isfile(arg):
        args.append("--extra-css")
        args.append(arg)
    args.append("--disable-font-rescaling")
    args.append("--smarten-punctuation")
    args.append("--expand-css")
    args.append("--line-height")
    args.append("15")
    return args

def pdf_conversion(folder, args):
    output = "basic-legal-citation.pdf"
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
        args.append(arg)
        args.append("--insert-metadata")

    arg = folder + "cover.jpeg"#raw_input("Type the cover file (if any): ")
    if os.path.isfile(arg):
        args.append("--cover")
        args.append(arg)

    arg = folder + "pdf.css"#raw_input("Type a extra css file (if any): ")
    if os.path.isfile(arg):
        args.append("--extra-css")
        args.append(arg)
    args.append("--pdf-page-numbers")
    args.append("--disable-font-rescaling")
    args.append("--smarten-punctuation")
    return args

def mobi_conversion(folder, args):
    output = "basic-legal-citation.mobi"
    args.append(output)
    return args

def copyfolder(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def deletefolder(folder):
    shutil.rmtree(folder)

# put the files in a sepparate folder so you won't loose information
def create_convertible_folder():
    dir_path = '*.html'
    files = glob.glob(dir_path)
    folder = "ebook"
    copyfolder("state_samples", folder+"/state_samples")
    if os.path.isfile("pdf.css"): 
        shutil.copy("pdf.css", folder)
    if os.path.isfile("cover.jpeg"): 
        shutil.copy("cover.jpeg", folder)
    for filename in files:
        print "Working on file " + filename
        html = filename
        if os.path.isfile(html): #verify if the file exists
            soup = get_beautiful_file(html)
            linearize_tables(soup)
            ignore_on_conversion(soup)
            
            new_filename = filename[:-4]
            if not os.path.exists(folder):
                os.makedirs(folder)
            new_filename = folder+"/"+ new_filename +"html"
            f = open(new_filename, "w")
            f.write(soup.prettify("utf-8"))
            f.close()
    return folder

if __name__ == "__main__":
    folder = create_convertible_folder()
    
    args = []
    command = "ebook-convert"
    args.append(command)
    arg = folder + "/pdf-toc.html"#raw_input("Type the input HTML (Table of Contents) file: ")
    if os.path.isfile(arg):
        args.append(arg)
        args = pdf_conversion(folder + '/', args)
        call(args)
    
    args = []
    command = "ebook-convert"
    args.append(command)
    arg = folder + "/ebook-toc.html"#raw_input("Type the input HTML (Table of Contents) file: ")
    if os.path.isfile(arg):
        args.append(arg)
        args = epub_conversion(folder + '/', args)
        call(args)

    args = []
    command = "ebook-convert"
    args.append(command)
    arg = "basic-legal-citation.epub"#raw_input("Type the input HTML (Table of Contents) file: ")
    if os.path.isfile(arg):
        args.append(arg)
        args = mobi_conversion(folder + '/', args)
        call(args)
    
    deletefolder(folder)