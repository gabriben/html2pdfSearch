from setuptools import setup

setup(name='html2pdfSearch',
      version='0.1',
      description='Search a collection of names in an html in a PDF',
      url='http://github.com/gabriben/html2pdfSearch',
      author='Gabriel Bénédict',
      author_email='gbndict@gmail.com',
      license='MIT',
      packages=['html2pdfSearch'],
      install_requires=['PyPDF2', 'bs4'],
      zip_safe=False)
