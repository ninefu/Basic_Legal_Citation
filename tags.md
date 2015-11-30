![HTML5 TAGS](https://github.com/johncurcio/fluffy-rainbow-colored-unicorn/blob/master/tags.jpg?raw=true)

**Status:**

    - Tags created: 3
    - Tags documented: 3
    - Tags reviewed: 
        - By team: 3
        - By Sylvia: 0
    - Tags added to HTML: 0

# Tags
---
Document defining all tags added to the HTML5 files in the Legal Citation Website. All attributes and tags must not use plural form. 

```
<abbreviation>
```

Tag used to be a generalized placeholder for abbreviations (excluding states abbreviations) a reader may search in the text. All abbreviations must be surrounded by this tag.

> Attributes:

  * **type =** type of abbreviation.
    - nothing: it's just an abbreviation
    - 'omission': the abbreviation is an omission;     
        > *example:* ``<abbreviation omission> </abbreviation>``
    
    - 'state', 'month', 'journal', 'spacing', 'period'. 

Refer to page 1-400 for a full set of attributes that may be needed for the HTML files. 


```
<citation>
```

Tag used to encapsule anything that's related to a citation and citation examples. This includes, but it's not limited to, the citations used in the example boxes. 

> Attributes:

  * **book =** book style used in the citation example, which can be either *BB*, bluebook, *ALWD* or *undefined*. 
    - *example:* ``<citation book = "BB"> </citation>``
  * **form=** the citation can be either full or short to identify its form. 
  * **type =** type of citation (agency, attorney, treaty...) in case we have multiple citation types worth highlighting.
    - *example:* ``<citation type = "electronic" > </citation>``
    - *types identified:* 
        - 'electronic': used for electronic sources;
        - 'judicial' or 'case': used for judicial opinions. Cases might require attributes such as 'unpublished' and 'neutral';
        - 'constitution': used to cite constitutions;
        - 'statute': used to cite all statutes, and might need attributes such as 'session', 'bill', 'revenue';
        - 'ordinance': used to cite local ordinance citations;
        - 'treaty': used to cite treaty citation;
        - 'regulation': used to cite all regulation citations;
        - 'adjudication': used to cite agency adjudication citations;
        - 'report': used to cite agency report citations;
        - 'attorney': used in citations to attorney general and other advisory opinions. 
        - 'executive': used to cite executive orders citations;
        - 'proclamation': used to cite proclamation citations;
        - 'arbitration': used to cite arbitration decisions;
        - 'court': used to cite court rules;
        - 'books': used to cite books, it might be necessary to add attributes for the different kinds of books, such as 'annotations';
        - 'journal': used to cite journal article citations;
        - 'document': used to cite case document citations.

```
<quote>
```

A citation can be quoted. This tag identifies when it's a quote from a citation. 

```
<signals>
```

Citations may have signals. We can use this tag to identify those signals separetely. 

```
<state>
```

Tag used for states names and it's different types of state-related citations. 
>  Attributes:

  * **name =** full name of the U.S. state
    - *example:* ``<state name = "District of Columbia"> </state>``    
  * **abbr =** abbreviation of the state name in uppercase letters (optional)
    - *example:* ``<state name = "Detroit" abbr = "DT" > </state>``


# Pages overview
---

Explains briefly where each tags come from and which pages must (![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png)) and must not (![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png)) be tagged in order to make a complete metadata search bar. 

#### §1-000:
    
* ![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png) *§ 1-100:* introductory text, no need for tagging. 
    * **Comments:** Each citation has a book name (Bluebook or ALWD) associated with it. 
*  ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 1-200:* first citation example found here (copyright case). Wrap the text around tags.
    * **Comments:** The example given is such that each part of the citation has an important meaning, but we're only considering the citation as a whole. We identified the "standard" attribute in a legal citation. 
        > *Cmty. for Creative Non-Violence v. Reid  , 490 U.S. 730 (1989).* 

    * The text prior to the citation (which includes the reason for this citation) may need to be wrapped around a ``<citation type = "standard" > </citation>`` tag as well. 
*   ![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png) *§ 1-300:* principles of citation, no need for tagging.
*   ![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png) *§ 1-400:* explains what should be learned from the material, no need for tagging.
    * **Comments:** An ``abbreviation`` tag might be needed, as the reader must master a set of abbreviations. Abbreviations can represent: *reporters for contemporary federal decisions, codified federal statutes and regulations, regional reporters of state decisions, etc*.
    * If the abbreviation is associated with a ``state`` (another tag) law, they can represent: *the case reports, statutory compilations, and regulations of that state*. 

*   ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 1-500:* explains the change in North Dakota's citation, it needs to be tagged. 
    * **Comments:**  We may have to tag that "ND App" (North Dakota Court of Appeals) is now "ND"; and the examples in the page.
    
        > N.D. R. Ct. 11.6 (b). 

*  ![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png) *§ 1-600:* explains that citations are not centralized and there are a few books; may not need tagging.   
    * **Comments:**  There's a  citation example, but I don't consider that's important enough for a tag ``citation``.
    
        > Butner  v.  United States  , 440 U.S. 48, 55 (1979)  
    
#### §2-000:

* ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 2-100:* add tags ``citation`` to the examples in the page. 
    * **Comments:** This is probably the only tag necessary
        > ``<citation type = "electronic"></citation>``

* ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 2-200:* add tags ``citation`` to the examples in the page. 
    * **Comments:**  This is probably the only tag necessary, the attribute type can be either "judicial" or "case", followed by space and another attribute such as 'unpublished' or 'neutral'. 
        > ``<citation type = "case unpublished"></citation>``

* ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 2-300:* add tags ``citation`` to the examples in the page. 
    * **Comments:**  Add a tag ``citation`` with the attributes treaty, statute, constitution, and ordinance. The citation with statute attribute may contain a second attribute such as bill, session, act, revenue, etc.  
        > ``<citation type = "statute bill"></citation>``

* ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 2-400:* add tags ``citation`` to the examples in the page. 
    * **Comments:**  Identify the attributes regulation, attorney, agency etc. 
        > ``<citation type = "regulation"></citation>``

* ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 2-500:* add tags ``citation`` to the examples in the page. 
    * **Comments:**  Identify the attribute 'arbitration'. 
        > ``<citation type = "arbitration"></citation>``

* ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 2-600:* add tags ``citation`` to the examples in the page. 
    * **Comments:**  Identify the attributes 'court' and 'rule'. 
        > ``<citation type = "court rule"></citation>``

* ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 2-700:* add tags ``citation`` to the examples in the page. 
    * **Comments:**  Identify the attribute 'journal' and its special cases. 
        > ``<citation type = "journal"></citation>``

* ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 2-800:* add tags ``citation`` to the examples in the page. 
    * **Comments:**  Identify the attribute 'self' used to indicate the citation is an earlier from the same case. 
        > ``<citation type = "case self"></citation>``

#### §3-000:

 * ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ All:* add tags ``citation`` to the examples in each page. 

 * ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 3-200 to 3-400:* add tags ``state`` and ``abbreviation`` to each part of the examples they apply to. 

#### §4-000:

 * ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 4-100:* add tags ``abbreviation`` to the table in the page. Also add tags ``citation`` to the examples each abbreviation links to.  
 * ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 4-200:* add tags ``abbreviation`` to the table in the page.
 * ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 4-300:* add tags ``abbreviation`` with the attribute 'type' associated with it in the examples that include omission. 
 * ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 4-400 to 4-800:* add tags ``abbreviation`` with the attribute 'type' associated with it. 

#### §5-000:

*  ![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png) *§ 5-000:* explains how to create a citation and apply styling to it. No need for tagging.   
*  ![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png) *§ 5-100 to 5-300:* explains how to create a citation and apply styling to it. No need for tagging.
    * **Comments:**  We can maybe add a ``<definition>`` tag in case those kinds of definitions become important. But I doubt it will be the case. 

#### §6-000:

* ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 6-100:* Identify tag ``quote``. The section explains how to quote a citation. We have a few examples that need to be tagged. 
* ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 6-200:* Examples need to be tagged using the ``citation`` tag.  
 * ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 6-300:* Identify tag ``signals``. Used in citation examples that contain signals and in the signals themselves. 
 * ![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png) *§ 6-400:* No need for tagging. Only explains the order in which signals should be considered. 
 * ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 6-500:* Identify the attributes ``short`` and ``full`` used in the ``citation`` tag to indentify whether the citation is in the Short form or the Full form. 
 * ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 6-600:* Citation examples need to be properly tagged using ``citation`` and ``quote``.
 * ![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png) *§ 6-700:* No need for tagging. Explains what's a table of authorities and gives a very short example. 

#### §7-000:
 * ![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png) *§ 7-000:* No need for tagging. Explains the differences in Bluebook and ALWD.
 *  ![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png) *§ 7-100:* No need for tagging. Introduction to the theme.
 *  ![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png) *§ 7-200:* No need for tagging. Explains the differences in Bluebook's editions. 
 *  ![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png) *§ 7-300:* No need for tagging. However the cross reference table **might be important** to determine which book the citation is from.
 *  ![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png) *§ 7-400:* No need for tagging. However the cross reference table **might be important** to determine which book the citation is from.
 *  ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 7-500:* It should be already tagged at this point.
