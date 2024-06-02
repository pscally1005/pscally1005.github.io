import pandas as pd
import os
import glob
import csv

# path to csv files
path = r"C:\Users\mets1\Documents\website\_data\*.csv"
# path = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\_data\*.csv"

# loop through all the files
changed = 0
for fname in glob.glob(path):

    # only use files that haven't been parsed yet
    if(fname[-10:] != "-facts.csv" and fname[-8:] != "-ing.csv"):
        with open(fname, 'r') as fin:
            data = fin.read().splitlines(True)

        # remove first and last few rows from file
        temp = fname[:-4] + "-temp.csv"
        with open(temp, 'w') as fout:
            fout.writelines(data[6:-7])

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

        # print(blank)
        
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

        print(fname)
            
        # os.remove(temp)
        # os.remove(ing)
        # os.remove(facts)

        changed += 1

print(str(changed) + " files updated")