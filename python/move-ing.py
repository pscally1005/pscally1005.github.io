import os
import shutil

# Define source and destination folders
source_folder = r"C:\Users\mets1\Documents\website\_data\servingSizes"
destination_folder = r"C:\Users\mets1\Documents\website\_data\TEMP\new"

# Create destination folder if it doesn’t exist
os.makedirs(destination_folder, exist_ok=True)

# Loop through all files in the source folder
count = 0
for filename in os.listdir(source_folder):
    # Check if it’s a CSV file ending with "-ing.csv"
    if ("ing" in filename.lower()) or ("100g" in filename.lower()):
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(destination_folder, filename)

        # Move the file
        shutil.move(src_path, dst_path)
        print(f"Moved: {filename}")
        count += 1

print("✅ Done moving CSV files.")
print("Changed " + str(count) + " files")
