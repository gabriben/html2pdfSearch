# import packages
import PyPDF2
import re
import requests
from bs4 import BeautifulSoup
import codecs
    

def html2pdfSearch(url, pdfPath):
    names = collectNamesInHtml(url)

    occuringNames, fuzzyOccuringNames = searchInPDF(pdfPath, names)

    return occuringNames, fuzzyOccuringNames

        
# write a script that parses the html and find all elements where class = "name"
def collectNamesInHtml(url):
    # get the html
    html = requests.get(url)
    # parse the html
    soup = BeautifulSoup(html.text, 'html.parser')
    # find the names
    nameFields = soup.find_all('a', class_="name")
    names = []
    for n in nameFields:
        names.append(n.contents[0])
    # return the names
    return names

def searchInPDF(pdfPath, names):

    firstNames = []
    lastNames = []

    for n in names:
        lastNames.append(n.split()[1])
        firstNames.append(n.split()[0])

    
    # open the pdf file
    pdf = PyPDF2.PdfFileReader(pdfPath)
    # get number of pages
    NumPages = pdf.getNumPages()

    occuringNames = []
    fuzzyOccuringNames = []# either first name or last name only

    # extract text and do the search
    for i in range(0, NumPages):
        text = pdf.getPage(i).extractText()

        for f, l in zip(firstNames, lastNames):
            fResult = re.search(f, text)
            lResult = re.search(l, text)
            flResult = re.search(f + " " + l, text)
            lfResult = re.search(l + " " + f, text)
            FlResult = re.search(f[0] + ". " + l, text)
            LfResult = re.search(l[0] + ". " + f, text)

            if flResult is not None or flResult is not None or\
               FlResult is not None or LfResult is not None:
                if (f + " " + l) not in occuringNames:
                    occuringNames.append(f + " " + l)

            if fResult is not None and lResult is not None:
                if (f + " " + l) not in occuringNames:
                    if (f + " " + l) not in fuzzyOccuringNames:
                        fuzzyOccuringNames.append(f + " " + l)

    return occuringNames, fuzzyOccuringNames




occuringNames, fuzzyOccuringNames = html2pdfSearch("https://www.jmlr.org/tmlr/editorial-board.html", "main.pdf")
