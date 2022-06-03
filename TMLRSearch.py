from html2pdfSearch import html2pdfSearch

occuringNames, fuzzyOccuringNames = html2pdfSearch.html2pdfSearch("https://www.jmlr.org/tmlr/editorial-board.html", "main.pdf")

print(occuringNames)
print(fuzzyOccuringNames)
