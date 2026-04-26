# Download csv to /python/testing folder, and run script to fix ingredient names in ingredients file

import pandas as pd
import os
import glob
import csv

def ingredients(food):
    f = food

    # Misc
    if food == "Water, generic, bottled" or food == "Beverages, well, tap, water":
        f = "Water"
    elif food == "Nutricost Electrolyte Mix":
        f = "Electrolyte mix"

    # Beans
    elif food == "crockpotbeans":
        f = "Slow Cooker Dried Beans"
    elif food == "Beans, canned, mature seeds, navy":
        f = "Navy beans, drained and rinsed"
    elif food == "Beans, raw, mature seeds, black":
        f = "Dried beans"
    elif food == "Chickpeas, canned, drained and rinsed" or food == "Chickpeas (garbanzo beans, bengal gram), rinsed in tap water, drained, canned, mature seeds" or food == "Chickpeas (garbanzo beans, bengal gram), drained solids, canned, mature seeds":
        f = "Chickpeas, drained and rinsed"
    elif food == "Chickpeas, canned, whole":
        f = "Chickpeas, NOT drained or rinsed"
    elif food == "Beans, drained solids, canned, pinto" or food == "Beans, rinsed in tap water, drained solids, canned, mature seeds, pinto" or food == "Beans, solids and liquids, canned, mature seeds, pinto":
        f = "Pinto beans, drained and rinsed"
    elif food == "Pinto beans, canned, whole":
        f = "Pinto beans, NOT drained or rinsed"
    elif food == "Black beans, canned, drained and rinsed" or food == "Beans, with salt, boiled, cooked, mature seeds, black" or food == "Beans, rinsed in tap water, drained solids, canned, mature seeds, black" or food == "Beans, canned, mature seeds, all types, black" or food == "Beans, drained solids, canned, black":
        f = "Black beans, drained and rinsed"
    elif food == "Black beans, canned, whole":
        f = "Black beans, NOT drained or rinsed"
    elif food == "Kidney beans, canned, drained and rinsed" or food == "Beans, drained solids, canned, mature seeds, red, kidney" or food == "Beans, canned, mature seeds, all types, kidney":
        f = "Kidney beans, drained and rinsed"
    elif food == "Kidney beans, canned, whole":
        f = "Kidney beans, NOT drained or rinsed"
    elif food == "Beans, raw, black":
        f = "Dried beans"
    elif food == "Split red lentils by ROYAL" or food == "Split red lentils by CEDAR PHOENICIA" or food == "Red lentils" or food == "Lentils, raw, pink or red":
        f = "Red split lentils"
    elif food == "Beans, with salt, boiled, cooked, mature seeds, navy":
        f = "Cooked navy beans"

    # Spices
    elif food == "Spices, coriander seed":
        f = "Coriander, ground"
    elif food == "Capers, canned":
        f = "Capers"
    elif food == "Soup, mix, dry, onion":
        f = "Onion soup mix"
    elif food == "Garam masala by NATCO Foods Ltd":
        f = "Garam masala"
    elif food == "Spices, dried, rosemary":
        f = "Rosemary, dried"
    elif food == "Spices, dried, dill weed":
        f = "Dill, dried"
    elif food == "Salt, table" or food == "Table salt by FIRST STREET" or food == "Table salt by Morton Salt, Inc." or food == "Salt by Morton Salt, Inc." or food == "Table salt by Cardenas Markets":
        f = "Salt"
    elif food == "Flakey salt":
        f = "Flaky salt"
    elif food == "Spices, garlic powder" or food == "Garlic powder by EL SABOR" or food == "Garlic powder by Target Stores" or food == "Garlic powder by STONEMILL":
        f = "Garlic powder"
    elif food == "Spices, onion powder" or food == "Onion powder by ADAMS" or food == "Onion powder by STONEMILL" or food == "Onion powder by Adams Extract Co." or food == "Onion powder by Target Stores":
        f = "Onion powder"
    elif food == "Onions, dehydrated flakes":
        f = "Dried onion flakes"
    elif food == "Spices, ground, cinnamon" or food == "Cinnamon ground by ROUNDY'S":
        f = "Cinnamon"
    elif food == "Spices, ground, ginger" or food == "Ginger ground organic spices by PRIDE OF INDIA" or food == "Organic ground ginger by MEMBER'S MARK":
        f = "Ginger, ground"
    elif food == "Spices, paprika" or food == "Paprika by ROUNDY'S":
        f = "Paprika"
    elif food == "Spices, chili powder" or food == "Chili powder by ADAMS":
        f = "Chili powder"
    elif food == "Spices, black, pepper" or food == "Ground black pepper by MEMBER'S MARK" or food == "Ground black pepper by Grace Kennedy Co. Ltd":
        f = "Black pepper, ground"
    elif food == "Spices, ground, nutmeg" or food == "Ground nutmeg by Rose Spice, Inc.":
        f = "Nutmeg, ground"
    elif food == "Spices, ground, cloves" or food == "Cloves ground by Sugar 'N Spice, Inc.":
        f = "Cloves, ground"
    elif food == "Lemon pepper by LA CRIOLLA" or food == "Lemon pepper by La Criolla Inc." or food == "Lemon pepper by SHURFINE":
        f = "Lemon pepper"
    elif food == "Cilantro lightly dried by MCCORMICK & COMPANY, INC.":
        f = "Cilantro, dried"
    elif food == "Cumin ground by ROUNDY'S" or food == "Ground cumin by STONEMILL" or food == "Spices, cumin seed":
        f = "Cumin, ground"
    elif food == "Spices, dried, oregano":
        f = "Oregano, dried"
    elif food == "Spices, dried, thyme":
        f = "Thyme, dried"
    elif food == "Spices, dried, basil" or food == "Lightly dried basil by Eyebobs, LLC " or food == "Basil lightly dried by GOURMET GARDEN" or food == "Lightly dried basil by Eyebobs, LLC" or food == "Lightly dried basil by Eyebobs, LLC":
        f = "Basil, dried"
    elif food == "Spices, ground, allspice":
        f = "Allspice, ground"
    elif food == "Spices, red or cayenne, pepper" or food == "Cayenne pepper by MEMBER'S MARK":
        f = "Cayenne pepper"
    elif food == "Spices, celery seed":
        f = "Celery seed"
    elif food == "Old bay, seasoning by Baltimore Spice Co":
        f = "Old Bay"
    elif food == "Nutritional yeast seasoning by BRAGG" or food == "Nutritional yeast superfoods by FOODS ALIVE":
        f = "Nutritional yeast"
    elif food == "Chives, freeze-dried":
        f = "Chives, dried"
    elif food == "Italian seasoning by Raley's" or food == "Italian seasoning by ROUNDY'S":
        f = "Italian seasoning"
    elif food == "Everything but the bagel seasoning by Big Y Foods, Inc." or food == "Seasoning everything bagel by Whole Foods Market, Inc.":
        f = "Everything bagel seasoning"
    elif food == "Extra hot red pepper flakes by DOC MEYERS BRAND":
        f = "Red pepper flakes"
    elif food == "Spices, dried, parsley":
        f = "Parsley, dried"
    elif food == "Powdered chicken, bouillon by Goya Foods, Inc." or food == "Powdered bouillon by Goya Foods, Inc." or food == "Powdered chicken flavored bouillon by Goya Foods, Inc.":
        f = "Chicken bouillon powder"
    elif food == "Spices, ground, turmeric":
        f = "Turmeric, ground"
    elif food == "Seaweed, dried":
        f = "Dried seaweed"


    # Oil, vinegar, other liquids
    elif food == "Fat, chicken":
        f = "Chicken fat"
    elif food == "Oil, salad or cooking, olive" or food == "Extra virgin olive oil by OLIO" or food == "Extra virgin olive oil by QO" or food == "Extra virgin olive oil by GAEA" or food == "Extra virgin olive oil by BRAGG":
        f = "Extra virgin olive oil"
    elif food == "Extra virgin coconut oil by KELAPO" or food == "Oil, coconut" or food == "Extra virgin coconut oil by VITA BRAND":
        f = "Extra virgin coconut oil"
    elif food == "Oil, sesame" or food == "Sesame oil by DABUR" or food == "Oil, salad or cooking, sesame":
        f = "Sesame oil"
    elif food == "Vinegar, distilled" or food == "White distilled vinegar by FAREWAY" or food == "Distilled white vinegar by Raley's" or food == "White wine vinegar by CIRIO" or food == "Distilled white vinegar by HYTOR" or food == "Distilled white vinegra by OLIO":
        f = "White vinegar"
    elif food == "Vinegar, red wine":
        f = "Red wine vinegar"
    elif food == "Vinegar, cider" or food == "Apple cider vinegar by BRAGG":
        f = "Apple cider vinegar"
    elif food == "Italian dressing, fat free" or food == "Salad dressing, fat-free, italian dressing":
        f = "Fat free Italian dressing"
    elif food == "Lime juice, raw" or food == "Lime juice from concentrate by Safeway, Inc." or food == "Lime juice from concentrate by ITALIAN GARDEN" or food == "Lime juice from concentrate by Harris-Teeter Inc." or food == "Lime juice, freshly squeezed, 100%":
        f = "Lime juice"
    elif food == "Beet juice":
        f = "Pickled beet juice"
    elif food == "Vinegar, balsamic" or food == "Balsamic vinegar of modena" or food == "Balsamic vinegar by ELSA":
        f = "Balsamic vinegar"
    elif food == "Hot pepper sauce" or food == "Hot sauce by LOUISIANA" or food == "Hot sauce, louisiana style by La Preferida In" or food == "Hot sauce, louisiana style by La Preferida Inc" or food == "Sauce by LOUISIANA":
        f = "Hot sauce"
    elif food == "Minced garlic by STONEMILL" or food == "Minced garlic by MEMBER'S MARK" or food == "Minced garlic by EL SABOR":
        f = "Minced garlic"
    elif food == "Mustard, horseradish" or food == "Mustard" or food == "Dijon mustard by KOOPS'" or food == "Dijon mustard by BRANDLESS" or food == "Dijon mustard by Raley's" or food == "Dijon mustard by SPARTAN":
        f = "Dijon mustard"
    elif food == "White dry cooking wine by CONCHITA":
        f = "White cooking wine"
    elif food == "Lemon juice, raw" or food == "Lemon juice from concentrate, REAL LEMON, bottled" or food == "Lemon juice from concentrate, canned or bottled" or food == "Lemon juice from concentrate by GOLDEN SUN" or food == "Lemon juice from concentrate, CONCORD, bottled":
        f = "Lemon juice"
    elif food == "Low sodium soy sauce" or food == "Soy sauce made from soy (tamari)" or food == "Soy sauce made from soy and wheat (shoyu)" or food == "Soy sauce made from soy and wheat (shoyu), low sodium" or food == "Low Sodium Soy Sauce by First Street":
        f = "Soy sauce, low sodium, gluten free"
    elif food == "Low sodium chicken broth by Glencourt Inc." or food == "Soup, canned, low sodium, chicken broth" or food == "whole-chicken-broth":
        f = "Low sodium chicken broth"
    elif food == "Soup, vegetable broth, SWANSON" or food == "Low sodium vegetable broth by The Hain Celestial Group, Inc.":
        f = "Low sodium vegetable broth"
    elif food == "Gochujang sauce by BRANDLESS" or food == "Gochujang korean hot sauce by WE RUB YOU":
        f = "Gochujang"
    elif food == "Sugar free bbq sauce by G HUGHES SMOKEHOUSE" or food == "bbq":
        f = "Unsweetened BBQ sauce"
    elif food == "ketchup":
        f = "Date sweetened ketchup"
    elif food == "Soup, ready-to-serve, chicken broth":
        f = "Chicken bone broth"
    elif food == "shredded-chicken":
        f = "Simple Shredded Chicken"

    # Baking
    elif food == "Frostings, ready-to-eat, creamy, vanilla":
        f = "Frosting"
    elif food == "protein-frosting":
        f = "Protein Frosting, Vanilla"
    elif food == "protein-frosting-choc":
        f = "Protein Frosting, Chocolate"
    elif food == "Dubai chocolate":
        f = "Dubai chocolate, storebought"
    elif food == "Sugar Free Dubai Chocolate" or food == "dubai-100g" or food == "dubai100g" or food == "dubai":
        f = "Dubai chocolate, homemade"
    elif food == "Nuts, almond paste" or food == "Almond paste":
        f = "Marzipan"
    elif food == "marzipan-sugar":
        f = "Marzipan, homemade, with sugar"
    elif food == "marzipan-sf":
        f = "Marzipan, homemade, sugar free"
    elif food == "quick-nutella":
        f = "Single Serving Quick Nutella"
    elif food == "Spelt, uncooked":
        f = "Spelt flour"
    elif food == "Rye grain":
        f = "Rye flour"
    elif food == "Barley, raw, pearled":
        f = "Barley"
    elif food == "Vanilla instant pudding by SHURFINE":
        f = "Vanilla instant pudding mix"
    elif food == "Allulose plant-based sweetener by Dr. Desai Soap LLC":
        f = "Allulose"
    elif food == "Nabisco, Nabisco Grahams Crackers":
        f = "Graham cracker"
    elif food == "Psyllium husk" or food == "Now, whole psyllium husks by Now Health Group Inc.":
        f = "Psyllium husks, whole"
    elif food == "Millet flour":
        f = "Millet flour"
    elif food == "Leavening agents, baking soda" or food == "Baking soda by The Kroger Co.":
        f = "Baking soda"
    elif food == "Baking powder by The Kroger Co." or food == "Baking powder by SE GROCERS" or food == "Baking powder by Raley's":
        f = "Baking powder"
    elif food == "Leavening agents, active dry, baker's, yeast":
        f = "Dry yeast"
    elif food == "Vital wheat gluten by The King Arthur Flour Company, Inc.":
        f = "Vital wheat gluten"
    elif food == "Wheat flour, whole-grain" or food == "Whole wheat flour by Target Stores" or food == "Whole wheat flour by Raley's" or food == "Whole wheat flour by FAREWAY" or food == "Whole wheat flour by LIDL":
        f = "Whole wheat flour"
    elif food == "Oat flour by Bob's Red Mill Natural Foods, Inc." or food == "Organic oat flour by The Hain Celestial Group, Inc." or food == "Organic oat flour by Hodgson Mill Inc":
        f = "Oat flour"
    elif food == "Cornstarch by Tops Markets, LLC" or food == "Cornstarch by Bob's Red Mill Natural Foods, Inc.":
        f = "Cornstarch"
    elif food == "Organic coconut flour by Bob's Red Mill Natural Foods, Inc." or food == "Coconut flour by BRANDLESS":
        f = "Coconut flour"
    elif food == "Cereals, Dry, Quick Oats, QUAKER" or food == "Cereals, Dry, Quick Oats with Iron, QUAKER" or food == "Quick cook rolled oats by BRANDLESS":
        f = "Quick oats"
    elif food == "Rolled oats by MILLVILLE" or food == "Rolled oats whole grain by Bob's Red Mill Natural Foods, Inc." or food == "Oats by The Quaker Oats Company":
        f = "Rolled oats"
    elif food == "Unsweetened flaked coconut by Raley's" or food == "Unsweetened coconut flakes by Hy-Vee, Inc." or food == "Shredded unsweetened coconut by Bob's Red Mill Natural Foods, Inc." or food == "Unsweetened coconut flakes by Wal-Mart Stores, Inc.":
        f = "Unsweetened coconut flakes"
    elif food == "Applesauce, unsweetened" or food == "Unsweetened applesauce by Iga, Inc.":
        f = "Unsweetened applesauce"
    elif food == "Raw pure honey":
        f = "Honey"
    elif food == "hot-honey":
        f = "Hot honey"
    elif food == "Seeds, dried, chia seeds" or food == "Chia seeds by GREENWISE" or food == "Chia seed by NO BRAND" or food == "Chia seed by Hy-Vee, Inc.":
        f = "Chia seeds"
    elif food == "Seeds, flaxseed" or food == "Whole ground flaxseed meal by Bob's Red Mill Natural Foods, Inc." or food == "Premium whole ground flax seed meal by Bob's Red Mill Natural Foods, Inc.":
        f = "Ground flaxseed"
    elif food == "Sugar substitute, stevia, liquid" or food == "Sugar substitute, liquid, stevia" or food == "Stevia zero calorie liquid sweetener by PURE VIA" or food == "Liquid stevia or monk fruit":
        f = "Liquid monk fruit"
    elif food == "Peanut butter powder by PBFIT" or food == "Powdered peanut butter by PB2":
        f = "Powdered peanut butter"
    elif food == "Premium quality pure almond extract by Morton Bassett Inc." or food == "Pure almond extract by FIRST STREET" or food == "Pure almond extract by Morton Bassett Inc." or food == "Almond extract by Morton Bassett Inc.":
        f = "Almond extract"
    elif food == "Syrups, maple" or food == "Syrup, Canadian, maple":
        f = "Maple syrup"
    elif food == "Sweetener, agave, syrup":
        f = "Agave"
    elif food == "Jellies" or food == "jam" or food == "chia-jam" or food == "Smucker's Raspberry Sugar Free Jam" or food == "Raspberry jelly" or food == "Low Sugar Berry Jam" or food == "Jellies":
        f = "Low sugar berry jam"
    elif food == "sugar-free-syrup" or food == "Syrups, sugar free" or food == "Syrups, sugar free or maple" or food == "Sugar free syrup by Supervalu, Inc." or food == "Sugar free syrup by IHOP AT HOME":
        f = "Sugar free syrup"
    elif food == "Almond flour by RALEY'S" or food == "Almond flour by Supervalu, Inc.":
        f = "Almond flour"
    elif food == "Pitted dates by DELILAH" or food == "Dates, deglet noor" or food == "Pitted dates" or food == "Date":
        f = "Dates"
    elif food == "Fig, dried":
        f = "Dried figs"
    elif food == "Plums, uncooked, dried (prunes)":
        f = "Prunes"
    elif food == "Sweet potato, without salt, flesh, baked in skin, cooked" or food == "Organic sweet potato puree by Stahlbush Island Farms, Inc." or food == "Sweet potato, mashed, canned" or food == "Sweet potato, with salt, flesh, baked in skin, cooked" or food == "sweetpotato":
        f = "Sweet potato puree"
    elif food == "butternut":
        f = "Butternut squash puree"
    elif food == "Pumpkin, without salt, canned" or food == "Pumpkin puree by Whole Foods Market, Inc." or food == "Pumpkin puree, pumpkin by Goya Foods, Inc." or food == "Organic pumpkin puree by Pacific Foods of Oregon, Inc." or food == "pumpkin-puree":
        f = "Pumpkin puree"
    elif food == "Potatoes, raw, flesh and skin":
        f = "Potato"
    elif food == "Pure vanilla extract by CITLALI" or food == "Pure vanilla extract by FIRST STREET":
        f = "Vanilla extract"
    elif food == "Granulated no calorie sweetener with erythritol & monk fruit extract by Topco Associates, Inc.":
        f = "Granulated monk fruit"
    elif food == "Powdered monkfruit sweetener with erythritol by LAKANTO":
        f = "Powdered monk fruit"
    elif food == "Carob flour, or cocoa powder" or food == "Carob flour":
        f = "Carob powder"
    elif food == "No Sugar Added Apple Spread" or food == "applespread":
        f = "No sugar added apple spread"
    elif food == "Sugars, granulated":
        f = "Granulated sugar"
    elif food == "Sugars, brown":
        f = "Brown sugar"
    elif food == "Unsalted butter by FAREWAY" or food == "Butter, without salt":
        f = "Unsalted butter"
    elif food == "Butter, salted":
        f = "Salted butter"
    elif food == "All purpose flour by PIONEER" or food == "Wheat flour, bleached, enriched, all-purpose, white" or food == "Wheat flour, unenriched, all-purpose, white":
        f = "All purpose flour"
    elif food == "duncan hines keto brownie mix":
        f = "Duncan Hines Keto Brownie Mix"
    elif food == "Cocoa, unsweetened, dry powder":
        f = "Cocoa powder"
    elif food == "Sugar, powdered, confectioner's, white" or food == "Sugars, powdered":
        f = "Powdered sugar"
    elif food == "Vegetable oil, palm kernel" or food == "Oil, canola" or food == "Vegetable oil" or food == "Oil, corn and canola":
        f = "Canola oil"
    elif food == "Pumpkin, raw":
        f = "Sugar pumpkin"
    elif food == "Chickpea flour (besan)":
        f = "Chickpea flour"
    elif food == "Coffee, not reconstituted , decaffeinated, instant" or food == "Coffee, instant, decaffeinated, not reconstituted":
        f = "Ground coffee, decaf"
    elif food == "Seeds, hulled, hemp seed":
        f = "Hemp hearts"

    # Dairy & Eggs
    elif food == "Ice cream, vanilla" or food == "Ice creams, vanilla":
        f = "Vanilla ice cream"
    elif food == "Coconut milk, canned, full fat, unsweetened":
        f = "Coconut milk, full fat"
    elif food == "Coconut milk, canned, lowfat, unsweetened":
        f = "Coconut milk, lite"
    elif food == "Sour cream, regular":
        f = "Sour cream"
    elif food == "Cheese, low fat, cream":
        f = "Cream cheese, 1/3 less fat"
    elif food == "Cheese, cream":
        f = "Cream cheese"
    elif food == 'cashew-ricotta':
        f = "Dairy Free Cashew Ricotta Cheese"
    elif food == 'Cheese, Ricotta':
        f = "Ricotta cheese"
    elif food == "labneh-skim":
        f = "Labneh cheese, skim"
    elif food == "Cheese, blue":
        f = "Blue cheese"
    elif food == "Cheese, nonfat, mozzarella":
        f = "Mozzarella cheese, fat free"
    elif food == "Cheese, whole milk, mozzarella" or food == "Shredded mozzarella cheese by ROUNDY'S" or food == "Shredded mozzarella cheese" or food == "Cheese, shredded, part-skim, low moisture, mozzarella" or food == "Cheese, part skim milk, mozzarella" or food == "Cheese, part-skim, low moisture, mozzarella":
        f = "Shredded mozzarella cheese, low moisture part skim"
    elif food == "Unflavored Casein Protein Powder by PROMIX" or food == "Nutricost Casein Unflavored Protein Powder":
        f = "Casein protein powder, unflavored"
    elif food == "Levels Vanilla Casein Protein Powder":
        f = "Whey protein powder, vanilla"
    elif food == "Yogurt, Greek, nonfat milk, plain" or food == "Plain nonfat greek yogurt by Foodtown, Inc." or food == "Yogurt, nonfat, plain, Greek" or food == "Yogurt, plain, nonfat milk" or food == "Yogurt, plain, nonfat milk, Greek" or food == "Plain greek nonfat yogurt by NOSTIMO":
        f = "Plain nonfat greek yogurt"
    elif food == "Yogurt, whole milk, plain, Greek":
        f = "Plain whole milk greek yogurt"
    elif food == "Chobani 20g Protein, Vanilla Yogurt":
        f = "Vanilla Protein Greek Yogurt"
    elif food == "Buttermilk, low fat (1%)" or food == "Buttermilk, fat free (skim)":
        f = "Buttermilk"
    elif food == "Milk, dried, buttermilk":
        f = "Buttermilk powder"
    elif food == "Fat free ultra-filtered milk by FAIRLIFE" or food == "Fairlife Skim Milk":
        f = "Fairlife skim milk"
    elif food == "Milk, with added vitamin A, evaporated, canned":
        f = "Evaporated milk"
    elif food == "Milk, fat free (skim), evaporated":
        f = "Fat free evaporated milk"
    elif food == "Eggs, egg whole, Large, Grade A" or food == "Large egg" or food == "Large Egg":
        f = "Egg"
    elif food == "100% liquid egg whites by KROGER":
        f = "Liquid egg whites"
    elif food == "Beverages, Protein powder whey based" or food == "Unflavored 100% whey protein isolate protein powder, unflavored by ISOPURE" or food == "Unflavored 100% whey protein isolate protein powder" or food == "Nutricost Whey Unflavored Protein Powder":
        f = "Whey protein powder, unflavored"
    elif food == "Levels Vanilla Whey Protein Powder":
        f = "Whey protein powder, vanilla"
    elif food == "Cottage cheese, 1% fat, Friendship Dairies" or food == "Cheese, large or small curd, dry, uncreamed, nonfat, cottage" or food == "Nonfat cottage cheese by FRESH & EASY" or food == "Nonfat cottage cheese by HP Hood LLC" or food == "Nonfat cottage cheese by Dean Foods Company":
        f = "Nonfat cottage cheese"
    elif food == "Cheese, grated, parmesan" or food == "Kraft Grated Parmesan Cheese" or food == "Grated parmesan cheese by POPE" or food == "Cheese, grated, parmesan":
        f = "Grated parmesan cheese"
    elif food == "Unsweetened original almond milk by Supervalu, Inc." or food == "Almond milk, unsweetened":
        f = "Unsweetened almond milk"
    elif food == "Unsweetened vanilla almondmilk by ORGAIN" or food == "Unsweetened vanilla almond milk, unsweetened vanilla by Danone US, LLC" or food == "Unsweetened vanilla almondmilk by Target Stores" or food == "Unsweetened vanilla almond milk, unsweetened vanilla by Supervalu, Inc." or food == "Unsweetened vanilla almondmilk by Hy-Vee, Inc.":
        f = "Unsweetened vanilla almond milk"
    elif food == "Cheese, feta":
        f = "Feta cheese"
    elif food == "Egg, fresh, raw, white" or food == "Eggs, egg white, Large, Grade A":
        f = "Egg whites"
    elif food == "Eggs, egg yolk, Large, Grade A" or food == "Egg, fresh, raw, yolk":
        f = "Egg yolk"
    elif food == "Cheese, cheddar" or food == "Shredded mild cheddar cheese by BORDEN" or food == "Shredded cheese mexican blend by HOMELAND" or food == "Cheese, Mexican blend":
        f = "Shredded cheddar cheese"
    elif food == "Cheese, Cheddar, nonfat or fat free":
        f = "Cheddar cheese, fat free"
    elif food == "Cheese, soft type, goat":
        f = "Goat cheese"
    elif food == "Milk, with added vitamin A and vitamin D (fat free or skim), fluid, nonfat" or food == "Milk, fat free (skim)":
        f = "Skim milk"

    # Fresh produce
    elif food == "Broccoli raab, raw":
        f = "Broccoli rabe"
    elif food == "Endive, raw":
        f = "Escarole"
    elif food == "Tangerines, raw, (mandarin oranges)":
        f = "Mandarin orange"
    elif food == "Corn, raw, yellow, sweet":
        f = "Corn on the cob"
    elif food == "Cabbage, raw" or food == "Cabbage, raw, green":
        f = "Cabbage"
    elif food == "Sweet potato, without skin, boiled, cooked":
        f = "Cooked sweet potato"
    elif food == "Bananas, raw, overripe" or food == "Bananas, raw, ripe and slightly ripe" or food == "Bananas, raw":
        f = "Banana, overripe"
    elif food == "Onions, raw" or food == "Onions, raw, red" or food == "Onions, raw, yellow" or food == "Onions, raw, white":
        f = "Onion"
    elif food == "Apples, with skin, gala, raw" or food == "Apples, with skin, raw":
        f = "Apple, gala"
    elif food == "Carrots, raw, baby":
        f = "Baby carrots"
    elif food == "Avocados, California, raw":
        f = "Avocado"
    elif food == "Tomatoes, raw":
        f = "Tomato"
    elif food == "Tomatoes, sun-dried":
        f = "Sun dried tomatoes"
    elif food == "Tomatoes, raw, grape":
        f = "Cherry tomatoes"
    elif food == "Peppers, raw, red, sweet" or food == "Pepper, raw, red, sweet" or food == "Peppers, raw, green, sweet":
        f = "Bell pepper"
    elif food == "Sweet potato, unprepared, raw" or food == "Sweet potato, washed":
        f = "Sweet potato"
    elif food == "Strawberries, raw":
        f = "Strawberries"
    elif food == "Ripe plantain, raw" or food == "Plantains, raw, yellow":
        f = "Plantain, yellow"
    elif food == "Plantains, raw, green":
        f = "Plantain, green"
    elif food == "Carrots, raw":
        f = "Carrots"
    elif food == "Coleslaw mix by Bread & Circus Inc.":
        f = "Coleslaw mix"
    elif food == "Cucumber, raw" or food == "Cucumber, raw, with peel":
        f = "Cucumber"
    elif food == "Lettuce, raw" or food == "Lettuce, raw, cos or romaine" or food == "Romaine lettuce, raw":
        f = "Romaine lettuce"
    elif food == "Squash, raw, acorn, winter":
        f = "Acorn squash"
    elif food == "Mushrooms, raw, white" or food == "White Mushrooms":
        f = "White mushrooms"
    elif food == "Fruit peels apple banana by Target Stores":
        f = "Banana peel"
    elif food == "Ginger root, raw" or food == "Minced ginger by McCormick & Company, Inc.":
        f = "Ginger, fresh"
    elif food == "Cranberries, raw":
        f = "Cranberries"
    elif food == "Eggplant, raw":
        f = "Eggplant"
    elif food == "Fresh dill weed, fresh" or food == "Dill weed, fresh":
        f = "Dill, fresh"
    elif food == "Squash, raw, butternut, winter":
        f = "Butternut squash"
    elif food == "Squash, raw, includes skin, zucchini, summer":
        f = "Zucchini"
    elif food == "Squash, raw, spaghetti, winter":
        f = "Spaghetti squash"
    elif food == "Spinach, raw, or arugula" or food == "Spinach, raw":
        f = "Spinach, fresh"
    elif food == "Kale, raw":
        f = "Kale"
    elif food == "Garlic, raw":
        f = "Garlic, fresh"
    elif food == "Pineapple, all varieties, raw":
        f = "Pineapple"
    elif food == "Mangos, raw":
        f = "Mango"
    elif food == "Beets, raw":
        f = "Beets"
    elif food == "Blackberries, raw":
        f = "Blackberries"
    elif food == "Summer squash, raw, yellow":
        f = "Yellow squash"
    elif food == "Red jalapeno salsa by The Kroger Co.":
        f = "Red jalapenos"
    elif food == "Cilantro, raw":
        f = "Cilantro, fresh"
    elif food == "Kiwi fruit" or food == "Kiwifruit, raw, green":
        f = "Kiwi"
    elif food == "Celery, raw":
        f = "Celery"

    # Empanadas / pierogi
    elif food == "af-empanada-dough":
        f = "Empanada/Pierogi dough"

    # Frozen produce
    elif food == "Corn, unprepared, kernels cut off cob, frozen, yellow, sweet":
        f = "Frozen corn"
    elif food == "Squash, unprepared, frozen, butternut, winter":
        f = "Frozen butternut squash, thawed"
    elif food == "Blueberries, frozen, wild" or food == "Blueberries, unsweetened, frozen":
        f = "Frozen blueberries"
    elif food == "Raspberries, frozen" or food == "Raspberries, unsweetened, red, frozen":
        f = "Frozen raspberries"
    elif food == "Spinach, unprepared, chopped or leaf, frozen":
        f = "Frozen spinach, thawed"
    elif food == "Blackberries, unsweetened, frozen":
        f = "Frozen blackberries"
    elif food == "Strawberries, unsweetened, frozen":
        f = "Frozen strawberries"
    elif food == "Broccoli, unprepared, chopped, frozen" or food == "Frozen broccoli":
        f = "Frozen broccoli, thawed"
    elif food == "Fruit mixture, frozen":
        f = "Frozen fruit"
    elif food == "Brussels sprouts, unprepared, frozen":
        f = "Frozen brussel sprouts, thawed"
    elif food == "Cauliflower, unprepared, frozen":
        f = "Frozen cauliflower, thawed"
    elif food == "Kale, unprepared, frozen":
        f = "Frozen kale, thawed"
    elif food == "Vegetables, unprepared, frozen, mixed":
        f = "Vegetables"

    # Canned & jarred
    elif food == "Ginger root, pickled":
        f = "Pickled ginger"
    elif food == "cheese-sauce":
        f = "Gooey cheese sauce"
    elif food == "sauce":
        f = "Simple pasta sauce"
    elif food == "Fish, drained solids, canned, pink, salmon":
        f = "Canned salmon"
    elif food == "Tomato products, sauce, canned" or food == "Hunt's, pasta sauce, no added sugar, hunt's, pasta sauce, no added sugar by Conagra Brands, Inc.":
        f = "Unsweetened tomato sauce"
    elif food == "Artichoke hearts by MATIZ" or food == "Canned artichokes":
        f = "Artichokes"
    elif food == "Roasted red peppers by GALIL":
        f = "Roasted red peppers"
    elif food == "Diced tomatoes, canned" or food == "Tomatoes, diced, ripe, red, canned" or food == "Tomatoes, canned, diced" or food == "Fire roasted diced tomatoes by Raley's" or food == "Canned diced tomatoes":
        f = "Diced tomatoes"
    elif food == "Tomatoes, canned, crushed" or food == "Canned crushed tomatoes":
        f = "Crushed tomatoes"
    elif food == "Tomato products, without salt added, paste, canned" or food == "Tomato paste" or food == "Tomato paste by FIESTA" or food == "Tomato paste by REDPACK" or food == "Tomato products, paste, canned" or food == "Canned tomato paste" or food == "Tomato paste, canned" or food == "Tomato paste by TAT":
        f = "Tomato paste, canned"
    elif food == "Grape leaves, raw":
        f = "Grape leaves"
    elif food == "Clams, canned" or food == "Minced clams in juice by Bumble Bee Foods, LLC" or food == "Canned clams":
        f = "Clams"
    elif food == "Clam juice by Casa Imports Inc.":
        f = "Clam juice"
    elif food == "Tuna, canned in water" or food == "Fish, drained solids, canned in water, light, tuna" or food == "Canned tuna, in water":
        f = "Tuna, in water"
    elif food == "Pickles, sour, cucumber":
        f = "Pickles"
    elif food == "Capers by RALEY'S" or food == "Capers, canned":
        f = "Capers"
    elif food == "Sardines in water" or food == "Sardines, canned in water":
        f = "Sardines, in water"
    elif food == "No salt added diced tomatoes by VINE RIPE":
        f = "Diced tomatoes, unsalted"
    elif food == "Peppers, canned, green, chili" or food == "Diced green chiles by Raley's" or food == "Diced green chiles by HATCH" or food == "Diced green chile by Iga, Inc." or food == "Diced green chilies by SPARTAN" or food == "Diced green chilies by ELRIO":
        f = "Diced green chiles"
    elif food == "Chipotle peppers in adobo sauce by Goya Foods, Inc.":
        f = "Chipotle peppers in adobo sauce"
    elif food == "Kalamata olives, pitted":
        f = "Kalamata olives"
    elif food == "Olives, green, canned or bottled, pickled":
        f = "Olives"
    elif food == "Anchovy, canned":
        f = "Anchovies, canned"
    elif food == "Yeast extract by MARMITE":
        f = "Marmite"
    elif food == "Sauerkraut, solids and liquids, canned" or food == "Raw sauerkraut by Bader Publishing":
        f = "Sauerkraut"

    # Nuts, chocolate, dried fruit
    elif food == "Pretzels, hard, flavored":
        f = "Pretzels"
    elif food == "allulose-choc":
        f = "Allulose chocolate bar"
    elif food == "Chocolate, 45- 59% cacao solids, dark":
        f = "50% chocolate"
    elif food == "Almond butter by JUSTIN'S" or food == "Almond butter, lower sodium" or food == "Nuts, without salt added, plain, almond butter":
        f = "Almond butter"
    elif food == "pb" or food == "Peanut Butter, smooth" or food == "Natural peanut butter by HAMPTON FARMS" or food == "Organic natural chunky peanut butter by The Federated Group, Inc." or food == "Natural peanut butter by Kohl Corporation":
        f = "Natural peanut butter"
    elif food == "Tahini by BRANDLESS":
        f = "Tahini"
    elif food == "Nuts, almonds" or food == "Nuts, with salt added, dry roasted, almonds" or food == "Nuts, without salt added, dry roasted, almonds":
        f = "Almonds"
    elif food == "Chopped peanuts by Raley's" or food == "Peanuts, raw, all types" or food == "Peanuts, unsalted, roasted" or food == "Peanuts, unsalted, dry roasted" or food == "Peanuts, lightly salted, dry roasted" or food == "Peanuts, salted, dry roasted" or food == "Peanuts, without salt, dry-roasted, all types" or food == "Peanuts, dry roasted, unsalted":
        f = "Peanuts"
    elif food == "Dark chocolate baking chips, dark chocolate by LILYS" or food == "Hersheys Zero Sugar Chocolate Chips":
        f = "Sugar free chocolate chips"
    elif food == "Candies, semisweet chocolate" or food == "Semisweet chocolate mini chips by Harris-Teeter Inc." or food == "Chocolate chips, semisweet by Giant Eagle, Inc.":
        f = "Semi-sweet chocolate chips"
    elif food == "Candies, white chocolate" or food == "White chocolate candy":
        f = "White chocolate chips"
    elif food == "white-choc":
        f = "Tangy white chocolate"
    elif food == "choc-free":
        f = "Chocolate free chocolate"
    elif food == "90% cocoa dark chocolate by Lindt" or food == "90% cocoa dark chocolate by Lindt & Sprungli (Schweiz) AG":
        f = "90% chocolate"
    elif food == "Raw cashews" or food == "Nuts, raw, cashew nuts" or food == "Nuts, with salt added, dry roasted, cashew nuts":
        f = "Cashews"
    elif food == "Raisins, seedless, dark" or food == "Raisins, seedless, golden":
        f = "Raisins"
    elif food == str("85% dark chocolate by Sinless Raw Food Inc"):
        f = "85% chocolate"
    elif food == str("Bakers Premium 70% Dark Chocolate Baking Bar"):
        f = "70% chocolate"
    elif food == "Chopped Walnuts, Great Value" or food == "Walnut chopped pieces" or food == "Chopped walnuts by DIAMOND" or food == "Nuts, english, walnuts":
        f = "Walnuts"
    elif food == "Walnut butter by Lyle Style":
        f = "Walnut butter"
    elif food == "Nuts, dried, pine nuts":
        f = "Pine nuts"
    elif food == "Nuts, pecans, or peanuts" or food == "Nuts, pecans":
        f = "Pecans"
    elif food == "Seeds, with salt added, dry roasted, sunflower seed kernels" or food == "Seeds, dried, sunflower seed kernels":
        f = "Sunflower kernels"
    elif food == "Seeds, with salt added, sunflower seed butter":
        f = "Sunflower seed butter"
    elif food == "Nuts, raw, pistachio nuts" or food == "Nuts, with salt added, dry roasted, pistachio nuts" or food == "Dry roasted pistachios" or food == "Nuts, raw, pistachios":
        f = "Pistachios"
    elif food == "Raw hazelnuts" or food == "Nuts, hazelnuts or filberts":
        f = "Hazelnuts"
    elif food == "Roasted pumpkin seed butter, roasted by 88 ACRES" or food == "Pumpkin seed butter by Wilderness Poets LLC":
        f = "Pumpkin seed butter"
    elif food == "Baking chocolate, squares, unsweetened" or food == "100%" or food == "choc" or food == "100" or food == "Baking chocolate, liquid, unsweetened":
        f = "100% chocolate"
    elif food == "monk-fruit-choc":
        f = "Monk fruit chocolate chunks"
    elif food == "Seeds, dried, pumpkin and squash seed kernels" or food == "Seeds, without salt, roasted, pumpkin and squash seed kernels":
        f = "Pumpkin seeds"
    elif food == "cranberry-sauce":
        f = "Sugar free cranberry sauce"

    # Carbs
    elif food == "sourdough-starter":
        f = "Sourdough starter"
    elif food == "cc-flatbread-white-psyllium":
        f = "Cottage cheese flatbread"
    elif food == "tortillas" or food == "Whole wheat protein tortillas by La Tortilla Factory Inc":
        f = "Whole wheat tortilla"
    elif food == "Bread, whole wheat" or food == "ww-bread":
        f = "Whole wheat bread"
    elif food == "ww-bagles":
        f = "Whole wheat bagel"
    elif food == "baguette":
        f = "Whole wheat baguette"
    elif food == "Rice, raw, long-grain, brown":
        f = "Brown rice"
    elif food == "Wild rice, raw":
        f = "Wild rice"
    elif food == "Farro, raw":
        f = "Farro"
    elif food == "Quinoa, uncooked":
        f = "Quinoa"
    elif food == "Pasta, dry, whole-wheat":
        f = "Whole wheat pasta"
    elif food == "Pasta, unenriched, dry":
        f = "Pasta"
    elif food == "Couscous, dry":
        f = "Couscous"
    elif food == "Panko, crispy breadcrumbs by George DeLallo Co., Inc.":
        f = "Panko breadcrumbs"
    elif food == "Tortilla, whole wheat":
        f = "Whole wheat tortilla"
    elif food == "Chickpeas pasta by Banza LLC" or food == "Chickpeas pasta, penne by Banza LLC":
        f = "Chickpea pasta"
    elif food == "Organic red lentil pasta by TOLERANT":
        f = "Red lentil pasta"
    elif food == "Cornmeal, yellow, whole-grain":
        f = "Cornmeal"
    elif food == "cracker" or food == "cracker-choc":
        f = "Gluten free graham crackers"
    elif food == "pie-crust-choc":
        f = "Healthier Graham Cracker Pie Crust, chocolate"
    elif food == "pie-crust":
        f = "Healthier Graham Cracker Pie Crust"

    # Meat & fish
    elif food == "Ham, cooked, smoked, honey":
        f = "Ham, cooked"
    elif food == "Beef, raw, liver, variety meats and by-products":
        f = "Beef liver"
    elif food == "Chicken, raw, meat and skin, thigh, broilers or fryers":
        f = "Chicken thighs, bone in, skin on"
    elif food == "Chicken, raw, meat only, boneless, skinless, breast, broiler or fryers":
        f = "Boneless skinless chicken breast"
    elif food == "Chicken, raw, meat only, thigh, dark meat, broilers or fryers" or food == "Boneless skinless chicken thigh filets by PERDUE":
        f = "Boneless skinless chicken thighs"
    elif food == "Chicken, raw, meat and skin, wing, broilers or fryers":
        f = "Chicken wings"
    elif food == "Chicken, raw, ground":
        f = "Ground chicken thighs"
    elif food == str("Turkey, raw, 7% fat, 93% lean, ground"):
        f = "Ground turkey, 93/7"
    elif food == "Tilapia fillet" or food == "Fish, raw, tilapia":
        f = "Tilapia"
    elif food == "Fish, raw, pink, salmon" or food == "Salmon fillet by WILD ALASKAN SOCKEYE":
        f = "Salmon"
    elif food == "Smoked Salmon":
        f = "Smoked salmon"
    elif food == "Crustaceans, raw (may contain additives to retain moisture), mixed species, shrimp" or food == "Peeled & deveined raw shrimp by PACIFIC SURF":
        f = "Frozen raw shrimp, peeled and deveined"
    elif food == "Beef, raw, select, trimmed to 1/8 fat, separable lean only, steak, top sirloin":
        f = "Beef top sirloin"
    elif food == "Beef, raw, 93% lean meat / 7% fat, ground":
        f = "Ground beef, 93/7"
    elif food == "Pork, raw, separable lean only, tenderloin, loin, fresh":
        f = "Pork tenderloin"
    elif food == "Shredded rotisserie chicken, rotisserie by Target Stores":
        f = "Shredded rotisserie chicken"
    elif food == "Extra firm tofu" or food == "Tofu, prepared with calcium sulfate, regular, raw":
        f = "Tofu, firm"

    return f

def main(path = ""):


    os.system('cls')

    if path == "":
        # path to csv files
        path = r"C:\Users\mets1\Documents\website\python\testing\*-ing.csv"
        # path = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\python\testing\*-ing.csv"
        print("empty path")

    # loop through all the files
    changed = 0
    for fname in glob.glob(path):

        with open(fname, 'r+', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

            i = 0
            for row in spamreader:
                row[0] = ingredients(row[0])

                temp = fname[:-4] + "-temp.csv"

                if len(row) == 4 and i != 0:
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
