from pypdf import PdfReader, PdfWriter, PageObject
from pdf_is_consistent_size import pdfIsConsistentSize
from pdf_get_diptych_fit import pdfGetDiptychFit

# Define the input file path. This is PDF we'll be transforming for binding.
inputFilePath = "fixtures/2024-12-05-sixteen-pages.pdf"

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

if pageCount % 4 != 0:
    print("ERROR: page count needs to be divisible by 4.")
    print("TODO: learn how to actually throw an error... for now, whatever.")

#
# PSEUDO-CODE
#
# Use the page count to get folio specifications
# runningTotalPages = 0
# signatureSpecs = getSignatures(pageCount)
# folioSpecs = []
# for signaturePageCount of signatureSpecs:
#   folioSpec = getFolios(signaturePageCount)
#   withOffset = offsetPages(folioSpecs, runningTotalPages)
#   folioSpecs.append(folioSpec)
#   runningTotalPages += signaturePageCount
# 

# Initialize the output PDF
merger = PdfWriter()

#
# TODO: split out a separate function, makeDiptychPage, or something
# Could use it here for the demo, and re-use for the "real" code to write.
#
# Add an example diptych page to the output PDF.
# Later, we'll want to loop through all pages in the input PDF,
# and use some magic to position pages so that when the output PDF
# is printed double-sided-flip-short-edge, we end up with the appropriate
# folios, which can be assembled into signatures, and bound into a book.
#
# But for now, we make a couple demo pages from the first four input pages.
# 
# Create a new page with the target size
demoPage = PageObject.create_blank_page(width=targetSize["width"], height=targetSize["height"])
# Merge the left page onto the new page
demoPage.merge_translated_page(reader.pages[0], x1, y1)
# Merge the right page onto the new page
demoPage.merge_translated_page(reader.pages[1], x2, y2)
# Add the merged page to the output PDF
merger.add_page(demoPage)
# Do it all again
demoPage2 = PageObject.create_blank_page(width=targetSize["width"], height=targetSize["height"])
demoPage2.merge_translated_page(reader.pages[2], x1, y1)
demoPage2.merge_translated_page(reader.pages[3], x2, y2)
merger.add_page(demoPage2)

#
# PSEUDO-CODE
#
# Use the folios specs to build the output PDF
# for folioSpec of folioSpecs:
#   for folioSide of folioSpec:
#      leftPageIndex, rightPageIndex = folioSide
#      # TODO make a diptych of leftPage + rightPage, push to PDF

# Write and close the output PDF
merger.write("fixtures/2024-12-22-demo-pdf-diy-binding-paginator.pdf")
merger.close()
