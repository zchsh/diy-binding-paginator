# Given a guide, which is an array of folios, where each folio is
# an array of sides and each side is a tuple of two page index integers,
# and also given an offset integer,
#
# Return the input guide but with all page index integers adjusted by
# adding the provided offset.
def offsetPageNumbers(guide, offset):
  guideWithOffset = []
  for fi, folio in enumerate(guide):
    folioWithOffset = []
    for si, side in enumerate(folio):
      sideWithOffset = []
      for pageIndex in side:
        sideWithOffset.append(pageIndex + offset)
      folioWithOffset.append(sideWithOffset)
    guideWithOffset.append(folioWithOffset)
  return guideWithOffset