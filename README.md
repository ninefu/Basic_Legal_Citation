# CS_5150
subteam 1:
Tasks to complete (me + yihui + 2 more opening)
-----------------
Website :
- replace the layouting format with ng-view. Only main layout in index.html. Individual pages to be fetched and plugged in dynamically
- Add scroll bar to left navigation menu
- remove search bar (unless we plan to implement it)
- add a "download button" for epub, mobi in top right corner navi tab
- use ng-filter for dynamic content rendering in the list of states page
- check notes for usability comments from prof. martin
- ensure that css styling is perfectly done

subteam 2:
scripting + xhtml:
------------------
inconsistencies found:
a. sara's html folder has diff. content from LII site
   currently using s/w discovered by akshay to crawl the lii site and extract html pages
   some pages could not be extracted from hosted site.
   some example pages may be missing too.
b. some tags are like <a href="6-200.html#string">
    This is used to jump to a particular location in an external link
    such tags mustn't be converted into angular js ng-show (6-200.html is too big to be displayed under an <<e.g.>>)
    the current script can now handle this condition
    
    possible that more such corner cases exist. ensure that the beautifulSoupTest.py correctly converts all such corner case <<e.g.>> tags.

    what if there is no <ul> tag in <a href="...">. Currently, we will retain this as normal hyperlink. Must we copy the example to current page and use ng-show? must we change script so that ng-show is added only if target="iframe" or can this be ignored?

c. the hosted LII site has all pages ending with .html. Saras files had .htm extension. The href in new site stopped working as our script has hardcoded .htm extension. Fixed the bug in script. New generated files are now .html

d. too messy folder structure. Edited structure as:
    - converterSrc - all the calibre stuff (John's domain)
    - oldLIIHtmlFiles - Saras files
    - html - AngularJS files. (my + Yihui domain)
    - LIIWebsiteHTMLFiles - contains files extractd from hosted LII site. Generated from akshays tool. Also contains beautifulSoupTest.py
    - ParsedHTMLAngularJSSite - the beautifulSoupTest.py output

tasks to complete:
1. proof read
   45 output files: 
    (if you manually edit a file, leave a comment in google doc link - 
    https://docs.google.com/document/d/1OQBlbDOuCzkb7qIepXyJuvxfE6vr9wXVmUYQcPm5fXA/edit?usp=sharing
    )
     - check if content is same as hosted LII site
     - check if all e.g. tags are working as expected (user must click on each e.g. and manually check that things work. we found corner case scenarios by manual testing today)
     - check that styling is readable. (edit stray . " , etc)

2. XHTML tagging research

3. conversion to pdf... on new site - STRICTLY witheld until all other tasks are complete
target : sunday!!
