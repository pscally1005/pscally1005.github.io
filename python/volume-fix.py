import pandas as pd
import os
import glob
import csv

def fix(vol):
    if vol == "0.5 dash" or vol == "1 small pinch":
        return str("Small pinch")
    elif vol == "1 dash":
        return str("Pinch")
    elif vol == "2 dash":
        return str("Large pinch")
    elif vol == "0.125 tsp" or vol == "0.125 tsp, ground" or vol == "1/8 tsp, ground" or vol == "1/8 tsp, leaves" or vol == "0.125 tsp | about" or vol == "0.125 tsp (1.2 ml) aprx" or vol == "0.125 teaspoon" or vol == "1/2 1/4 tsp":
        return str("1/8 tsp")
    elif vol == "0.25 tsp" or vol == "0.25 tsp, ground" or vol == "1/4 tsp, ground" or vol == "1/4 tsp, leaves" or vol == "0.25 tsp | about" or vol == "0.25 tsp (1.2 ml) aprx" or vol == "0.25 teaspoon" or vol == "1 1/4 tsp":
        return str("1/4 tsp")
    elif vol == "0.5 tsp" or vol == "0.5 tsp, ground" or vol == "1.2 tsp" or vol == "1/2 tsp, ground" or vol == "1/2 tsp, leaves" or vol == "0.5 tsp | about" or vol == "0.5 tsp (1.2 ml) aprx" or vol == "0.5 teaspoon" or vol == "0.15 tbsp (15.0 ml) aprx" or vol == "2 1/4 tsp":
        return str("1/2 tsp")
    elif vol == "0.75 tsp" or vol == "3/4 tsp, ground" or vol == "0.75 tsp, ground" or vol == "3/4 tsp, leaves" or vol == "0.75 tsp, leaves" or vol == "0.75 tsp | about" or vol == "0.75 tsp (1.2 ml) aprx" or vol == "0.75 teaspoon" or vol == "3 1/4 tsp":
        return str("3/4 tsp")
    elif vol == "0.33 tbsp" or vol == "0.33 tbsp (15.0 ml) aprx" or vol == "1 tsp, leaves" or vol == "1 tsp, ground" or vol == "1 tsp | about" or vol == "1 tsp (1.2 ml) aprx" or vol == "1 teaspoon" or vol == "0.33 tablespoon" or vol == "4 1/4 tsp" or vol == "1 tsp aprx":
        return str("1 tsp")
    elif vol == "1.5 tsp" or vol == "0.5 tbsp" or vol == "1.5 tsp, ground" or vol == "1.5 tsp, leaves" or vol == "1/2 tbsp, ground" or vol == "1/2 tbsp, leaves" or vol == "1/2 tablespoon" or vol == "1.5 tsp | about" or vol == "1.5 tsp (1.2 ml) aprx" or vol == "1.5 teaspoon" or vol == "0.5 tablespoon" or vol == "4.5 1/4 tsp":
        return str("1/2 tbsp")
    elif vol == "0.66 tbsp" or vol == "0.67 tbsp" or vol == "0.66 tbsp (15.0 ml) aprx" or vol == "0.67 tbsp (15.0 ml) aprx" or vol == "2 tsp, leaves" or vol == "2 tsp, leaves" or vol == "2 tsp | about" or vol == "2 tsp (1.2 ml) aprx" or vol == "2 teaspoon" or vol == "0.67 tablespoon" or vol == "0.66 tablespoon" or vol == "6 1/4 tsp":
        return str("2 tsp")
    elif vol == "3 tsp" or vol == "0.0625 cup" or vol == "3 tsp, leaves" or vol == "1 tbsp (15.0 ml) aprx" or vol == "3 tsp, ground" or vol == "1 tablespoon" or vol == "3 tsp | about" or vol == "0.0625 cup (240.0 ml) aprx" or vol == "3 tsp (1.2 ml) aprx" or vol == "3 teaspoon" or vol == "9 1/4 tsp" or vol == "tbsp" or vol == "0.0825 cup (60.0 ml) aprx":
        return str("1 tbsp")
    elif vol == "6 tsp" or vol == "0.125 cup" or vol == "6 tsp, leaves" or vol == "2 tbsp (15.0 ml) aprx" or vol == "2 tablespoon" or vol == "0.125 cup (240.0 ml) aprx":
        return str("2 tbsp")
    elif vol == "9 tsp":
        return str("3 tbsp")
    elif vol == "4 tbsp" or vol == "0.25 cup" or vol == "0.25 cup (240.0 ml) aprx" or vol =="0.25 cup, sliced" or vol =="0.3325 cup (60.0 ml) aprx":
        return str("1/4 cup")
    elif vol == "5.33 tbsp" or vol == "0.33 cup" or vol == "0.33 cup (240.0 ml) aprx":
        return str("1/3 cup")
    elif vol == "8 tbsp" or vol == "0.5 cup" or vol == "0.5 cup (240.0 ml) aprx" or vol == "0.5 cup, unthawed" or vol == "1/2 cup, frozen":
        return str("1/2 cup")
    elif vol == "9 tbsp" or vol == "0.5625 cup":
        return str("1/2cup + 1tbsp")
    elif vol == "10 tbsp" or vol == "0.625 cup":
        return str("1/2cup + 2tbsp")
    elif vol == "2/3 cup, unthawed" or vol == "0.66 cup (240.0 ml) aprx" or vol == "0.67 cup (240.0 ml) aprx":
        return str("2/3 cup")
    elif vol == "12 tbsp" or vol == "0.75 cup" or vol == "0.75 cup (240.0 ml) aprx":
        return str("3/4 cup")
    elif vol == "16 tbsp" or vol == "1 cup (240.0 ml) aprx" or vol == "1 cup, frozen":
        return str("1 cup")
    elif vol == "1.0989 cup":
        return str("1 heaping cup")
    elif vol == "1.32 cup":
        return str("1.33 cup")
    elif vol == "2 cup, frozen":
        return str("2 cup")
    elif vol == "1 can drained, rinsed" or vol == "1 can" or vol == "1 can drained solids":
        return str("15.5oz can")
    elif vol == "16 oz" or vol == "16 ounce":
        return str("1 pound")
    elif vol == "32 oz" or vol == "32 ounce":
        return str("2 pound")
    elif vol == "0.5 scoop | about" or vol == "0.5 serving" or vol == "0.5 scoop":
        return str("1/2 scoop")
    elif vol == "1.05 scoop | about" or vol == "1.05 serving":
        return str("1 scoop")
    elif vol == "1.55 scoop | about" or vol == "1.55 serving":
        return str("1.5 scoop")
    elif vol == "2.08 scoop | about" or vol == "2.08 serving":
        return str("2 scoop")
    elif vol == "3.1 scoop | about" or vol == "3.1 serving":
        return str("3 scoop")
    elif vol == "0.5 fruit, without skin and seed":
        return str("1/2 avocado")
    elif vol == "1 fruit, without skin and seed":
        return str("1 avocado")
    elif vol == "2 fruit, without skin and seed":
        return str("2 avocado")
    elif vol == "3 fruit, without skin and seed":
        return str("3 avocado")
    else:
        return vol

def main():

    os.system('cls')

    # path to csv files
    # path = r"C:\Users\mets1\Documents\website\_data\*-ing.csv"
    # path = r"C:\Users\mets1\Documents\website\python\testing\*-ing.csv"
    # path = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\_data\*.csv"
    path = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\python\testing\*-ing.csv"

    # loop through all the files
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

if __name__ == '__main__':
    main()