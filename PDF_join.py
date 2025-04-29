import os
from PyPDF2 import PdfMerger

# List of PDFs to merge (replace with your actual file paths)
pdf_files = ['1.pdf', '2.pdf', '3.pdf', '4.pdf', '5.pdf', '6.pdf', '6.pdf', '7.pdf', '8.pdf', '9.pdf']

# Create a merger object
merger = PdfMerger()

# Append each PDF
for pdf in pdf_files:
    merger.append(pdf)

# Write out the merged PDF
output_filename = 'merged_output.pdf'
merger.write(output_filename)
merger.close()

print(f'Merged PDF saved as {output_filename}')
