# Download csv to /python/testing folder, and run script to fix volume measurements in ingredients file

import pandas as pd
import os
import glob
import csv

def fix(vol):
    v = vol

    # cups
    if vol == "3/4 cup + 2tbsp, 3.5 oz":
        v = "3/4 cup + 2 tbsp, or 3.5 oz"
    elif vol == "1cup + 2tbsp":
        v = "1 cup + 2 tbsp"
    elif vol == "1/2cup + 1tbsp":
        v = "1/2 cup + 1 tbsp"
    if vol == "1/2cup + 2tbsp":
        v = "1/2 cup + 2 tbsp"
    elif vol == "1.25 cup":
        v = "1 1/4 cup"
    elif vol == "1.33 cup":
        v = "1 1/3 cup"
    elif vol == "1.5 cup":
        v = "1 1/2 cup"
    elif vol == "1.67 cup":
        v = "1 2/3 cup"
    elif vol == "1.75 cup":
        v = "1 3/4 cup"
    elif vol == "2.25 cup":
        v = "2 1/4 cup"
    elif vol == "2.33 cup":
        v = "2 1/3 cup"
    elif vol == "2.5 cup":
        v = "2 1/2 cup"
    elif vol == "2.67 cup":
        v = "2 2/3 cup"
    elif vol == "2.75 cup":
        v = "2 3/4 cup"
    elif vol == "3.25 cup":
        v = "3 1/4 cup"
    elif vol == "3.33 cup":
        v = "3 1/3 cup"
    elif vol == "3.5 cup":
        v = "3 1/2 cup"
    elif vol == "3.67 cup":
        v = "3 2/3 cup"
    elif vol == "3.75 cup":
        v = "3 3/4 cup"
    elif vol == "4.25 cup":
        v = "4 1/4 cup"
    elif vol == "4.33 cup":
        v = "4 1/3 cup"
    elif vol == "4.5 cup":
        v = "4 1/2 cup"
    elif vol == "4.67 cup":
        v = "4 2/3 cup"
    elif vol == "4.75 cup":
        v = "4 3/4 cup"

    # teaspoons
    elif vol == "1.25 tsp":
        v = "1 1/4 tsp"
    elif vol == "1.33 tsp":
        v = "1 1/3 tsp"
    elif vol == "1.5 tsp":
        v = "1 1/2 tsp"
    elif vol == "1.67 tsp":
        v = "1 2/3 tsp"
    elif vol == "1.75 tsp":
        v = "1 3/4 tsp"
    elif vol == "2.25 tsp":
        v = "2 1/4 tsp"
    elif vol == "2.33 tsp":
        v = "2 1/3 tsp"
    elif vol == "2.5 tsp":
        v = "2 1/2 tsp"
    elif vol == "2.67 tsp":
        v = "2 2/3 tsp"
    elif vol == "2.75 tsp":
        v = "2 3/4 tsp"
    elif vol == "3.25 tsp":
        v = "3 1/4 tsp"
    elif vol == "3.33 tsp":
        v = "3 1/3 tsp"
    elif vol == "3.5 tsp":
        v = "3 1/2 tsp"
    elif vol == "3.67 tsp":
        v = "3 2/3 tsp"
    elif vol == "3.75 tsp":
        v = "3 3/4 tsp"
    elif vol == "4.25 tsp":
        v = "4 1/4 tsp"
    elif vol == "4.33 tsp":
        v = "4 1/3 tsp"
    elif vol == "4.5 tsp":
        v = "4 1/2 tsp"
    elif vol == "4.67 tsp":
        v = "4 2/3 tsp"
    elif vol == "4.75 tsp":
        v = "4 3/4 tsp"

    # tablespoons
    elif vol == "1.25 tbsp":
        v = "1 1/4 tbsp"
    elif vol == "1.33 tbsp":
        v = "1 1/3 tbsp"
    elif vol == "1.5 tbsp":
        v = "1 1/2 tbsp"
    elif vol == "1.67 tbsp":
        v = "1 2/3 tbsp"
    elif vol == "1.75 tbsp":
        v = "1 3/4 tbsp"
    elif vol == "2.25 tbsp":
        v = "2 1/4 tbsp"
    elif vol == "2.33 tbsp":
        v = "2 1/3 tbsp"
    elif vol == "2tbsp + 1tsp":
        v = "2 tbsp + 1 tsp"
    elif vol == "2.5 tbsp":
        v = "2 1/2 tbsp"
    elif vol == "2.67 tbsp":
        v = "2 2/3 tbsp"
    elif vol == "2tbsp + 2tsp":
        v = "2 tbsp + 2 tsp"
    elif vol == "2.75 tbsp":
        v = "2 3/4 tbsp"
    elif vol == "3.25 tbsp":
        v = "3 1/4 tbsp"
    elif vol == "3.33 tbsp":
        v = "3 1/3 tbsp"
    elif vol == "3.5 tbsp":
        v = "3 1/2 tbsp"
    elif vol == "3.67 tbsp":
        v = "3 2/3 tbsp"
    elif vol == "3.75 tbsp":
        v = "3 3/4 tbsp"
    elif vol == "4.25 tbsp":
        v = "4 1/4 tbsp"
    elif vol == "4.33 tbsp":
        v = "4 1/3 tbsp"
    elif vol == "4.5 tbsp":
        v = "4 1/2 tbsp"
    elif vol == "4.67 tbsp":
        v = "4 2/3 tbsp"
    elif vol == "4.75 tbsp":
        v = "4 3/4 tbsp"
    elif vol == "9tbsp + 1tsp":
        v = "9 tbsp + 1 tsp"

    # cans
    elif vol == "14.5oz can" or vol == "14.5oz cans" or vol == "14.5 oz cans" or vol == "14.5oz can petite":
        v = "14.5 oz can"
    elif vol == "2x14.5oz can" or vol == "2x14.5oz cans" or vol == "2 14.5oz can" or vol == "2 14.5oz cans":
        v = "2 x 14.5 oz can"
    elif vol == "15.5oz can" or vol == "15.5oz cans" or vol == "15.5 oz cans" or vol == "1x15.5oz can" or vol == "1x15.5 oz can":
        v = "15.5 oz can"
    elif vol == "3/4 cup, liquid from 15.5oz can chickpeas":
        v = "3/4 cup, liquid from 15.5 oz can chickpeas"
    elif vol == "2x15.5oz can" or vol == "2x15.5oz cans" or vol == "2 15.5oz can" or vol == "2 15.5oz cans":
        v = "2 x 15.5 oz can"
    elif vol == "3x15.5oz can" or vol == "3x15.5oz cans" or vol == "3 15.5oz can" or vol == "3 15.5oz cans":
        v = "3 x 15.5 oz can"
    elif vol == "4x15.5oz can" or vol == "4x15.5oz cans" or vol == "4 15.5oz can" or vol == "4 15.5oz cans":
        v = "4 x 15.5 oz can"
    elif vol == "4x6.5oz cans, with juice" or vol == "4x6.5oz can, with juice":
        v = "4 x 6.5 oz can, with juice"

    # protein powder
    elif vol == "1.25 scoop":
        v = "1 1/4 scoop"
    elif vol == "1.33 scoop":
        v = "1 1/3 scoop"
    elif vol == "1.5 scoop":
        v = "1 1/2 scoop"
    elif vol == "1.67 scoop":
        v = "1 2/3 scoop"
    elif vol == "1.75 scoop":
        v = "1 3/4 scoop"
    elif vol == "2.25 scoop":
        v = "2 1/4 scoop"
    elif vol == "2.33 scoop":
        v = "2 1/3 scoop"
    elif vol == "2.5 scoop":
        v = "2 1/2 scoop"
    elif vol == "2.67 scoop":
        v = "2 2/3 scoop"
    elif vol == "2.75 scoop":
        v = "2 3/4 scoop"
    elif vol == "3.25 scoop":
        v = "3 1/4 scoop"
    elif vol == "3.33 scoop":
        v = "3 1/3 scoop"
    elif vol == "3.5 scoop":
        v = "3 1/2 scoop"
    elif vol == "3.67 scoop":
        v = "3 2/3 scoop"
    elif vol == "3.75 scoop":
        v = "3 3/4 scoop"

    return v

def main(path = ""):

    os.system('cls')

    if path == "":
        # path to csv files
        # path = r"C:\Users\mets1\Documents\website\_data\*-ing.csv"
        path = r"C:\Users\mets1\Documents\website\python\testing\*-ing.csv"
        # path = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\_data\*-ing.csv"
        # path = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\python\testing\*-ing.csv"
        print("empty path")

    # loop through all the files
    changed = 0
    for fname in glob.glob(path):

        with open(fname, 'r+', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

            i = 0
            for row in spamreader:
                temp = fname[:-4] + "-temp.csv"

                if len(row) == 4 and i != 0:
                    row[3] = fix(row[3])
                    line = '"' + row[0] + '",' + row[1] + ',' + row[2] + ',"' + row[3] + '"\n'
                else:
                    line = ','.join(row) + "\n"

                with open(temp, 'a') as fout:
                    fout.writelines(line)

                i = i+1

        os.remove(fname)
        os.rename(temp, fname)
        print(fname)
        changed += 1

    print(str(changed) + " files updated")

if __name__ == '__main__':
    main()
