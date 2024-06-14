import os
import split
import ingredients
import volume

def main():
    # path to csv files
    # path = r"C:\Users\mets1\Documents\website\_data\*.csv"
    path = r"C:\Users\mets1\Documents\website\python\testing\*.csv"
    # path = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\_data\*.csv"
    # path = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\python\testing\*.csv"

    split.main(path)
    ingredients.main(path)
    volume.main(path)

if __name__ == '__main__':
    main()