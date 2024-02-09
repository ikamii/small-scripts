"""
 _ _                   _ _ _____ 
(_) | ____ _ _ __ ___ (_|_)___ / 
| | |/ / _` | '_ ` _ \| | | |_ \ 
| |   < (_| | | | | | | | |___) |
|_|_|\_\__,_|_| |_| |_|_|_|____/ 
                                
"""


import argparse
from pypdf import PdfMerger
import os

# Set up argument parser
parser = argparse.ArgumentParser(description="Merge specified PDF files")
parser.add_argument('-d', '--directory', type=str, help='Directory containing PDF files to merge')
parser.add_argument('-o', '--output', type=str, required=True, help='Name of the output merged PDF file')
parser.add_argument('-f', '--files', nargs='+', help='List of PDF files to merge')

# Parse arguments
args = parser.parse_args()

# Initialize PdfMerger object
merger = PdfMerger()

if args.files:
    # Merge files specified in the list
    for filename in args.files:
        try:
            with open(filename, 'rb') as f:
                merger.append(f)
        except Exception as e:
            print(f"Error opening file {filename}: {e}")
elif args.directory:
    # Check if directory exists
    if not os.path.isdir(args.directory):
        raise ValueError(f"The specified directory does not exist: {args.directory}")

    # Retrieve and sort the list of filenames
    sorted_files = sorted([file for file in os.listdir(args.directory) if file.endswith('.pdf')])

    # Append each sorted pdf to the merger
    for filename in sorted_files:
        file_path = os.path.join(args.directory, filename)
        try:
            with open(file_path, 'rb') as f:
                merger.append(f)
        except Exception as e:
            print(f"Error opening file {file_path}: {e}")
else:
    raise ValueError("Either a directory or a list of files must be provided")

# Write out the merged PDF to the specified output file
try:
    merger.write(args.output)
    merger.close()
    print(f"Merged PDF created at {args.output}")
except Exception as e:
    print(f"Error writing merged PDF: {e}")
