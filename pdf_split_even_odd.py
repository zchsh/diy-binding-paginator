from pypdf import PdfReader, PdfWriter

inputFilePath = "/Users/zachshilton/Downloads/2025-02-22-observers-guide-paginated.pdf"
# TODO: could derive the below from the above, but I'm too lazy right now
outputFilePathEven = "/Users/zachshilton/Downloads/2025-02-22-observers-guide-paginated-even.pdf"
outputFilePathOdd = "/Users/zachshilton/Downloads/2025-02-22-observers-guide-paginated-odd.pdf"

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