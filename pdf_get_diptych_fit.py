from pypdf import PdfReader

# The PDF spec defines the default user space unit as 1/72 inch.
# In theory a user could define their own unit, in practice it's unlikely.
defaultUserSpaceUnitsPerInch = 72.0

# Given a page size and a target area,
# determine if two pages could fit within the target area.
# If the smaller page fits within the target area, return the coordinates
# of the top-left corner of both smaller pages within the target area, in the
# format [x1, y1, x2, y2].
# Else return and array of null.
#
# By default, the pages will be centered on both axes within the target area.
# There will be no space between them. If the spaceBetweenPages parameter is
# set, the pages will be separated by that amount of space.
def pdfGetDiptychFit(pageSize, targetArea, spaceBetweenPages=0):
  # The page with must not be greater than half the target area width
  if pageSize["width"] > (targetArea["width"] / 2):
    return [None, None, None, None]

  # The page height must not be greater than the target area height
  if pageSize["height"] > targetArea["height"]:
    return [None, None, None, None]

  # Imagining the target area as a and the pages as p,
  # and the space between the pages as s, we can visualize
  # the layout as something like:
  #
  # aaaaa aaaaa
  # appps spppa
  # appps spppa
  # aaaaa aaaaa
  #
  # With this mental model in mind:
  #
  # First we center the pages on x, pretending there's no space between them.
  x1 = (targetArea["width"] / 2) - pageSize["width"]
  x2 = targetArea["width"] / 2
  # Now we account for custom spacing. The first page will be shift to the left
  # when space is added, the second page will be shifted to the right.
  x1 -= (spaceBetweenPages / 2)
  x2 += (spaceBetweenPages / 2)
  # The pages will both be centered vertically, with identical y values.
  y1 = (targetArea["height"] - pageSize["height"]) / 2
  y2 = y1
  # Finally we return the co-ordinates for both pages
  return [x1, y1, x2, y2]
