# Download csv to /python/testing folder, and run script to swap amount and description columns

import pandas as pd
import os
import glob
import csv
import re

def fix_vol_col(mass, vol):
    if len(mass) != 0 and len(vol) == 0:
       if re.search('[a-zA-Z]', mass):
            temp = mass
            # mass = vol
            mass = 0
            vol = temp

    return mass, vol

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
                    row[1], row[3] = fix_vol_col(row[1], row[3])
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
