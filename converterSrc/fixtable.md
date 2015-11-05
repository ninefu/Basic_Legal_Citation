What needs to be fixed:
---

In order to have a smooth conversion to pdf and epub we need to use different css files ``pdf.css`` for pdf and ``epub.css`` for epub. There are a few discrepancies between the website files and the files in the books which are going to be documented here:

1. We need to replace the link in ``<head>`` to include the respective ``pdf.css`` or ``epub.css`` file for ebook conversion.
2. The class ``.ITALICSORUNDERLINE`` should be replaced to ``.italics``. 
3. PDF and epub have different first page, preface and table of contents styles. We need to address this issue. 
4. The titles have a background color in the original ebooks. 
5. There's a navigation pane (removed) in the original ebooks. 
6. We need to define styling for the pages. Section, subsection and table styling. 

PDF
---

1. ``1-200.html``, the tag ``<hr width="60%"/>`` needs to be replaced to ``<hr class = "smallrow tinyrow" />``
2. The page ``pdf-firstpage.html`` needs to be added after the cover page. 
3. The classes ``.text-level`` are different in the ``pdf.css`` that they would be in ``citation.css``. 
4. ``1-300.html``, the tags ``<li class = "text-level2">`` need spacing in PDF, so we need to add a second class called spaced ``<li class = "text-level2 spaced">``, in order to add a space and remove list bullet style.  
5. ``1-500.html``, the tag ``<p class ="text-level2">`` which contain the information "When available,..." needs to gain a slight ``margin-left`` of 30px, so replace this unique tag with ``<p class ="text-level2 left">``.
6. ``2-100.html``. There are a lot of inconsistency. One of the examples is missing.

EPUB
---
