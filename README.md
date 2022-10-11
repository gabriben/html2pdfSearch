# Search a collection of names in an html in a PDF

```python
from html2pdfSearch import html2pdfSearch

occuringNames, fuzzyOccuringNames = html2pdfSearch.html2pdfSearch("https://www.jmlr.org/tmlr/editorial-board.html", "main.pdf")
```

# installation

```
git clone https://github.com/gabriben/html2pdfSearch
cd html2pdfSearch
pip install -e .
