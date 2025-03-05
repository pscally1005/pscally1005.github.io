# Download csv to /python/testing folder, and run script to fix grams in ingredients file

import pandas as pd
import os
import glob
import csv

def grams(food, mass, vol):
    # Salt, baking powder, bakign soda
    if food == "Salt" or food == "Baking powder" or food == "Baking soda":
        if vol == "1/4 tsp":
            return str("1.5")
        elif vol == "1/2 tsp":
            return str("3")
        elif vol == "3/4 tsp":
            return str("4.5")
        elif vol == "1 tsp":
            return str("6")
        else:
            return str(mass)
    
    # Extracts
    elif food == "Liquid monk fruit" or food == "Vanilla extract" or food == "Almond extract" or food == "Mint extract" or food == "Butter extract" or food == "Maple extract" or food == "Rum extract":
        if vol == "1/4 tsp":
            return str("1.25")
        elif vol == "1/2 tsp":
            return str("2.5")
        elif vol == "3/4 tsp":
            return str("3.75")
        elif vol == "1 tsp":
            return str("5")
        elif vol == "1/2 tbsp" or vol == "1.5 tsp":
            return str("7.5")
        elif vol == "2 tsp":
            return str("10")
        else:
            return str(mass)
        
    # Spices
    elif food == "Garlic powder" or food == "Onion powder" or food == "Black pepper, ground" or food == "Paprika" or food == "Cumin, ground" or food == "Chili powder" or food == "Cayenne pepper":
        if vol == "1/4 tsp":
            return str("0.75")
        elif vol == "1/2 tsp":
            return str("1.5")
        elif vol == "1 tsp":
            return str("3")
        elif vol == "1/2 tbsp" or vol == "1.5 tsp":
            return str("4.5")
        elif vol == "2 tsp":
            return str("6")
        elif vol == "3 tsp" or vol == "1 tbsp":
            return str("10")
        else:
            return str(mass)
        
    # Herbs
    elif food == "Basil, dried" or food == "Oregano, dried" or food == "Thyme, dried" or food == "Parsley, dried":
        if vol == "1/2 tsp":
            return str("0.5")
        elif vol == "1 tsp":
            return str("1")
        elif vol == "1/2 tbsp" or vol == "1.5 tsp":
            return str("1.5")
        elif vol == "2 tsp":
            return str("2")
        elif vol == "3 tsp" or vol == "1 tbsp":
            return str("3")
        elif vol == "6 tsp" or vol == "2 tbsp":
            return str("6")
        else:
            return str(mass)
    
    # Liquids
    elif food == "Water" or food == "Unsweetened original almond milk" or food == "Unsweetened almond milk" or food == "Unsweetened vanilla almond milk" or food == "Skim milk" or food == "Fairlife skim milk" or food == "Extra virgin olive oil" or food == "Extra virgin coconut oil" or food == "Soy sauce, low sodium, gluten free" or food == "Balsamic vinegar" or food == "White vinegar" or food == "Apple cider vinegar" or food == "Nonfat cottage cheese" or food == "Plain nonfat greek yogurt" or food == "Unsweetened applesauce":
        if vol == "1/2 tbsp":
            return str("7.5")
        elif vol == "1 tbsp":
            return str("15")
        elif vol == "2 tbsp":
            return str("30")
        elif vol == "3 tbsp":
            return str("45")
        elif vol == "4 tbsp" or vol == "1/4 cup":
            return str("60")
        elif vol == "5 tbsp":
            return str("75")
        elif vol == "1/3 cup":
            return str("80")
        elif vol == "6 tbsp":
            return str("90")
        elif vol == "1/2 cup" or vol == "8 tbsp":
            return str("120")
        elif vol == "3/4 cup" or vol == "12 tbsp":
            return str("180")
        elif vol == "1 cup":
            return str("240")
        elif vol == "1.25 cup":
            return str("300")
        elif vol == "1.5 cup":
            return str("360")
        elif vol == "2 cup":
            return str("480")
        elif vol == "3 cup":
            return str("720")
        elif vol == "4 cup":
            return str("960")
        elif vol == "5 cup":
            return str("1200")
        else:
            return str(mass)

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