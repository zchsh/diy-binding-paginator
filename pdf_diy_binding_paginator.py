import sys
import argparse

from pypdf import PdfReader, PdfWriter, PageObject, Transformation
from pdf_is_consistent_size import pdfIsConsistentSize
from pdf_get_diptych_fit import pdfGetDiptychFit
from get_signatures import getSignatures
from get_folios import getFolios
from offset_page_numbers import offsetPageNumbers
from pdf_add_sewing_dots import addSewingDots

parser = argparse.ArgumentParser(
        prog='ArgumentParserTest',
        description='Tests parsing arguments')

parser.add_argument('-i', '--input-file')
parser.add_argument('-o', '--output-file')
parser.add_argument('-s', '--scale')
parser.add_argument('-g', '--gutter')

args = parser.parse_args()

# Given two page objects, and two sets of co-ordinates,
# as well as a targetSize representing an output page target,
# Return a PageObject representing a diptych of both input pages
#
# TODO: could split this out, I think? Not really sure... it feels
# like a bit of a weird abstraction. But I'm fine with it for now.
def createDiptychPage(targetSize, pageLeft, pageRight, x1, y1, x2, y2, scaleFactor):
    # Create a new page with the target size
    outputPage = PageObject.create_blank_page(width=targetSize["width"], height=targetSize["height"])
    # Merge the left page onto the new page
    pageLeftTransform = Transformation().scale(scaleFactor, scaleFactor).translate(x1, y1)
    outputPage.merge_transformed_page(pageLeft, pageLeftTransform)
    # Merge the right page onto the new page
    pageRightTransform = Transformation().scale(scaleFactor, scaleFactor).translate(x2, y2)
    outputPage.merge_transformed_page(pageRight, pageRightTransform)
    # Return the output page
    return outputPage


# Define the input file path. This is PDF we'll be transforming for binding.
inputFilePath = args.input_file
outputFilePath = args.output_file

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

scaleRatio = float(args.scale)

knownSizeScaled = {
    "width": knownSize["width"] * scaleRatio,
    "height": knownSize["height"] * scaleRatio
}

gutter = float(args.gutter)

print('gutter')
print(gutter)

# Get the co-ordinates with which we'll merge the pages
x1, y1, x2, y2 = pdfGetDiptychFit(knownSizeScaled, targetSize, gutter)

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

# TODO: make these command line options maybe?
dotInset = 1.0 * 72
dotSpacing = 1.25 * 72
dotScale = 0.03
pageVerticalInset = (targetSize["height"] - knownSizeScaled["height"]) / 2
dotInsetCalc = pageVerticalInset + dotInset

# Use the folios specs to build the output PDF
inputPages = reader.pages
for folioSpec in folioSpecs:
  folioPageIndex = -1
  for folioPage in folioSpec:
    folioPageIndex += 1
    isInnerPage = folioPageIndex == len(folioSpec) - 1
    folioSideIndex = -1
    for folioSide in folioPage:
        folioSideIndex += 1
        isInnerSide = folioSideIndex == len(folioSide) - 1
        leftPageIndex, rightPageIndex = folioSide
        left = inputPages[leftPageIndex]
        right = inputPages[rightPageIndex]
        outputPage = createDiptychPage(targetSize, left, right, x1, y1, x2, y2, scaleRatio)
        if isInnerPage and isInnerSide: 
            outputPageWithDots = addSewingDots(outputPage, dotInsetCalc, dotSpacing, dotScale)
            merger.add_page(outputPageWithDots)
        else:
            merger.add_page(outputPage)

# Write and close the output PDF
merger.write(outputFilePath)
merger.close()
