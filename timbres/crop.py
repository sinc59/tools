#!/usr/bin/python3
import PyPDF2
from os import listdir
from os.path import isfile, join

rows=[683,561,442,324,204]
columns=[74,360]
x1=74
y1=685
num=0
pageNum=0
largeur=173.5
hauteur=90

source="sources/test.pdf"
dirDest="sources/timbres/"

reader = PyPDF2.PdfFileReader(source)
while pageNum < reader.getNumPages():
    page = reader.getPage(pageNum)
    pageNum+=1
    for row in rows:
        for column in columns:
            x1=column
            y1=row
            x2=x1+largeur
            y2=y1+hauteur
            page.cropBox.upperLeft = [x1, y1]
            page.cropBox.lowerRight = [x2,y2]
            writer = PyPDF2.PdfFileWriter()
            writer.addPage(page)
            with open(dirDest+'cropped-'+str(num)+'.pdf', 'wb') as outfp:
                writer.write(outfp)
            num+=1
