# Download csv to /python/testing folder, and run script to fix grams in ingredients file

import pandas as pd
import os
import glob
import csv

def grams(food, mass, vol):
    # Salt
    if food == "Salt":
        if mass == "1" and vol == "1/4 tsp":
            return str("1.5")
        elif mass == "2" and vol == "1/4 tsp":
            return str("1.5")
        elif mass == "4" and vol == "3/4 tsp":
            return str("4.5")
        else:
            return str(mass)
    
    # Extracts
    elif (food == "Liquid monk fruit" or food == "Vanilla extract" or food == "Almond extract"):
        if mass == "1" and vol == "1/4 tsp":
            return str("1.25")
        elif mass == "2" and vol == "1/2 tsp":
            return str("2.5")
        elif mass == "3" and vol == "1/2 tsp":
            return str("2.5")
        elif mass == "3" and vol == "3/4 tsp":
            return str("3.75")
        elif mass == "4" and vol == "3/4 tsp":
            return str("3.75")
        elif mass == "7" and vol == "1/2 tbsp":
            return str("7.5")
        elif mass == "8" and vol == "1/2 tbsp":
            return str("7.5")
        else:
            return str(mass)
        
    # Spices
    elif (food == "Garlic powder" or food == "Onion powder" or food == "Black pepper, ground"):
        if mass == "0" and vol == "1/4 tsp":
            return str("0.75")
        if mass == "1" and vol == "1/4 tsp":
            return str("0.75")
        if mass == "1" and vol == "1/2 tsp":
            return str("1.5")
        if mass == "2" and vol == "1/2 tsp":
            return str("1.5")
        elif mass == "4" and vol == "1 tsp":
            return str("3")
        elif mass == "5" and vol == "1/2 tbsp":
            return str("4.5")
        else:
            return str(mass)
    
    # Water
    elif food == "Water":
        if mass == "44" and vol == "3 tbsp":
            return str("45")
        elif mass == "237" and vol == "1 cup":
            return str("240")
        elif mass == "474" and vol == "2 cup":
            return str("480")
        elif mass == "711" and vol == "3 cup":
            return str("720")
        elif mass == "948" and vol == "4 cup":
            return str("960")
        elif mass == "1185" and vol == "5 cup":
            return str("1200")
        else:
            return str(mass)
    
    # Milk
    elif food == "Skim milk":
        if mass == "245" and vol == "1 cup":
            return str("240")
        elif mass == "490" and vol == "2 cup":
            return str("480")
        elif mass == "735" and vol == "3 cup":
            return str("7200")
        elif mass == "980" and vol == "4 cup":
            return str("960")
        elif mass == "1225" and vol == "5 cup":
            return str("1200")
        else:
            return str(mass)
        
    # Liquid tbsp
    elif (food == "Extra virgin olive oil" or food == "Extra virgin coconut oil" or food == "Balsamic vinegar" or food == "Soy sauce, low sodium, gluten free"):
        if mass == "7" and vol == "1/2 tbsp":
            return str("7.5")
        elif mass == "8" and vol == "1/2 tbsp":
            return str("7.5")
        elif mass == "13" and vol == "1 tbsp":
            return str("15")
        elif mass == "14" and vol == "1 tbsp":
            return str("15")
        elif mass == "16" and vol == "1 tbsp":
            return str("15")
        else:
            return str(mass)
        
    # Baking soda
    elif food == "Baking soda":
        if mass == "6" and vol == "1 tsp":
            return str("5.6")
        elif mass == "3" and vol == "1/2 tsp":
            return str("2.8")
        elif mass == "1" and vol == "1/4 tsp":
            return str("1.4")
        elif mass == "4" and vol == "3/4 tsp":
            return str("4.2")
        else:
            return str(mass)
        
    # TODO: Baking powder, sweeteners, more EVOO vols

    # Else
    else:
        return str(mass)

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
                    row[1] = grams(row[0], row[1], row[3])
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