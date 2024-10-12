import pandas as pd
import os
import glob
import csv

def fix(vol):
    # salt
    if vol == "0.5 dash" or vol == "1 small pinch" or vol == "Few grains":
        return str("Small pinch")
    elif vol == "1 dash":
        return str("Pinch")
    elif vol == "2 dash":
        return str("Large pinch")
    
    # tsp
    elif vol == "0.128 tsp" or vol == "0.125 tsp" or vol == "0.125 tsp, ground" or vol == "1/8 tsp, ground" or vol == "1/8 tsp, leaves" or vol == "0.125 tsp | about" or vol == "0.125 tsp (1.2 ml) aprx" or vol == "0.125 teaspoon" or vol == "1/2 1/4 tsp":
        return str("1/8 tsp")
    elif vol == "0.25 tsp (1.0 ml) aprx" or vol == "0.25 tsp" or vol == "0.25 tsp, ground" or vol == "1/4 tsp, ground" or vol == "1/4 tsp, leaves" or vol == "0.25 tsp | about" or vol == "0.25 tsp (1.2 ml) aprx" or vol == "0.25 teaspoon" or vol == "1 1/4 tsp":
        return str("1/4 tsp")
    elif vol == "0.375 tsp":
        return str("3/8 tsp")
    elif vol == "0.5 tsp (5.0 ml) aprx" or vol == "0.5 tsp (1.0 ml) aprx" or vol == "0.5 tsp" or vol == "0.165 tbsp (15.0 ml) aprx" or vol == "4 1/8 tsp" or vol == "0.5 tsp, ground" or vol == "1.2 tsp" or vol == "1/2 tsp, ground" or vol == "1/2 tsp, leaves" or vol == "0.5 tsp | about" or vol == "0.5 tsp (1.2 ml) aprx" or vol == "0.5 teaspoon" or vol == "0.15 tbsp (15.0 ml) aprx" or vol == "2 1/4 tsp":
        return str("1/2 tsp")
    elif vol == "0.75 tsp" or vol == "0.25 tbsp (15.0 ml) aprx" or vol == "0.25 tbsp" or vol == "3/4 tsp, ground" or vol == "0.75 tsp, ground" or vol == "3/4 tsp, leaves" or vol == "0.75 tsp, leaves" or vol == "0.75 tsp | about" or vol == "0.75 tsp (1.2 ml) aprx" or vol == "0.75 teaspoon" or vol == "3 1/4 tsp":
        return str("3/4 tsp")
    elif vol == "1.1 tsp" or vol == "1 tsp (1.0 ml) aprx" or vol == "0.33 tbsp" or vol == "1.15 tsp" or vol == "8 1/8 tsp" or vol == "0.33 tbsp (15.0 ml) aprx" or vol == "0.25 tbsp" or vol == "1 tsp (5.0 ml) aprx" or vol == "1 tsp, leaves" or vol == "1 tsp, ground" or vol == "1 tsp | about" or vol == "1 tsp (1.2 ml) aprx" or vol == "1 teaspoon" or vol == "0.33 tablespoon" or vol == "4 1/4 tsp" or vol == "1 tsp aprx":
        return str("1 tsp")
    elif vol == "8 1/4 tsp" or vol == "0.66 tbsp" or vol == "2 tsp, ground" or vol == "0.67 tbsp" or vol == "2 tsp (5.0 ml) aprx" or vol == "0.66 tbsp (15.0 ml) aprx" or vol == "0.67 tbsp (15.0 ml) aprx" or vol == "2 tsp, leaves" or vol == "2 tsp, leaves" or vol == "2 tsp | about" or vol == "2 tsp (1.2 ml) aprx" or vol == "2 teaspoon" or vol == "0.67 tablespoon" or vol == "0.66 tablespoon" or vol == "6 1/4 tsp":
        return str("2 tsp")
    elif vol == "20 1/8 tsp":
        return str("2.5 tsp")
    elif vol == "1.33 tbsp" or vol == "4 1 tsp" or vol == "0.0833 cup" or vol == "0.0833 cup (240.0 ml) aprx":
        return str("4 tsp")
    
    # tbsp
    elif vol == "0.5 tbsp (15.0 ml) aprx" or vol == "1.5 tsp" or vol == "0.5 tbsp" or vol == "1.5 tsp, ground" or vol == "1.5 tsp, leaves" or vol == "1/2 tbsp, ground" or vol == "1/2 tbsp, leaves" or vol == "1/2 tablespoon" or vol == "1.5 tsp | about" or vol == "1.5 tsp (1.2 ml) aprx" or vol == "1.5 teaspoon" or vol == "0.5 tablespoon" or vol == "4.5 1/4 tsp":
        return str("1/2 tbsp")
    elif vol == "0.85 serving 1 tbsp" or vol == "3 tsp" or vol == "0.99 tbsp" or vol == "0.05 cup" or vol == "24 1/8 tsp" or vol == "1.15 tbsp" or vol == "0.0625 cup" or vol == "1 serving 1 tbsp" or vol == "3 tsp (5.0 ml) aprx" or vol == "3 tsp, leaves" or vol == "1 tbsp (15.0 ml) aprx" or vol == "3 tsp, ground" or vol == "1 tablespoon" or vol == "3 tsp | about" or vol == "0.0625 cup (240.0 ml) aprx" or vol == "3 tsp (1.2 ml) aprx" or vol == "3 teaspoon" or vol == "9 1/4 tsp" or vol == "tbsp" or vol == "1 tbsp, leaves" or vol == "0.0825 cup (60.0 ml) aprx":
        return str("1 tbsp")
    elif vol == "2.0100000000000002 tbsp" or vol == "6 teaspoons" or vol == "6 teaspoon" or vol == "1.9 tbsp" or vol == "0.5 1/4 cup" or vol == "0.1 cup" or vol == "6 tsp" or vol == "0.1254 cup" or vol == "0.125 cup, NFS" or vol == "0.125 cup" or vol == "6 tsp (5.0 ml) aprx" or vol == "6 tsp, leaves" or vol == "2 tbsp (15.0 ml) aprx" or vol == "2 tablespoon" or vol == "0.125 cup (240.0 ml) aprx":
        return str("2 tbsp")
    elif vol == "9 tsp" or vol == "0.67 scoop" or vol == "0.66 1/4 cup" or vol == "9 tsp (5.0 ml) aprx" or vol == "9 tsp, leaves" or vol == "9 teaspoons" or vol == "0.1875 cup" or vol == "0.1875 cup (15.0 ml) aprx" or vol == "0.1875 cup (240.0 ml) aprx":
        return str("3 tbsp")
    elif vol == "15 tsp (5.0 ml) aprx" or vol == "15 tsp" or vol == "15 teaspoon" or vol == "15 teaspoons":
        return str("5 tbsp")
    elif vol == "0.25 cup sprigs":
        return str("4 tbsp")
    elif vol == "0.375 cup" or vol == "0.75 1/2 cup":
        return str("6 tbsp")
    elif vol == "9.33 tbsp" or vol == "9.33 Tbsp":
        return str("9tbsp + 1tsp")
    
    # cup
    elif vol == "102.86399999999999 chips" or vol == "102.72 chips" or vol == "0.2508 cup" or vol == "1 oz (167 kernels)" or vol == "0.245 cup" or vol == "0.255 cup" or vol == "1 1/4 cup" or vol == "4 tbsp" or vol == "0.5 1/2 cup" or vol == "0.48 cup, NFS" or vol == "4 Tbsp" or vol == "0.25 cup" or vol == "1 About 1/4 cup" or vol == "1.4 cup" or vol == "12 teaspoons" or vol == "12 tsp" or vol == "1/4 cup, crumbled" or vol == "0.25 crumbled" or vol == "0.25 cup (240.0 ml) aprx" or vol =="0.25 cup, sliced" or vol == "12 tsp (5.0 ml) aprx" or vol =="0.3325 cup (60.0 ml) aprx":
        return str("1/4 cup")
    elif vol == "5.334 level tbsp" or vol == "5.334 tbsp" or vol == "0.305 cup" or vol == "0.338 cup" or vol == "5.33 tbsp" or vol == "5.33 tbsp (15.0 ml) aprx" or vol == "0.33 cup" or vol == "0.33 cup (240.0 ml) aprx" or vol == "16 tsp (5.0 ml) aprx" or vol == "0.33 cup, crumbled" or vol == "1/3 cup, crumbled":
        return str("1/3 cup")
    elif vol == "24 teaspoons" or vol == "154.08 chips" or vol == "154.07999999999998 chips" or vol == "0.5 cup, packed" or vol == "8 level tbsp" or vol == "8.001 tbsp" or vol == "0.435 cup, halves and whole" or vol == "154.272 chips" or vol == "0.5 cup, NFS" or vol == "0.46 cup" or vol  == "0.975 1/2 cup" or vol == "0.5 cup, shredded" or vol == "0.5 cup, mashed" or vol == "7.949999999999999 tbsp" or vol == "8 tablespoon" or vol == "0.49 cup, whole" or vol == "0.48 cup, NFS" or vol == "2.32 1/4 cup" or vol == "0.58 cup" or vol == "154.8 chips" or vol == "1 1/2 cup" or vol == "0.49 cup" or vol == "8 tbsp" or vol == "8 Tbsp" or vol == "0.5 cup" or vol == "24 tsp" or vol == "1/2 cup, whole" or vol == "0.5 cup, whole" or vol == "1/2 cup, crumbled" or vol == "0.5 crumbled" or vol == "24 tsp (5.0 ml) aprx" or vol == "0.5 cup (240.0 ml) aprx" or vol == "0.5 cup, unthawed" or vol == "1/2 cup, frozen" or vol == "0.5 cup, sliced" or vol == "0.5 cup, frozen":
        return str("1/2 cup")
    elif vol == "9 tbsp" or vol == "9 Tbsp" or vol == "0.5625 cup" or vol == "0.5625 cup (240.0 ml) aprx":
        return str("1/2cup + 1tbsp")    
    elif vol == "10 tbsp" or vol == "10 Tbsp" or vol == "0.625 cup":
        return str("1/2cup + 2tbsp")
    elif vol == "0.66 cup, unthawed" or vol == "0.665 cup" or vol == "2/3 cup, unthawed" or vol == "0.9 3/4 cup" or vol == "0.67 cup" or vol == "0.66 cup" or vol == "0.66 cup (240.0 ml) aprx" or vol == "0.67 cup (240.0 ml) aprx" or vol == "32 tsp (5.0 ml) aprx":
        return str("2/3 cup")
    elif vol == "0.7375 cup" or vol == "3 1/4 cup" or vol == "0.75 cup whole kernels" or vol == "1 3/4 cup" or vol == "0.695 cup" or vol == "0.76 cup" or vol == "0.75 cup (240.0 ml) aprx" or vol == "1.545 1/2 cup" or vol == "12 tbsp" or vol == "12 Tbsp" or vol == "0.75 cup" or vol == "0.75 cup (240.0 ml) aprx" or vol == "3/4 cup, crumbled" or vol == "0.75 crumbled" or vol == "0.75 cup crumbled" or vol == "0.75 cup, shredded":
        return str("3/4 cup")
    elif vol == "0.815 cup":
        return str("7/8 cup")
    elif vol == "0.99 cup" or vol == "1 cup whole kernels" or vol == "0.922 cup" or vol == "0.9 cup, whole" or vol == "1 cup, whole" or vol == "4 1/4 cup" or vol == "0.9225 cup" or vol == "0.921 cup" or vol == "16 tbsp" or vol == "16 Tbsp" or vol == "1 cup (240.0 ml) aprx" or vol == "1 cup, frozen" or vol == "1 cup, crumbled" or vol == "48 tsp (5.0 ml) aprx" or vol == "1 cup, unthawed" or vol == "48 tsp" or vol == "50 tsp":
        return str("1 cup")
    elif vol == "1.0989 cup":
        return str("1 heaping cup")
    elif vol == "2.5 1/2 cup":
        return str("1.25 cup")
    elif vol == "1.32 cup" or vol == "1.33 cup (240.0 ml) aprx":
        return str("1.33 cup")
    elif vol == "24 tbsp" or vol == "1.555 cup, NFS" or vol == "3.25 1/2 cup" or vol == "1.5 cup, chunks" or vol == "1.5 cup pieces" or vol == "2 3/4 cup":
        return str("1.5 cup")
    elif vol == "2.665 container" or vol == "2 cup, frozen" or vol == "5 1/3 cup" or vol == "7.5 1/3 cup" or vol == "2 cup, chopped" or vol == "32 tbsp" or vol == "32 Tbsp" or vol == "1.855 cup":
        return str("2 cup")
    elif vol == "2.52 cup":
        return str("2.5 cup")
    elif vol == "6 1/2 cup" or vol == "48 tbsp" or vol == "48 Tbsp" or vol == "50 tbsp" or vol == "50 Tbsp" or vol == "3.11 cup, NFS" or vol == "2.99 cup drained, rinsed":
        return str("3 cup")
    elif vol == "14 1/4 cup":
        return str("3.5 cup")
    
    # oz
    elif vol == "1/2 ounce" or vol == "0.5 ounce" or vol == "0.5 oz" or vol == "0.5 oz square Bakers":
        return str("1/2 oz")
    elif vol == "1 ounce":
        return str("1 oz")
    elif vol == "2 ounce":
        return str("2 oz")
    elif vol == "3 ounce":
        return str("3 oz")
    elif vol == "4 ounce" or vol == "1/4 lb" or vol == "1/4 pound" or vol == "0.25 lb" or vol == "0.25 pound":
        return str("4 oz")
    elif vol == "6 ounce" or vol == "2 3 oz fillets":
        return str("6 oz")
    elif vol == "7 ounce":
        return str("7 oz")
    elif vol == "1/2 lb" or vol == "0.5 pound" or vol == "8 ounce" or vol == "0.5 lb" or vol == "1/2 pound":
        return str("8 oz")
    elif vol == "9 ounce":
        return str("9 oz")
    elif vol == "12 ounce":
        return str("12 oz")
    elif vol == "14 ounce":
        return str("14 oz")
    elif vol == "15 ounce":
        return str("15 oz")
    
    # cans
    elif vol == "1 can (2 oz) drained":
        return str("2 oz, drained")
    elif vol == "1 can, drained (4.4 oz)":
        return str("4.4 oz")
    elif vol == "14.5 ounce":
        return str("14.5oz can")
    elif vol == "0.5 can drained solids" or vol == "0.5 can" or vol == "0.5 can, drained, rinsed" or vol == "0.5 can drained" or vol == "0.5 15.5oz can drained, rinsed":
        return str("1/2 15.5oz can")
    elif vol == "1 can drained solids" or vol == "1 can drained, rinsed" or vol == "1 can" or vol == "1 can, drained, rinsed" or vol == "1 can drained" or vol == "15.5oz can drained, rinsed":
        return str("15.5oz can")
    elif vol == "19.5 ounce" or vol == "3 6.5oz cans":
        return str("3x6.5oz cans")
    elif vol == "28 ounce":
        return str("28oz can")
    elif vol == "56 ounce" or vol == "2 28oz cans":
        return str("2x28oz cans")
    elif vol == "29 ounce":
        return str("2x14.5oz can")
    elif vol == "2 can drained solids" or vol == "2 can" or vol == "2 can, drained, rinsed" or vol == "2 can drained" or vol == "2x15.5oz can drained, rinsed" or vol == "2 15.5oz cans":
        return str("2x15.5oz cans")
    elif vol == "3 can drained solids" or vol == "3 can" or vol == "3 can, drained, rinsed" or vol == "3 can drained" or vol == "3x15.5oz can drained, rinsed" or vol == "3 15.5oz cans":
        return str("3x15.5oz cans")
    elif vol == "4 can drained solids" or vol == "4 can" or vol == "4 can, drained, rinsed" or vol == "4 can drained" or vol == "4x15.5oz can drained, rinsed" or vol == "4 15.5oz cans":
        return str("4x15.5oz cans")
    elif vol == "87 ounce" or vol == "87 oz":
        return str("6x14.5oz can")
    
    # lb
    elif vol == "16 oz" or vol == "16 ounce" or vol == "1 pound" or vol == "1 pound dried beans":
        return str("1 lb")
    elif vol == "1.3 pound":
        return str("1.3 lb")
    elif vol == "1.5 pound" or vol == "24 oz" or vol == "24 ounce" or vol == "1.5 pounds":
        return str("1.5 lb")
    elif vol == "32 oz" or vol == "32 ounce" or vol == "2 pound":
        return str("2 lb")
    elif vol == "3 pound":
        return str("3 lb")
    elif vol == "4 pound":
        return str("4 lb")
    
    # protein powder
    elif vol == "0.5 scoop | about" or vol == "0.5 serving" or vol == "0.5 scoop" or vol == "1/2 serving" or vol == "0.5 scoops":
        return str("1/2 scoop")
    elif vol == "0.75 scoop | about" or vol == "0.75 scoop":
        return str("3/4 scoop")
    elif vol == "1.05 scoop | about" or vol == "1.05 serving" or vol == "1 serving" or vol == "1 scoop | about":
        return str("1 scoop")
    elif vol == "1.55 scoop | about" or vol == "1.55 serving" or vol == "1.5 serving" or vol == "1.5 scoops" or vol == "1.5 scoop | about":
        return str("1.5 scoop")
    elif vol == "2.08 scoop | about" or vol == "2.08 serving" or vol == "2 serving" or vol == "2 scoops" or vol == "2 scoop | about":
        return str("2 scoop")
    elif vol == "3.1 scoop | about" or vol == "3.1 serving" or vol == "3 serving" or vol == "3 scoops" or vol == "3 scoop | about":
        return str("3 scoop")
    elif vol == "6.21 scoop | about":
        return str("6 scoop")
    
    # dates & olives
    elif vol == "11 date, pitted" or vol == "11 olives":
        return str("11 pitted")
    elif vol == "16 date, pitted":
        return str("16 pitted")
    elif vol == "20 date, pitted":
        return str("20 pitted")
    elif vol == "28 date, pitted" or vol == "28 -6 dates":
        return str("28 pitted")
    elif vol == "30 date, pitted":
        return str("30 pitted")
    elif vol == "31 date, pitted":
        return str("31 pitted")
    elif vol == "32 date, pitted":
        return str("32 pitted")
    
    # produce
    elif vol == "1/2 fruit, without skin and seed" or vol == "0.5 fruit, without skin and seed" or vol == "0.5 Banana" or vol == "0.5 banana" or vol == "1/2 banana" or vol == "1/2 Banana" or vol == "1/2 Onion" or vol == "0.5 Onion" or vol == "1/2 onion" or vol == "0.5 onion" or vol == "0.5 medium bell pepper" or vol == "1/2 medium bell pepper" or vol == "0.5 whole" or vol == "1/2 whole" or vol == "0.5 English" or vol == "1/2 English" or vol == "0.5 Italian tomato" or vol == "1/2 Italian tomato" or vol =="0.5 small" or vol == "1/2 small" or vol == "1/2 eggplant, unpeeled (approx 1-1/4 lb)"or vol == "0.5 eggplant, unpeeled (approx 1-1/4 lb)":
        return str("1/2 medium")
    elif vol == "1 medium (2-1/2 dia)" or vol == "1 fruit, without skin and seed" or vol == "1 medium (approx 2-3/4 long, 2-1/2 dia.)" or vol == "1.33 medium" or vol == "1 banana" or vol == "1 Banana" or vol == "1 onion" or vol == "1 Onion" or vol == "1 medium bell pepper" or vol == "1 whole" or vol == "1 English" or vol == "1 Italian tomato"or vol == "1 plum tomato" or vol =="1 small" or vol == "1 eggplant, unpeeled (approx 1-1/4 lb)":
        return str("1 medium")
    elif vol == "2 fruit, without skin and seed" or vol == "2 medium (2-1/2 dia)" or vol == "2 banana" or vol == "2 Banana" or vol == "2 onion" or vol == "2 Onion" or vol == "2 medium bell peppers" or vol == "2 whole" or vol == "2 English" or vol == "2 Italian tomato"or vol == "2 plum tomato" or vol == "2 small" or vol == "2 eggplant, unpeeled (approx 1-1/4 lb)":
        return str("2 medium")
    elif vol == "3 fruit, without skin and seed" or vol == "3 medium (approx 2-3/4 long, 2-1/2 dia.)" or vol == "3 banana" or vol == "3 Banana" or vol == "3 onion" or vol == "3 Onion" or vol == "3 medium bell peppers" or vol == "3 whole" or vol == "3 English" or vol == "3 Italian tomato"or vol == "3 plum tomato" or vol == "3 small" or vol == "3 eggplant, unpeeled (approx 1-1/4 lb)":
        return str("3 medium")
    elif vol == "4 fruit, without skin and seed" or vol == "4 banana" or vol == "4 Banana" or vol == "4 onion" or vol == "4 Onion" or vol == "4 medium bell peppers" or vol == "4 whole" or vol == "4 English" or vol == "4 Italian tomato"or vol == "4 plum tomato" or vol == "4 small" or vol == "4 eggplant, unpeeled (approx 1-1/4 lb)":
        return str("4 medium")
    elif vol == "5 fruit, without skin and seed" or vol == "5 banana" or vol == "5 Banana" or vol == "5 onion" or vol == "5 Onion" or vol == "5 medium bell peppers" or vol == "5 whole" or vol == "5 English" or vol == "5 Italian tomato"or vol == "5 plum tomato" or vol == "5 small" or vol == "5 eggplant, unpeeled (approx 1-1/4 lb)":
        return str("5 medium")
    elif vol == "8 small":
        return str("8 medium")
    elif vol == "9 small":
        return str("9 medium")
    elif vol == "1 kiwi | per":
        return str("1 medium")
    elif vol == "2 kiwi | per":
        return str("2 medium")
    elif vol == "0.82 Banana":
        return str("1 small")
    elif vol == "1 plantain":
        return str("1 large or 2 small")
    
    # eggs
    elif vol == "1 egg":
        return str("1 large")
    elif vol == "2 egg":
        return str("2 large")
    elif vol == "3 egg":
        return str("3 large")
    elif vol == "4.13 Banana" or vol == "4 egg":
        return str("4 large")
    elif vol == "5 egg":
        return str("5 large")
    elif vol == "6 egg":
        return str("6 large")
    elif vol == "8 egg":
        return str("8 large")
    
    # garlic
    elif vol == "11 clove" or vol == "15 clove":
        return str("1 head")
    elif vol == "22 clove" or vol == "30 clove":
        return str("2 head")
    
    # other
    elif vol == "16 cup":
        return str("1 gallon")

    # else
    else:
        return vol

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