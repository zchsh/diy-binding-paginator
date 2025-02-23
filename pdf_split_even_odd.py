import sys
import argparse

from pypdf import PdfReader, PdfWriter

parser = argparse.ArgumentParser(
	prog='PdfSplitEvenOdd',
	description='Split a PDF file into two separate PDF files, one with even pages, and the other with odd pages.')

parser.add_argument('-i', '--input-file')
args = parser.parse_args()

inputFilePath = args.input_file
inputFilePathParts = inputFilePath.rsplit('.', 1)
basePath = inputFilePathParts[0]
extension = inputFilePathParts[1]
outputFilePathEven = basePath + '-even' + '.' + extension
outputFilePathOdd = basePath + '-odd' + '.' + extension

inputpdf = PdfReader(open(inputFilePath, "rb"))
outputEvenPdf = PdfWriter()
outputOddPdf = PdfWriter()

for i in range(len(inputpdf.pages)):
    if i % 2 == 0:
        outputEvenPdf.add_page(inputpdf.pages[i])
    else:
        outputOddPdf.add_page(inputpdf.pages[i])

# Write out the PDFs
outputEvenPdf.write(outputFilePathEven)
outputEvenPdf.close()

outputOddPdf.write(outputFilePathOdd)
outputOddPdf.close()
