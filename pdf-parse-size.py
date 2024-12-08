from pypdf import PdfReader

# The PDF spec defines the default user space unit as 1/72 inch.
# In theory a user could define their own unit, in practice it's unlikely.
defaultUserSpaceUnitsPerInch = 72.0

inputFilePath = "fixtures/2024-12-05-two-pages.pdf"

reader = PdfReader(inputFilePath)

print('')
print('PAGE SIZES:')

for i in range(len(reader.pages)):
    page = reader.pages[i]
    box = page.mediabox
    widthInches = box.width / defaultUserSpaceUnitsPerInch
    heightInches = box.height / defaultUserSpaceUnitsPerInch
    print(f'Page {i}: {box.width}x{box.height} units, or {widthInches}x{heightInches} inches')

print('')