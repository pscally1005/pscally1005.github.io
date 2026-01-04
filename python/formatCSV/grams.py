# Download csv to /python/testing folder, and run script to fix grams in ingredients file

import pandas as pd
import os
import glob
import csv

def grams(food, mass, vol):
    m = mass

    # Oz to g
    if vol == "1 oz":
        m = "28"
    elif vol == "2 oz":
        m = "56"
    elif vol == "3 oz":
        m = "85"
    elif vol == "4 oz" or vol == "1/4 lb":
        m = "113"
    elif vol == "6 oz":
        m = "168"
    elif vol == "8 oz" or vol == "1/2 lb":
        m = "226"
    elif vol == "12 oz":
        m = "340"
    elif vol == "14 oz":
        m = "400"
    elif vol == "14.5 oz" or vol == "14.5oz can" or vol == "14.5 oz can":
        m = "410"
    elif vol == "15 oz":
        m = "425"
    elif vol == "15.5oz can" or vol == "15.5 oz" or vol == "15.5 oz can":
        m = "440"
    elif vol == "16 oz" or vol == "1 lb":
        m = "454"
    elif vol == "1.3 lb":
        m = "590"
    elif vol == "1.5 lb":
        m = "681"
    elif vol == "32 oz" or vol == "2 lb":
        m = "908"
    elif vol == "2.5 lb":
        m = "1135"
    elif vol == "3 lb":
        m = "1362"

    # Salt, baking powder, baking soda
    elif food == "Salt" or food == "Baking powder" or food == "Baking soda" or food == "Potassium Chloride" or food == "Flakey salt" or food == "Flaky salt":
        if vol == "Small pinch" or vol == "Tiny pinch":
            m = "0.15"
        if vol == "1/16 tsp" or vol == "Pinch":
            m = "0.38"
        elif vol == "1/8 tsp" or vol == "Large pinch" or vol == "Big pinch":
            m = "0.75"
        elif vol == "1/4 tsp":
            m = "1.5"
        elif vol == "1/2 tsp":
            m = "3"
        elif vol == "3/4 tsp":
            m = "4.5"
        elif vol == "1 tsp":
            m = "6"
        elif vol == "1.25 tsp" or vol == "1 1/4 tsp":
            m = "8"
        elif vol == "1/2 tbsp" or vol == "1.5 tsp" or vol == "1 1/2 tsp":
            m = "9"
        elif vol == "2 tsp":
            m = "12"
        elif vol == "1 tbsp" or vol == "3 tsp":
            m = "18"

    # Bananas
    elif food == "Banana, overripe" or food == "Banana, overripe" or food == "Frozen banana" or food == "Frozen bananas, overripe" or food == "Frozen Bananas, overripe" or food == "Frozen overripe banans" or food == "Banana, overripe, or unsweetened applesauce":
        if vol == "1/2 medium":
            m = "55"
        elif vol == "1 medium":
            m = "110"
        elif vol == "2 medium":
            m = "2200"
        elif vol == "3 medium":
            m = "330"
        elif vol == "4 medium":
            m = "440"
        elif vol == "5 medium":
            m = "550"
        elif vol == "6 medium":
            m = "660"

    # Mandarin orange
    elif food == "Mandarin orange":
        if vol == "1/2 medium":
            m = "44"
        elif vol == "1 medium":
            m = "88"
        elif vol == "2 medium":
            m = "176"
        elif vol == "3 medium":
            m = "264"
        elif vol == "4 medium":
            m = "352"
        elif vol == "5 medium":
            m = "440"
        elif vol == "6 medium":
            m = "528"

    # Hemp hearts
    elif food == "Hemp hearts" or food == "Hemp seeds":
        if vol == "1 tbsp":
            m = "10"
        elif vol == "2 tbsp":
            m = "20"
        elif vol == "3 tbsp":
            m = "30"
        elif vol == "1/4 cup":
            m = "40"

    # Yeast
    elif food == "Dry yeast":
        if vol == "1 tbsp":
            m = "12"

    # Salty spices
    elif food == "Chicken bouillon powder" or food == "Bouillon powder" or food == "Lemon pepper" or food == "Everything bagel seasoning":
        if vol == "1/2 tsp":
            m = "2"
        elif vol == "1 tsp":
            m = "4"
        elif vol == "1.5 tsp" or vol == "1/2 tbsp" or vol == "1 1/2 tsp":
            m = "6"
        elif vol == "2 tsp":
            m = "8"
        elif vol == "3 tsp" or vol == "1 tbsp":
            m = "12"

    # Extracts and sweeteners
    elif food == "Liquid monk fruit" or food == "Liquid stevia" or food == "Liquid stevia or monk fruit" or food == "Vanilla extract" or food == "Almond extract" or food == "Mint extract" or food == "Butter extract" or food == "Maple extract" or food == "Rum extract" or food == "Almond extract, or vanilla" or food == "Vanilla extract, or almond":
        if vol == "1/4 tsp":
            m = "1.25"
        elif vol == "1/2 tsp":
            m = "2.5"
        elif vol == "3/4 tsp":
            m = "3.75"
        elif vol == "1 tsp":
            m = "5"
        elif vol == "1/2 tbsp" or vol == "1.5 tsp" or vol == "1 1/2 tsp":
            m = "7.5"
        elif vol == "2 tsp":
            m = "10"
        elif vol == "3 tsp" or vol == "1 tbsp":
            m = "15"
        elif vol == "4.5 tsp" or vol == "1.5 tbsp" or vol == "1 1/2 tbsp":
            m = "22.5"


    # Denser spices
    elif food == "Nutmeg, ground" or food == "Garlic powder" or food == "Onion powder" or food == "Black pepper, ground" or food == "Paprika" or food == "Cumin, ground" or food == "Chili powder" or food == "Cayenne pepper" or food == "Old Bay" or food == "Turmeric, ground" or food == "Black pepper" or food == "Cinnamon, ground" or food == "Cinnamon":
        if vol == "1/8 tsp":
            m = "0.38"
        elif vol == "1/4 tsp":
            m = "0.75"
        elif vol == "1/2 tsp":
            m = "1.5"
        elif vol == "1 tsp":
            m = "3"
        elif vol == "1/2 tbsp" or vol == "1.5 tsp" or vol == "1 1/2 tsp":
            m = "4.5"
        elif vol == "2 tsp":
            m = "6"
        elif vol == "3 tsp" or vol == "1 tbsp":
            m = "10"
        elif vol == "6 tsp" or vol == "2 tbsp":
            m = "20"


    # Less dense spices
    elif food == "Allspice, ground" or food == "Cloves, ground" or food == "Garam masala" or food == "Ginger, ground" or food == "Coriander, ground":
        if vol == "1/8 tsp":
            m = "0.25"
        elif vol == "1/4 tsp":
            m = "0.5"
        elif vol == "1/2 tsp":
            m = "1"
        elif vol == "1 tsp":
            m = "2"
        elif vol == "1/2 tbsp" or vol == "1.5 tsp" or vol == "1 1/2 tsp":
            m = "3"
        elif vol == "2 tsp":
            m = "4"
        elif vol == "3 tsp" or vol == "1 tbsp":
            m = "6"
        elif vol == "6 tsp" or vol == "2 tbsp":
            m = "12"


    # Nutritional yeast, cocoa, coconut flakes, psyllium
    elif food == "Nutritional yeast" or food == "Cocoa powder" or food == "Carob powder" or food == "Cacao powder" or food == "Unsweetened coconut flakes" or food == "Psyllium husks, whole":
        if vol == "1/2 tbsp" or vol == "1.5 tsp" or vol == "1 1/2 tsp":
            m = "2.5"
        elif vol == "1 tbsp":
            m = "5"
        elif vol == "2 tbsp":
            m = "10"
        elif vol == "3 tbsp":
            m = "15"
        elif vol == "4 tbsp" or vol == "1/4 cup":
            m = "20"
        elif vol == "5 tbsp":
            m = "25"
        elif vol == "1/3 cup":
            m = "27"
        elif vol == "6 tbsp":
            m = "30"
        elif vol == "7 tbsp":
            m = "35"
        elif vol == "8 tbsp" or vol == "1/2 cup":
            m = "40"
        elif vol == "9 tbsp":
            m = "45"
        elif vol == "10 tbsp" or vol == "1/2cup + 2tbsp" or vol == "1/2 cup + 2 tbsp":
            m = "50"
        elif vol == "2/3 cup":
            m = "53"
        elif vol == "11 tbsp":
            m = "55"
        elif vol == "12 tbsp" or vol == "3/4 cup":
            m = "60"
        elif vol == "13 tbsp":
            m = "65"
        elif vol == "14 tbsp":
            m = "70"
        elif vol == "15 tbsp":
            m = "75"
        elif vol == "16 tbsp" or vol == "1 cup":
            m = "80"
        elif vol == "1.5 cup" or vol == "1 1/2 cup":
            m = "120"
        elif vol == "2 cup":
            m = "160"

    # Herbs
    elif food == "Basil, dried" or food == "Oregano, dried" or food == "Thyme, dried" or food == "Parsley, dried" or food == "Red pepper flakes" or food == "Rosemary, dried" or food == "Italian seasoning" or food == "Cilantro, dried" or food == "Chives, dried":
        if vol == "1/2 tsp":
            m = "0.5"
        elif vol == "1 tsp":
            m = "1"
        elif vol == "1/2 tbsp" or vol == "1.5 tsp" or vol == "1 1/2 tsp":
            m = "1.5"
        elif vol == "2 tsp":
            m = "2"
        elif vol == "3 tsp" or vol == "1 tbsp":
            m = "3"
        elif vol == "6 tsp" or vol == "2 tbsp":
            m = "6"


    # Sauce
    elif food == "Simple pasta sauce":
        if vol == "1 serving":
            m = "100"
        elif vol == "1.2 serving":
            m = "120"
        elif vol == "2.4 serving":
            m = "240"


    # Liquids
    elif food == "Water" or food == "Unsweetened original almond milk" or food == "Unsweetened almond milk" or food == "Unsweetened vanilla almond milk" or food == "Skim milk" or food == "Fairlife skim milk" or food == "Extra virgin olive oil" or food == "Soy sauce, low sodium, gluten free" or food == "Balsamic vinegar" or food == "White vinegar" or food == "Apple cider vinegar" or food == "Unsweetened applesauce" or food == "White vinegar, or apple cider vinegar" or food == "Unsweetened almond milk, or water" or food == "Unsweetened vanilla almond milk, or water" or food == "Pumpkin puree" or food == "Pumpkin Puree" or food == "Pumpkin puree, or sweet potato" or food == "Pumpkin puree, or sweet potato puree" or food == "Sweet potato puree" or food == "Sweet Potato puree, Pumpkin puree, or Butternut Squash puree" or food == "Sweet potato Puree, or Pumpkin puree" or food == "Low sodium soy sauce" or food == "Fat free Italian dressing" or food == "Italian dressing" or food == "Lime juice" or food == "Lemon juice" or food == "Sesame oil" or food == "Canola oil" or food == "Vegetable oil" or food == "Evaporated milk" or food == "Fat free evaporated milk" or food == "Chicken bone broth" or food == "Chicken broth" or food == "Vegetable broth" or food == "Low sodium chicken broth" or food == "Low sodium vegetable broth" or food == "Dijon mustard" or food == "Minced garlic" or food == "Red wine vinegar" or food == "Hot sauce" or food == "Kefir, plain, 1% fat" or food == "Kefir, plain, 3.25% fat":
        if vol == "1/4 tsp":
            m = "1.25"
        elif vol == "1/2 tsp":
            m = "2.5"
        elif vol == "1 tsp":
            m = "5"
        elif vol == "1/2 tbsp":
            m = "7.5"
        elif vol == "2 tsp":
            m = "10"
        elif vol == "1 tbsp":
            m = "15"
        elif vol == "2 tbsp":
            m = "30"
        elif vol == "3 tbsp":
            m = "45"
        elif vol == "4 tbsp" or vol == "1/4 cup":
            m = "60"
        elif vol == "5 tbsp":
            m = "75"
        elif vol == "1/3 cup":
            m = "80"
        elif vol == "6 tbsp":
            m = "90"
        elif vol == "7 tbsp":
            m = "105"
        elif vol == "1/2 cup" or vol == "8 tbsp":
            m = "120"
        elif vol == "2/3 cup":
            m = "160"
        elif vol == "3/4 cup" or vol == "12 tbsp":
            m = "180"
        elif vol == "1 cup":
            m = "240"
        elif vol == "1.25 cup" or vol == "1 1/4 cup":
            m = "300"
        elif vol == "1.33 cup" or vol == "1 1/3 cup":
            m = "320"
        elif vol == "1.5 cup" or vol == "1 1/2 cup":
            m = "360"
        elif vol == "1.67 cup" or vol == "1 2/3 cup":
            m = "400"
        elif vol == "1.75 cup" or vol == "1 3/4 cup":
            m = "420"
        elif vol == "2 cup":
            m = "480"
        elif vol == "3 cup":
            m = "720"
        elif vol == "4 cup":
            m = "960"
        elif vol == "5 cup":
            m = "1200"

    # Powdered sugar & monk fruit
    elif food == "Powdered monk fruit" or food == "Powdered sugar":
        if vol == "1 tbsp":
            m = "8"
        elif vol == "2 tbsp":
            m = "16"
        elif vol == "3 tbsp":
            m = "24"
        elif vol == "4 tbsp":
            m = "32"


    # Coconut oil
    elif food == "Extra virgin coconut oil" or food == "Extra virgin coconut oil, or extra virgin olive oil" or food == "Unsalted butter" or food == "Salted butter":
        if vol == "1/2 tsp":
            m = "2.5"
        elif vol == "1 tsp":
            m = "5"
        elif vol == "1/2 tbsp":
            m = "7"
        elif vol == "1 tbsp":
            m = "14"
        elif vol == "2 tbsp":
            m = "28"
        elif vol == "3 tbsp":
            m = "42"
        elif vol == "4 tbsp" or vol == "1/4 cup":
            m = "56"
        elif vol == "5 tbsp":
            m = "70"
        elif vol == "6 tbsp":
            m = "84"
        elif vol == "7 tbsp":
            m = "98"
        elif vol == "8 tbsp" or vol == "1/2 cup":
            m = "112"


    # Labneh cheese
    elif food == "Labneh cheese, skim":
        if vol == "0.5 serving":
            m = "15"
        elif vol == "1 serving":
            m = "30"
        elif vol == "1.5 serving":
            m = "45"
        elif vol == "2 serving":
            m = "60"

    # Rice
    elif food == "Brown rice" or food == "Wild rice":
        if vol == "1/4 cup":
            m = "45"
        elif vol == "1/3 cup":
            m = "60"
        elif vol == "1/2 cup":
            m = "90"
        elif vol == "2/3 cup":
            m = "120"
        elif vol == "3/4 cup":
            m = "135"
        elif vol == "1 cup":
            m = "180"
        elif vol == "1.5 cup" or vol == "1 1/2 cup":
            m = "270"
        elif vol == "2 cup":
            m = "360"
        elif vol == "3 cup":
            m = "540"
        elif vol == "4 cup":
            m = "720"

    # Empanadas / pierogi
    elif food == "Empanada/Pierogi dough":
        if vol == "12 serving":
            m = "333"

    # Yogurt & cottage cheese
    elif food == "Nonfat cottage cheese" or food == "Plain nonfat greek yogurt" or food == "Plain whole milk greek yogurt" or food == "Vanilla Nonfat Greek Yogurt, Sugar Free" or food == "Ricotta cheese":
        if vol == "1 tbsp":
            m = "14"
        elif vol == "2 tbsp":
            m = "28"
        elif vol == "1/4 cup" or vol == "4 tbsp":
            m = "56"
        elif vol == "1/2 cup" or vol == "8 tbsp":
            m = "113"
        elif vol == "3/4 cup":
            m = "170"
        elif vol == "1 cup":
            m = "226"
        elif vol == "1.25 cup" or vol == "1 1/4 cup":
            m = "283"
        elif vol == "1.5 cup" or vol == "1 1/2 cup":
            m = "340"
        elif vol == "1.75 cup" or vol == "1 3/4 cup":
            m = "396"
        elif vol == "2 cup":
            m = "454"
        elif vol == "3 cup":
            m = "681"
        elif vol == "4 cup":
            m = "908"

    # Cashew ricotta
    elif food == "Dairy Free Cashew Ricotta Cheese":
        if vol == "1 serving":
            m = "56"
        elif vol == "2 serving":
            m = "112"
        elif vol == "3 serving":
            m = "168"
        elif vol == "4 serving":
            m = "224"
        elif vol == "5 serving":
            m = "280"
        elif vol == "6 serving":
            m = "336"

    # Flours
    elif food == "Vital wheat gluten" or food == "Flour" or food == "All purpose flour" or food == "White flour" or food == "Whole wheat flour" or food == "Cornmeal" or food == "Panko breadcrumbs" or food == "Whole wheat breadcrumbs" or food == "Breadcrumbs" or food == "Millet flour" or food == "Chickpea flour" or food == "Coconut flour" or food == "Grated parmesan cheese":
        if vol == "2 tbsp":
            m = "15"
        elif vol == "3 tbsp":
            m = "22.5"
        elif vol == "4 tbsp" or vol == "1/4 cup":
            m = "30"
        elif vol == "1/2 cup":
            m = "60"
        elif vol == "3/4 cup":
            m = "90"
        elif vol == "1 cup":
            m = "120"
        elif vol == "1.5 cup" or vol == "1 1/2 cup":
            m = "180"
        elif vol == "2 cup":
            m = "240"
        elif vol == "2.33 cup" or vol == "2 1/3 cup":
            m = "280"
        elif vol == "2.5 cup" or vol == "2 1/2 cup":
            m = "300"
        elif vol == "3 cup":
            m = "360"


    # Protein powder
    elif food == "Whey protein powder, unflavored" or food == "Whey protein powder, chocolate" or food == "Whey protein powder, vanilla" or food == "Nutricost Whey Unflavored Protein Powder" or food == "Casein protein powder, unflavored" or food == "Casein protein powder, chocolate" or food == "Casein protein powder, vanilla" or food == "Nutricost Casein Unflavored Protein Powder":
        if vol == "1/3 scoop":
            m = "10"
        elif vol == "1/2 scoop":
            m = "15"
        elif vol == "2/3 scoop":
            m = "20"
        elif vol == "1 scoop":
            m = "30"
        elif vol == "1.33 scoop" or vol == "1 1/3 scoop":
            m = "40"
        elif vol == "1.5 scoop" or vol == "1 1/2 scoop":
            m = "45"
        elif vol == "2 scoop":
            m = "60"
        elif vol == "2.5 scoop" or vol == "2 1/2 scoop":
            m = "75"
        elif vol == "3 scoop":
            m = "90"
        elif vol == "4 scoop":
            m = "120"


    # Nut butters
    elif food == "Almond butter" or food == "Peanut butter" or food == "Natural peanut butter" or food == "Natural peanut butter, or tahini" or food == "Walnut butter" or food == "Cashew butter" or food == "Sunflower seed butter" or food == "Sunflower butter" or food == "Pistachio butter" or food == "Pumpkin seed butter" or food == "Tahini, or any other nut/seed butter":
        if vol == "1/2 tbsp":
            m = "8"
        elif vol == "1 tbsp":
            m = "16"
        elif vol == "1.5 tbsp" or vol == "1 1/2 tbsp":
            m = "24"
        elif vol == "2 tbsp":
            m = "32"
        elif vol == "2.5 tbsp" or vol == "2 1/2 tbsp":
            m = "40"
        elif vol == "3 tbsp":
            m = "48"
        elif vol == "4 tbsp" or vol == "1/4 cup":
            m = "64"
        elif vol == "5 tbsp":
            m = "80"
        elif vol == "6 tbsp":
            m = "96"
        elif vol == "8 tbsp" or vol == "1/2 cup":
            m = "128"
        elif vol == "12 tbsp" or vol == "3/4 cup":
            m = "196"
        elif vol == "16 tbsp" or vol == "1 cup":
            m = "256"

    # Miso
    elif food == "Miso" or food == "Miso paste":
        if vol == "1/2 tbsp":
            m = "8.5"
        elif vol == "1 tbsp":
            m = "17"
        elif vol == "1.5 tbsp" or vol == "1 1/2 tbsp":
            m = "25.5"
        elif vol == "2 tbsp":
            m = "34"
        elif vol == "3 tbsp":
            m = "51"
        elif vol == "4 tbsp" or vol == "1/4 cup":
            m = "68"
        elif vol == "5 tbsp":
            m = "85"
        elif vol == "6 tbsp":
            m = "102"
        elif vol == "8 tbsp" or vol == "1/2 cup":
            m = "136"

    # Syrup
    elif food == "Sugar free syrup" or food == "Sugar free syrup, or maple syrup or honey" or food == "Sugar free syrup, or honey or maple syrup" or food == "Sugar free syrup, or honey" or food == "Sugar free syrup, or maple syrup" or food == "Sugar free syrup, optional" or food == "Maple syrup" or food == "Maple syrup, or honey":
        if vol == "1/2 tbsp" or vol == "0.5 serving":
            m = "10"
        elif vol == "1 tbsp" or vol == "1 serving":
            m = "20"
        elif vol == "1.5 tbsp" or vol == "1.5 serving" or vol == "1 1/2 tbsp":
            m = "30"
        elif vol == "2 tbsp" or vol == "2 serving":
            m = "40"
        elif vol == "3 tbsp" or vol == "3 serving":
            m = "60"
        elif vol == "4 tbsp" or vol == "1/4 cup" or vol == "4 serving":
            m = "80"
        elif vol == "5 tbsp" or vol == "5 serving":
            m = "100"
        elif vol == "1/3 cup" or vol == "5.33 serving":
            m = "107"
        elif vol == "6 tbsp" or vol == "6 serving":
            m = "120"
        elif vol == "7 tbsp" or vol == "7 serving":
            m = "140"
        elif vol == "8 tbsp" or vol == "1/2 cup" or vol == "8 serving":
            m = "160"
        elif vol == "9 tbsp" or vol == "9 serving":
            m = "180"
        elif vol == "10 tbsp" or vol == "10 serving":
            m = "200"
        elif vol == "2/3 cup" or vol == "10.67 serving":
            m = "213"
        elif vol == "11 tbsp" or vol == "11 serving":
            m = "220"
        elif vol == "12 tbsp" or vol == "3/4 cup" or vol == "12 serving":
            m = "240"
        elif vol == "13 tbsp" or vol == "13 serving":
            m = "260"
        elif vol == "14 tbsp" or vol == "14 serving":
            m = "280"
        elif vol == "15 tbsp" or vol == "15 serving":
            m = "300"
        elif vol == "16 tbsp" or vol == "1 cup" or vol == "16 serving":
            m = "320"


    # Honey
    elif food == "Honey" or food == "Honey, or maple syrup":
        if vol == "1/2 tbsp":
            m = "10.5"
        elif vol == "1 tbsp":
            m = "21"
        elif vol == "1.5 tbsp" or vol == "1 1/2 tbsp":
            m = "31.5"
        elif vol == "2 tbsp":
            m = "42"
        elif vol == "3 tbsp":
            m = "63"
        elif vol == "4 tbsp" or vol == "1/4 cup":
            m = "84"
        elif vol == "5 tbsp":
            m = "105"
        elif vol == "1/3 cup":
            m = "112"
        elif vol == "6 tbsp":
            m = "126"
        elif vol == "7 tbsp":
            m = "147"
        elif vol == "8 tbsp" or vol == "1/2 cup":
            m = "168"
        elif vol == "9 tbsp":
            m = "189"
        elif vol == "10 tbsp":
            m = "210"
        elif vol == "2/3 cup":
            m = "224"
        elif vol == "11 tbsp":
            m = "231"
        elif vol == "12 tbsp" or vol == "3/4 cup":
            m = "252"
        elif vol == "13 tbsp":
            m = "273"
        elif vol == "14 tbsp":
            m = "294"
        elif vol == "15 tbsp":
            m = "315"
        elif vol == "16 tbsp" or vol == "1 cup":
            m = "336"


    # Onions
    elif food == "Onion":
        if vol == "1/2 medium":
            m = "55"
        elif vol == "1 medium":
            m = "110"
        elif vol == "2 medium":
            m = "220"
        elif vol == "3 medium":
            m = "330"
        elif vol == "4 medium":
            m = "440"
        elif vol == "5 medium":
            m = "550"


    # Peppers
    elif food == "Bell pepper":
        if vol == "1/2 medium":
            m = "60"
        elif vol == "1 medium":
            m = "120"
        elif vol == "2 medium":
            m = "240"
        elif vol == "3 medium":
            m = "360"
        elif vol == "4 medium":
            m = "480"
        elif vol == "5 medium":
            m = "600"


    # Tomatoes
    elif food == "Tomato":
        if vol == "1/2 medium":
            m = "50"
        elif vol == "1 medium":
            m = "100"
        elif vol == "2 medium":
            m = "200"
        elif vol == "3 medium":
            m = "300"
        elif vol == "4 medium":
            m = "400"
        elif vol == "5 medium":
            m = "500"


    # Lettuce
    elif food == "Lettuce" or food == "Romaine lettuce":
        if vol == "1/2 head" or vol == "4 oz":
            m = "113"
        elif vol == "1 head"  or vol == "8 oz, about 2 heads" or vol == "8 oz":
            m = "226"
        elif vol == "2 heads" or vol == "2 head":
            m = "454"
        elif vol == "3 medium":
            m = "360"
        elif vol == "4 medium":
            m = "480"
        elif vol == "5 medium":
            m = "600"


    # Powdered pb
    elif food == "Powdered peanut butter":
        if vol == "1/2 tbsp" or vol == "1.5 tsp" or vol == "1 1/2 tsp":
            m = "3"
        elif vol == "1 tbsp":
            m = "6"
        elif vol == "1.5 tbsp" or vol == "1 1/2 tbsp":
            m = "9"
        elif vol == "2 tbsp":
            m = "12"
        elif vol == "3 tbsp":
            m = "18"
        elif vol == "4 tbsp" or vol == "1/4 cup":
            m = "24"
        elif vol == "5 tbsp":
            m = "30"
        elif vol == "1/3 cup":
            m = "32"
        elif vol == "6 tbsp":
            m = "36"
        elif vol == "7 tbsp":
            m = "42"
        elif vol == "8 tbsp" or vol == "1/2 cup":
            m = "48"
        elif vol == "9 tbsp":
            m = "54"
        elif vol == "10 tbsp":
            m = "60"
        elif vol == "2/3 cup":
            m = "64"
        elif vol == "11 tbsp":
            m = "66"
        elif vol == "12 tbsp" or vol == "3/4 cup":
            m = "72"
        elif vol == "13 tbsp":
            m = "78"
        elif vol == "14 tbsp":
            m = "84"
        elif vol == "15 tbsp":
            m = "90"
        elif vol == "16 tbsp" or vol == "1 cup":
            m = "96"


    # Chia seeds
    elif food == "Chia seeds":
        if vol == "1/2 tbsp" or vol == "1.5 tsp":
            m = "6"
        elif vol == "1 tbsp":
            m = "12"
        elif vol == "1.5 tbsp" or vol == "1 1/2 tbsp":
            m = "18"
        elif vol == "2 tbsp":
            m = "24"
        elif vol == "3 tbsp":
            m = "36"
        elif vol == "4 tbsp" or vol == "1/4 cup":
            m = "48"
        elif vol == "5 tbsp":
            m = "60"
        elif vol == "1/3 cup":
            m = "64"
        elif vol == "6 tbsp":
            m = "72"
        elif vol == "7 tbsp":
            m = "84"
        elif vol == "8 tbsp" or vol == "1/2 cup":
            m = "96"
        elif vol == "9 tbsp":
            m = "108"
        elif vol == "10 tbsp":
            m = "120"
        elif vol == "2/3 cup":
            m = "128"
        elif vol == "11 tbsp":
            m = "132"
        elif vol == "12 tbsp" or vol == "3/4 cup":
            m = "144"
        elif vol == "13 tbsp":
            m = "156"
        elif vol == "14 tbsp":
            m = "168"
        elif vol == "15 tbsp":
            m = "180"
        elif vol == "16 tbsp" or vol == "1 cup":
            m = "192"


    # Oat flour
    elif food == "Oat flour" or food == "Oat flour, or almond flour" or food == "Oat flour, or almond":
        if vol == "1/2 tbsp" or vol == "1.5 tsp":
            m = "3"
        elif vol == "1 tbsp":
            m = "6"
        elif vol == "1.5 tbsp" or vol == "1 1/2 tbsp":
            m = "9"
        elif vol == "2 tbsp":
            m = "11"
        elif vol == "3 tbsp":
            m = "17"
        elif vol == "4 tbsp" or vol == "1/4 cup":
            m = "23"
        elif vol == "5 tbsp":
            m = "28"
        elif vol == "1/3 cup":
            m = "30"
        elif vol == "6 tbsp":
            m = "34"
        elif vol == "7 tbsp":
            m = "39"
        elif vol == "8 tbsp" or vol == "1/2 cup":
            m = "45"
        elif vol == "9 tbsp" or vol == "1/2cup + 1tbsp" or vol == "1/2 cup + 1 tbsp":
            m = "51"
        elif vol == "10 tbsp":
            m = "56"
        elif vol == "2/3 cup":
            m = "60"
        elif vol == "11 tbsp":
            m = "62"
        elif vol == "12 tbsp" or vol == "3/4 cup":
            m = "68"
        elif vol == "13 tbsp":
            m = "73"
        elif vol == "14 tbsp":
            m = "79"
        elif vol == "15 tbsp":
            m = "84"
        elif vol == "16 tbsp" or vol == "1 cup":
            m = "90"
        elif vol == "17 tbsp" or vol == "1cup + 1tbsp" or vol == "1 cup + 1 tbsp" or vol == "Heaping cup" or vol == "1 heaping cup" or vol == "1 Heaping cup":
            m = "96"
        elif vol == "18 tbsp" or vol == "1cup + 2tbsp" or vol == "1 cup + 2 tbsp":
            m = "101"
        elif vol == "1.25 cup" or vol == "1 1/4 cup":
            m = "113"
        elif vol == "1.33 cup" or vol == "1 1/3 cup":
            m = "120"
        elif vol == "1.5 cup" or vol == "1 1/2 cup":
            m = "135"
        elif vol == "1.67 cup" or vol == "1.66 cup" or vol == "1 2/3 cup":
            m = "150"
        elif vol == "1.75 cup" or vol == "1 3/4 cup":
            m = "158"
        elif vol == "2 cup":
            m = "180"
        elif vol == "2.5 cup" or vol == "2 1/2 cup":
            m = "225"
        elif vol == "3 cup":
            m = "270"


    # Almond flour
    elif food == "Almond flour" or food == "Almond flour, or oat flour" or food == "Almond flour, or oat" or food == "Almond flour (or whole nuts)":
        if vol == "1/2 tbsp" or vol == "1.5 tsp" or vol == "1 1/2 tsp":
            m = "3.5"
        elif vol == "1 tbsp":
            m = "7"
        elif vol == "1.5 tbsp" or vol == "1 1/2 tbsp":
            m = "10.5"
        elif vol == "2 tbsp":
            m = "14"
        elif vol == "3 tbsp":
            m = "21"
        elif vol == "4 tbsp" or vol == "1/4 cup":
            m = "28"
        elif vol == "5 tbsp":
            m = "35"
        elif vol == "1/3 cup":
            m = "37"
        elif vol == "6 tbsp":
            m = "42"
        elif vol == "7 tbsp":
            m = "49"
        elif vol == "8 tbsp" or vol == "1/2 cup":
            m = "56"
        elif vol == "9 tbsp":
            m = "63"
        elif vol == "10 tbsp":
            m = "70"
        elif vol == "2/3 cup":
            m = "75"
        elif vol == "11 tbsp":
            m = "77"
        elif vol == "12 tbsp" or vol == "3/4 cup":
            m = "84"
        elif vol == "13 tbsp":
            m = "91"
        elif vol == "14 tbsp":
            m = "98"
        elif vol == "15 tbsp":
            m = "105"
        elif vol == "16 tbsp" or vol == "1 cup":
            m = "112"
        elif vol == "17 tbsp" or vol == "1cup + 1tbsp" or vol == "1 cup + 1 tbsp" or vol == "Heaping cup" or vol == "1 heaping cup" or vol == "1 Heaping cup":
            m = "119"
        elif vol == "18 tbsp" or vol == "1cup + 2tbsp" or vol == "1 cup + 2 tbsp":
            m = "126"
        elif vol == "1.25 cup" or vol == "1 1/4 cup":
            m = "140"
        elif vol == "1.33 cup" or vol == "1 1/3 cup":
            m = "149"
        elif vol == "1.5 cup" or vol == "1 1/2 cup":
            m = "168"
        elif vol == "1.67 cup" or vol == "1.66 cup" or vol == "1 2/3 cup":
            m = "187"
        elif vol == "1.75 cup" or vol == "1 3/4 cup":
            m = "196"
        elif vol == "2 cup":
            m = "224"
        elif vol == "2.5 cup" or vol == "2 1/2 cup":
            m = "280"
        elif vol == "3 cup":
            m = "336"


    # Oats
    elif food == "Rolled oats" or food == "Quick oats" or food == "Rolled oats, or quick oats" or food == "Rolled oats, or quick" or food == "Quick oats, or rolled oats" or food == "Quick oats, or rolled" or food == "Quick oats, or oat flour" or food == "Rolled oats, or oat flour":
        if vol == "1/2 tbsp" or vol == "1.5 tsp" or vol == "1 1/2 tsp":
            m = "2.5"
        elif vol == "1 tbsp":
            m = "5"
        elif vol == "1.5 tbsp" or vol == "1 1/2 tbsp":
            m = "7.5"
        elif vol == "2 tbsp":
            m = "10"
        elif vol == "3 tbsp":
            m = "15"
        elif vol == "4 tbsp" or vol == "1/4 cup":
            m = "20"
        elif vol == "5 tbsp":
            m = "25"
        elif vol == "1/3 cup":
            m = "27"
        elif vol == "6 tbsp":
            m = "30"
        elif vol == "7 tbsp":
            m = "35"
        elif vol == "8 tbsp" or vol == "1/2 cup":
            m = "40"
        elif vol == "9 tbsp":
            m = "45"
        elif vol == "10 tbsp":
            m = "50"
        elif vol == "2/3 cup":
            m = "53"
        elif vol == "11 tbsp":
            m = "55"
        elif vol == "12 tbsp" or vol == "3/4 cup":
            m = "60"
        elif vol == "13 tbsp":
            m = "65"
        elif vol == "14 tbsp":
            m = "70"
        elif vol == "15 tbsp":
            m = "75"
        elif vol == "16 tbsp" or vol == "1 cup":
            m = "80"
        elif vol == "17 tbsp" or vol == "1cup + 1tbsp" or vol == "1 cup + 1 tbsp" or vol == "Heaping cup" or vol == "1 heaping cup" or vol == "1 Heaping cup":
            m = "85"
        elif vol == "18 tbsp" or vol == "1cup + 2tbsp" or vol == "1 cup + 2 tbsp":
            m = "90"
        elif vol == "1.25 cup" or vol == "1 1/4 cup":
            m = "100"
        elif vol == "1.33 cup" or vol == "1 1/3 cup":
            m = "107"
        elif vol == "1.5 cup" or vol == "1 1/2 cup":
            m = "120"
        elif vol == "1.67 cup" or vol == "1.66 cup" or vol == "1 2/3 cup":
            m = "133"
        elif vol == "1.75 cup" or vol == "1 3/4 cup":
            m = "140"
        elif vol == "2 cup":
            m = "160"
        elif vol == "2.5 cup" or vol == "2 1/2 cup":
            m = "200"
        elif vol == "3 cup":
            m = "240"


    # Ground Flaxseed
    elif food == "Ground flaxseed":
        if vol == "1/2 tbsp" or vol == "1.5 tsp" or vol == "1 1/2 tbsp":
            m = "3.25"
        elif vol == "1 tbsp":
            m = "6.5"
        elif vol == "1.5 tbsp" or vol == "1 1/2 tbsp":
            m = "9.75"
        elif vol == "2 tbsp":
            m = "13"
        elif vol == "3 tbsp":
            m = "20"
        elif vol == "4 tbsp" or vol == "1/4 cup":
            m = "26"
        elif vol == "5 tbsp":
            m = "33"
        elif vol == "1/3 cup":
            m = "35"
        elif vol == "6 tbsp":
            m = "39"
        elif vol == "7 tbsp":
            m = "46"
        elif vol == "8 tbsp" or vol == "1/2 cup":
            m = "52"
        elif vol == "9 tbsp":
            m = "59"
        elif vol == "10 tbsp":
            m = "65"
        elif vol == "2/3 cup":
            m = "69"
        elif vol == "11 tbsp":
            m = "72"
        elif vol == "12 tbsp" or vol == "3/4 cup":
            m = "78"
        elif vol == "13 tbsp":
            m = "85"
        elif vol == "14 tbsp":
            m = "91"
        elif vol == "15 tbsp":
            m = "98"
        elif vol == "16 tbsp" or vol == "1 cup":
            m = "104"
        elif vol == "17 tbsp" or vol == "1cup + 1tbsp" or vol == "1 cup + 1 tbsp" or vol == "Heaping cup" or vol == "1 heaping cup" or vol == "1 Heaping cup":
            m = "111"
        elif vol == "18 tbsp" or vol == "1cup + 2tbsp" or vol == "1 cup + 2 tbsp":
            m = "117"
        elif vol == "1.25 cup" or vol == "1 1/4 cup":
            m = "130"
        elif vol == "1.33 cup" or vol == "1 1/3 cup":
            m = "138"
        elif vol == "1.5 cup" or vol == "1 1/2 cup":
            m = "156"
        elif vol == "1.67 cup" or vol == "1.66 cup" or vol == "1 2/3 cup":
            m = "174"
        elif vol == "1.75 cup" or vol == "1 3/4 cup":
            m = "182"
        elif vol == "2 cup":
            m = "208"
        elif vol == "2.5 cup" or vol == "2 1/2 cup":
            m = "260"
        elif vol == "3 cup":
            m = "312"


    # Chocolate chips
    elif food == "90% chocolate" or food == "85% chocolate" or food == "Sugar free chocolate chips" or food == "Chocolate chips" or food == "Semisweet chocolate chips" or food == "Semi-sweet chocolate chips" or food == "Semisweet chocolate chips (optional)" or food == "Dark chocolate chips" or food == "100% chocolate" or food == "70% chocolate" or food == "50% chocolate" or food == "Allulose chocolate bar":
        if vol == "1/2 tbsp":
            m = "7.5"
        elif vol == "1 tbsp":
            m = "15"
        elif vol == "2 tbsp":
            m = "30"
        elif vol == "4 tbsp" or vol == "1/4 cup":
            m = "45"
        elif vol == "1/3 cup":
            m = "60"
        elif vol == "1/2 cup":
            m = "90"
        elif vol == "3/4 cup":
            m = "135"
        elif vol == "1 cup":
            m = "180"


    # Eggs
    elif food == "Egg":
        if vol == "1 large":
            m = "50"
        elif vol == "2 large":
            m = "100"
        elif vol == "3 large":
            m = "150"
        elif vol == "4 large":
            m = "200"
        elif vol == "5 large":
            m = "250"
        elif vol == "6 large":
            m = "300"
        elif vol == "7 large":
            m = "350"
        elif vol == "8 large":
            m = "400"

    # Egg whites
    elif food == "Egg whites" or food == "Liquid egg whites":
        if vol == "1/4 tsp":
            m = "1.25"
        elif vol == "1/2 tsp":
            m = "2.5"
        elif vol == "1 tsp":
            m = "5"
        elif vol == "1/2 tbsp":
            m = "7.5"
        elif vol == "2 tsp":
            m = "10"
        elif vol == "1 tbsp":
            m = "15"
        elif vol == "2 tbsp":
            m = "30"
        elif vol == "1 large":
            m = "33"
        elif vol == "3 tbsp":
            m = "45"
        elif vol == "4 tbsp" or vol == "1/4 cup":
            m = "60"
        elif vol == "2 large":
            m = "66"
        elif vol == "5 tbsp":
            m = "75"
        elif vol == "1/3 cup":
            m = "80"
        elif vol == "6 tbsp":
            m = "90"
        elif vol == "3 large":
            m = "99"
        elif vol == "7 tbsp":
            m = "105"
        elif vol == "1/2 cup" or vol == "8 tbsp":
            m = "120"
        elif vol == "2/3 cup":
            m = "160"
        elif vol == "3/4 cup" or vol == "12 tbsp":
            m = "180"
        elif vol == "1 cup":
            m = "240"
        elif vol == "1.25 cup" or vol == "1 1/4 cup":
            m = "300"
        elif vol == "1.33 cup" or vol == "1 1/3 cup":
            m = "320"
        elif vol == "1.5 cup" or vol == "1 1/2 cup":
            m = "360"
        elif vol == "1.67 cup" or vol == "1 2/3 cup":
            m = "400"
        elif vol == "1.75 cup" or vol == "1 3/4 cup":
            m = "420"
        elif vol == "2 cup":
            m = "480"
        elif vol == "3 cup":
            m = "720"
        elif vol == "4 cup":
            m = "960"
        elif vol == "5 cup":
            m = "1200"

    # Apples
    elif food == "Apple, gala":
        if vol == "1 medium":
            m = "172"
        elif vol == "2 medium":
            m = "344"
        elif vol == "3 medium":
            m = "516"
        elif vol == "4 medium":
            m = "688"
        elif vol == "5 medium":
            m = "860"
        elif vol == "6 medium":
            m = "1032"
        elif vol == "7 medium":
            m = "1204"
        elif vol == "8 medium":
            m = "1376"
        elif vol == "9 medium":
            m = "1548"
        elif vol == "10 medium":
            m = "1720"

    # Sugar, etc.
    elif food == "Granulated sugar" or food == "Brown sugar" or food == "Granular sweetener: sugar, erythritol, stevia, etc." or food == "Allulose" or food == "Granulated monk fruit" or food == "Granulated stevia" or food == "Inulin":
        if vol == "1 tbsp":
            m = "12"
        elif vol == "2 tbsp":
            m = "25"
        elif vol == "3 tbsp":
            m = "38"
        elif vol == "1/4 cup" or vol == "4 tbsp":
            m = "50"
        elif vol == "5 tbsp":
            m = "63"
        elif vol == "1/3 cup":
            m = "67"
        elif vol == "6 tbsp":
            m = "75"
        elif vol == "7 tbsp":
            m = "88"
        elif vol == "1/2 cup" or vol == "8 tbsp":
            m = "100"
        elif vol == "9 tbsp":
            m = "113"
        elif vol == "10 tbsp":
            m = "125"
        elif vol == "2/3 cup":
            m = "133"
        elif vol == "11 tbsp":
            m = "138"
        elif vol == "3/4 cup" or vol == "12 tbsp":
            m = "150"
        elif vol == "13 tbsp":
            m = "163"
        elif vol == "14 tbsp":
            m = "175"
        elif vol == "15 tbsp":
            m = "188"
        elif vol == "1 cup" or vol == "16 tbsp":
            m = "200"
        elif vol == "1.25 cup" or vol == "1 1/4 cup":
            m = "250"

    # Popcorn
    elif food == "Popcorn kernels":
        if vol == "3 tbsp":
            m = "40"


    return m

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
