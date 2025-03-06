# Download csv to /python/testing folder, and run script to fix grams in ingredients file

import pandas as pd
import os
import glob
import csv

def grams(food, mass, vol):
    # Salt, baking powder, baking soda
    if food == "Salt" or food == "Baking powder" or food == "Baking soda" or food == "Potassium Chloride" or food == "Flakey salt":
        if vol == "Small pinch" or vol == "Tiny pinch":
            return str("0.15")
        if vol == "1/16 tsp" or vol == "Pinch":
            return str("0.38")
        elif vol == "1/8 tsp" or vol == "Large pinch" or vol == "Big pinch":
            return str("0.75")
        elif vol == "1/4 tsp":
            return str("1.5")
        elif vol == "1/2 tsp":
            return str("3")
        elif vol == "3/4 tsp":
            return str("4.5")
        elif vol == "1 tsp":
            return str("6")
        else:
            return str(mass)
        
    # Salty spices
    if food == "Chicken bouillon powder" or food == "Bouillon powder" or food == "Lemon pepper" or food == "Everything bagel seasoning":
        if vol == "1/2 tsp":
            return str("2")
        elif vol == "1 tsp":
            return str("4")
        elif vol == "1.5 tsp" or vol == "1/2 tbsp":
            return str("6")
        elif vol == "2 tsp":
            return str("8")
        elif vol == "3 tsp" or vol == "1 tbsp":
            return str("12")
        else:
            return str(mass)
    
    # Extracts and sweeteners
    elif food == "Liquid monk fruit" or food == "Liquid stevia" or food == "Liquid stevia or monk fruit" or food == "Vanilla extract" or food == "Almond extract" or food == "Mint extract" or food == "Butter extract" or food == "Maple extract" or food == "Rum extract" or food == "Almond extract, or vanilla" or food == "Vanilla extract, or almond":
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
        
    # Denser spices
    elif food == "Garlic powder" or food == "Onion powder" or food == "Black pepper, ground" or food == "Paprika" or food == "Cumin, ground" or food == "Chili powder" or food == "Cayenne pepper" or food == "Old Bay" or food == "Turmeric, ground" or food == "Black pepper" or food == "Cinnamon, ground" or food == "Cinnamon":
        if vol == "1/8 tsp":
            return str("0.38")
        elif vol == "1/4 tsp":
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
        
    # Less dense spices
    elif food == "Allspice, ground" or food == "Cloves, ground" or food == "Garam masala" or food == "Ginger, ground":
        if vol == "1/8 tsp":
            return str("0.25")
        elif vol == "1/4 tsp":
            return str("0.5")
        elif vol == "1/2 tsp":
            return str("1")
        elif vol == "1 tsp":
            return str("2")
        elif vol == "1/2 tbsp" or vol == "1.5 tsp":
            return str("3")
        elif vol == "2 tsp":
            return str("4")
        elif vol == "3 tsp" or vol == "1 tbsp":
            return str("6")
        elif vol == "6 tsp" or vol == "2 tbsp":
            return str("12")
        else:
            return str(mass)
        
    # Nutritional yeast, cocoa, coconut flakes
    elif food == "Nutritional yeast" or food == "Cocoa powder" or food == "Carob powder" or food == "Cacao powder" or food == "Unsweetened coconut flakes":
        if vol == "1/2 tbsp" or vol == "1.5 tsp":
            return str("2.5")
        elif vol == "1 tbsp":
            return str("5")
        elif vol == "2 tbsp":
            return str("10")
        elif vol == "3 tbsp":
            return str("15")
        elif vol == "4 tbsp" or vol == "1/4 cup":
            return str("20")
        elif vol == "5 tbsp":
            return str("25")
        elif vol == "1/3 cup":
            return str("27")
        elif vol == "6 tbsp":
            return str("30")
        elif vol == "7 tbsp":
            return str("35")
        elif vol == "8 tbsp" or vol == "1/2 cup":
            return str("40")
        elif vol == "9 tbsp":
            return str("45")
        elif vol == "10 tbsp":
            return str("50")
        elif vol == "2/3 cup":
            return str("53")
        elif vol == "11 tbsp":
            return str("55")
        elif vol == "12 tbsp" or vol == "3/4 cup":
            return str("60")
        elif vol == "13 tbsp":
            return str("65")
        elif vol == "14 tbsp":
            return str("70")
        elif vol == "15 tbsp":
            return str("75")
        elif vol == "16 tbsp" or vol == "1 cup":
            return str("80")
        elif vol == "1.5 cup":
            return str("120")
        elif vol == "2 cup":
            return str("160")
        else:
            return str(mass)
        
    # Herbs
    elif food == "Basil, dried" or food == "Oregano, dried" or food == "Thyme, dried" or food == "Parsley, dried" or food == "Red pepper flakes" or food == "Rosemary, dried" or food == "Italian seasoning":
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
    elif food == "Water" or food == "Unsweetened original almond milk" or food == "Unsweetened almond milk" or food == "Unsweetened vanilla almond milk" or food == "Skim milk" or food == "Fairlife skim milk" or food == "Extra virgin olive oil" or food == "Soy sauce, low sodium, gluten free" or food == "Balsamic vinegar" or food == "White vinegar" or food == "Apple cider vinegar" or food == "Unsweetened applesauce" or food == "White vinegar, or apple cider vinegar" or food == "Unsweetened almond milk, or water" or food == "Unsweetened vanilla almond milk, or water" or food == "Pumpkin puree" or food == "Pumpkin Puree" or food == "Pumpkin puree, or sweet potato" or food == "Pumpkin puree, or sweet potato puree" or food == "Sweet potato puree" or food == "Sweet Potato puree, Pumpkin puree, or Butternut Squash puree" or food == "Sweet potato Puree, or Pumpkin puree" or food == "Low sodium soy sauce" or food == "Fat free Italian dressing" or food == "Italian dressing" or food == "Lime juice" or food == "Lemon juice" or food == "Sesame oil" or food == "Egg whites" or food == "Liquid egg whites" or food == "Canola oil" or food == "Vegetable oil" or food == "Evaporated milk" or food == "Fat free evaporated milk" or food == "Chicken bone broth" or food == "Chicken broth" or food == "Vegetable broth" or food == "Low sodium chicken broth" or food == "Low sodium vegetable broth":
        if vol == "1/4 tsp":
            return str("1.25")
        elif vol == "1/2 tsp":
            return str("2.5")
        elif vol == "1 tsp":
            return str("5")
        elif vol == "1/2 tbsp":
            return str("7.5")
        elif vol == "2 tsp":
            return str("10")
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
        elif vol == "7 tbsp":
            return str("105")
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
        
    # Coconut oil
    if food == "Extra virgin coconut oil" or food == "Extra virgin coconut oil, or extra virgin olive oil":
        if vol == "1 tsp":
            return str("2")
        elif vol == "1/2 tbsp":
            return str("7")
        elif vol == "1 tbsp":
            return str("14")
        elif vol == "2 tbsp":
            return str("28")
        elif vol == "3 tbsp":
            return str("42")
        elif vol == "4 tbsp" or vol == "1/4 cup":
            return str("56")
        elif vol == "5 tbsp":
            return str("70")
        elif vol == "6 tbsp":
            return str("84")
        elif vol == "7 tbsp":
            return str("98")
        elif vol == "8 tbsp" or vol == "1/2 cup":
            return str("112")
        else:
            return str(mass)
        
    # Yogurt & cottage cheese
    elif food == "Nonfat cottage cheese" or food == "Plain nonfat greek yogurt" or food == "Vanilla Nonfat Greek Yogurt, Sugar Free":
        if vol == "1 tbsp":
            return str("14")
        elif vol == "2 tbsp":
            return str("28")
        elif vol == "1/4 cup" or vol == "4 tbsp":
            return str("56")
        elif vol == "1/2 cup" or vol == "8 tbsp":
            return str("113")
        elif vol == "3/4 cup":
            return str("170")
        elif vol == "1 cup":
            return str("226")
        elif vol == "1.25 cup":
            return str("283")
        elif vol == "1.5 cup":
            return str("340")
        elif vol == "1.75 cup":
            return str("396")
        elif vol == "2 cup":
            return str("454")
        else:
            return str(mass)
        
    # Flours
    if food == "Vital wheat gluten" or food == "Flour" or food == "All purpose flour" or food == "White flour" or food == "Whole wheat flour" or food == "Cornmeal" or food == "Panko breadcrumbs" or food == "Whole wheat breadcrumbs" or food == "Breadcrumbs" or food == "Millet flour" or food == "Chickpea flour" or food == "Coconut flour":
        if vol == "2 tbsp":
            return str("15")
        elif vol == "4 tbsp" or vol == "1/4 cup":
            return str("30")
        elif vol == "1/2 cup":
            return str("60")
        elif vol == "3/4 cup":
            return str("90")
        elif vol == "1 cup":
            return str("120")
        elif vol == "1.5 cup":
            return str("180")
        elif vol == "2 cup":
            return str("240")
        else:
            return str(mass)
        
    # Protein powder
    if food == "Whey protein powder, unflavored" or food == "Whey protein powder, chocolate" or food == "Whey protein powder, vanilla" or food == "Nutricost Whey Unflavored Protein Powder" or food == "Casein protein powder, unflavored" or food == "Casein protein powder, chocolate" or food == "Casein protein powder, vanilla" or food == "Nutricost Casein Unflavored Protein Powder":
        if vol == "1/3 scoop":
            return str("10")
        elif vol == "1/2 scoop":
            return str("15")
        elif vol == "2/3 scoop":
            return str("20")
        elif vol == "1 scoop":
            return str("30")
        elif vol == "1.33 scoop":
            return str("40")
        elif vol == "1.5 scoop":
            return str("45")
        elif vol == "2 scoop":
            return str("60")
        elif vol == "2.5 scoop":
            return str("75")
        elif vol == "3 scoop":
            return str("90")
        elif vol == "4 scoop":
            return str("120")
        else:
            return str(mass)
        
    # Nut butters
    if food == "Almond butter" or food == "Peanut butter" or food == "Natural peanut butter" or food == "Natural peanut butter, or tahini" or food == "Walnut butter" or food == "Cashew butter" or food == "Sunflower seed butter" or food == "Sunflower butter" or food == "Pistachio butter" or food == "Pumpkin seed butter" or food == "Tahini, or any other nut/seed butter":
        if vol == "1/2 tbsp":
            return str("8")
        elif vol == "1 tbsp":
            return str("16")
        elif vol == "1.5 tbsp":
            return str("24")
        elif vol == "2 tbsp":
            return str("32")
        elif vol == "2.5 tbsp":
            return str("40")
        elif vol == "3 tbsp":
            return str("48")
        elif vol == "4 tbsp" or vol == "1/4 cup":
            return str("64")
        elif vol == "5 tbsp":
            return str("80")
        elif vol == "6 tbsp":
            return str("96")
        elif vol == "8 tbsp" or vol == "1/2 cup":
            return str("128")
        elif vol == "12 tbsp" or vol == "3/4 cup":
            return str("196")
        elif vol == "16 tbsp" or vol == "1 cup":
            return str("256")
        else:
            return str(mass)
        
    # Syrup
    if food == "Sugar free syrup" or food == "Sugar free syrup, or maple syrup or honey" or food == "Sugar free syrup, or honey or maple syrup" or food == "Sugar free syrup, or honey" or food == "Sugar free syrup, or maple syrup" or food == "Sugar free syrup, optional" or food == "Maple syrup" or food == "Maple syrup, or honey":
        if vol == "1/2 tbsp":
            return str("10")
        elif vol == "1 tbsp":
            return str("20")
        elif vol == "1.5 tbsp":
            return str("30")
        elif vol == "2 tbsp":
            return str("40")
        elif vol == "3 tbsp":
            return str("60")
        elif vol == "4 tbsp" or vol == "1/4 cup":
            return str("80")
        elif vol == "5 tbsp":
            return str("100")
        elif vol == "1/3 cup":
            return str("107")
        elif vol == "6 tbsp":
            return str("120")
        elif vol == "8 tbsp" or vol == "1/2 cup":
            return str("160")
        elif vol == "2/3 cup":
            return str("213")
        elif vol == "12 tbsp" or vol == "3/4 cup":
            return str("240")
        elif vol == "16 tbsp" or vol == "1 cup":
            return str("320")
        else:
            return str(mass)
        
    # Onions
    if food == "Onion":
        if vol == "1/2 medium":
            return str("55")
        elif vol == "1 medium":
            return str("110")
        elif vol == "2 medium":
            return str("220")
        elif vol == "3 medium":
            return str("330")
        elif vol == "4 medium":
            return str("440")
        elif vol == "5 medium":
            return str("550")
        else:
            return str(mass)
        
    # Peppers
    if food == "Bell pepper":
        if vol == "1/2 medium":
            return str("60")
        elif vol == "1 medium":
            return str("120")
        elif vol == "2 medium":
            return str("240")
        elif vol == "3 medium":
            return str("360")
        elif vol == "4 medium":
            return str("480")
        elif vol == "5 medium":
            return str("600")
        else:
            return str(mass)
        
    # Tomatoes
    if food == "Tomato":
        if vol == "1/2 medium":
            return str("50")
        elif vol == "1 medium":
            return str("100")
        elif vol == "2 medium":
            return str("200")
        elif vol == "3 medium":
            return str("300")
        elif vol == "4 medium":
            return str("400")
        elif vol == "5 medium":
            return str("500")
        else:
            return str(mass)
        
    # Lettuce
    if food == "Lettuce" or food == "Romaine lettuce":
        if vol == "1/2 head" or vol == "4 oz":
            return str("113")
        elif vol == "1 head"  or vol == "8 oz, about 2 heads" or vol == "8 oz":
            return str("226")
        elif vol == "2 heads" or vol == "2 head":
            return str("454")
        elif vol == "3 medium":
            return str("360")
        elif vol == "4 medium":
            return str("480")
        elif vol == "5 medium":
            return str("600")
        else:
            return str(mass)
        
    # Powdered pb
    if food == "Powdered peanut butter":
        if vol == "1/2 tbsp" or vol == "1.5 tsp":
            return str("3")
        elif vol == "1 tbsp":
            return str("6")
        elif vol == "1.5 tbsp":
            return str("9")
        elif vol == "2 tbsp":
            return str("12")
        elif vol == "3 tbsp":
            return str("18")
        elif vol == "4 tbsp" or vol == "1/4 cup":
            return str("24")
        elif vol == "5 tbsp":
            return str("30")
        elif vol == "1/3 cup":
            return str("32")
        elif vol == "6 tbsp":
            return str("36")
        elif vol == "7 tbsp":
            return str("42")
        elif vol == "8 tbsp" or vol == "1/2 cup":
            return str("48")
        elif vol == "9 tbsp":
            return str("54")
        elif vol == "10 tbsp":
            return str("60")
        elif vol == "2/3 cup":
            return str("64")
        elif vol == "11 tbsp":
            return str("66")
        elif vol == "12 tbsp" or vol == "3/4 cup":
            return str("72")
        elif vol == "13 tbsp":
            return str("78")
        elif vol == "14 tbsp":
            return str("84")
        elif vol == "15 tbsp":
            return str("90")
        elif vol == "16 tbsp" or vol == "1 cup":
            return str("96")
        else:
            return str(mass)
        
    # Chia seeds
    if food == "Chia seeds":
        if vol == "1/2 tbsp" or vol == "1.5 tsp":
            return str("6")
        elif vol == "1 tbsp":
            return str("12")
        elif vol == "1.5 tbsp":
            return str("18")
        elif vol == "2 tbsp":
            return str("24")
        elif vol == "3 tbsp":
            return str("36")
        elif vol == "4 tbsp" or vol == "1/4 cup":
            return str("48")
        elif vol == "5 tbsp":
            return str("60")
        elif vol == "1/3 cup":
            return str("64")
        elif vol == "6 tbsp":
            return str("72")
        elif vol == "7 tbsp":
            return str("84")
        elif vol == "8 tbsp" or vol == "1/2 cup":
            return str("96")
        elif vol == "9 tbsp":
            return str("108")
        elif vol == "10 tbsp":
            return str("120")
        elif vol == "2/3 cup":
            return str("128")
        elif vol == "11 tbsp":
            return str("132")
        elif vol == "12 tbsp" or vol == "3/4 cup":
            return str("144")
        elif vol == "13 tbsp":
            return str("156")
        elif vol == "14 tbsp":
            return str("168")
        elif vol == "15 tbsp":
            return str("180")
        elif vol == "16 tbsp" or vol == "1 cup":
            return str("192")
        else:
            return str(mass)
        
    # Oat flour
    if food == "Oat flour" or food == "Oat flour, or almond flour" or food == "Oat flour, or almond":
        if vol == "1/2 tbsp" or vol == "1.5 tsp":
            return str("3")
        elif vol == "1 tbsp":
            return str("6")
        elif vol == "1.5 tbsp":
            return str("9")
        elif vol == "2 tbsp":
            return str("11")
        elif vol == "3 tbsp":
            return str("17")
        elif vol == "4 tbsp" or vol == "1/4 cup":
            return str("23")
        elif vol == "5 tbsp":
            return str("28")
        elif vol == "1/3 cup":
            return str("30")
        elif vol == "6 tbsp":
            return str("34")
        elif vol == "7 tbsp":
            return str("39")
        elif vol == "8 tbsp" or vol == "1/2 cup":
            return str("45")
        elif vol == "9 tbsp":
            return str("51")
        elif vol == "10 tbsp":
            return str("56")
        elif vol == "2/3 cup":
            return str("60")
        elif vol == "11 tbsp":
            return str("62")
        elif vol == "12 tbsp" or vol == "3/4 cup":
            return str("68")
        elif vol == "13 tbsp":
            return str("73")
        elif vol == "14 tbsp":
            return str("79")
        elif vol == "15 tbsp":
            return str("84")
        elif vol == "16 tbsp" or vol == "1 cup":
            return str("90")
        elif vol == "17 tbsp" or vol == "1cup + 1tbsp" or vol == "1 cup + 1 tbsp" or vol == "Heaping cup":
            return str("96")
        elif vol == "18 tbsp" or vol == "1cup + 2tbsp" or vol == "1 cup + 2 tbsp":
            return str("101")
        elif vol == "1.25 cup":
            return str("113")
        elif vol == "1.33 cup":
            return str("120")
        elif vol == "1.5 cup":
            return str("135")
        elif vol == "1.67 cup" or vol == "1.66 cup":
            return str("150")
        elif vol == "1.75 cup":
            return str("158")
        elif vol == "2 cup":
            return str("180")
        elif vol == "2.5 cup":
            return str("225")
        elif vol == "3 cup":
            return str("270")
        else:
            return str(mass)
        
    # Almond flour
    if food == "Almond flour" or food == "Almond flour, or oat flour" or food == "Almond flour, or oat" or food == "Almond flour (or whole nuts)":
        if vol == "1/2 tbsp" or vol == "1.5 tsp":
            return str("3.5")
        elif vol == "1 tbsp":
            return str("7")
        elif vol == "1.5 tbsp":
            return str("10.5")
        elif vol == "2 tbsp":
            return str("14")
        elif vol == "3 tbsp":
            return str("21")
        elif vol == "4 tbsp" or vol == "1/4 cup":
            return str("28")
        elif vol == "5 tbsp":
            return str("35")
        elif vol == "1/3 cup":
            return str("37")
        elif vol == "6 tbsp":
            return str("42")
        elif vol == "7 tbsp":
            return str("49")
        elif vol == "8 tbsp" or vol == "1/2 cup":
            return str("56")
        elif vol == "9 tbsp":
            return str("63")
        elif vol == "10 tbsp":
            return str("70")
        elif vol == "2/3 cup":
            return str("75")
        elif vol == "11 tbsp":
            return str("77")
        elif vol == "12 tbsp" or vol == "3/4 cup":
            return str("84")
        elif vol == "13 tbsp":
            return str("91")
        elif vol == "14 tbsp":
            return str("98")
        elif vol == "15 tbsp":
            return str("105")
        elif vol == "16 tbsp" or vol == "1 cup":
            return str("112")
        elif vol == "17 tbsp" or vol == "1cup + 1tbsp" or vol == "1 cup + 1 tbsp" or vol == "Heaping cup":
            return str("119")
        elif vol == "18 tbsp" or vol == "1cup + 2tbsp" or vol == "1 cup + 2 tbsp":
            return str("126")
        elif vol == "1.25 cup":
            return str("140")
        elif vol == "1.33 cup":
            return str("149")
        elif vol == "1.5 cup":
            return str("168")
        elif vol == "1.67 cup" or vol == "1.66 cup":
            return str("187")
        elif vol == "1.75 cup":
            return str("196")
        elif vol == "2 cup":
            return str("224")
        elif vol == "2.5 cup":
            return str("280")
        elif vol == "3 cup":
            return str("336")
        else:
            return str(mass)
        
    # Oats
    if food == "Rolled oats" or food == "Quick oats" or food == "Rolled oats, or quick oats" or food == "Rolled oats, or quick" or food == "Quick oats, or rolled oats" or food == "Quick oats, or rolled" or food == "Quick oats, or oat flour" or food == "Rolled oats, or oat flour":
        if vol == "1/2 tbsp" or vol == "1.5 tsp":
            return str("2.5")
        elif vol == "1 tbsp":
            return str("5")
        elif vol == "1.5 tbsp":
            return str("7.5")
        elif vol == "2 tbsp":
            return str("10")
        elif vol == "3 tbsp":
            return str("15")
        elif vol == "4 tbsp" or vol == "1/4 cup":
            return str("20")
        elif vol == "5 tbsp":
            return str("25")
        elif vol == "1/3 cup":
            return str("27")
        elif vol == "6 tbsp":
            return str("30")
        elif vol == "7 tbsp":
            return str("35")
        elif vol == "8 tbsp" or vol == "1/2 cup":
            return str("40")
        elif vol == "9 tbsp":
            return str("45")
        elif vol == "10 tbsp":
            return str("50")
        elif vol == "2/3 cup":
            return str("53")
        elif vol == "11 tbsp":
            return str("55")
        elif vol == "12 tbsp" or vol == "3/4 cup":
            return str("60")
        elif vol == "13 tbsp":
            return str("65")
        elif vol == "14 tbsp":
            return str("70")
        elif vol == "15 tbsp":
            return str("75")
        elif vol == "16 tbsp" or vol == "1 cup":
            return str("80")
        elif vol == "17 tbsp" or vol == "1cup + 1tbsp" or vol == "1 cup + 1 tbsp" or vol == "Heaping cup":
            return str("85")
        elif vol == "18 tbsp" or vol == "1cup + 2tbsp" or vol == "1 cup + 2 tbsp":
            return str("90")
        elif vol == "1.25 cup":
            return str("100")
        elif vol == "1.33 cup":
            return str("107")
        elif vol == "1.5 cup":
            return str("120")
        elif vol == "1.67 cup" or vol == "1.66 cup":
            return str("133")
        elif vol == "1.75 cup":
            return str("140")
        elif vol == "2 cup":
            return str("160")
        elif vol == "2.5 cup":
            return str("200")
        elif vol == "3 cup":
            return str("240")
        else:
            return str(mass)
        
    # Ground Flaxseed
    if food == "Ground flaxseed":
        if vol == "1/2 tbsp" or vol == "1.5 tsp":
            return str("3.25")
        elif vol == "1 tbsp":
            return str("6.5")
        elif vol == "1.5 tbsp":
            return str("9.75")
        elif vol == "2 tbsp":
            return str("13")
        elif vol == "3 tbsp":
            return str("20")
        elif vol == "4 tbsp" or vol == "1/4 cup":
            return str("26")
        elif vol == "5 tbsp":
            return str("33")
        elif vol == "1/3 cup":
            return str("35")
        elif vol == "6 tbsp":
            return str("39")
        elif vol == "7 tbsp":
            return str("46")
        elif vol == "8 tbsp" or vol == "1/2 cup":
            return str("52")
        elif vol == "9 tbsp":
            return str("59")
        elif vol == "10 tbsp":
            return str("65")
        elif vol == "2/3 cup":
            return str("69")
        elif vol == "11 tbsp":
            return str("72")
        elif vol == "12 tbsp" or vol == "3/4 cup":
            return str("78")
        elif vol == "13 tbsp":
            return str("85")
        elif vol == "14 tbsp":
            return str("91")
        elif vol == "15 tbsp":
            return str("98")
        elif vol == "16 tbsp" or vol == "1 cup":
            return str("104")
        elif vol == "17 tbsp" or vol == "1cup + 1tbsp" or vol == "1 cup + 1 tbsp" or vol == "Heaping cup":
            return str("111")
        elif vol == "18 tbsp" or vol == "1cup + 2tbsp" or vol == "1 cup + 2 tbsp":
            return str("117")
        elif vol == "1.25 cup":
            return str("130")
        elif vol == "1.33 cup":
            return str("138")
        elif vol == "1.5 cup":
            return str("156")
        elif vol == "1.67 cup" or vol == "1.66 cup":
            return str("174")
        elif vol == "1.75 cup":
            return str("182")
        elif vol == "2 cup":
            return str("208")
        elif vol == "2.5 cup":
            return str("260")
        elif vol == "3 cup":
            return str("312")
        else:
            return str(mass)
        
    # Chocolate chips
    if food == "90% chocolate" or food == "85% chocolate" or food == "Sugar free chocolate chips" or food == "Chocolate chips" or food == "Semisweet chocolate chips" or food == "Semi-sweet chocolate chips" or food == "Semisweet chocolate chips (optional)" or food == "Dark chocolate chips" or food == "100% chocolate" or food == "70% chocolate" or food == "50% chocolate" or food == "Allulose chocolate bar":
        if vol == "1/2 tbsp":
            return str("7.5")
        elif vol == "1 tbsp":
            return str("15")
        elif vol == "2 tbsp":
            return str("30")
        elif vol == "4 tbsp" or vol == "1/4 cup":
            return str("45")
        elif vol == "1/3 cup":
            return str("60")
        elif vol == "1/2 cup":
            return str("90")
        elif vol == "3/4 cup":
            return str("135")
        elif vol == "1 cup":
            return str("180")
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