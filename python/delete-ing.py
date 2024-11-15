import os
import glob

# Specify the directory you want to search in
os.system('cls')
path = r"C:\Users\mets1\Documents\website\python\testing"
# path = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\python\testing"

# Search for all CSV files ending with '-ing.csv' in the specified directory
csv_files = glob.glob(os.path.join(path, '*-ing.csv'))

# Delete each file found
count = 0
for file_path in csv_files:
    try:
        os.remove(file_path)
        print(f"Deleted: {file_path}")
        count += 1
    except Exception as e:
        print(f"Error deleting {file_path}: {e}")

print(str(count) + " files have been deleted.")
