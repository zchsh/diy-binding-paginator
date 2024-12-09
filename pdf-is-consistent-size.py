from pypdf import PdfReader

# The PDF spec defines the default user space unit as 1/72 inch.
# In theory a user could define their own unit, in practice it's unlikely.
defaultUserSpaceUnitsPerInch = 72.0

# Given some input file,
# read the page sizes from the PDF file.
# Return [true, width, height] if all pages have the same size,
# or [false, null, null] otherwise.
# TODO - write this function

inputFilePath = "fixtures/2024-12-05-sixteen-pages.pdf"

reader = PdfReader(inputFilePath)



def getPageSize(page):
  return { "width": page.mediabox.width, "height": page.mediabox.height}

pageSizes = list(map(getPageSize, reader.pages))

print('')
print('PAGE SIZES:')

for i in range(len(pageSizes)):
    pageSize = pageSizes[i]
    print(f'Page {i}: {pageSize["width"]}x{pageSize["height"]} units')

isConsistent = True
knownSize = None

for pageSize in pageSizes:
    if knownSize is None:
        knownSize = pageSize
        continue
    isSameSize = knownSize == pageSize
    isConsistent = isConsistent and isSameSize

print('')
print('IS CONSISTENT:')

if isConsistent:
    print(f'All pages are the same size: {knownSize["width"]}x{knownSize["height"]} units')
else:
    print('Pages have different sizes.')
