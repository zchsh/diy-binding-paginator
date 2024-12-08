from pypdf import PdfWriter

inputFilePath = "fixtures/2024-12-05-many-pages.pdf"
outputFilePath = "fixtures/2024-12-05-two-pages.pdf"

# Set up a writer class, this allows us to append and merge PDFs
writer = PdfWriter()

# Open the input PDF, `r` for read mode, `b` for binary mode
inputPdf = open(inputFilePath, "rb")

# Add the first 2 pages of inputPdf document to output
writer.append(fileobj=inputPdf, pages=(0, 2))

# Write to an output PDF document
output = open(outputFilePath, "wb")
writer.write(output)

# Close file descriptors
writer.close()
output.close()