# Given a signaturePageCount, representing the number of pages
# in a signature that needs to be generated,
# 
# Returns a "guide" for a set of folios that make up the specific signature.
# This "guide" is an array of folios.
# A folio represents a double-sided page in the the output PDF.
# A folio has two pages, so a folio is an array of pages.
# Each page will be a diptych, combining two pages from the input PDF.
# So each page is a tuple of two integers, [leftPageIndex, rightPageIndex],
# with each page index referencing the original input PDF.
#
# If the provided signaturePageCount is not evenly divisible by 4, we cannot
# produce a suitable guide, so we return None.
def getFolios(signaturePageCount):
  # signaturePageCount must be evenly divisible by 4
  if (signaturePageCount % 4 != 0):
    return None
  # Each "folio" is a double-sided page, and each
  # page has two source pages arranged in a diptych.
  # Therefore, we need 1 folio for each 4 pages.
  # Note the using of the `//` integer divider here,
  # rather than `/` float divider.
  folioCount = signaturePageCount // 4
  folios = []
  lastPageIndex = signaturePageCount - 1
  # Iterate over the folio count, building each folio as we go
  for folioIndex in range(folioCount):
    offsetFacingIn = (folioIndex * 2) + 1
    offsetFacingOut = folioIndex * 2
    folioFacingIn = [offsetFacingIn, lastPageIndex - offsetFacingIn]
    folioFacingOut = [lastPageIndex - offsetFacingOut, offsetFacingOut]
    folios.append([folioFacingOut, folioFacingIn])
  # Return the array of folios
  return folios