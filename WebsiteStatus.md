30-Nov-2015

-New additions:

Folder: LatestHTMLFiles 
Contains all the files given by Prof. Martin. Extracted Prof.Martin_HTML_files.zip

Folder : ParsedHTML 
Ran a parser for replacing iframes with popups and initial example to show in an angular js box. The output of the parser is stored in this folder.

Folder : PopupParser
Trial and Error, testing of the parser was done in this folder.

-Changes:

Popup Parser: 
1. To show the initial example, an angular js box is created which references to an html file of the form '*_ex0.html'
2. All other examples which are to be shown on click of <<e.g>> are embedded in the parent *.html file.
3. For conversion to a pdf, we do not need the initial example and since it is referenced by some external file, it will not be reflected in the pdf. The other examples will be shown.
4. Files that exist now are '*00.html', which are the parent html files and '*ex0.html', which are the initial example files. 


Folder: html

Earlier 'pages' folder was renamed to 'pages1'
The new 'pages' folder contains the popup parsed HTML files.

Warning: The new files are parsed only to replace the iframes. Removing of the header/footer and other things that were done earlier are not in these files. So do not freak put when you see stale pages on the site. I wanted to check the interaction of the popups on the site so pushed just these

To do: 
1. Merging of the earlier parser with the new parser so that all changes can be seen on the website. 
2. CSS has to be applied to center align the example boxes and content of the popups.
3. Manual changes, to remove misplaced dots (.) and commas (,) has to be done. 



