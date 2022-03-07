# cs5293sp22-project0
NORMAN POLICE DEPARTMENT,DAILY INCIDENT SUMMARY EXTRACTION

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

Email: kovida.mothukuri-1@ou.edu

## PACKAGES USED

To run this code we require following packages:
1. urllib.request
2. tempfile
3. PyPDF2
4. re
5. sqlite3
6. import argparse

## FUNCTIONS
I made a folder called project0 with two files titled __init__.py and
main.py in it.
I've written code for five functions in the __init__.py file. I called
these functions that I wrote in __init__.py in the main.py file.

1. **fetchincidents(url):**
    As an input parameter, I used url. To read the file, I used 
    urlib.request.urlopen to open it from the website of the Norman 
    Police Department.This function returns a byte stream named data.
2. **extractincidents(data):**
    In a brief, this function reads PDF file and extracts incidents,
    which contain values of data/time, incident number, location,
    nature, and incident ORI.
    In this function we will pass data which is returned from 
    fetchincidents() function.
    we are using  PyPdf2.pdf.PdfFileReader class to extract pages 
    and text from those pages.
    The extracted rows from all of the pages are string type. 
    
    So, first, I split the string using the data/time regex, which gives
    me a list of each and every row as a string without date/time values
    say s, and then I created a list of data/time values, f, using the
    findall method. I made a new list called l1, to which I appended 
    all of the values from lists s and f in the proper order.
    List l1 is a list of strings of each row in a PDF file, with \n
    characters between each value in the string. To get rid of those 
    \n characters in between, I broke the list up by character and 
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
    appended those to the list lis.if the length is equal to 6, then
    we have to merge the string in indexes 2 and 3 and placed that 
    merged string in the correct position.

    Finally,by iterating through sequence of parameters in list lis,
    I changed the type of parameter from list to tuple.This function
    returns a list of values of each row in the form of tuple.
3. **createdb():**
    This function creates a database named "normanpd.db" and a table
    if it doesnot exist already named incidents with the columns 
    incident time,incident number,incident location,nature,incident ori
    using cur.execute(), which accepts the sql query.
4. **populatedb(cur,tlis):**
    As an input parameters, i passed cur and tuplelist which is 
    returned from extractincidents function.Here, cur.executemany()
    method is used to insert the values to the table by iterating 
    through the sequence of parameters in tuple.
5. **status(cur):**
    From the database, this function displays the nature and the
    number of times it has occurred. Here, the function returns list
    of tuple of nature and count of it.
    
## COMMANDS TO RUN:

Here to run the file we have to use below command

pipenv run python project0/main.py --incidents <url>

pipenv run python project0/main.py --incidents "https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-03_daily_incident_summary.pdf"

To run test cases we can use any one of the following commands

pipenv run pytest or pipenv run python -m pytest

## EXTERNAL LINKS USED:

[https://www.tutorialspoint.com/sqlite/sqlite_create_database.htm](https://www.tutorialspoint.com/sqlite/sqlite_create_database.htm) , This link helped me to get more knowledge on how to write queries in SQLite3.

[https://www.w3schools.com/python/python_regex.asp](https://www.w3schools.com/python/python_regex.asp), I used this link to write regex expression.


