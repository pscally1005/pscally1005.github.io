# format all csv and scale all images

import os
import glob
import csv
from PIL import Image

os.system('cls')

def scale_images_in_directory(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith("-scaled.jpg") or filename.endswith("-scaled.JPG"):
                continue
            elif filename.endswith(".jpg") or filename.endswith(".JPG"):
                filepath = os.path.join(root, filename)
                try:
                    img = Image.open(filepath)
                    
                    # Check for EXIF orientation and rotate if necessary
                    exif = img._getexif()
                    if exif:
                        orientation = exif.get(0x0112)
                        if orientation == 3:
                            img = img.rotate(180, expand=True)
                        elif orientation == 6:
                            img = img.rotate(270, expand=True)
                        elif orientation == 8:
                            img = img.rotate(90, expand=True)
                    
                    # Resize the image
                    width, height = img.size
                    new_width = int(width * 0.25)
                    new_height = int(height * 0.25)
                    resized_img = img.resize((new_width, new_height), Image.LANCZOS)
                    new_filepath = filepath[0:-4] + "-scaled.jpg"
                    resized_img.save(new_filepath)
                    # print(f"{filename} scaled successfully")
                    img.close()
                    os.remove(filepath)
                except Exception as e:
                    print(f"Error scaling {filename}: {e}")


def split_csv_file(path_csv):
    for fname in glob.glob(path_csv):

        # only use files that haven't been parsed yet
        if(fname[-10:] != "-facts.csv" and fname[-8:] != "-ing.csv"):
            with open(fname, 'r') as fin:
                data = fin.read().splitlines(True)

            # remove first and last few rows from file
            temp = fname[:-4] + "-temp.csv"
            with open(temp, 'w') as fout:
                fout.writelines(data[6:-5])

            # get row of blank (separation between 2 tables)
            blank = -1
            with open(temp, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ')
                i = 0
                for row in spamreader:
                    # print(', '.join(row))
                    # print(len(row))
                    if(len(row) == 0):
                        blank = i
                        # print(', '.join(row))
                        break
                    i += 1

            #  now, read from temp file
            with open(temp, 'r') as fin:
                data = fin.read().splitlines(True)

            # put first half in ingredients file
            ing = fname[:-4] + "-ing.csv"
            with open(ing, 'w') as fout:
                fout.writelines(data[:blank])

            # put second half in facts file
            facts = fname[:-4] + "-facts.csv"
            with open(facts, 'w') as fout:
                fout.writelines(data[blank+1:])

            # delete original and temp file
            os.remove(fname)
            os.remove(temp)
            os.remove(ing)

def main():
    path_images = r'C:\Users\mets1\Documents\website\assets\Misc\Serving'
    scale_images_in_directory(path_images)

    path_csv = r'C:\Users\mets1\Documents\website\_data\serving\*.csv'
    # path_csv = r'C:\Users\mets1\Documents\website\_data\meat\*.csv'
    split_csv_file(path_csv)


if __name__ == '__main__':
    main()