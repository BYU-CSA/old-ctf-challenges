# BYU OSINT Series
This is a BYU focused OSINT Series. You will be faced with challenges dealing primarily with tools, websites and other offerings by BYU. 
NO active scanning or reconaissance is required! BIG NO NO.  Googling, Exploring the depths of BYU's pages and simply Point-and-Click is all that is required, apart from dilligence and logical thinking. 
These challenges may involve logging in with CAS to various sites, but are available to all students.
The first three are in series, and the rest are independant from one another. 

Goodluck!
-----
## Challenge #1  Mediun
Welcome! Like the first week of school, this is your first challenge. 

BYU once beat Georgia Tech, 38-20.
Around that time, BYU IT program seniors had the possibility of working in small groups under a few guests to BYU. 
Two guests have .edu email accounts available. The flag  is the longer of the two emails.

byuctf{email}
i.e. byuctf{wyatt.p.pangerl@TheOhioState.edu}


<details>
  <summary>Solution</summary>

```  
 Flag: byuctf{dgayler@kennesaw.edu}
https://learningsuite.byu.edu/view/HWt6Oton5IH1.html#instructorInformation
syllibi.byu.edu -> Fall 2013 -> Senior Classes, -> IT 446-> Dick Gayler or Rob Byrd -> dgayler@kennesaw.edu
  ```
</details>


## Challenge #2 Medium
-----
Although we love our 3rd floor classrooms, often a lot of IT&C classes are given on the 2nd floor of the Crabtree. 
Who taught the same class as the problem before, but nine years previously?


byuctf{Last name, First Middle}
i.e. byuctf{Giboney, Justin Superman}


<details>
  <summary>Solution</summary>

```
Flag: byuctf{Romney, Gordon Wilson}

Google byu rooms
https://y.byu.edu/class_schedule/cgi/classRoom.cgi
9 years before = 2004 
2nd floor of CTB: 240-250 classrooms
240, fall 2004, IT 446 - Romney Gordon Wilson

```
  
</details>


## Challenge #3 Easy
-----
One class that shares that room stands out as foreign, compared to the others. What's that professor's name and main rate my professor score?

byuctf{first_last_score}
i.e. byuctf{justin_giboney_5}


<details>
  <summary>Solution</summary>

```
Flag: byuctf{debra_robbins_4}
Class: Chinese 101, 
Professor Debra Robins
rate my professor score: 4
```
</details>






## Challenge #4 Easy 
-----
Can you find the database language patch version for this BYU scheduling software?
https://emsweb.byu.edu/VirtualEMS/Default.aspx

byuctf{version number}
ie byuctf{12.345.6789}


<details>
  <summary>Solution</summary>
 
```
Flag: byuctf{202002100}
click the question mark, followed by "About" drop down option. 
SQL Patch version -> 202002100
```
</details>



## Challenge #5 Medium
-----
we all know how fancy the new engineering building is. Can you find the brand of AC units mounted on top of the building?

byuctf{companyname}
i.e. byuctf{tacobell}


<details>
  <summary>Solution</summary>

```
Flag: byuctf{vekton}

https://3dbyu.byu.edu/model-directory
Using Version 2, you can pan and zoom into the roof of the EB to view in multiple words saying VekTon. 
```
</details>




## Challenge #6 Medium
-----
Can you find the earliest suggested browser and version # for a site used by prospective BYU students to apply to BYU?

byuctf{browser_version#}
i.e. byuctf{chrome_5.0}

<details>
  <summary>Solution</summary>
 
```
Flag: byuctf{netscape_4.0}

Earliest suggests old, therefor looking to webarchive for the best site.
Students should try admissions.byu.edu or some other combination. 
This will direct you to a form of the following link. 
They then need to identify that Netscape is a browser. 
https://web.archive.org/web/19980430235838/http://ar.byu.edu:80/admissions/
```
</details>





## Challenge #7 Medium
-----
What month and year did LSIT (college of life sciences IT) most recently switch their phone system?

byuctf{month_year}
i.e. byuctf{january_1900}

<details>
  <summary>Solution</summary>

```
Flag: byuctf{june_2022}

Google BYU LSIT phone 
https://www.google.com/search?q=BYU+LSIT+phone&rlz=1C1CHBF_enUS1004US1004&oq=byu+lsit+phone&aqs=chrome.0.69i59.4597j0j1&sourceid=chrome&ie=UTF-8
https://lifesciences.byu.edu/it
https://lifesciences.byu.edu/ringcentral-migration-from-cisco-ip-phones
```
</details>




## Challenge #8 Insane
-----
Let's say for purely scientific reasons that you wanted to perform research on a rodent from a central entity on campus. 
Once on the actual site to order, who would you email for assistance in obtaining an approved account? 

flag: byuctf{email}
i.e. byuctf{wyattt.p.pangerl@TheOhioStateUniversity.byu.edu}


<details>
  <summary>Solution</summary>
  
```
Flag: byuctf{sgarrett@byu.edu}

https://cac.byu.edu/animalOrders
```

</details>
