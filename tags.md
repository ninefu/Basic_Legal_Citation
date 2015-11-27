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
Document defining all tags added to the HTML5 files in the Legal Citation Website. 

```
<abbreviation>
```

Tag used to be a generalized placeholder for abbreviations (excluding states abbreviations) a reader may search in the text. All abbreviations must be surrounded by this tag.

```
<citation>
```

Tag used to encapsule anything that's related to a citation and citation examples. This includes, but it's not limited to, the citations used in the example boxes. 

> Attributes:

  * **book =** book style used in the citation example, which can be either *BB*, bluebook, *ALWD* or *undefined*. 
    - *example:* ``<citation book = "BB"> </citation>``
  * **type =** type of citation (agency, attorney, treaty...) in case we have multiple citation types worth highlighting.
    - *example:* ``<citation type = "agency" > </citation>``

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

 >  **§1-000:**
    
* ![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png) *§ 1-100:* introductory text, no need for tagging. 
    * **Comments:** Each citation has a book name (Bluebook or ALWD) associated with it. 
*  ![ok](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/yellow-ok-icon.png) *§ 1-200:* first citation example found here (copyright case). Wrap the text around tags.
    * **Comments:** The example given is such that each part of the citation has an important meaning, but we're only considering the citation as a whole. We identified the "standard" attribute in a legal citation. 
        > *Cmty. for Creative Non-Violence v. Reid  , 490 U.S. 730 (1989).* 

    * The text prior to the citation (which includes the reason for this citation) may need to be wrapped around a ``<citation type = "standard" > </citation>`` tag as well. 
*   ![x](http://icons.iconarchive.com/icons/double-j-design/origami-colored-pencil/16/red-cross-icon.png) *§ 1-300:* principles of citation, no need for tagging.
    
 >  **§2-000:**
 
 >  **§3-000:**
 
 >  **§4-000:**
 
 >  **§5-000:**
 
 >  **§6-000:**
 
 >  **§7-000:**
