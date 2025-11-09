# Download csv to /python/testing folder, and run script to swap amount and description columns

import pandas as pd
import os
import glob
import csv
import re

def vol_from_mass(food, mass, vol):
    v = vol

    # Sugar, etc.
    if food == "Granulated sugar" or food == "Brown sugar" or food == "Granular sweetener: sugar, erythritol, stevia, etc." or food == "Allulose" or food == "Granulated monk fruit" or food == "Granulated stevia" or food == "Inulin":

        if mass == "12" or mass == "12.5" or mass == "15":
            v = "1 tbsp"
        elif mass == "25" or mass == "24":
            v = "2 tbsp"
        elif mass == "37.5" or mass == "37" or mass == "38" or mass == "36":
            v = "3 tbsp"
        elif mass == "50" or mass == "48":
            v = "1/4 cup"
        elif mass == "62.5" or mass == "62" or mass == "63" or mass == "60":
            v = "5 tbsp"
        elif mass == "67":
            v = "1/3 cup"
        elif mass == "75" or mass == "72":
            v = "6 tbsp"
        elif mass == "87.5" or mass == "87" or mass == "88" or mass == "84":
            v = "7 tbsp"
        elif mass == "100" or mass == "96":
            v = "1/2 cup"
        elif mass == "112.5" or mass == "112" or mass == "113" or mass == "108":
            v = "9 tbsp"
        elif mass == "125" or mass == "120":
            v = "10 tbsp"
        elif mass == "133":
            v = "2/3 cup"
        elif mass == "137.5" or mass == "137" or mass == "138" or mass == "132":
            v = "11 tbsp"
        elif mass == "150" or mass == "144":
            v = "3/4 cup"
        elif mass == "162.5" or mass == "162" or mass == "163" or mass == "156":
            v = "13 tbsp"
        elif mass == "175" or mass == "168":
            v = "14 tbsp"
        elif mass == "187.5" or mass == "187" or mass == "188" or mass == "180":
            v = "15 tbsp"
        elif mass == "200" or mass == "192":
            v = "1 cup"

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
                    row[3] = vol_from_mass(row[0], row[1], row[3])
                    line = '"' + row[0] + '",' + str(row[1]) + ',' + row[2] + ',"' + row[3] + '"\n'
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
