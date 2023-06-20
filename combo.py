import os
import argparse
import PyPDF2

# Create argument parser
parser = argparse.ArgumentParser(description='Combine two PDF files into one.')
parser.add_argument('input_file1', help='name of the first input PDF file')
parser.add_argument('input_file2', help='name of the second input PDF file')
parser.add_argument('output_file', help='name of the output PDF file')
args = parser.parse_args()

# Create output directory if it doesn't exist
output_dir = os.path.dirname(args.output_file)
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Open input files
pdf1 = open(args.input_file1, 'rb')
pdf2 = open(args.input_file2, 'rb')

# Create PDF reader objects
reader1 = PyPDF2.PdfReader(pdf1)
reader2 = PyPDF2.PdfReader(pdf2)

# Create PDF writer object
writer = PyPDF2.PdfWriter()

# Add pages from first PDF file to writer object
for i in range(len(reader1.pages)):
    page = reader1.pages[i]
    writer.add_page(page)

# Add pages from second PDF file to writer object
for i in range(len(reader2.pages)):
    page = reader2.pages[i]
    writer.add_page(page)

# Write combined pages to output file
output = open(args.output_file, 'wb')
writer.write(output)

# Close input and output files
pdf1.close()
pdf2.close()
output.close()

print("PDF files combined successfully!")