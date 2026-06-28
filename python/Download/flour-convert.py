import os

# prints selection options
# if a number [1,24] is entered, just prints out the 1 flour entered
# otherwise, prints the entire election list
def options(num):
    if(num == 1):
        return ("All Purpose Flour (Not Heat Treated)")
    elif(num == 2):
        return ("All Purpose Flour (Heat Treated)")
    elif(num == 3):
        return ("Whole Wheat Flour (Not Heat Treated)")
    elif(num == 4):
        return ("Whole Wheat Flour (Heat Treated)")
    elif(num == 5):
        return ("Vital Wheat Gluen (Not Heat Treated)")
    elif(num == 6):
        return ("Vital Wheat Gluten (Heat Treated)")
    elif(num == 7):
        return ("Oat Flour")
    elif(num == 8):
        return ("Quick Oats")
    elif(num == 9):
        return ("Cornstarch")
    elif(num == 10):
        return ("Cocoa Powder")
    elif(num == 11):
        return ("Whey Protein Powder")
    elif(num == 12):
        return ("Casein Protein Powder")
    elif(num == 13):
        return ("Pea Protein Powder")
    elif(num == 14):
        return ("Coconut Flour")
    elif(num == 15):
        return ("Chia Seeds")
    elif(num == 16):
        return ("Peanut Flour")
    elif(num == 17):
        return ("Flaxmeal")
    elif(num == 18):
        return ("Almond Flour")
    elif(num == 19):
        return ("Almond Meal")
    elif(num == 20):
        return ("Millet Flour")
    elif(num == 21):
        return ("Hemp Seeds")
    elif(num == 22):
        return ("Psyllium Husk")
    elif(num == 23):
        return ("Ground Coffee")
    elif(num == 24):
        return ("Granulated Sugar")
    else:
        print("1:  All Purpose Flour (Not Heat Treated)")
        print("2:  All Purpose Flour (Heat Treated)")
        print("3:  Whole Wheat Flour (Not Heat Treated)")
        print("4:  Whole Wheat Flour (Heat Treated)")
        print("5:  Vital Wheat Gluten (Not Heat Treated)")
        print("6:  Vital Wheat Gluten (Heat Treated)")
        print("7:  Oat Flour")
        print("8:  Quick Oats")
        print("9:  Cornstarch")
        print("10: Cocoa Powder")
        print("11: Whey Protein Powder")
        print("12: Casein Protein Powder")
        print("13: Pea Protein Powder")
        print("14: Coconut Flour")
        print("15: Chia Seeds")
        print("16: Peanut Flour")
        print("17: Flaxmeal")
        print("18: Almond Flour")
        print("19: Almond Meal")
        print("20: Millet Flour")
        print("21: Hemp Seeds")
        print("22: Psyllium Husk")
        print("23: Ground Coffee")
        print("24: Granulated Sugar")

# user input for entering FROM flour, FROM amount, and TO flour
# returns all 3 entered values
def select():
    # FROM flour
    options(0)
    while(True):
        try:
            f = int(input("\nEnter a number to select your FROM flour: "))
            if(f < 1 or f > 23):
                f = int("abc")
            print("You selected: ", end="")
            print(options(f))
            break
        except:
            continue

    print()

    # FROM amount
    while(True):
        try:
            g = float(input("\nEnter the amount (in grams) of your FROM flour: "))
            if(g < 0):
                g = int("abc")
            print("Amount [g]: ", end="")
            print(g)
            break
        except:
            continue

    print()

    # TO flour
    options(0)
    while(True):
        try:
            t = int(input("\nEnter a number to select your TO flour: "))
            if(t < 1 or t > 23):
                t = int("abc")
            print("You selected: ", end="")
            print(options(t))
            break
        except:
            continue

    print()

    return f, g, t

# conversion calculations
def calc(f, g, t):
    # factors for 30 g water
    ap_noHeat = 53
    ap_heat = 45
    ww_noHeat = 41
    ww_heat = 40
    vwg_noHeat = 36
    vwg_heat = 29
    oatFlour = 41
    quickOat = 45
    cornstarch = 35
    cocoa = 23
    whey = 64
    casein = 13
    pea = 15
    coconut = 8
    chia = 30
    pb2 = 31
    flax = 43
    almondFlour = 53
    almondMeal = 45
    milletFlour = 45
    hemp = 60
    psyllium = 10
    coffee = 60
    sugar = 180

    arr = [0] * 24
    arr[1] = ap_noHeat
    arr[2] = ap_heat
    arr[3] = ww_noHeat
    arr[4] = ww_heat
    arr[5] = vwg_noHeat
    arr[6] = vwg_heat
    arr[7] = oatFlour
    arr[8] = quickOat
    arr[9] = cornstarch
    arr[10] = cocoa
    arr[11] = whey
    arr[12] = casein
    arr[13] = pea
    arr[14] = coconut
    arr[15] = chia
    arr[16] = pb2
    arr[17] = flax
    arr[18] = almondFlour
    arr[19] = almondMeal
    arr[20] = milletFlour
    arr[21] = hemp
    arr[22] = psyllium
    arr[23] = coffee
    arr[24] = sugar

    num = round(float(float(g / arr[f]) * arr[t]),1)
    print("For " + str(g) + " g of " + options(f).upper() + ", you will need APPROXIMATELY " + str(num) + " g of " + options(t).upper())
    return num


def main():
    os.system('cls')
    f, g, t = select()
    num = calc(f, g, t)

if __name__ == '__main__':
    main()
