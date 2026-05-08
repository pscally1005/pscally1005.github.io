# Download csv to /python/testing folder, and run script to fix volume measurements in ingredients file

import pandas as pd
import os
import glob
import csv

def fix(vol):
    v = vol

    # salt
    if vol == "0.5 dash" or vol == "1 small pinch" or vol == "Few grains" or vol == "0.05 tsp":
        v = "Small pinch"
    elif vol == "1 dash":
        v = "Pinch"
    elif vol == "2 dash":
        v = "Large pinch"

    # tsp
    elif vol == "0.0625 tsp":
        v = "1/16 tsp"
    elif vol == "0.128 tsp" or vol == "0.125 tsp" or vol == "0.125 tsp, ground" or vol == "1/8 tsp, ground" or vol == "1/8 tsp, leaves" or vol == "0.125 tsp | about" or vol == "0.125 tsp (1.2 ml) aprx" or vol == "0.125 teaspoon" or vol == "1/2 1/4 tsp":
        v = "1/8 tsp"
    elif vol == "0.25 tsp (1.0 ml) aprx" or vol == "0.25 tsp" or vol == "0.25 tsp, ground" or vol == "1/4 tsp, ground" or vol == "1/4 tsp, leaves" or vol == "0.25 tsp | about" or vol == "0.25 tsp (1.2 ml) aprx" or vol == "0.25 teaspoon" or vol == "1 1/4 tsp":
        v = "1/4 tsp"
    elif vol == "0.375 tsp":
        v = "3/8 tsp"
    elif vol == "0.167 tbsp" or vol == "0.5 tsp, whole" or vol == "0.1667 tbsp" or vol == "0.16 tbsp (15.0 ml) aprx" or vol == "0.5 tsp (5.0 ml) aprx" or vol == "0.5 tsp (1.0 ml) aprx" or vol == "0.5 tsp" or vol == "0.165 tbsp (15.0 ml) aprx" or vol == "4 1/8 tsp" or vol == "0.5 tsp, ground" or vol == "1/2 tsp, ground" or vol == "1/2 tsp, leaves" or vol == "0.5 tsp | about" or vol == "0.5 tsp (1.2 ml) aprx" or vol == "0.5 teaspoon" or vol == "0.15 tbsp (15.0 ml) aprx" or vol == "2 1/4 tsp" or vol == "1/2 tsp,round" or vol == "1/2 tsp, round" or vol == "0.5 tsp,round" or vol == "0.5 tsp, round":
        v = "1/2 tsp"
    elif vol == "0.75 tsp" or vol == "0.25 tbsp (15.0 ml) aprx" or vol == "0.25 tbsp" or vol == "3/4 tsp, ground" or vol == "0.75 tsp, ground" or vol == "3/4 tsp, leaves" or vol == "0.75 tsp, leaves" or vol == "0.75 tsp | about" or vol == "0.75 tsp (1.2 ml) aprx" or vol == "0.75 teaspoon" or vol == "3 1/4 tsp":
        v = "3/4 tsp"
    elif vol == "0.334 tbsp" or vol == "0.0208 cup" or vol == "1 teaspoonsful (10.0 ml) aprx" or vol == "1.2 tsp" or vol == "1.1 tsp" or vol == "1 tsp (1.0 ml) aprx" or vol == "0.33 tbsp" or vol == "1.15 tsp" or vol == "8 1/8 tsp" or vol == "0.33 tbsp (15.0 ml) aprx" or vol == "0.25 tbsp" or vol == "1 tsp (5.0 ml) aprx" or vol == "1 tsp, leaves" or vol == "1 tsp, ground" or vol == "1 tsp | about" or vol == "1 tsp (1.2 ml) aprx" or vol == "1 teaspoon" or vol == "0.33 tablespoon" or vol == "4 1/4 tsp" or vol == "1 tsp aprx":
        v = "1 tsp"
    elif vol == "5 1/4 tsp":
        v = "1 1/4 tsp"
    elif vol == "0.667 tbsp" or vol == "2.1 tsp" or vol == "0.04167 cup" or vol == "0.7 tablespoon" or vol == "8 1/4 tsp" or vol == "0.66 tbsp" or vol == "2 tsp, ground" or vol == "0.67 tbsp" or vol == "2 tsp (5.0 ml) aprx" or vol == "0.66 tbsp (15.0 ml) aprx" or vol == "0.67 tbsp (15.0 ml) aprx" or vol == "2 tsp, leaves" or vol == "2 tsp, leaves" or vol == "2 tsp | about" or vol == "2 tsp (1.2 ml) aprx" or vol == "2 teaspoon" or vol == "0.67 tablespoon" or vol == "0.66 tablespoon" or vol == "6 1/4 tsp":
        v = "2 tsp"
    elif vol == "20 1/8 tsp":
        v = "2 1/2 tsp"
    elif vol == "4 teaspoons" or vol == "1.33 tbsp" or vol == "4 1 tsp" or vol == "0.0833 cup" or vol == "0.0833 cup (240.0 ml) aprx":
        v = "4 tsp"

    # tbsp
    elif vol == "0.03125 cup" or vol == "0.5 tbsp (15.0 ml) aprx" or vol == "1.5 tsp" or vol == "0.5 tbsp" or vol == "1.5 tsp, ground" or vol == "1.5 tsp, leaves" or vol == "1/2 tbsp, ground" or vol == "1/2 tbsp, leaves" or vol == "1/2 tablespoon" or vol == "1.5 tsp | about" or vol == "1.5 tsp (1.2 ml) aprx" or vol == "1.5 teaspoon" or vol == "0.5 tablespoon" or vol == "4.5 1/4 tsp":
        v = "1/2 tbsp"
    elif vol == "2.8 tsp" or vol == "1 tbsp, ground" or vol == "1.0625 tbsp" or vol == "1.08 tbsp" or vol == "0.85 serving 1 tbsp" or vol == "3 tsp" or vol == "0.99 tbsp" or vol == "0.05 cup" or vol == "24 1/8 tsp" or vol == "1.15 tbsp" or vol == "0.0625 cup" or vol == "1 serving 1 tbsp" or vol == "3 tsp (5.0 ml) aprx" or vol == "3 tsp, leaves" or vol == "1 tbsp (15.0 ml) aprx" or vol == "3 tsp, ground" or vol == "1 tablespoon" or vol == "3 tsp | about" or vol == "0.0625 cup (240.0 ml) aprx" or vol == "3 tsp (1.2 ml) aprx" or vol == "3 teaspoon" or vol == "9 1/4 tsp" or vol == "tbsp" or vol == "1 tbsp, leaves" or vol == "0.0825 cup (60.0 ml) aprx":
        v = "1 tbsp"
    elif vol == "0.09375 cup" or vol == "4.5 tsp":
        v = "1 1/2 tbsp"
    elif vol == "2.1 tbsp" or vol == "2.01 tbsp" or vol == "0.124 cup" or vol == "0.125 serving 8 fl oz 8 fl oz" or vol == "0.12375 cup" or vol == "2.2 tbsp" or vol == "0.1245 cup" or vol == "0.1225 cup" or vol == "2.2 level tbsp" or vol == "2.0100000000000002 tbsp" or vol == "6 teaspoons" or vol == "6 teaspoon" or vol == "1.9 tbsp" or vol == "0.5 1/4 cup" or vol == "0.1 cup" or vol == "6 tsp" or vol == "0.1254 cup" or vol == "0.125 cup, NFS" or vol == "0.125 cup" or vol == "6 tsp (5.0 ml) aprx" or vol == "6 tsp, leaves" or vol == "2 tbsp (15.0 ml) aprx" or vol == "2 tablespoon" or vol == "0.125 cup (240.0 ml) aprx":
        v = "2 tbsp"
    elif vol == "3 tbsp unsifted" or vol == "3.2 tablespoon" or vol == "3 tablespoon" or vol == "0.185 cup" or vol == "3 tbsp, leaves" or vol == "9 tsp" or vol == "0.66 1/4 cup" or vol == "9 tsp (5.0 ml) aprx" or vol == "9 tsp, leaves" or vol == "9 teaspoons" or vol == "0.1875 cup" or vol == "0.1875 cup (15.0 ml) aprx" or vol == "0.1875 cup (240.0 ml) aprx":
        v = "3 tbsp"
    elif vol == "4.25 tablespoon" or vol == "3.75 tablespoon" or vol == "3.95 tablespoon" or vol == "4 tablespoon" or vol == "4.2 tbsp" or vol == "0.25 cup sprigs" or vol == "3.99 tbsp":
        v = "4 tbsp"
    elif vol == "15 tsp (5.0 ml) aprx" or vol == "15 tsp" or vol == "15 teaspoon" or vol == "15 teaspoons":
        v = "5 tbsp"
    elif vol == "6 tbsp, drained" or vol == "0.3675 cup" or vol == "18 tsp" or vol == "0.375 cup" or vol == "0.75 1/2 cup":
        v = "6 tbsp"
    elif vol == "9.33 tbsp" or vol == "9.33 Tbsp":
        v = "9 tbsp + 1 tsp"

    # cup
    elif vol == "12 teaspoon, dry" or vol == "0.5 stick" or vol == "0.2475 cup" or vol == "0.24 cup, chopped" or vol == "0.275 cup (not packed)" or vol == "0.265 cup" or vol == "0.355 container" or vol == "102.86399999999999 chips" or vol == "102.72 chips" or vol == "0.2508 cup" or vol == "1 oz (167 kernels)" or vol == "0.245 cup" or vol == "0.255 cup" or vol == "1 1/4 cup" or vol == "4 tbsp" or vol == "0.5 1/2 cup" or vol == "0.48 cup, NFS" or vol == "4 Tbsp" or vol == "0.25 cup" or vol == "1 About 1/4 cup" or vol == "1.4 cup" or vol == "12 teaspoons" or vol == "12 tsp" or vol == "1/4 cup, crumbled" or vol == "0.25 crumbled" or vol == "0.25 cup (240.0 ml) aprx" or vol =="0.25 cup, sliced" or vol == "12 tsp (5.0 ml) aprx" or vol =="0.3325 cup (60.0 ml) aprx":
        v = "1/4 cup"
    elif vol == "5.34 tbsp" or vol == "0.3325 cup" or vol == "0.325 cup" or vol == "0.345 cup mini chips" or vol == "0.3275 cup" or vol == "5.334 level tbsp" or vol == "5.334 tbsp" or vol == "0.305 cup" or vol == "0.338 cup" or vol == "5.33 tbsp" or vol == "5.33 tbsp (15.0 ml) aprx" or vol == "0.33 cup" or vol == "0.33 cup (240.0 ml) aprx" or vol == "16 tsp (5.0 ml) aprx" or vol == "0.33 cup, crumbled" or vol == "1/3 cup, crumbled":
        v = "1/3 cup"
    elif vol == "0.52 cup" or vol == "0.54 cup" or vol == "0.521 cup" or vol == "0.542 cup" or vol == "1/2 cup, shredded" or vol == "0.5 cup, undrained" or vol == "1 stick" or vol == "0.4925 cup" or vol == "8 tbsp (15.0 ml) aprx" or vol == "7.9 tablespoon" or vol == "8 tablespoon" or vol == "0.5295 cup" or vol == "0.49 cup mini chips" or vol == "0.5 cup mini chips" or vol == "0.41 cup, NFS" or vol == "2 1/4 cup" or vol == "0.78 cup (not packed)" or vol == "0.705 container" or vol == "0.495 cup" or vol == "0.495 cup, shredded" or vol == "24 teaspoons" or vol == "154.08 chips" or vol == "154.07999999999998 chips" or vol == "0.5 cup, packed" or vol == "8 level tbsp" or vol == "8.001 tbsp" or vol == "0.435 cup, halves and whole" or vol == "154.272 chips" or vol == "0.5 cup, NFS" or vol == "0.46 cup" or vol  == "0.975 1/2 cup" or vol == "0.5 cup, shredded" or vol == "0.5 cup, mashed" or vol == "7.949999999999999 tbsp" or vol == "8 tablespoon" or vol == "0.49 cup, whole" or vol == "0.48 cup, NFS" or vol == "2.32 1/4 cup" or vol == "0.58 cup" or vol == "154.8 chips" or vol == "1 1/2 cup" or vol == "0.49 cup" or vol == "8 tbsp" or vol == "8 Tbsp" or vol == "0.5 cup" or vol == "24 tsp" or vol == "1/2 cup, whole" or vol == "0.5 cup, whole" or vol == "1/2 cup, crumbled" or vol == "0.5 crumbled" or vol == "24 tsp (5.0 ml) aprx" or vol == "0.5 cup (240.0 ml) aprx" or vol == "0.5 cup, unthawed" or vol == "1/2 cup, frozen" or vol == "0.5 cup, sliced" or vol == "0.5 cup, frozen":
        v = "1/2 cup"
    elif vol == "9 tbsp" or vol == "9 Tbsp" or vol == "0.5625 cup" or vol == "0.5625 cup (240.0 ml) aprx":
        v = "1/2 cup + 1 tbsp"
    elif vol == "10 tbsp" or vol == "10 Tbsp" or vol == "0.625 cup" or vol == "30 tsp (5.0 ml) aprx":
        v = "1/2 cup + 2 tbsp"
    elif vol == "0.66675 cup" or vol == "0.695 cup, whole" or vol == "0.882 container" or  vol == "0.645 cup, unthawed" or vol == "0.88 3/4 cup" or vol == "0.66 cup, unthawed" or vol == "0.665 cup" or vol == "2/3 cup, unthawed" or vol == "0.9 3/4 cup" or vol == "0.67 cup" or vol == "0.66 cup" or vol == "0.66 cup (240.0 ml) aprx" or vol == "0.67 cup (240.0 ml) aprx" or vol == "32 tsp (5.0 ml) aprx" or vol == "0.6675 cup":
        v = "2/3 cup"
    elif vol == "0.75 cup, NFS" or vol == "0.738 cup" or vol == "11.84 tablespoon" or vol == "0.735 cup" or vol == "0.7375 cup" or vol == "3 1/4 cup" or vol == "0.75 cup whole kernels" or vol == "1 3/4 cup" or vol == "0.695 cup" or vol == "0.76 cup" or vol == "0.75 cup (240.0 ml) aprx" or vol == "1.545 1/2 cup" or vol == "12 tbsp" or vol == "12 Tbsp" or vol == "0.75 cup" or vol == "0.75 cup (240.0 ml) aprx" or vol == "3/4 cup, crumbled" or vol == "0.75 crumbled" or vol == "0.75 cup crumbled" or vol == "0.75 cup, shredded":
        v = "3/4 cup"
    elif vol == "0.815 cup":
        v = "7/8 cup"
    elif vol == "1 cup slices" or vol == "1 cup, shredded" or vol == "0.9975 cup" or vol == "0.914 cup" or vol == "0.98 cup" or vol == "1.95 1/2 cup" or vol == "0.99 cup" or vol == "1 cup whole kernels" or vol == "0.922 cup" or vol == "0.9 cup, whole" or vol == "1 cup, whole" or vol == "4 1/4 cup" or vol == "0.9225 cup" or vol == "0.921 cup" or vol == "16 tbsp" or vol == "16 Tbsp" or vol == "1 cup (240.0 ml) aprx" or vol == "1 cup, frozen" or vol == "1 cup, crumbled" or vol == "48 tsp (5.0 ml) aprx" or vol == "1 cup, unthawed" or vol == "48 tsp" or vol == "50 tsp":
        v = "1 cup"
    elif vol == "1.0989 cup":
        v = "1 heaping cup"
    elif vol == "1.125 cup":
        v = "1 cup + 2 tbsp"
    elif vol == "1.265 cup" or vol == "60 tsp" or vol == "2.5 1/2 cup" or vol == "20 tbsp":
        v = "1 1/4 cup"
    elif vol == "1.32 cup" or vol == "1.33 cup (240.0 ml) aprx":
        v = "1 1/3 cup"
    elif vol == "1.47 cup" or vol == "1.52 cup" or vol == "2.338 cup (not packed)" or vol == "2 container" or vol == "24 tbsp" or vol == "1.555 cup, NFS" or vol == "3.25 1/2 cup" or vol == "1.5 cup, chunks" or vol == "1.5 cup pieces" or vol == "2 3/4 cup":
        v = "1 1/2 cup"
    elif vol == "1.65375 cup":
        v = "1 2/3 cup"
    elif vol == "1.78 cup":
        v = "1.75 cup"
    elif vol == "2 cup, shredded" or vol == "2.025 cup" or vol == "2.0025 cup" or vol == "2.19 cup, chopped" or vol == "2.08 cup" or vol == "1.79 cup, whole" or vol == "1.88 cup, unthawed" or vol == "1.98 cup" or vol == "2.665 container" or vol == "2 cup, frozen" or vol == "5 1/3 cup" or vol == "7.5 1/3 cup" or vol == "2 cup, chopped" or vol == "32 tbsp" or vol == "32 Tbsp" or vol == "1.855 cup":
        v = "2 cup"
    elif vol == "2.22 cup":
        v = "2 1/4 cup"
    elif vol == "40 tbsp" or vol == "2.52 cup":
        v = "2 1/2 cup"
    elif vol == "3 cup (240.0 ml) aprx" or vol == "3 cup unsifted" or vol == "6 1/2 cup" or vol == "48 tbsp" or vol == "48 Tbsp" or vol == "50 tbsp" or vol == "50 Tbsp" or vol == "3.11 cup, NFS" or vol == "2.99 cup drained, rinsed":
        v = "3 cup"
    elif vol == "14 1/4 cup":
        v = "3 1/2 cup"

    # oz
    elif vol == "1/2 ounce" or vol == "0.5 ounce" or vol == "0.5 oz" or vol == "0.5 oz square Bakers":
        v = "1/2 oz"
    elif vol == "1 ounce":
        v = "1 oz"
    elif vol == "2 ounce":
        v = "2 oz"
    elif vol == "3 ounce":
        v = "3 oz"
    elif vol == "4 oz (23 whole kernels)" or vol == "4 ounce" or vol == "1/4 lb" or vol == "1/4 pound" or vol == "0.25 lb" or vol == "0.25 pound":
        v = "4 oz"
    elif vol == "1 can (6 oz)" or vol == "6 ounce" or vol == "2 3 oz fillets":
        v = "6 oz"
    elif vol == "7 ounce":
        v = "7 oz"
    elif vol == "1/2 lb" or vol == "0.5 pound" or vol == "8 ounce" or vol == "0.5 lb" or vol == "1/2 pound":
        v = "8 oz"
    elif vol == "9 ounce":
        v = "9 oz"
    elif vol == "12 ounce":
        v = "12 oz"
    elif vol == "14 ounce":
        v = "14 oz"
    elif vol == "15 ounce":
        v = "15 oz"

    # cans
    elif vol == "7 oz":
        v = "7 oz can"
    elif vol == "13.5 fl oz can":
        v = "13.5 oz can"
    elif vol == "27 fl oz can":
        v = "2 x 13.5 oz can"
    elif vol == "1 can (2 oz) drained":
        v = "2 oz, drained"
    elif vol == "1 can, drained (4.4 oz)":
        v = "4.4 oz"
    elif vol == "14.5 ounce":
        v = "14.5 oz can"
    elif vol == "0.5 can drained solids" or vol == "0.5 can" or vol == "0.5 can, drained, rinsed" or vol == "0.5 can drained" or vol == "0.5 15.5oz can drained, rinsed":
        v = "1/2 x 15.5 oz can"
    elif vol == "1 15.5oz can, drained and rinsed" or vol == "1 can drained solids" or vol == "1 can drained, rinsed" or vol == "1 can, drained, rinsed" or vol == "1 can drained" or vol == "15.5oz can drained, rinsed" or vol == "15.5oz can, NOT drained or rinsed" or vol == "1 15.5oz can, NOT drained or rinsed":
        v = "15.5 oz can"
    elif vol == "1.5 can drained solids":
        v = "1 1/2 x 15.5 oz can"
    elif vol == "19.5 ounce" or vol == "3 6.5oz cans":
        v = "3 x 6.5oz can"
    elif vol == "28 ounce":
        v = "28 oz can"
    elif vol == "56 ounce" or vol == "2 28oz cans":
        v = "2 x 28 oz can"
    elif vol == "29 ounce":
        v = "2 x 14.5oz can"
    elif vol == "2 15.5oz can, drained and rinsed" or vol == "2 can drained solids" or vol == "2 can" or vol == "2 can, drained, rinsed" or vol == "2 can drained" or vol == "2x15.5oz can drained, rinsed" or vol == "2 15.5oz cans" or vol == "2 15.5oz can, NOT drained or rinsed":
        v = "2 x 15.5 oz can"
    elif vol == "3 15.5oz can, drained and rinsed" or vol == "3 can drained solids" or vol == "3 can" or vol == "3 can, drained, rinsed" or vol == "3 can drained" or vol == "3x15.5oz can drained, rinsed" or vol == "3 15.5oz cans" or vol == "3 15.5oz can, NOT drained or rinsed":
        v = "3 x 15.5 oz can"
    elif vol == "4 15.5oz can, drained and rinsed" or vol == "4 can drained solids" or vol == "4 can" or vol == "4 can, drained, rinsed" or vol == "4 can drained" or vol == "4x15.5oz can drained, rinsed" or vol == "4 15.5oz cans" or vol == "4 15.5oz can, NOT drained or rinsed":
        v = "4 x 15.5 oz can"
    elif vol == "87 ounce" or vol == "87 oz":
        v = "6 x 14.5oz can"

    # lb
    elif vol == "0.25 pound" or vol == "0.25 lb":
        v = "1/4 lb"
    elif vol == "0.33 pound" or vol == "0.33 lb":
        v = "1/3 lb"
    elif vol == "0.5 pound" or vol == "0.5 lb":
        v = "1/2 lb"
    elif vol == "0.66 pound" or vol == "0.66 lb" or vol == "0.67 pound" or vol == "0.67 lb":
        v = "2/3 lb"
    elif vol == "0.75 pound" or vol == "0.75 lb":
        v = "3/4 lb"
    elif vol == "16 oz" or vol == "16 ounce" or vol == "1 pound" or vol == "1 pound dried beans":
        v = "1 lb"
    elif vol == "1.3 pound":
        v = "1.3 lb"
    elif vol == "1.5 pound" or vol == "24 oz" or vol == "24 ounce" or vol == "1.5 pounds":
        v = "1.5 lb"
    elif vol == "32 oz" or vol == "32 ounce" or vol == "2 pound":
        v = "2 lb"
    elif vol == "3 pound":
        v = "3 lb"
    elif vol == "4 pound":
        v = "4 lb"

    # protein powder
    elif vol == "0.25 scoop":
        v = "1/4 scoop"
    elif vol == "0.5 scoop | about" or vol == "0.5 scoop" or vol == "0.5 scoops":
        v = "1/2 scoop"
    elif vol == "0.67 scoop | about" or vol == "0.67 scoop" or vol == "0.66 scoop | about" or vol == "0.66 scoop":
        v = "2/3 scoop"
    elif vol == "0.75 scoop | about" or vol == "0.75 scoop":
        v = "3/4 scoop"
    elif vol == "1.05 scoop | about" or vol == "1 scoop | about":
        v = "1 scoop"
    elif vol == "1.55 scoop | about" or vol == "1.5 scoops" or vol == "1.5 scoop | about":
        v = "1 1/2 scoop"
    elif vol == "2.08 scoop | about" or vol == "2 scoops" or vol == "2 scoop | about":
        v = "2 scoop"
    elif vol == "3.1 scoop | about" or vol == "3 scoops" or vol == "3 scoop | about":
        v = "3 scoop"
    elif vol == "6.21 scoop | about":
        v = "6 scoop"

    # dates & olives
    elif vol == "11 date, pitted" or vol == "11 olives":
        v = "11 pitted"
    elif vol == "16 date, pitted":
        v = "16 pitted"
    elif vol == "20 date, pitted":
        v = "20 pitted"
    elif vol == "28 date, pitted" or vol == "28 -6 dates":
        v = "28 pitted"
    elif vol == "30 date, pitted":
        v = "30 pitted"
    elif vol == "31 date, pitted":
        v = "31 pitted"
    elif vol == "32 date, pitted":
        v = "32 pitted"

    # produce
    elif vol == "1/2 fruit, without skin and seed" or vol == "0.5 fruit, without skin and seed" or vol == "0.5 Banana" or vol == "0.5 banana" or vol == "1/2 banana" or vol == "1/2 Banana" or vol == "1/2 Onion" or vol == "0.5 Onion" or vol == "1/2 onion" or vol == "0.5 onion" or vol == "0.5 medium bell pepper" or vol == "1/2 medium bell pepper" or vol == "0.5 whole" or vol == "1/2 whole" or vol == "0.5 English" or vol == "1/2 English" or vol == "0.5 Italian tomato" or vol == "1/2 Italian tomato" or vol =="0.5 small" or vol == "1/2 small" or vol == "1/2 eggplant, unpeeled (approx 1-1/4 lb)"or vol == "0.5 eggplant, unpeeled (approx 1-1/4 lb)" or vol == "0.5 medium":
        v = "1/2 medium"
    elif vol == "1.09 small (6 to 6-7/8 long)" or vol == "1 fruit (2 dia)" or vol == "1 medium (2-1/2 dia)" or vol == "1 fruit, without skin and seed" or vol == "1 medium (approx 2-3/4 long, 2-1/2 dia.)" or vol == "1.33 medium" or vol == "1 banana" or vol == "1 Banana" or vol == "1 onion" or vol == "1 Onion" or vol == "1 medium bell pepper" or vol == "1 whole" or vol == "1 English" or vol == "1 Italian tomato"or vol == "1 plum tomato" or vol =="1 small" or vol == "1 eggplant, unpeeled (approx 1-1/4 lb)":
        v = "1 medium"
    elif vol == "1.825 eggplant, unpeeled (approx 1-1/4 lb)" or vol == "2.18 small (6 to 6-7/8 long)" or vol == "2 fruit, without skin and seed" or vol == "2 medium (2-1/2 dia)" or vol == "2 banana" or vol == "2 Banana" or vol == "2 onion" or vol == "2 Onion" or vol == "2 medium bell peppers" or vol == "2 whole" or vol == "2 English" or vol == "2 Italian tomato"or vol == "2 plum tomato" or vol == "2 small" or vol == "2 eggplant, unpeeled (approx 1-1/4 lb)":
        v = "2 medium"
    elif vol == "3 medium (2-1/2 dia)" or vol == "3.27 small (6 to 6-7/8 long)" or vol == "3 fruit, without skin and seed" or vol == "3 medium (approx 2-3/4 long, 2-1/2 dia.)" or vol == "3 banana" or vol == "3 Banana" or vol == "3 onion" or vol == "3 Onion" or vol == "3 medium bell peppers" or vol == "3 whole" or vol == "3 English" or vol == "3 Italian tomato"or vol == "3 plum tomato" or vol == "3 small" or vol == "3 eggplant, unpeeled (approx 1-1/4 lb)":
        v = "3 medium"
    elif vol == "4.36 small (6 to 6-7/8 long)" or vol == "4 medium (2-1/2 dia)" or vol == "4 fruit, without skin and seed" or vol == "4 banana" or vol == "4 Banana" or vol == "4 onion" or vol == "4 Onion" or vol == "4 medium bell peppers" or vol == "4 whole" or vol == "4 English" or vol == "4 Italian tomato"or vol == "4 plum tomato" or vol == "4 small" or vol == "4 eggplant, unpeeled (approx 1-1/4 lb)":
        v = "4 medium"
    elif vol == "5 fruit, without skin and seed" or vol == "5 banana" or vol == "5 Banana" or vol == "5 onion" or vol == "5 Onion" or vol == "5 medium bell peppers" or vol == "5 whole" or vol == "5 English" or vol == "5 Italian tomato"or vol == "5 plum tomato" or vol == "5 small" or vol == "5 eggplant, unpeeled (approx 1-1/4 lb)":
        v = "5 medium"
    elif vol == "8 small":
        v = "8 medium"
    elif vol == "9 small":
        v = "9 medium"
    elif vol == "1 kiwi | per":
        v = "1 medium"
    elif vol == "2 kiwi | per":
        v = "2 medium"
    elif vol == "0.89 small (6 to 6-7/8 long)" or vol == "0.82 Banana" or vol == "0.735 fruit, without skin and seed":
        v = "1 small"
    elif vol == "1 plantain":
        v = "1 large or 2 small"
    elif vol == "5.385 sweetpotato, 5 long":
        v = "6 small"

    # eggs
    elif vol == "1.25 eggplant, unpeeled (approx 1-1/4 lb)" or vol == "1 egg" or vol == "2.44 beet (2 dia)" or vol == "1 large (2-1/4 per pound, approx 3-3/4 long, 3 dia.)":
        v = "1 large"
    elif vol == "2 egg":
        v = "2 large"
    elif vol == "2.5 egg":
        v = "2 1/2 large"
    elif vol == "3 egg":
        v = "3 large"
    elif vol == "4.13 Banana" or vol == "4 egg":
        v = "4 large"
    elif vol == "5 egg":
        v = "5 large"
    elif vol == "6 egg":
        v = "6 large"
    elif vol == "8 egg":
        v = "8 large"

    # thighs
    elif vol == "6 thigh without skin":
        v = "6 medium"

    # garlic
    elif vol == "9.99 cloves":
        v = "1 small head"
    elif vol == "11 clove" or vol == "15 clove":
        v = "1 head"
    elif vol == "22 clove" or vol == "30 clove":
        v = "2 head"

    # beets
    elif vol == "1 beet (2 dia)":
        v = "1 small"

    # other
    elif vol == "16 cup":
        v = "1 gallon"

    return v

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
        changed += 1

    print(str(changed) + " files updated")

if __name__ == '__main__':
    main()
