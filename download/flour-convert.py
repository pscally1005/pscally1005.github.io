import os

# prints selection options
# if a number [1,14] is entered, just prints out the 1 flour entered
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
        return ("Coconut Flour")
    elif(num == 14):
        return ("Chia Seeds")
    # elif(num == 15):
    #     return ("Flaxmeal")
    # elif(num == 16):
    #     return ("Peanut Flour")
    # elif(num == 17):
    #     return ("Almond Flour")
    # elif(num == 18):
    #     return ("Almond Meal")
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
        print("13: Coconut Flour")
        print("14: Chia Seeds")
        # print("15: Flaxmeal")
        # print("16: Peanut Flour")
        # print("17: Almond Flour")
        # print("18: Almond Meal")

# user input for entering FROM flour, FROM amount, and TO flour
# returns all 3 entered values
def select():
    # FROM flour
    options(0)
    while(True):
        try:
            f = int(input("\nEnter a number to select your FROM flour: "))
            if(f < 1 or f > 14):
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
            if(t < 1 or t > 14):
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
    coconut = 8
    chia = 30
    # flax = 
    # pb2 = 
    # almondFlour = 
    # almondMeal = 

    arr = [0] * 15
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
    arr[13] = coconut
    arr[14] = chia
    # arr[15] = flax
    # arr[16] = pb2
    # arr[17] = almondFlour
    # arr[18] = almondMeal

    num = round(float(float(g / arr[f]) * arr[t]),1)
    print("For " + str(g) + " g of " + options(f).upper() + ", you will need APPROXIMATELY " + str(num) + " g of " + options(t).upper())
    return num


def main():
    os.system('cls')
    f, g, t = select()
    num = calc(f, g, t)

if __name__ == '__main__':
    main()