from pypdf import PdfReader, PageObject, Transformation

# The PDF spec defines the user space unit as 1/71 inch.
# In theory a user could define their own unit, in practice it's unlikely.
defaultUserSpaceUnitsPerInch = 72.0

def getPageSize(page):
    return { "width": page.mediabox.width, "height": page.mediabox.height }

def getCoords(centerCoords, pageSize):
    centerX, centerY = centerCoords
    lowerLeftX = centerX - (pageSize["width"] / 2)
    lowerLeftY = centerY - (pageSize["height"] / 2)
    return [lowerLeftX, lowerLeftY]

def addSewingDots(page, insetUnits, spacingUnits, dotScale):
    pageSize = getPageSize(page)
    pageCenterX = pageSize["width"] / 2
    # TODO: maybe make this an argument to the function?
    dotFilePath = "./circle.pdf"
    # Read in the dot page
    reader = PdfReader(dotFilePath)
    dotPage = reader.pages[0]
    dotPageSize = getPageSize(dotPage)
    dotSize = { "width": dotPageSize["width"] * dotScale, "height": dotPageSize["height"] * dotScale }
    # Define transforms for each of the dots
    # TODO: determine co-ordinates for the top, upper, lower, and bottom dots
    # TODO: add the upper, lower, and bottom dots as well
    # top
    dotTopPos = pageSize["height"] - insetUnits
    dotTopX, dotTopY = getCoords([pageCenterX, dotTopPos], dotSize)
    dotTopTransform = Transformation().scale(dotScale, dotScale).translate(dotTopX, dotTopY)
    # upper
    dotUpperPos = dotTopPos - spacingUnits
    dotUpperX, dotUpperY = getCoords([pageCenterX, dotUpperPos], dotSize)
    dotUpperTransform = Transformation().scale(dotScale, dotScale).translate(dotUpperX, dotUpperY)
    # bottom
    dotBottomPos = insetUnits
    dotBottomX, dotBottomY = getCoords([pageCenterX, dotBottomPos], dotSize)
    dotBottomTransform = Transformation().scale(dotScale, dotScale).translate(dotBottomX, dotBottomY)
    # lower
    dotLowerPos = dotBottomPos + spacingUnits
    dotLowerX, dotLowerY = getCoords([pageCenterX, dotLowerPos], dotSize)
    dotLowerTransform = Transformation().scale(dotScale, dotScale).translate(dotLowerX, dotLowerY)
    # Add the dots to the page
    page.merge_transformed_page(dotPage, dotTopTransform)
    page.merge_transformed_page(dotPage, dotUpperTransform)
    page.merge_transformed_page(dotPage, dotLowerTransform)
    page.merge_transformed_page(dotPage, dotBottomTransform)
    # Return the output page
    return page

