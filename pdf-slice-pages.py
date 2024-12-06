from pypdf import PdfWriter

# Set up a writer class, this allows us to append and merge PDFs
writer = PdfWriter()

# Open the input PDF, `r` for read mode, `b` for binary mode
inputPdf = open("fixtures/2024-12-05-many-pages.pdf", "rb")

# Add the first 2 pages of inputPdf document to output
writer.append(fileobj=inputPdf, pages=(0, 2))

# Write to an output PDF document
output = open("fixtures/2024-12-05-two-pages.pdf", "wb")
writer.write(output)

# Close file descriptors
writer.close()
output.close()