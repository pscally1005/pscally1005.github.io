# Download csv to /python/testing folder, and run script to swap amount and description columns

import pandas as pd
import os
import glob
import csv
import re

def vol_from_mass(food, mass, vol):
    v = vol

    # Sugar, etc.
    if food == "Granulated sugar" or food == "Brown sugar" or food == "Granular sweetener: sugar, erythritol, stevia, etc." or food == "Allulose" or food == "Granulated monk fruit" or food == "Granulated stevia" or food == "Inulin" or food == "Coconut sugar" or food == "Date sugar":
        if mass == "4":
            v = "1 tsp"
        elif mass == "6":
            v = "1/2 tbsp"
        elif mass == "8":
            v = "2 tsp"
        elif mass == "12" or mass == "12.5" or mass == "15":
            v = "1 tbsp"
        elif mass == "25" or mass == "24":
            v = "2 tbsp"
        elif mass == "37.5" or mass == "37" or mass == "38" or mass == "36":
            v = "3 tbsp"
        elif mass == "50" or mass == "48" or mass == "56":
            v = "1/4 cup"
        elif mass == "62.5" or mass == "62" or mass == "63" or mass == "60":
            v = "5 tbsp"
        elif mass == "67":
            v = "1/3 cup"
        elif mass == "75" or mass == "72":
            v = "6 tbsp"
        elif mass == "87.5" or mass == "87" or mass == "88" or mass == "84":
            v = "7 tbsp"
        elif mass == "100" or mass == "96":
            v = "1/2 cup"
        elif mass == "112.5" or mass == "112" or mass == "113" or mass == "108":
            v = "9 tbsp"
        elif mass == "125" or mass == "120":
            v = "10 tbsp"
        elif mass == "133":
            v = "2/3 cup"
        elif mass == "137.5" or mass == "137" or mass == "138" or mass == "132":
            v = "11 tbsp"
        elif mass == "150" or mass == "144":
            v = "3/4 cup"
        elif mass == "162.5" or mass == "162" or mass == "163" or mass == "156":
            v = "13 tbsp"
        elif mass == "175" or mass == "168":
            v = "14 tbsp"
        elif mass == "187.5" or mass == "187" or mass == "188" or mass == "180":
            v = "15 tbsp"
        elif mass == "200" or mass == "192":
            v = "1 cup"
        elif mass == "250":
            v = "1 1/4 cup"
        elif mass == "267":
            v = "1 1/3 cup"
        elif mass == "300":
            v = "1 1/2 cup"
        elif mass == "333":
            v = "1 2/3 cup"
        elif mass == "350":
            v = "1 3/4 cup"
        elif mass == "400":
            v = "2 cup"

    # Drained and rinsed beans
    if food == "Chickpeas, drained and rinsed" or food == "Black beans, drained and rinsed" or food == "Kidney beans, drained and rinsed" or food == "Pinto beans, drained and rinsed" or food == "Cannellini beans, drained and rinsed" or food == "Great northern beans, drained and rinsed" or food == "Navy beans, drained and rinsed" or food == "Beans, drained and rinsed" or food == "Cooked black beans" or food == "Cooked navy beans" or food == "Slow Cooker Dried Beans":
        if mass == "255":
            v = "15.5 oz can"
        elif mass == "128":
            v = "1/2 15.5 oz can"
        elif mass == "510":
            v = "2 x 15.5 oz can"
        elif mass == "765":
            v = "3 x 15.5 oz can"
        elif mass == "1020":
            v = "4 x 15.5 oz can"
        elif mass == "180":
            v = "1 cup"
        elif mass == "360":
            v = "2 cup"
        elif mass == "135":
            v = "3/4 cup"
        elif mass == "120":
            v = "2/3 cup"
        elif mass == "90":
            v = "1/2 cup"
        elif mass == "60":
            v = "1/3 cup"
        elif mass == "45":
            v = "1/4 cup"
        elif mass == "1260":
            # v = "7 cup"
            v = "1 batch"

    # NOT drained and rinsed beans
    elif food == "Chickpeas, NOT drained or rinsed" or food == "Black beans, NOT drained or rinsed" or food == "Kidney beans, NOT drained or rinsed" or food == "Pinto beans, NOT drained or rinsed" or food == "Cannellini beans, NOT drained or rinsed" or food == "Great northern beans, NOT drained or rinsed" or food == "Navy beans, NOT drained or rinsed" or food == "Beans, NOT drained or rinsed":
        if mass == "440":
          v = "15.5 oz can"
        elif mass == "220":
            v = "1/2 15.5 oz can"
        elif mass == "880":
            v = "2 x 15.5 oz can"
        elif mass == "1320":
            v = "3 x 15.5 oz can"
        elif mass == "1760":
            v = "4 x 15.5 oz can"

    # Quick nutella
    elif food == "Single Serving Quick Nutella":
        if mass == "54":
            v = "1 serving"
        elif mass == "108":
            v = "2 serving"
        elif mass == "162":
            v = "3 serving"
        elif mass == "216":
            v = "4 serving"
        elif mass == "270":
            v = "5 serving"
        elif mass == "324":
            v = "6 serving"


    # Cornstarch
    elif food == "Cornstarch":
        if mass == "4":
            v = "1/2 tbsp"
        elif mass == "8":
            v = "1 tbsp"
        elif mass == "16":
            v = "2 tbsp"
        elif mass == "20":
            v = "2.5 tbsp"
        elif mass == "24":
            v = "3 tbsp"
        elif mass == "32" or mass == "30":
            v = "1/4 cup"
        elif mass == "40":
            v = "5 tbsp"
        elif mass == "48":
            v = "6 tbsp"
        elif mass == "56":
            v = "7 tbsp"
        elif mass == "64":
            v = "1/2 cup"
        elif mass == "72":
            v = "9 tbsp"
        elif mass == "80":
            v = "10 tbsp"
        elif mass == "85":
            v = "2/3 cup"
        elif mass == "88":
            v = "11 tbsp"
        elif mass == "96":
            v = "3/4 cup"
        elif mass == "104":
            v = "13 tbsp"
        elif mass == "112":
            v = "14 tbsp"
        elif mass == "120":
            v = "15 tbsp"
        elif mass == "128":
            v = "1 cup"

    # Sourdough
    elif food == "Sourdough starter":
        if mass == "120":
            v = "1/2 cup"
        elif mass == "240":
            v = "1 cup"

    # Lactase
    elif food == "Lactase enzyme":
        if mass == "10":
            v = "2 scoops"
        elif mass == "60":
            v = "12 scoops"
        elif mass == "80":
            v == "16 scoops"

    # Labneh
    elif food == "Labneh cheese, skim":
        if mass == "15":
            v = "1 tbsp"
        elif mass == "30":
            v = "2 tbsp"
        elif mass == "45":
            v = "3 tbsp"
        elif mass == "60":
            v = "4 tbsp"

    # Sugar free syrup
    elif food == "Sugar free syrup" or food == "Sugar free syrup, or maple syrup or honey" or food == "Sugar free syrup, or honey or maple syrup" or food == "Sugar free syrup, or honey" or food == "Sugar free syrup, or maple syrup" or food == "Sugar free syrup, optional" or food == "Agave" or food == "Agave syrup" or food == "Date syrup":
        if mass == "6.5":
          v = "1 tsp"
        elif mass == "10":
          v = "1/2 tbsp"
        elif mass == "20":
            v = "1 tbsp"
        elif mass == "30":
            v = "1 1/2 tbsp"
        elif mass == "40":
            v = "2 tbsp"
        elif mass == "60":
            v = "3 tbsp"
        elif mass == "80":
            v = "1/4 cup"
        elif mass == "100":
            v = "5 tbsp"
        elif mass == "107":
            v = "1/3 cup"
        elif mass == "120":
            v = "6 tbsp"
        elif mass == "140":
            v = "7 tbsp"
        elif mass == "160":
            v = "1/2 cup"
        elif mass == "180":
            v = "9 tbsp"
        elif mass == "200":
            v = "10 tbsp"
        elif mass == "213":
            v = "2/3 cup"
        elif mass == "220":
            v = "11 tbsp"
        elif mass == "240":
            v = "3/4 cup"
        elif mass == "260":
            v = "13 tbsp"
        elif mass == "280":
            v = "14 tbsp"
        elif mass == "300":
            v = "15 tbsp"
        elif mass == "320":
            v = "1 cup"
        elif mass == "480":
            v = "1.5 cup"

    # Honey
    elif food == "Honey" or food == "Honey, or maple syrup" or food == "Molasses, or honey":
        if mass == "7":
            v = "1 tsp"
        elif mass == "10.5":
            v = "1/2 tbsp"
        elif mass == "21":
            v = "1 tbsp"
        elif mass == "31.5":
            v = "1.5 tbsp"
        elif mass == "42":
            v = "2 tbsp"
        elif mass == "63":
            v = "3 tbsp"
        elif mass == "84":
            v = "1/4 cup"
        elif mass == "105":
            v = "5 tbsp"
        elif mass == "112":
            v = "1/3 cup"
        elif mass == "126":
            v = "6 tbsp"
        elif mass == "147":
            v = "7 tbsp"
        elif mass == "168":
            v = "1/2 cup"
        elif mass == "189":
            v = "9 tbsp"
        elif mass == "210":
            v = "10 tbsp"
        elif mass == "224":
            v = "2/3 cup"
        elif mass == "231":
            v = "11 tbsp"
        elif mass == "252":
            v = "3/4 cup"
        elif mass == "273":
            v = "13 tbsp"
        elif mass == "294":
            v = "14 tbsp"
        elif mass == "315":
            v = "15 tbsp"
        elif mass == "336":
            v = "1 cup"
        elif mass == "504":
            v = "1.5 cup"

    # Capers
    elif food == "Capers":
        if mass == "15":
            v = "2 tbsp"

    # Diced green chiles
    elif food == "Diced green chiles":
        if mass == "113":
            v = "4 oz can"

    # Avocado
    elif food == "Avocado":
        if mass == "50":
            v = "1/2 medium"
        elif mass == "100":
            v = "1 medium"
        elif mass == "200":
            v = "2 medium"
        elif mass == "300":
            v = "3 medium"
        elif mass == "400":
            v = "4 medium"
        elif mass == "500":
            v = "5 medium"
        elif mass == "600":
            v = "6 medium"

    # Banana
    elif food == "Banana, overripe" or food == "Frozen banana" or food == "Banana, underripe" or food == "Frozen bananas, overripe" or food == "Frozen overripe bananas" or food == "Banana, overripe, or unsweetened applesauce":
        if mass == "55":
            v = "1/2 medium"
        elif mass == "90":
            v = "1 small"
        elif mass == "110":
            v = "1 medium"
        elif mass == "220":
            v = "2 medium"
        elif mass == "275":
            v = "2 large"
        elif mass == "330":
            v = "3 medium"
        elif mass == "440":
            v = "4 medium"
        elif mass == "550":
            v = "5 medium"
        elif mass == "660":
            v = "6 medium"

    # Empanadas / pierogi
    elif food == "Empanada/Pierogi dough":
        if mass == "333":
            v = "12 circles"

    # Cheese
    elif food == "Shredded mozzarella cheese, low moisture part skim" or food == "Cheddar cheese" or food == "Mozzarella cheese, fat free" or food == "Shredded cheddar cheese":
        if mass == "28":
            v = "1/4 cup"
        elif mass == "56":
            v = "1/2 cup"
        elif mass == "84" or mass == "85":
            v = "3/4 cup"
        elif mass == "112" or mass == "113":
            v = "1 cup"
        elif mass == "142":
            v = "1 1/4 cup"
        elif mass == "168":
            v = "1 1/2 cup"
        elif mass == "198":
            v = "1 3/4 cup"
        elif mass == "224" or mass == "226":
            v = "2 cup"

    # Coconut milk
    elif food == "Coconut milk, full fat" or food == "Coconut milk, lite":
        if mass == "405":
            v = "13.5 oz can"
        elif mass == "810":
            v = "2 x 13.5 oz can"

    # Frosting
    elif food == "Protein Frosting, Vanilla" or food == "Protein Frosting, Chocolate":
        if mass == "29":
            v = "2 tbsp"
        elif mass == "351" or mass == "371":
            v = "1 batch"

    # Shredded chicken
    elif food == "Simple Shredded Chicken":
        if mass == "28":
            v = "1 oz"
        elif mass == "56":
            v = "2 oz"
        elif mass == "85":
            v = "3 oz"
        elif mass == "113":
            v = "4 oz"
        elif mass == "142":
            v = "5 oz"
        elif mass == "170":
            v = "6 oz"
        elif mass == "198":
            v = "7 oz"
        elif mass == "226":
            v = "8 oz"
        elif mass == "255":
            v = "9 oz"
        elif mass == "283":
            v = "10 oz"
        elif mass == "311":
            v = "11 oz"
        elif mass == "340":
            v = "12 oz"
        elif mass == "368":
            v = "13 oz"
        elif mass == "396":
            v = "14 oz"
        elif mass == "425":
            v = "15 oz"
        elif mass == "454":
            v = "16 oz"

    # PB Dressing
    elif food == "Peanut Chili Salad Dressing":
        if mass == "87.5":
            v = "1 serving"
        elif vol == "175":
            v = "2 servings"

    # Spring rolls
    elif food == "Fresh Veggie Spring Roll":
        if mass == "86":
            v = "1 piece"
        elif mass == "1032":
            v = "12 pieces"

    # Liquids
    elif food == "Water" or food == "Unsweetened original almond milk" or food == "Unsweetened almond milk" or food == "Unsweetened vanilla almond milk" or food == "Skim milk" or food == "Fairlife skim milk" or food == "Extra virgin olive oil" or food == "Soy sauce, low sodium, gluten free" or food == "Balsamic vinegar" or food == "White vinegar" or food == "Apple cider vinegar" or food == "Unsweetened applesauce" or food == "White vinegar, or apple cider vinegar" or food == "Unsweetened almond milk, or water" or food == "Unsweetened vanilla almond milk, or water" or food == "Pumpkin puree" or food == "Pumpkin Puree" or food == "Pumpkin puree, or sweet potato" or food == "Pumpkin puree, or sweet potato puree" or food == "Sweet potato puree" or food == "Sweet Potato puree, Pumpkin puree, or Butternut Squash puree" or food == "Butternut squash puree" or food == "Sweet potato Puree, or Pumpkin puree" or food == "Low sodium soy sauce" or food == "Fat free Italian dressing" or food == "Italian dressing" or food == "Lime juice" or food == "Lemon juice" or food == "Sesame oil" or food == "Egg whites" or food == "Liquid egg whites" or food == "Evaporated milk" or food == "Fat free evaporated milk" or food == "Chicken bone broth" or food == "Chicken broth" or food == "Vegetable broth" or food == "Low sodium chicken broth" or food == "Low sodium vegetable broth" or food == "Liquid egg whites" or food == "Dijon mustard" or food == "Minced garlic" or food == "Simple pasta sauce" or food == "Sour cream" or food == "Vanilla extract" or food == "Almond extract" or food == "Mint extract" or food == "Maple extract" or food == "Coconut extract" or food == "Salsa" or food == "Sauerkraut" or food == "Pickled beet juice" or food == "Buttermilk" or food == "No sugar added apple spread" or food == "Vodka":
        if mass == "0.625":
            v = "1/8 tsp"
        elif mass == "1.25":
            v = "1/4 tsp"
        elif mass == "2.5":
            v = "1/2 tsp"
        elif mass == "5":
            v = "1 tsp"
        elif mass == "7.5":
            v = "1/2 tbsp"
        elif mass == "10":
            v = "2 tsp"
        elif mass == "15":
            v = "1 tbsp"
        elif mass == "30":
            v = "2 tbsp"
        elif mass == "45":
            v = "3 tbsp"
        elif mass == "60":
            v = "1/4 cup"
        elif mass == "75":
            v = "5 tbsp"
        elif mass == "80":
            v = "1/3 cup"
        elif mass == "90":
            v = "6 tbsp"
        elif mass == "105":
            v = "7 tbsp"
        elif mass == "120" or mass == "112":
            v = "1/2 cup"
        elif mass == "160":
            v = "2/3 cup"
        elif mass == "180":
            v = "3/4 cup"
        elif mass == "240":
            v = "1 cup"
        elif mass == "300":
            v = "1 1/4 cup"
        elif mass == "320":
            v = "1 1/3cup"
        elif mass == "360":
            v = "1 1/2 cup"
        elif mass == "400":
            v = "1 2/3 cup"
        elif mass == "420":
            v = "1 3/4 cup"
        elif mass == "480":
            v = "2 cup"
        elif mass == "720":
            v = "3 cup"
        elif mass == "960":
            v = "4 cup"
        elif mass == "1200":
            v = "5 cup"
        elif mass == "800" and food == "Simple pasta sauce":
            v = "1 batch, 3 cup"

    # Cottage cheese flatbread
    elif food == "Cottage cheese flatbread":
        if mass == "45":
            v = "1 medium"
        elif mass == "90":
            v = "2 medium"
        elif mass == "135":
            v = "3 medium"
        elif mass == "180":
            v = "4 medium"

    # Buttermilk powder
    elif food == "Buttermilk powder":
        if mass == "5.75":
              v = "1 tbsp"
        elif mass == "11.5":
            v = "2 tbsp"
        elif mass == "17.25":
            v = "3 tbsp"
        elif mass == "23":
            v = "1/4 cup"
        elif mass == "28.75":
            v = "5 tbsp"
        elif mass == "34.5":
            v = "6 tbsp"
        elif mass == "40.25":
            v = "7 tbsp"
        elif mass == "46":
            v = "1/2 cup"
        elif mass == "51.75":
            v = "9 tbsp"
        elif mass == "57.5" or mass == "56":
            v = "10 tbsp"
        elif mass == "63.25":
            v = "11 tbsp"
        elif mass == "69":
            v = "3/4 cup"
        elif mass == "74.75":
            v = "13 tbsp"
        elif mass == "80.5":
            v = "14 tbsp"
        elif mass == "86.25":
            v = "15 tbsp"
        elif mass == "92":
            v = "1 cup"

    # Nutritional yeast, cocoa, psyllium
    elif food == "Nutritional yeast" or food == "Cocoa powder" or food == "Carob powder" or food == "Cacao powder" or food == "Psyllium husks, whole":
        if mass == "2.5":
            v = "1/2 tbsp"
        elif mass == "5":
            v = "1 tbsp"
        elif mass == "10":
            v = "2 tbsp"
        elif mass == "15":
            v = "3 tbsp"
        elif mass == "20":
            v = "1/4 cup"
        elif mass == "25":
            v = "5 tbsp"
        elif mass == "27":
            v = "1/3 cup"
        elif mass == "30":
            v = "6 tbsp"
        elif mass == "35":
            v = "7 tbsp"
        elif mass == "40":
            v = "1/2 cup"
        elif mass == "45":
            v = "9 tbsp"
        elif mass == "50":
            v = "1/2 cup + 2 tbsp"
        elif mass == "53":
            v = "2/3 cup"
        elif mass == "55":
            v = "11 tbsp"
        elif mass == "60":
            v = "3/4 cup"
        elif mass == "65":
            v = "13 tbsp"
        elif mass == "70":
            v = "14 tbsp"
        elif mass == "75":
            v = "15 tbsp"
        elif mass == "80":
            v = "1 cup"
        elif mass == "120":
            v = "1.5 cup"
        elif mass == "160":
            v = "2 cup"

    # Oils
    elif food == "Extra virgin coconut oil" or food == "Extra virgin coconut oil, or extra virgin olive oil" or food == "Canola oil" or food == "Vegetable oil" or food == "Unsalted butter" or food == "Salted butter":
        if mass == "2.5":
            v = "1/2 tsp"
        elif mass == "5":
            v = "1 tsp"
        elif mass == "7":
            v = "1/2 tbsp"
        elif mass == "14":
            v = "1 tbsp"
        elif mass == "28":
            v = "2 tbsp"
        elif mass == "42":
            v = "3 tbsp"
        elif mass == "56":
            v = "1/4 cup"
        elif mass == "70":
            v = "5 tbsp"
        elif mass == "84":
            v = "6 tbsp"
        elif mass == "98":
            v = "7 tbsp"
        elif mass == "112":
            v = "1/2 cup"
        elif mass == "126":
            v = "9 tbsp"
        elif mass == "140":
            v = "10 tbsp"

    # Lentils
    elif food == "Red lentils" or food == "Red split lentils" or food == "Green lentils" or food == "Brown lentils" or food == "Lentils":
        if mass == "48":
            v = "1/4 cup"
        elif mass == "64":
            v = "1/3 cup"
        elif mass == "96":
            v = "1/2 cup"
        elif mass == "128":
            v = "2/3 cup"
        elif mass == "144":
            v = "3/4 cup"
        elif mass == "192":
            v = "1 cup"
        elif mass == "240":
            v = "1 1/4 cup"
        elif mass == "256":
            v = "1 1/3 cup"
        elif mass == "288":
            v = "1 1/2 cup"
        elif mass == "320":
            v = "1 2/3 cup"
        elif mass == "336":
            v = "1 3/4 cup"
        elif mass == "384":
            v = "2 cup"

    # Frozen corn
    elif food == "Frozen corn":
        if mass == "34":
            v = "1/4 cup"
        elif mass == "45":
            v = "1/3 cup"
        elif mass == "68":
            v = "1/2 cup"
        elif mass == "91":
            v = "2/3 cup"
        elif mass == "102":
            v = "3/4 cup"
        elif mass == "136":
            v = "1 cup"
        elif mass == "170":
            v = "1 1/4 cup"
        elif mass == "181":
            v = "1 1/3 cup"
        elif mass == "204":
            v = "1 1/2 cup"
        elif mass == "227":
            v = "1 2/3 cup"
        elif mass == "238":
            v = "1 3/4 cup"
        elif mass == "272":
            v = "2 cup"

    # Rice paper
    elif food == "Rice paper":
        if mass == "15":
            v = "1 medium"
        elif mass == "180":
            v = "12 medium"

    # Rice
    elif food == "Brown rice" or food == "Wild rice":
        if mass == "45":
            v = "1/4 cup"
        elif mass == "60":
            v = "1/3 cup"
        elif mass == "90":
            v = "1/2 cup"
        elif mass == "120":
            v = "2/3 cup"
        elif mass == "135":
            v = "3/4 cup"
        elif mass == "180":
            v = "1 cup"
        elif mass == "225":
            v = "1 1/4 cup"
        elif mass == "270":
            v = "1 1/2 cup"
        elif mass == "315":
            v = "1 3/4 cup"
        elif mass == "360":
            v = "2 cup"
        elif mass == "540":
            v = "3 cup"
        elif mass == "720":
            v = "4 cup"

    # Cashew ricotta
    elif food == "Dairy Free Cashew Ricotta Cheese":
        if mass == "56":
            v = "1/2 cup"
        elif mass == "112":
            v = "1 cup"
        elif mass == "168":
            v = "1 1/2 cup"
        elif mass == "224":
            v = "2 cup"
        elif mass == "280":
            v = "2 1/2 cup"
        elif mass == "336":
            v = "3 cup"

    # Ice cream
    elif food == "Vanilla ice cream":
        if mass == "135":
            v = "1 cup"

    # Yogurt & cottage cheese
    elif food == "Nonfat cottage cheese" or food == "Plain nonfat greek yogurt" or food == "Plain whole milk greek yogurt" or food == "Vanilla Nonfat Greek Yogurt, Sugar Free" or food == "Ricotta cheese" or food == "Vanilla Protein Greek Yogurt":
        if mass == "14":
            v = "1 tbsp"
        elif mass == "28":
            v = "2 tbsp"
        elif mass == "56":
            v = "1/4 cup"
        elif mass == "113":
            v = "1/2 cup"
        elif mass == "170":
            v = "3/4 cup"
        elif mass == "226":
            v = "1 cup"
        elif mass == "283":
            v = "1 1/4 cup"
        elif mass == "340":
            v = "1 1/2 cup"
        elif mass == "396":
            v = "1 3/4 cup"
        elif mass == "454":
            v = "2 cup"
        elif mass == "680":
            v = "3 cup"
        elif mass == "908" or mass == "907" or mass == "906" or mass == "905":
            v = "4 cup"
        elif food == "Vanilla Protein Greek Yogurt" and mass == "950":
            v = "4 cup, 32 oz"

    # Pie crust
    elif food == "Healthier Graham Cracker Pie Crust" or food == "Healthier Graham Cracker Pie Crust, chocolate":
        if mass == "255":
            v = "1 batch, 9 oz"

    # Marzipan
    elif food == "Marzipan, homemade, with sugar" or food == "Marzipan, homemade, sugar free":
        if mass == "377":
            v = "1 batch"

    # Flours
    elif food == "Vital wheat gluten" or food == "Flour" or food == "All purpose flour" or food == "White flour" or food == "Whole wheat flour" or food == "Cornmeal" or food == "Panko breadcrumbs" or food == "Whole wheat breadcrumbs" or food == "Breadcrumbs" or food == "Millet flour" or food == "Chickpea flour" or food == "Coconut flour" or food == "Grated parmesan cheese" or food == "Cornstarch" or food == "Unsweetened coconut flakes":
        if mass == "15":
            v = "2 tbsp"
        elif mass == "22.5":
            v = "3 tbsp"
        elif mass == "30":
            v = "1/4 cup"
        elif mass == "45":
            v = "6 tbsp"
        elif mass == "60":
            v = "1/2 cup"
        elif mass == "90":
            v = "3/4 cup"
        elif mass == "120":
            v = "1 cup"
        elif mass == "135":
            v = "18 tbsp"
        elif mass == "150":
            v = "1 1/4 cup"
        elif mass == "180":
            v = "1 1/2 cup"
        elif mass == "210":
            v = "1 3/4 cup"
        elif mass == "240":
            v = "2 cup"

    # Protein powder
    elif food == "Whey protein powder, unflavored" or food == "Whey protein powder, chocolate" or food == "Whey protein powder, vanilla" or food == "Nutricost Whey Unflavored Protein Powder" or food == "Casein protein powder, unflavored" or food == "Casein protein powder, chocolate" or food == "Casein protein powder, vanilla" or food == "Nutricost Casein Unflavored Protein Powder":
        if mass == "10":
            v = "1/3 scoop"
        elif mass == "15":
            v = "1/2 scoop"
        elif mass == "20":
            v = "2/3 scoop"
        elif mass == "30":
            v = "1 scoop"
        elif mass == "40":
            v = "1 1/3 scoop"
        elif mass == "45":
            v = "1 1/2 scoop"
        elif mass == "60":
            v = "2 scoop"
        elif mass == "75":
            v = "2 1/2 scoop"
        elif mass == "90":
            v = "3 scoop"
        elif mass == "120":
            v = "4 scoop"

    # Nuts
    elif food == "Almonds" or food == "Walnuts" or food == "Cashews" or food == "Pistachios" or food == "Pecans" or food == "Macadamia nuts" or food == "Hazelnuts" or food == "Brazil nuts" or food == "Mixed nuts" or food == "Mixed nuts, unsalted" or food == "Peanuts" or food == "Pine nuts":
        if mass == "5":
            v = "1 tsp, chopped"
        elif mass == "15":
            v = "2 tbsp"
        elif mass == "30":
            v = "1/4 cup"
        elif mass == "60" or mass == "64":
            v = "1/2 cup"
        elif mass == "90":
            v = "3/4 cup"
        elif mass == "120" or mass == "128":
            v = "1 cup"
        elif mass == "180" or mass == "196":
            v = "1 1/2 cup"
        elif mass == "240" or mass == "256" or mass == "250":
            v = "2 cup"

    # Jelly
    elif food == "Low sugar berry jam" or food == "Strawberry chia jam":
        if mass == "19":
            v = "1 tbsp"
        elif mass == "38":
            v = "2 tbsp"
        elif mass == "57":
            v = "3 tbsp"
        elif mass == "76":
            v = "1/4 cup"
        elif mass == "95":
            v = "5 tbsp"
        elif mass == "114":
            v = "6 tbsp"
        elif mass == "133":
            v = "7 tbsp"
        elif mass == "152":
            v = "1/2 cup"
        elif mass == "171":
            v = "9 tbsp"
        elif mass == "190":
            v = "10 tbsp"
        elif mass == "209":
            v = "11 tbsp"
        elif mass == "228":
            v = "3/4 cup"
        elif mass == "247":
            v = "13 tbsp"
        elif mass == "266":
            v = "14 tbsp"
        elif mass == "285":
            v = "15 tbsp"
        elif mass == "304":
            v = "1 cup"

    # Nut butters
    elif food == "Almond butter" or food == "Peanut butter" or food == "Natural peanut butter" or food == "Natural peanut butter, or tahini" or food == "Walnut butter" or food == "Cashew butter" or food == "Sunflower seed butter" or food == "Sunflower butter" or food == "Pistachio butter" or food == "Pumpkin seed butter" or food == "Tahini, or any other nut/seed butter" or food == "Tahini":
        if mass == "5" or mass == "6":
            v = "1 tsp"
        elif mass == "8":
            v = "1/2 tbsp"
        elif mass == "16":
            v = "1 tbsp"
        elif mass == "24":
            v = "1 1/2 tbsp"
        elif mass == "32":
            v = "2 tbsp"
        elif mass == "40":
            v = "2 1/2 tbsp"
        elif mass == "48":
            v = "3 tbsp"
        elif mass == "64":
            v = "1/4 cup"
        elif mass == "80":
            v = "5 tbsp"
        elif mass == "96":
            v = "6 tbsp"
        elif mass == "128":
            v = "1/2 cup"
        elif mass == "196":
            v = "3/4 cup"
        elif mass == "256":
            v = "1 cup"

    # Miso
    elif food == "Miso" or food == "Miso paste":
        if mass == "8.5":
            v = "1/2 tbsp"
        elif mass == "17":
            v = "1 tbsp"
        elif mass == "25.5":
            v = "1 1/2 tbsp"
        elif mass == "34":
            v = "2 tbsp"
        elif mass == "51":
            v = "3 tbsp"
        elif mass == "68":
            v = "1/4 cup"
        elif mass == "85":
            v = "5 tbsp"
        elif mass == "102":
            v = "6 tbsp"
        elif mass == "136":
            v = "1/2 cup"

    # Cucumber
    elif food == "Cucumber":
        if mass == "52":
            v = "1/2 cup"
        elif mass == "104":
            v = "1 cup"
        elif mass == "208":
            v = "208"
        elif mass == "150":
            v = "1/2 large"

    # Sweet potatoes
    elif food == "Sweet potato":
        if mass == "125":
            v = "1 small"
        elif mass == "250":
            v = "2 small"
        elif mass == "375":
            v = "3 small"
        elif mass == "500":
            v = "4 small"
        elif mass == "625":
            v = "5 small"
        elif mass == "750":
            v = "6 small"
        elif mass == "170":
            v = "1 medium"
        elif mass == "340":
            v = "2 medium"
        elif mass == "510":
            v = "3 medium"
        elif mass == "680":
            v = "4 medium"
        elif mass == "850":
            v = "5 medium"
        elif mass == "1020":
            v = "6 medium"

    # Pumpkin
    elif food == "Pumpkin" or food == "Pumpkin, raw" or food == "Sugar pumpkin":
        if mass == "764":
            v = "1 small"

    # Radishes
    elif food == "Radish":
        if mass == "200":
            v = "1 bunch"

    # Cabbage
    elif food == "Red cabbage" or food == "Green cabbage" or food == "Cabbage":
        if mass == "210":
            v = "1/4 head"

    # Onions
    elif food == "Onion":
        if mass == "55":
            v = "1/2 medium"
        elif mass == "110":
            v = "1 medium"
        elif mass == "150":
            v = "1 large"
        elif mass == "220":
            v = "2 medium"
        elif mass == "300":
            v = "2 large"
        elif mass == "330":
            v = "3 medium"
        elif mass == "440" or mass == "500":
            v = "4 medium"
        elif mass == "450":
            v = "3 large"
        elif mass == "550":
            v = "5 medium"

    # Zucchini
    elif food == "Zucchini" or food == "Yellow squash":
        if mass == "60":
            v = "1/2 medium"
        elif mass == "125":
            v = "1 medium"
        elif mass == "250":
            v = "2 medium"
        elif mass == "375":
            v = "3 medium"
        elif mass == "500":
            v = "4 medium"
        elif mass == "625":
            v = "5 medium"

    # Carrots
    elif food == "Carrots":
        if mass == "100":
            v = "1 medium"
        elif mass == "200":
            v = "2 medium"
        elif mass == "300":
            v = "3 medium"
        elif mass == "400":
            v = "4 medium"
        elif mass == "500":
            v = "5 medium"
        elif mass == "72":
            v = "1 large"

    # Peppers
    elif food == "Bell pepper":
        if mass == "60":
            v = "1/2 medium"
        elif mass == "120":
            v = "1 medium"
        elif mass == "150":
            v = "1 large"
        elif mass == "240":
            v = "2 medium"
        elif mass == "300":
            v = "2 large"
        elif mass == "360":
            v = "3 medium"
        elif mass == "450":
            v = "3 medium"
        elif mass == "480" or mass == "500":
            v = "4 medium"
        elif mass == "600":
            v = "5 medium"

    # Tomatoes
    elif food == "Tomato":
        if mass == "50":
            v = "1/2 medium"
        elif mass == "100":
            v = "1 medium"
        elif mass == "200":
            v = "2 medium"
        elif mass == "300":
            v = "3 medium"
        elif mass == "400":
            v = "4 medium"
        elif mass == "500":
            v = "5 medium"

    # Lettuce
    elif food == "Lettuce" or food == "Romaine lettuce":
        if mass == "113":
            v = "1/2 head"
        elif mass == "226":
            v = "1 head"
        elif mass == "454":
            v = "2 heads"
        elif mass == "360":
            v = "3 medium"
        elif mass == "480":
            v = "4 medium"
        elif mass == "600":
            v = "5 medium"
        elif mass == "72":
            v = "12 leaves"

    # Powdered PB
    elif food == "Powdered peanut butter":
        if mass == "3":
            v = "1/2 tbsp"
        elif mass == "6":
            v = "1 tbsp"
        elif mass == "9":
            v = "1 1/2 tbsp"
        elif mass == "12":
            v = "2 tbsp"
        elif mass == "18":
            v = "3 tbsp"
        elif mass == "24":
            v = "1/4 cup"
        elif mass == "30":
            v = "5 tbsp"
        elif mass == "32":
            v = "1/3 cup"
        elif mass == "36":
            v = "6 tbsp"
        elif mass == "42":
            v = "7 tbsp"
        elif mass == "48":
            v = "1/2 cup"
        elif mass == "54":
            v = "9 tbsp"
        elif mass == "60":
            v = "10 tbsp"
        elif mass == "64":
            v = "2/3 cup"
        elif mass == "66":
            v = "11 tbsp"
        elif mass == "72":
            v = "3/4 cup"
        elif mass == "78":
            v = "13 tbsp"
        elif mass == "84":
            v = "14 tbsp"
        elif mass == "90":
            v = "15 tbsp"
        elif mass == "96":
            v = "1 cup"

    # Chia seeds
    elif food == "Chia seeds":
        if mass == "6":
            v = "1/2 tbspp"
        elif mass == "12":
            v = "1 tbsp"
        elif mass == "18":
            v = "1 1/2 tbsp"
        elif mass == "24":
            v = "2 tbsp"
        elif mass == "36":
            v = "3 tbsp"
        elif mass == "48":
            v = "1/4 cup"
        elif mass == "60":
            v = "5 tbsp"
        elif mass == "64":
            v = "1/3 cup"
        elif mass == "72":
            v = "6 tbsp"
        elif mass == "84":
            v = "7 tbsp"
        elif mass == "96":
            v = "1/2 cup"
        elif mass == "108":
            v = "9 tbsp"
        elif mass == "120":
            v = "10 tbsp"
        elif mass == "128":
            v = "2/3 cup"
        elif mass == "132":
            v = "11 tbsp"
        elif mass == "144":
            v = "3/4 cup"
        elif mass == "156":
            v = "13 tbsp"
        elif mass == "168":
            v = "14 tbsp"
        elif mass == "180":
            v = "15 tbsp"
        elif mass == "192":
            v = "1 cup"

    # Oat flour
    elif food == "Oat flour" or food == "Oat flour, or almond flour" or food == "Oat flour, or almond":
        if mass == "3":
            v = "1/2 tbsp"
        elif mass == "6":
            v = "1 tbsp"
        elif mass == "9":
            v = "1 1/2 tbsp"
        elif mass == "11":
            v = "2 tbsp"
        elif mass == "17":
            v = "3 tbsp"
        elif mass == "23":
            v = "1/4 cup"
        elif mass == "28":
            v = "5 tbsp"
        elif mass == "30":
            v = "1/3 cup"
        elif mass == "34":
            v = "6 tbsp"
        elif mass == "39":
            v = "7 tbsp"
        elif mass == "45":
            v = "1/2 cup"
        elif mass == "51":
            v = "1/2 cup + 1 tbsp"
        elif mass == "56":
            v = "10 tbsp"
        elif mass == "60":
            v = "2/3 cup"
        elif mass == "62":
            v = "11 tbsp"
        elif mass == "68":
            v = "3/4 cup"
        elif mass == "73":
            v = "13 tbsp"
        elif mass == "79":
            v = "14 tbsp"
        elif mass == "84":
            v = "15 tbsp"
        elif mass == "90":
            v = "1 cup"
        elif mass == "96":
            v = "1 cup + 1 tbsp"
        elif mass == "101":
            v = "1 cup + 2 tbsp"
        elif mass == "113":
            v = "1 1/4 cup"
        elif mass == "120":
            v = "1 1/3 cup"
        elif mass == "135":
            v = "1 1/2 cup"
        elif mass == "150":
            v = "1 2/3 cup"
        elif mass == "158":
            v = "1 3/4 cup"
        elif mass == "180":
            v = "2 cup"
        elif mass == "225":
            v = "2 1/2 cup"
        elif mass == "270":
            v = "3 cup"

    # Almond flour
    elif food == "Almond flour" or food == "Almond flour, or oat flour" or food == "Almond flour, or oat" or food == "Almond flour (or whole nuts)":
        if mass == "3.5":
            v = "1/2 tbsp"
        elif mass == "7":
            v = "1 tbsp"
        elif mass == "10.5":
            v = "1 1/2 tbsp"
        elif mass == "14":
            v = "2 tbsp"
        elif mass == "21":
            v = "3 tbsp"
        elif mass == "28":
            v = "1/4 cup"
        elif mass == "35":
            v = "5 tbsp"
        elif mass == "37":
            v = "1/3 cup"
        elif mass == "42":
            v = "6 tbsp"
        elif mass == "49":
            v = "7 tbsp"
        elif mass == "56":
            v = "1/2 cup"
        elif mass == "63":
            v = "9 tbsp"
        elif mass == "70":
            v = "10 tbsp"
        elif mass == "75":
            v = "2/3 cup"
        elif mass == "77":
            v = "11 tbsp"
        elif mass == "84":
            v = "3/4 cup"
        elif mass == "91":
            v = "13 tbsp"
        elif mass == "98":
            v = "14 tbsp"
        elif mass == "105":
            v = "15 tbsp"
        elif mass == "112":
            v = "1 cup"
        elif mass == "119":
            v = "1 cup + 1 tbsp"
        elif mass == "126":
            v = "1 cup + 2 tbsp"
        elif mass == "140":
            v = "1 1/4 cup"
        elif mass == "149":
            v = "1 1/3 cup"
        elif mass == "168":
            v = "1 1/2 cup"
        elif mass == "182":
            v = "1 1/2 cup + 2 tbsp"
        elif mass == "187":
            v = "1 2/3 cup"
        elif mass == "196":
            v = "1 3/4 cup"
        elif mass == "224":
            v = "2 cup"
        elif mass == "280":
            v = "2 1/2 cup"
        elif mass == "336":
            v = "3 cup"

    # Oats
    elif food == "Rolled oats" or food == "Quick oats" or food == "Rolled oats, or quick oats" or food == "Rolled oats, or quick" or food == "Quick oats, or rolled oats" or food == "Quick oats, or rolled" or food == "Quick oats, or oat flour" or food == "Rolled oats, or oat flour":
        if mass == "2.5":
            v = "1/2 tbsp"
        elif mass == "5":
            v = "1 tbsp"
        elif mass == "7.5":
            v = "1 1/2 tbsp"
        elif mass == "10":
            v = "2 tbsp"
        elif mass == "15":
            v = "3 tbsp"
        elif mass == "20":
            v = "1/4 cup"
        elif mass == "25":
            v = "5 tbsp"
        elif mass == "27":
            v = "1/3 cup"
        elif mass == "30":
            v = "6 tbsp"
        elif mass == "35":
            v = "7 tbsp"
        elif mass == "40":
            v = "1/2 cup"
        elif mass == "45":
            v = "9 tbsp"
        elif mass == "50":
            v = "10 tbsp"
        elif mass == "53":
            v = "2/3 cup"
        elif mass == "55":
            v = "11 tbsp"
        elif mass == "60":
            v = "3/4 cup"
        elif mass == "65":
            v = "13 tbsp"
        elif mass == "70":
            v = "14 tbsp"
        elif mass == "75":
            v = "15 tbsp"
        elif mass == "80":
            v = "1 cup"
        elif mass == "85":
            v = "1 cup + 1 tbsp"
        elif mass == "90":
            v = "1 cup + 2 tbsp"
        elif mass == "100":
            v = "1 1/4 cup"
        elif mass == "107":
            v = "1 1/3 cup"
        elif mass == "120":
            v = "1 1/2 cup"
        elif mass == "133":
            v = "1 2/3 cup"
        elif mass == "140":
            v = "1 3/4 cup"
        elif mass == "160":
            v = "2 cup"
        elif mass == "200":
            v = "2 1/2 cup"
        elif mass == "240":
            v = "3 cup"

    # Ground flaxseed
    elif food == "Ground flaxseed":
        if mass == "3.25":
            v = "1/2 tbsp"
        elif mass == "6.5":
            v = "1 tbsp"
        elif mass == "9.75":
            v = "1 1/2 tbsp"
        elif mass == "13":
            v = "2 tbsp"
        elif mass == "20":
            v = "3 tbsp"
        elif mass == "26":
            v = "1/4 cup"
        elif mass == "33":
            v = "5 tbsp"
        elif mass == "35":
            v = "1/3 cup"
        elif mass == "39":
            v = "6 tbsp"
        elif mass == "46":
            v = "7 tbsp"
        elif mass == "52":
            v = "1/2 cup"
        elif mass == "59":
            v = "9 tbsp"
        elif mass == "65":
            v = "10 tbsp"
        elif mass == "69":
            v = "2/3 cup"
        elif mass == "72":
            v = "11 tbsp"
        elif mass == "78":
            v = "3/4 cup"
        elif mass == "85":
            v = "13 tbsp"
        elif mass == "91":
            v = "14 tbsp"
        elif mass == "98":
            v = "15 tbsp"
        elif mass == "104":
            v = "1 cup"
        elif mass == "111":
            v = "1 cup + 1 tbsp"
        elif mass == "117":
            v = "1 cup + 2 tbsp"
        elif mass == "130":
            v = "1 1/4 cup"
        elif mass == "138":
            v = "1 1/3 cup"
        elif mass == "156":
            v = "1 1/2 cup"
        elif mass == "174":
            v = "1 2/3 cup"
        elif mass == "182":
            v = "1 3/4 cup"
        elif mass == "208":
            v = "2 cup"
        elif mass == "260":
            v = "2 1/2 cup"
        elif mass == "312":
            v = "3 cup"

    # Chocolate chips
    elif food == "90% chocolate" or food == "85% chocolate" or food == "Sugar free chocolate chips" or food == "Chocolate chips" or food == "Semisweet chocolate chips" or food == "Semi-sweet chocolate chips" or food == "Semisweet chocolate chips (optional)" or food == "Dark chocolate chips" or food == "100% chocolate" or food == "70% chocolate" or food == "50% chocolate" or food == "Allulose chocolate bar" or food == "Chocolate chips" or food == "White chocolate chips" or food == "Tangy white chocolate" or food == "Sugar free chocolate bar" or food == "Chocolate free chocolate" or food == "Sugar free white chocolate" or food == "Monk fruit chocolate chunks":
        if mass == "5":
            v = "1 tsp"
        elif mass == "7.5":
            v = "1/2 tbsp"
        elif mass == "15":
            v = "1 tbsp"
        elif mass == "30":
            v = "2 tbsp"
        elif mass == "45":
            v = "1/4 cup"
        elif mass == "60":
            v = "1/3 cup"
        elif mass == "90" or mass == "85":
            v = "1/2 cup"
        elif mass == "135":
            v = "3/4 cup"
        elif mass == "180" or mass == "170":
            v = "1 cup"
        elif mass == "14":
            v = "1/2 oz"
        elif mass == "28":
            v = "1 oz"
        elif mass == "42":
            v = "1 1/2 oz"
        elif mass == "56":
            v = "2 oz"
        elif mass == "70":
            v = "2 1/2 oz"
        elif mass == "85":
            v = "3 oz"
        elif mass == "98":
            v = "3 1/2 oz"
        elif mass == "113":
            v = "4 oz"
        elif mass == "127":
            v = "4 1/2 oz"
        elif mass == "142":
            v = "5 oz"
        elif mass == "156":
            v = "5 1/2 oz"
        elif mass == "170":
            v = "6 oz"
        elif mass == "184":
            v = "6 1/2 oz"
        elif mass == "198":
            v = "7 oz"
        elif mass == "212":
            v = "7 1/2 oz"
        elif mass == "226":
            v = "8 oz"

    # Eggs
    elif food == "Egg":
        if mass == "50":
            v = "1 large"
        elif mass == "100":
            v = "2 large"
        elif mass == "150" or mass == "151":
            v = "3 large"
        elif mass == "200" or mass == "201":
            v = "4 large"
        elif mass == "250" or mass == "252":
            v = "5 large"
        elif mass == "300" or mass == "302":
            v = "6 large"
        elif mass == "350" or mass == "352":
            v = "7 large"
        elif mass == "400" or mass == "402":
            v = "8 large"

    # Yolks
    elif food == "Egg yolk":
        if mass == "17":
            v = "1 large"
        elif mass == "34":
            v = "2 large"
        elif mass == "51":
            v = "3 large"
        elif mass == "68":
            v = "4 large"
        elif mass == "85":
            v = "5 large"

    # Magnesium
    elif food == "Magnesium Glycinate":
        if mass == "1.8":
            v = "1 scoop"
        elif mass == "3.6":
            v = "2 scoop"
        elif mass == "5.4":
            v = "3 scoop"
        elif mass == "7.2":
            v = "4 scoop"
        elif mass == "9.0":
            v = "5 scoop"
        elif mass == "10.8":
            v = "6 scoop"


    # Creatine
    elif food == "Creatine Monohydrate":
        if mass == "5":
            v = "1 scoop"
        elif mass == "10":
            v = "2 scoop"
        elif mass == "15":
            v = "3 scoop"
        elif mass == "20":
            v = "4 scoop"
        elif mass == "25":
            v = "5 scoop"
        elif mass == "30":
            v = "6 scoop"

    # Dried fruit, olives
    elif food == "Dates" or food == "Pitted dates" or food == "Raisins" or food == "Dried figs" or food == "Olives":
        if mass == "40":
            v = "1/4 cup"
        elif mass == "80":
            v = "1/2 cup"
        elif mass == "120":
            v = "3/4 cup"
        elif mass == "160":
            v = "1 cup"
        elif mass == "200":
            v = "1 1/4 cup"
        elif mass == "240":
            v = "1 1/2 cup"
        elif mass == "320":
            v = "2 cup"

    # Popcorn
    elif food == "Popcorn kernels":
        if mass == "40":
            v = "3 tbsp"

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
                    row[3] = vol_from_mass(row[0], row[1], row[3])
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
