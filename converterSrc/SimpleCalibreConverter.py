from subprocess import call
import os.path

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


def epub_conversion(args):
    output = "basic-legal-citation.epub"
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

def pdf_conversion(args):
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
    args.append("--linearize-tables")
    args.append("--smarten-punctuation")
    return args

args = []
command = "ebook-convert"
args.append(command)

arg = "pdf-toc.html"#raw_input("Type the input HTML (Table of Contents) file: ")
if os.path.isfile(arg):
    args.append(arg)
    args = pdf_conversion(args)
    call(args)
    