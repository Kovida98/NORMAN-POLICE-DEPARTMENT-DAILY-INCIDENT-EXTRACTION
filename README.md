## NORMAN POLICE DEPARTMENT,DAILY INCIDENT SUMMARY EXTRACTION

Norman, Oklahoma police regularly report arrests, incidents, and other
activities. This information is distributed to the public in PDF format
through their website [Reports PDF link.](https://www.normanok.gov/public-safety/police-department/crime-prevention-data/department-activity-reports)

I used my python programming abilities and linux commands to extract
the daily incident PDF reports for this project.
To finish this project, I successfully completed following tasks:
1. From their website, I downloaded one PDf file.
2. Extracted the data from the PDf file.
3. To store the data, I created a SQLite database.
4. Inserted the data in to the database.
5. Printed each nature and count of number of times it appeared.

## AUTHOR
Kovida Mothukuri  

Author Email: kovida.mothukuri-1@ou.edu

## TREE STRUCTURE

```
├── LICENSE
├── README.md
├── normanpd.db
├── project0
│    ├── __init__.py
│    └── main.py
├── requirements.txt
├── docs/
├── setup.cfg
├── setup.py
└── tests
    ├── test_createdb.py
    ├── test_download.py
    ├── test_extractincidents.py
    ├── test_populateDB.py
    └── test_status.py
```

## PACKAGES USED

To run this code we require following packages:
1. urllib.request
2. tempfile
3. PyPDF2
4. re
5. sqlite3
6. import argparse


## FUNCTIONS
I made a folder called project0 with two files titled `__init__.py` and
main.py in it.
I've written code for five functions in the `__init__.py` file. I called
all these functions that I wrote in `__init__.py` in the main.py file.

1. **fetchincidents():**
    As an input parameter, I passed url. To read the file, I used 
    urlib.request.urlopen to open it from the website of the Norman 
    Police Department.This function returns a byte stream named data.
2. **extractincidents():**
    In a brief, this function reads PDF file and extracts incidents,
    which contain values of data/time, incident number, location,
    nature, and incident ORI.
    In this function we will pass data which is returned from 
    fetchincidents() function.
    we are using  PyPdf2.pdf.PdfFileReader class to extract pages 
    and text from those pages.
    The extracted rows from all of the pages are string type. 
    
    So, first, I split the string using the date/time regex
    `r'\d*\/\d*\/\d{4}\s\d*:\d*'`, which gives
    me a list of each and every row as a string without date/time values
    say s, and then I created a list of date/time values, f, using the
    findall method. I made a new list called l1, to which I appended 
    all of the values from lists s and f in the proper order.

    List l1 is a list of strings of each row in a PDF file, with `'\n'`
    characters between each value in the string. To get rid of those 
    `'\n'` characters in between, I broke the list up by character and 
    appended it to another new list named lis.
    In each and every document we have a date at the end of last page
    in the middle which is not necessary. Using del, I was able to 
    remove that date.
    List lis contains the list of values of each row.

    Now, by iterating through sequence of parameters in lis, if the 
    length of that particular list is less than 5 then i have removed
    those lists from lis and appended in to the new list temp which 
    segregates all the rows which have blank spaces in PDF file.
    Added null in the blank spaces by iterating through list temp and
    appended those to the list lis.If the length is equal to 6, then
    we have to merge the string in indexes 2 and 3 and placed that 
    merged string in the correct position.

    Finally,by iterating through sequence of parameters in list lis,
    I changed the type of parameter from list to tuple.This function
    returns a list of values of each row in the form of tuple.

3. **createdb():**
    This function creates a database named "normanpd.db" and a table
    if it doesn' t exist already named incidents with the columns 
    incident time,incident number,incident location,nature,incident ori
    using cur.execute(), which accepts the sql query.

4. **populatedb():**
    As an input parameters, i passed cur and tuplelist which is 
    returned from extractincidents function.Here, cur.executemany()
    method is used to insert the values to the table by iterating 
    through the sequence of parameters in tuple.
    `cur.executemany('INSERT INTO incidents VALUES (?,?,?,?,?)', tlis)`
    Here, before inserting the values i am deleting the values in table
    to avoid inserting the same values when we execute more than one time
    simultaneously.

6. **status():**
    From the database, this function displays the nature and the
    number of times it has occurred first by sorting with total 
    number of incidents and then alphabetically by the nature 
    and separated by pipe symbol. Here, the function returns list
    of tuple of nature and count of it.Here is the query to get the
    desired results: 
    `SELECT nature, count(nature) FROM incidents where nature is not null GROUP BY nature ORDER BY count(nature) DESC,nature ASC`

##TEST CASES:

Here i have created a folder named tests which contains five test cases 
files to test each function which i have written in `__init__.py`.


1. **test_fetch_incidents():** Here in this function, i am testing the
    funtion fetchincidents() by passing the url whether the data 
    returned by it is not none.
2. **test_extractincidents():** In this function i am testing the function 
    extractincidents() by considering three conditions.
    1. checked whether the list returned by the funtion extractincidents()
        is not none.
    2. Checked whether the type of that returning object is list.
    3. Actually, in my code function extractincidents() returns a list of
        tuple of values of each row of length five.so i checked the length 
        of each tuple is five by iterating through the list.
3. **test_createDB():** In this function, i checked whether the table
    created or not by calling the function createDB() in `__init__.py`.
4. **test_populateDB():** I tested the function populateDB by checking 
    whether the length or each row is equal to 5 or not after populating
    the table with values.
5. **test_status():** In this function, i am testing the length of each
    list is equal to 2 by iterating through the list which was returned
    from the function status() in `__init__.py`

   
## COMMANDS TO RUN:

Here to run the file we have to use below command

`pipenv run python project0/main.py --incidents <url>`


**For example:**

pipenv run python project0/main.py --incidents "https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-03_daily_incident_summary.pdf"

**Expected Output:**

```
Motorist Assist|26
Sick Person|21
Alarm|16
Welfare Check|13
Disturbance/Domestic|12
Transfer/Interfacility|12
Breathing Problems|10
```

To run test cases we can use any one of the following commands

`pipenv run pytest` or `pipenv run python -m pytest`

##ASSUMPTIONS and BUGS:

I assumed that all the incident report PDFs in their webpage has
empty spaces for the columns named location and nature and this project
works for the page of 5 columns. The code will not give desired
results if the empty spaces are in other columns and the number of
columns is other than 5. To clean the data, i have done some hard
coding like removing the spaces, deleting the headings in first page.
I assumed that the heading and subheading in first page should be 
`'NORMAN POLICE DEPARTMENT'` and `'Daily Incident Summary (Public)'` 
for every PDF. I assumed that every document has date at end of the 
last page.

## DIRECTIONS TO INSTALL 

You can create folders and files using mkdir and touch commands.
Here in this project we will be using python 3.10.2 version. to install that use this command.

`pipenv install --python 3.10.2`

After downloading the project from github, go to that directory using cd.Install pipenv by using
command. `pip install pipenv`. After that by checking requirements.txt file, you have to install all
required packages.  you need to install pytest using this command `pipenv install pytest`.Once the installation of pytest is done, you will be able to
run the unittests using `pipenv run python -m pytest`. you can run the code using
`pipenv run python project0/main.py --incidents <url>`.



## EXTERNAL LINKS USED:

[https://pythonhosted.org/PyPDF2/PdfFileReader.html](https://pythonhosted.org/PyPDF2/PdfFileReader.html) 

[https://www.tutorialspoint.com/sqlite/sqlite_create_database.htm](https://www.tutorialspoint.com/sqlite/sqlite_create_database.htm) 

[https://www.w3schools.com/python/python_regex.asp](https://www.w3schools.com/python/python_regex.asp)

[https://www.csestack.org/python-pytest/](https://www.csestack.org/python-pytest/)





