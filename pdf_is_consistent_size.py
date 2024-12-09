from pypdf import PdfReader

# The PDF spec defines the default user space unit as 1/72 inch.
# In theory a user could define their own unit, in practice it's unlikely.
defaultUserSpaceUnitsPerInch = 72.0

def getPageSize(page):
  return { "width": page.mediabox.width, "height": page.mediabox.height}

# Given some input file,
# read the page sizes from the PDF file.
# Return [true, width, height] if all pages have the same size,
# or [false, null, null] otherwise.
def pdfIsConsistentSize(inputFilePath):
  reader = PdfReader(inputFilePath)
  pageSizes = list(map(getPageSize, reader.pages))

  isConsistent = True
  knownSize = None

  for pageSize in pageSizes:
      if knownSize is None:
          knownSize = pageSize
          continue
      isSameSize = knownSize == pageSize
      isConsistent = isConsistent and isSameSize

  if isConsistent:
      return [True, knownSize]
  else:
      return [False, None]

