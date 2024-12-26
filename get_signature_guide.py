# Given a pageCount, representing the number of pages
# in an input PDF,
# 
# Returns a "guide" for a PDF arranged into folios and signatures.
# This "guide" is an array of folios.
# A folio represents a double-sided page in the the output PDF.
# A folio has two pages, so a folio is an array of pages.
# Each page will be a diptych, combining two pages from the input PDF.
# So each page is a tuple of two integers, [leftPageIndex, rightPageIndex],
# with each page index referencing the original input PDF.
#
# If the provided pageCount is not evenly divisible by 4, we cannot
# produce a suitable guide, so we return None.
def getSignatureGuide(pageCount):
  # pageCount must be evenly divisible by 4
  if (pageCount % 4 != 0):
    return None
  # Each "folio" is a double-sided page, and each
  # page has two source pages arranged in a diptych.
  # Therefore, we need 1 folio for each 4 pages.
  # Note the using of the `//` integer divider here,
  # rather than `/` float divider.
  folioCount = pageCount // 4
  folios = []
  lastPageIndex = pageCount - 1
  # Iterate over the folio count, building each folio as we go
  for folioIndex in range(folioCount):
    offsetFacingIn = (folioIndex * 2) + 1
    offsetFacingOut = folioIndex * 2
    folioFront = [offsetFacingIn, lastPageIndex - offsetFacingIn]
    folioBack = [lastPageIndex - offsetFacingOut, offsetFacingOut]
    folios.append([folioFront, folioBack])
  # Return the array of folios
  return folios