from pdf_is_consistent_size import pdfIsConsistentSize

inputFilePath = "fixtures/2024-12-05-sixteen-pages.pdf"
result = pdfIsConsistentSize(inputFilePath)

hasConsistentPageSize = result[0]
knownSize = result[1]

if hasConsistentPageSize:
    print(f'All pages are the same size: {knownSize["width"]}x{knownSize["height"]} units')
else:
    print('Pages have different sizes.')