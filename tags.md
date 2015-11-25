# Tags
---
Document defining all tags added to the HTML5 files in the Legal Citation Website. 
```
<citation>
```

Tag used to encapsule anything that's related to a citation and citation examples. 

> Attributes:
  * **book =** book style used in the citation example, which can be either *BB*, bluebook, *ALWD* or undefined.
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

```
<abbreviation>
```

Tag used to be a generalized placeholder for abbreviations a reader must remember in the text. All abbreviations must be surrounded by this tag.
