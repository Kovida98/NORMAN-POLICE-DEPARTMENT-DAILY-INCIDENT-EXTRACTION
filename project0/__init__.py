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



