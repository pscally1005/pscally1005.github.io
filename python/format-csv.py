# Download csv to /python/testing folder, and run script to split, ing fix, and vol fix

import os
import split
import ingredients
import volume
import grams

def main():
    os.system('cls')

    # path to csv files
    path1 = r"C:\Users\mets1\Documents\website\python\testing\*.csv"
    path2 = r"C:\Users\mets1\Documents\website\python\testing\*-ing.csv"
    # path1 = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\python\testing\*.csv"
    # path2= r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\python\testing\*-ing.csv"

    split.main(path1)
    ingredients.main(path2)
    volume.main(path2)
    grams.main(path2)

if __name__ == '__main__':
    main()