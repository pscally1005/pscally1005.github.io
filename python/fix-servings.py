import pandas as pd
import os
import glob
import csv

def main():

    os.system('cls')

    # path to csv files
    # path = r"C:\Users\mets1\Documents\website\_data\*-ing.csv"
    path = r"C:\Users\mets1\Documents\website\python\testing\*-ing.csv"
    # path = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\_data\*.csv"
    # path = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\python\testing\*-ing.csv"

    # loop through all the files
    for fname in glob.glob(path):

        with open(fname, 'r+', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

            i = 0
            for row in spamreader:

                temp = fname[:-4] + "-temp.csv"

                if len(row) == 4 and i != 0:
                    line = '"' + row[0] + '",' + row[1] + ',' + row[2] + ',"' + row[3] + '"\n'
                else:
                    line = ','.join(row) + "\n"
                    line = line.replace(" ", "") 

                with open(temp, 'a') as fout:
                    fout.writelines(line)

                i = i+1

        os.remove(fname)
        os.rename(temp, fname)            
        print(fname)

if __name__ == '__main__':
    main()