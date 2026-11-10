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
        return ("Oat Fiber")
    elif(num == 10):
        return ("Cornstarch")
    elif(num == 11):
        return ("Cocoa Powder")
    elif(num == 12):
        return ("Whey Protein Powder")
    elif(num == 13):
        return ("Casein Protein Powder")
    elif(num == 14):
        return ("Pea Protein Powder")
    elif(num == 15):
        return ("Coconut Flour")
    elif(num == 16):
        return ("Chia Seeds")
    elif(num == 17):
        return ("Peanut Flour")
    elif(num == 18):
        return ("Flaxmeal")
    elif(num == 19):
        return ("Almond Flour")
    elif(num == 20):
        return ("Almond Meal")
    elif(num == 21):
        return ("Millet Flour")
    elif(num == 22):
        return ("Hemp Seeds")
    elif(num == 23):
        return ("Psyllium Husk")
    elif(num == 24):
        return ("Ground Coffee")
    elif(num == 25):
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
        print("9:  Oat Fiber")
        print("10: Cornstarch")
        print("11: Cocoa Powder")
        print("12: Whey Protein Powder")
        print("13: Casein Protein Powder")
        print("14: Pea Protein Powder")
        print("15: Coconut Flour")
        print("16: Chia Seeds")
        print("17: Peanut Flour")
        print("18: Flaxmeal")
        print("19: Almond Flour")
        print("20: Almond Meal")
        print("21: Millet Flour")
        print("22: Hemp Seeds")
        print("23: Psyllium Husk")
        print("24: Ground Coffee")
        print("25: Granulated Sugar")

# user input for entering FROM flour, FROM amount, and TO flour
# returns all 3 entered values
def select():
    # FROM flour
    options(0)
    while(True):
        try:
            f = int(input("\nEnter a number to select your FROM flour: "))
            if(f < 1 or f > 25):
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
            if(t < 1 or t > 25):
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
    oatFiber = 19
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

    arr = [0] * 25
    arr[0] = ap_noHeat
    arr[1] = ap_heat
    arr[2] = ww_noHeat
    arr[3] = ww_heat
    arr[4] = vwg_noHeat
    arr[5] = vwg_heat
    arr[6] = oatFlour
    arr[7] = quickOat
    arr[8] = oatFiber
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

    num = round((g / arr[f-1]) * arr[t-1], 1)
    print("For " + str(g) + " g of " + options(f).upper() + ", you will need APPROXIMATELY " + str(num) + " g of " + options(t).upper())
    return num


def main():
    os.system('cls')
    f, g, t = select()
    num = calc(f, g, t)

if __name__ == '__main__':
    main()
