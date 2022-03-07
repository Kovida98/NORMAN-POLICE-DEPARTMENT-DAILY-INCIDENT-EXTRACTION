import urllib.request
import tempfile
import PyPDF2
import re
import sqlite3

def fetchincidents(url):
        headers = {}
            headers[
                User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

        data = urllib.request.urlopen(urllib.request.Request(url, headers=headers))
        return data



def extractincidents(data):

    fp = tempfile.TemporaryFile()

    # Write the pdf data to a temp file
    fp.write(data.read())

    # Set the curser of the file back to the begining
    fp.seek(0)

    # Read the PDF
    pdfReader = PyPDF2.pdf.PdfFileReader(fp)
    pagecount = pdfReader.getNumPages()

    # Get the first page
    page1 = pdfReader.getPage(0).extractText()
    sp_page1= page1.replace("NORMAN POLICE DEPARTMENT","")
    sp_page2 = sp_page1.replace("Daily Incident Summary (Public)", "")
    sp_page3=sp_page2.rstrip()


# Now get all the other pages
    for pagenum in range(1, pagecount):
        sp_page3 = sp_page3 + pdfReader.getPage(pagenum).extractText()

    s = re.split(r'\d*\/\d*\/\d{4}\s\d*:\d*', sp_page3)
    #print(s)
    f = re.findall(r'\d*\/\d*\/\d{4}\s\d*:\d*', sp_page3)
    #print(f)
    del s[0]

    l1 = []
    for i in range(len(s)):
        l1.append(f[i] + s[i])
    #print(l1)
    lis = []
    for i in l1:
        sp = i.split("\n")
        del sp[-1]
        lis.append(sp)
    del lis[-1]
    temp = []
    for i in lis:
        if len(i) < 5:
            temp.append(i)
            lis.remove(i)
        elif len(i) == 6:
            m=i[2]+i[3]
            i[2]=m
            del i[3]


    for i in range(len(temp)):
        j = len(temp[i])
        while len(temp[i]) < 5:
            temp[i].append('null')
        num = temp[i][j - 1]
        temp[i].pop(j - 1)
        temp[i].append(num)

    for j in temp:
        lis.append(j)
        #print(lis)

    tlis = []
    for i in lis:
        tlis.append(tuple(i))
    #print(tlis)
    return tlis
