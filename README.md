# CS_5150
##### Subteam 1: (Harish + Yihui + Aish + Akshay)

Tasks to complete 
-----------------

Website :

Prof Martin's comments:

First as to the rendition of "How to Cite ... Case Documents":
>> * For this and similar pages where currently propositions are illustrated through an "Examples Window" I strongly favor having the propositions preceded by a box that contains an initial set of examples that the user causes to change by selecting an "e.g." button next to one or more of those propositions (and can also clear back to the original content)
[I would also consider having, as an option, examples appearing in a popup triggered by selecting the "e.g." button.  A popup that the user would have to close before moving on.] In other words, I don't think inserting the example text after the proposition when the button is selected works as well.**[Solved]**
>> * As for the "e.g." button, I've thought that it might be good to have it appear more buttonish **[Solved]**
>> * As for the highlighting of text within the "Examples Window" I would like fresh thinking about what background color should be used.  You'll note that in the ebook versions I go for a stronger color. **[Changed to the color used in PDF]**

Next as to the rendition of the home page:
>> * It appears to me that the menu, which appears as a sidebar on the left when viewed on a large screen, disappears altogether on a small screen.  Perhaps, I am wrong, but it needs to redeploy and not disappear. **[Solved]**
>> * "Resources" should be "Additional Resources" **[Solved]**
>> * The three videos should be listed by name as "Additional Resources".  **[Solved]**

1. replace the layouting format with ng-view. Only main layout in `index.html`. Individual pages to be fetched and plugged in dynamically
2. add scroll bar to left navigation menu**(aish adds: done, but will look for better ways)**
3. remove search bar (unless we plan to implement it)**(aish adds: done)**
4. add a "download button" for epub, mobi in top right corner navi tab
5. use ng-filter for dynamic content rendering in the list of states page**(aish adds: done)**
6. check notes for usability comments from Prof. Martin
7. ensure that css styling is perfectly done
8. add a purchase button for amazon e-book purchase
9. add xmlns attribute to `<html>` in new website, and add an XHTML compatible `<!DOCTYPE>`. 

------------------

##### Subteam 2: (Sania + Joao + Brenda + Snigdha)

Scripting + XHTML:
------------------

Inconsistencies found:

* a. Sara's html folder has diff. content from LII site
   - currently using s/w discovered by akshay to crawl the LII site and extract *.html* pages
   - some pages could not be extracted from hosted site.
   - some example pages may be missing too.
* b. some tags are like `<a href="6-200.html#string">`
   - This is used to jump to a particular location in an external link
   - such tags mustn't be converted into angular js `ng-show` (`6-200.html` is too big to be displayed under an `<<e.g.>>`)
   - the current script can now handle this condition
   - possible that more such corner cases exist. ensure that the `beautifulSoupTest.py` correctly converts all such corner case `<<e.g.>>` tags.
   - what if there is no `<ul>` tag in `<a href="...">`. Currently, we will retain this as normal hyperlink. Must we copy the example to current page and use `ng-show`? must we change script so that `ng-show` is added only if `target="iframe"` or can this be ignored?

* c. the hosted LII site has all pages ending with *.html*. Sara's files had *.htm* extension. The `href` in new site stopped working as our script has hardcoded *.htm* extension. Fixed the bug in script. New generated files are now *.html*.

* d. too messy folder structure. Edited structure as:
   - **converterSrc** - all the calibre stuff (John's domain)
   - **oldLIIHtmlFiles** - Saras files
   - **html** - AngularJS files. (Harish + Yihui domain)
   - **LIIWebsiteHTMLFiles** - contains files extractd from hosted LII site. Generated from akshays tool. Also contains `beautifulSoupTest.py`
   - **ParsedHTMLAngularJSSite** - the `beautifulSoupTest.py` output

##### Tasks to complete:

1. ~~Proofread~~ (done)
   
   - 45 output files: 
    (if you manually edit a file, leave a comment in [google doc link](https://docs.google.com/document/d/1OQBlbDOuCzkb7qIepXyJuvxfE6vr9wXVmUYQcPm5fXA/edit?usp=sharing)
    )
   - check if content is same as hosted LII site
   - check if all `<<e.g.>>` tags are working as expected (user must click on each `<<e.g.>>` and manually check that things work. we found corner case scenarios by manual testing today)
   - check that styling is readable. (edit stray . " , etc)

2. XHTML tagging research **(done)**
3. Conversion to pdf... on new site - STRICTLY witheld until all other tasks are complete
4. Add tags to the HTML5 files

**Target : Sunday!!**
