import glob
import zipfile
import urllib
import sys
import os.path
import urlparse
import cgi
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
                if ''.join(td.findAll(text=True)) != '&nbsp;' and ''.join(td.findAll(text=True)) != '':
                    td.name = "li"
                    ul.append(td)
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

def get_first_three(soup, table):
    loop = 0
    first = 1
    enclose = Tag(soup, "div")
    for tr in table.findAll("tr"):
        li = Tag(soup, "li")
        for td in tr.findAll("td"):
            if loop != 3:
                if ''.join(td.findAll(text=True)) != '&nbsp;':
                    td.name = "span"
                    if first == 1:
                        first = 0
                        enclose.append(td)
                    else:
                        if loop != 2: td.append(' - ')
                        li.append(td)
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
                if ''.join(el.findAll(text=True)) != '&nbsp;':
                    el.name = "span"
                    if first == 1:
                        first = 0
                        enclose.append(el)
                    else:
                        if loop != 2: el.append(' - ')
                        li.append(el)
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
                if ''.join(td.findAll(text=True)) != '&nbsp;':
                    td.name = "span"
                    if loop != 1: td.append(' - ')
                    li.append(td)
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
                if ''.join(el.findAll(text=True)) != '&nbsp;':
                    el.name = "span"
                    if loop != 1: el.append(' - ')
                    li.append(el)
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
                if ''.join(td.findAll(text=True)) != '&nbsp;':
                    td.name = "span"
                    if loop != 2: td.append(' - ')
                    li.append(td)
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
                if ''.join(el.findAll(text=True)) != '&nbsp;':
                    el.name = "span"
                    if loop != 2: el.append(' - ')
                    li.append(el)
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
            if ''.join(td.findAll(text=True)) != '&nbsp;':
                string += ''.join(td.findAll(text=True)) 
                string += ', '
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
                if ''.join(td.findAll(text=True)) != '&nbsp;': 
                    if first == 1:
                        li.append(td)
                        first = 0
                    else:
                        td.replaceWith("")
                for subtable in td.findAll("table"):
                    sub = sub_table(soup, subtable)
                    if ''.join(td.findAll(text=True)) != '&nbsp;': 
                        li.append(sub)
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
            if ''.join(td.findAll(text=True)) != '&nbsp;':
                string += ''.join(td.findAll(text=True)) 
                string += ', '
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
                if ''.join(td.findAll(text=True)) != '&nbsp;': 
                    if first == 1:
                        li.append(td)
                        first = 0
                    else:
                        td.replaceWith("")
                for subtable in td.findAll("table"):
                    sub = sub_table2(soup, subtable)
                    if ''.join(td.findAll(text=True)) != '&nbsp;': 
                        li.append(sub)
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
        
count = 0
dir_path = '*7-400.htm'
files = glob.glob(dir_path)
for filename in files:
    print "Working on file " + filename
    html = filename
    if os.path.isfile(html): #verify if the file exists
        soup = get_beautiful_file(html)   # create a soup
        remove_all_navbars(soup)
        linearize_tables(soup)

        new_filename = filename[:-4]
        new_filename = new_filename +"_new.html"
        f = open(new_filename, "w")
        f.write(soup.prettify())
        f.close()
