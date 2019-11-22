"""
Created on Fri Nov 22 17:47:35 2019

@author: Pedro Augusto Danna
"""

import PyPDF2

#Change this string bellow with the path of the file you want to convert
file_location = "sample.pdf"

with open(file_location,'rb') as file_obj:
    pdf_reader = PyPDF2.PdfFileReader(file_obj)
    raw = pdf_reader.getPage(0).extractText()

print(raw)

