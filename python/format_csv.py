# Download csv to /python/testing folder, and run script to format the csv files correctly
# See formatCSV subfolder for specific sections

import os
from formatCSV import split
from formatCSV import ingredients
from formatCSV import amount_desc_swap
from formatCSV import volume
from formatCSV import vol_from_mass
from formatCSV import grams
from formatCSV import vol_dec_to_frac

def main():
    os.system('cls')

    # path to csv files
    path1 = r"C:\Users\mets1\Documents\website\python\testing\*.csv"
    path2 = r"C:\Users\mets1\Documents\website\python\testing\*-ing.csv"
    # path1 = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\python\testing\*.csv"
    # path2= r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\python\testing\*-ing.csv"

    split.main(path1)
    amount_desc_swap.main(path2)
    ingredients.main(path2)
    volume.main(path2)
    grams.main(path2)
    vol_from_mass.main(path2)
    vol_dec_to_frac.main(path2)

if __name__ == '__main__':
    main()
