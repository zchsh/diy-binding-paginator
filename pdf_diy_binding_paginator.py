import sys
import argparse

from pypdf import PdfReader, PdfWriter, PageObject
from pdf_is_consistent_size import pdfIsConsistentSize
from pdf_get_diptych_fit import pdfGetDiptychFit
from get_signatures import getSignatures
from get_folios import getFolios
from offset_page_numbers import offsetPageNumbers


parser = argparse.ArgumentParser(
        prog='ArgumentParserTest',
        description='Tests parsing arguments')

parser.add_argument('-i', '--input-file')
parser.add_argument('-o', '--output-file')

args = parser.parse_args()

# Given two page objects, and two sets of co-ordinates,
# as well as a targetSize representing an output page target,
# Return a PageObject representing a diptych of both input pages
#
# TODO: could split this out, I think? Not really sure... it feels
# like a bit of a weird abstraction. But I'm fine with it for now.
def createDiptychPage(targetSize, pageLeft, pageRight, x1, y1, x2, y2):
    # Create a new page with the target size
    outputPage = PageObject.create_blank_page(width=targetSize["width"], height=targetSize["height"])
    # Merge the left page onto the new page
    outputPage.merge_translated_page(pageLeft, x1, y1)
    # Merge the right page onto the new page
    outputPage.merge_translated_page(pageRight, x2, y2)
    # Return the output page
    return outputPage


# Define the input file path. This is PDF we'll be transforming for binding.
inputFilePath = args.input_file
# outputFilePath = "/Users/zachshilton/Downloads/2025-02-22-observers-guide-paginated.pdf"
outputFilePath = args.output_file
# inputFilePath = "fixtures/2024-12-05-many-pages.pdf"
# outputFilePath = "fixtures/2024-12-30-demo-pdf-diy-binding-paginator-many-pages.pdf"

print(inputFilePath)
print(outputFilePath)

# Ensure the PDF has consistent page sizes
# If we don't have consistent page sizes, we won't be able to make this work.
# (In theory we could find clever ways around this... but meh! Maybe later.)
hasConsistentPageSize, knownSize = pdfIsConsistentSize(inputFilePath)
if hasConsistentPageSize:
    print(f'All pages are the same size: {knownSize["width"]}x{knownSize["height"]} units')
else:
    print('Pages have different sizes.')
    exit()

# Define the target size for our new PDF.
# (In theory, this could be derived from the input PDF page size...
# but in practice, it seems like it makes sense to let the user decide.)
targetSize = { "width": 800, "height": 600 }

# Get the co-ordinates with which we'll merge the pages
x1, y1, x2, y2 = pdfGetDiptychFit(knownSize, targetSize)

# If any of the co-ordinates were null, exit early
if x1 is None or y1 is None or x2 is None or y2 is None:
    print('Failed pdfGetDiptychFit. Target size may be too small to hold two pages.')
    exit()

# Read the input PDF
reader = PdfReader(inputFilePath)

# Get the count of pages in the input PDF
pageCount = len(reader.pages)

print("Page count:")
print(pageCount)

# If the page count isn't an evenly divisible by 4, we can't do much.
# Well, I guess we could add blank pages... but for now we print an error
if pageCount % 4 != 0:
    print("ERROR: page count needs to be divisible by 4.")
    print("TODO: learn how to actually throw an error... for now, whatever.")
    exit()

# Use the page count to get folio specifications

signatureSpecs = getSignatures(pageCount)

print("Signature spec:")
print(signatureSpecs)

folioSpecs = []
runningTotalPages = 0
for signaturePageCount in signatureSpecs:
  folioSpec = getFolios(signaturePageCount)
  withOffset = offsetPageNumbers(folioSpec, runningTotalPages)
  folioSpecs.append(withOffset)
  runningTotalPages += signaturePageCount

print("Folio specs:")
for folioSpec in folioSpecs:
  print(folioSpec)

# Initialize the output PDF
merger = PdfWriter()

#
# DEMO
#
# As a demo, make a couple diptych pages from the first four input pages.
# pages = reader.pages
# merger.add_page(
#     createDiptychPage(targetSize, pages[0], pages[1], x1, y1, x2, y2)
# )
# merger.add_page(
#     createDiptychPage(targetSize, pages[2], pages[3], x1, y1, x2, y2)
# )

# Use the folios specs to build the output PDF
inputPages = reader.pages
for folioSpec in folioSpecs:
  for folioPage in folioSpec:
    for folioSide in folioPage:
        leftPageIndex, rightPageIndex = folioSide
        left = inputPages[leftPageIndex]
        right = inputPages[rightPageIndex]
        outputPage = createDiptychPage(targetSize, left, right, x1, y1, x2, y2)
        merger.add_page(outputPage)

# Write and close the output PDF
# merger.write("fixtures/2024-12-22-demo-pdf-diy-binding-paginator.pdf")
merger.write(outputFilePath)
merger.close()
