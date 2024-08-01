import pandas as pd
import os
import glob
import csv

def ingredients(food):
    # Misc
    if food == "Water, generic, bottled":
        return str("Water")

    # Beans
    elif food == "Chickpeas (garbanzo beans, bengal gram), rinsed in tap water, drained, canned, mature seeds" or food == "Chickpeas (garbanzo beans, bengal gram), drained solids, canned, mature seeds":
        return str("Chickpeas, drained and rinsed")
    elif food == "Beans, drained solids, canned, pinto" or food == "Beans, solids and liquids, canned, mature seeds, pinto":
        return str("Pinto beans, drained and rinsed")
    elif food == "Beans, rinsed in tap water, drained solids, canned, mature seeds, black" or food == "Beans, canned, mature seeds, all types, black" or food == "Beans, drained solids, canned, black":
        return str("Black beans, drained and rinsed")
    elif food == "Beans, drained solids, canned, mature seeds, red, kidney" or food == "Beans, canned, mature seeds, all types, kidney":
        return str("Kidney beans, drained and rinsed")
    elif food == "Beans, raw, black":
        return str("Dried beans")
    elif food == "Split red lentils by ROYAL" or food == "Split red lentils by CEDAR PHOENICIA" or food == "Red lentils":
        return str("Red split lentils")
    
    # Spices
    elif food == "Salt, table" or food == "Table salt by FIRST STREET" or food == "Table salt by Morton Salt, Inc." or food == "Salt by Morton Salt, Inc." or food == "Table salt by Cardenas Markets":
        return str("Salt")
    elif food == "Spices, garlic powder" or food == "Garlic powder by EL SABOR" or food == "Garlic powder by Target Stores" or food == "Garlic powder by STONEMILL":
        return str("Garlic powder")
    elif food == "Spices, onion powder" or food == "Onion powder by ADAMS" or food == "Onion powder by STONEMILL" or food == "Onion powder by Adams Extract Co." or food == "Onion powder by Target Stores":
        return str("Onion powder")
    elif food == "Spices, ground, cinnamon" or food == "Cinnamon ground by ROUNDY'S":
        return str("Cinnamon")
    elif food == "Spices, ground, ginger" or food == "Ginger ground organic spices by PRIDE OF INDIA" or food == "Organic ground ginger by MEMBER'S MARK":
        return str("Ginger, ground")
    elif food == "Spices, paprika" or food == "Paprika by ROUNDY'S":
        return str("Paprika")
    elif food == "Spices, chili powder" or food == "Chili powder by ADAMS":
        return str("Chili powder")
    elif food == "Spices, black, pepper" or food == "Ground black pepper by MEMBER'S MARK" or food == "Ground black pepper by Grace Kennedy Co. Ltd":
        return str("Black pepper, ground")
    elif food == "Spices, ground, nutmeg" or food == "Ground nutmeg by Rose Spice, Inc.":
        return str("Nutmeg, ground")
    elif food == "Spices, ground, cloves":
        return str("Cloves, ground")
    elif food == "Lemon pepper by LA CRIOLLA" or food == "Lemon pepper by La Criolla Inc." or food == "Lemon pepper by SHURFINE":
        return str("Lemon pepper")
    elif food == "Cilantro lightly dried by MCCORMICK & COMPANY, INC.":
        return str("Cilantro, dried")
    elif food == "Cumin ground by ROUNDY'S" or food == "Ground cumin by STONEMILL":
        return str("Cumin, ground")
    elif food == "Spices, dried, oregano":
        return str("Oregano, dried")
    elif food == "Spices, dried, thyme":
        return str("Thyme, dried")
    elif food == "Spices, dried, basil" or food == "Lightly dried basil by Eyebobs, LLC " or food == "Basil lightly dried by GOURMET GARDEN" or food == "Lightly dried basil by Eyebobs, LLC" or food == "Lightly dried basil by Eyebobs, LLC":
        return str("Basil, dried")
    elif food == "Spices, ground, allspice":
        return str("Allspice, ground")
    elif food == "Spices, red or cayenne, pepper" or food == "Cayenne pepper by MEMBER'S MARK":
        return str("Cayenne pepper")
    elif food == "Spices, celery seed":
        return str("Celery seed")
    elif food == "Old bay, seasoning by Baltimore Spice Co":
        return str("Old Bay")
    elif food == "Nutritional yeast seasoning by BRAGG" or food == "Nutritional yeast superfoods by FOODS ALIVE":
        return str("Nutritional yeast")
    elif food == "Chives, freeze-dried":
        return str("Chives, dried")
    elif food == "Italian seasoning by Raley's" or food == "Italian seasoning by ROUNDY'S":
        return str("Italian seasoning")
    elif food == "Everything but the bagel seasoning by Big Y Foods, Inc." or food == "Seasoning everything bagel by Whole Foods Market, Inc.":
        return str("Everything bagel seasoning")
    elif food == "Extra hot red pepper flakes by DOC MEYERS BRAND":
        return str("Red pepper flakes")
    elif food == "Spices, dried, parsley":
        return str("Parsley, dried")
    elif food == "Powdered chicken, bouillon by Goya Foods, Inc." or food == "Powdered bouillon by Goya Foods, Inc.":
        return str("Chicken bouillon powder")
    elif food == "Spices, ground, turmeric":
        return str("Turmeric, ground")
    
    
    # Oil, vinegar, other liquids
    elif food == "Extra virgin olive oil by OLIO" or food == "Extra virgin olive oil by QO" or food == "Extra virgin olive oil by GAEA" or food == "Extra virgin olive oil by BRAGG":
        return str("Extra virgin olive oil")
    elif food == "Extra virgin coconut oil by KELAPO" or food == "Oil, coconut" or food == "Extra virgin coconut oil by VITA BRAND":
        return str("Extra virgin coconut oil")
    elif food == "Oil, sesame":
        return str("Sesame oil")
    elif food == "White distilled vinegar by FAREWAY" or food == "Distilled white vinegar by Raley's" or food == "White wine vinegar by CIRIO" or food == "Distilled white vinegar by HYTOR" or food == "Distilled white vinegra by OLIO":
        return str("White vinegar")
    elif food == "Apple cider vinegar by BRAGG":
        return str("Apple cider vinegar")
    elif food == "Italian dressing, fat free" or food == "Salad dressing, fat-free, italian dressing":
        return str("Fat free Italian dressing")
    elif food == "Lime juice, raw" or food == "Lime juice from concentrate by Safeway, Inc." or food == "Lime juice from concentrate by ITALIAN GARDEN" or food == "Lime juice from concentrate by Harris-Teeter Inc." or food == "Lime juice, freshly squeezed, 100%":
        return str("Lime juice")
    elif food == "Vinegar, balsamic" or food == "Balsamic vinegar of modena" or food == "Balsamic vinegar by ELSA":
        return str("Balsamic vinegar")
    elif food == "Hot sauce by LOUISIANA" or food == "Hot sauce, louisiana style by La Preferida In" or food == "Hot sauce, louisiana style by La Preferida Inc" or food == "Sauce by LOUISIANA":
        return str("Hot sauce")
    elif food == "Minced garlic by STONEMILL" or food == "Minced garlic by MEMBER'S MARK" or food == "Minced garlic by EL SABOR":
        return str("Minced garlic")
    elif food == "Dijon mustard by KOOPS'" or food == "Dijon mustard by BRANDLESS" or food == "Dijon mustard by Raley's" or food == "Dijon mustard by SPARTAN":
        return str("Dijon mustard")
    elif food == "White dry cooking wine by CONCHITA":
        return str("White cooking wine")
    elif food == "Lemon juice from concentrate, REAL LEMON, bottled" or food == "Lemon juice from concentrate, canned or bottled" or food == "Lemon juice from concentrate by GOLDEN SUN" or food == "Lemon juice from concentrate, CONCORD, bottled":
        return str("Lemon juice")
    elif food == "Soy sauce made from soy and wheat (shoyu), low sodium" or food == "Low Sodium Soy Sauce by First Street":
        return str("Low sodium soy sauce")
    elif food == "Low sodium chicken broth by Glencourt Inc.":
        return str("Low sodium chicken broth")
    elif food == "Low sodium vegetable broth by The Hain Celestial Group, Inc.":
        return str("Low sodium vegetable broth")
    elif food == "Gochujang sauce by BRANDLESS" or food == "Gochujang korean hot sauce by WE RUB YOU":
        return str("Gochujang")
    elif food == "Sugar free bbq sauce by G HUGHES SMOKEHOUSE":
        return str("Unsweetened BBQ sauce")
    
    # Baking
    elif food == "Leavening agents, baking soda" or food == "Baking soda by The Kroger Co.":
        return str("Baking soda")
    elif food == "Baking powder by The Kroger Co." or food == "Baking powder by SE GROCERS" or food == "Baking powder by Raley's":
        return str("Baking powder")
    elif food == "Leavening agents, active dry, baker's, yeast":
        return str("Dry Yeast")
    elif food == "Vital wheat gluten by The King Arthur Flour Company, Inc.":
        return str("Vital wheat gluten")
    elif food == "Whole wheat flour by Target Stores" or food == "Whole wheat flour by FAREWAY" or food == "Whole wheat flour by LIDL":
        return str("Whole wheat flour")
    elif food == "Oat flour by Bob's Red Mill Natural Foods, Inc." or food == "Organic oat flour by The Hain Celestial Group, Inc." or food == "Organic oat flour by Hodgson Mill Inc":
        return str("Oat flour")
    elif food == "Cornstarch by Tops Markets, LLC" or food == "Cornstarch by Bob's Red Mill Natural Foods, Inc.":
        return str("Cornstarch")
    elif food == "Organic coconut flour by Bob's Red Mill Natural Foods, Inc.":
        return str("Coconut flour")    
    elif food == "Cereals, Dry, Quick Oats, QUAKER" or food == "Cereals, Dry, Quick Oats with Iron, QUAKER" or food == "Quick cook rolled oats by BRANDLESS":
        return str("Quick oats")
    elif food == "Rolled oats whole grain by Bob's Red Mill Natural Foods, Inc.":
        return str("Rolled oats")
    elif food == "Unsweetened coconut flakes by Hy-Vee, Inc." or food == "Shredded unsweetened coconut by Bob's Red Mill Natural Foods, Inc.":
        return str("Unsweetened coconut flakes")
    elif food == "Applesauce, unsweetened" or food == "Unsweetened applesauce by Iga, Inc.":
        return str("Unsweetened applesauce")
    elif food == "Raw pure honey":
        return str("Honey")
    elif food == "Chia seeds by GREENWISE" or food == "Chia seed by NO BRAND":
        return str("Chia seeds")
    elif food == "Whole ground flaxseed meal by Bob's Red Mill Natural Foods, Inc.":
        return str("Ground flaxseed")
    elif food == "Sugar substitute, liquid, stevia" or food == "Stevia zero calorie liquid sweetener by PURE VIA":
        return str("Liquid stevia or monk fruit")
    elif food == "Peanut butter powder by PBFIT" or food == "Powdered peanut butter by PB2":
        return str("Powdered peanut butter")
    elif food == "Pure almond extract by FIRST STREET" or food == "Pure almond extract by Morton Bassett Inc." or food == "Almond extract by Morton Bassett Inc.":
        return str("Almond extract")
    elif food == "Pumpkin puree by Whole Foods Market, Inc." or food == "Pumpkin puree, pumpkin by Goya Foods, Inc." or food == "Organic pumpkin puree by Pacific Foods of Oregon, Inc.":
        return str("Pumpkin puree")
    elif food == "Syrups, maple" or food == "Syrup, Canadian, maple":
        return str("Maple syrup")
    elif food == "Smucker's Raspberry Sugar Free Jam" or food == "Raspberry jelly" or food == "Low Sugar Berry Jam":
        return str("Low sugar berry jam")
    elif food == "Syrups, sugar free" or food == "Syrups, sugar free or maple" or food == "Sugar free syrup by Supervalu, Inc." or food == "Sugar free syrup by IHOP AT HOME":
        return str("Sugar free syrup")
    elif food == "Almond flour by RALEY'S":
        return str("Almond flour")
    elif food == "Pitted dates by DELILAH" or food == "Dates, deglet noor" or food == "Pitted dates":
        return str("Dates")
    elif food == "Organic sweet potato puree by Stahlbush Island Farms, Inc." or food == "Sweet potato, mashed, canned" or food == "Sweet potato, with salt, flesh, baked in skin, cooked":
        return str("Sweet potato puree")
    elif food == "Pure vanilla extract by CITLALI" or food == "Pure vanilla extract by FIRST STREET":
        return str("Vanilla extract")
    elif food == "Granulated no calorie sweetener with erythritol & monk fruit extract by Topco Associates, Inc.":
        return str("Granulated monk fruit")
    elif food == "Powdered monkfruit sweetener with erythritol by LAKANTO":
        return str("Powdered monk fruit")
    elif food == "Carob flour, or cocoa powder" or food == "Carob flour":
        return str("Carob powder")
    elif food == "No Sugar Added Apple Spread" or food == "applespread":
        return str("No sugar added apple spread")
    elif food == "Sugars, granulated":
        return str("Granulated sugar")
    elif food == "Unsalted butter by FAREWAY":
        return str("Unsalted butter")
    elif food == "All purpose flour by PIONEER":
        return str("All purpose flour")
    elif food == "duncan hines keto brownie mix":
        return str("Duncan Hines Keto Brownie Mix")
    elif food == "Cocoa, unsweetened, dry powder":
        return str("Cocoa powder")
    elif food == "Sugar, powdered, confectioner's, white":
        return str("Powdered sugar")
    elif food == "Vegetable oil, palm kernel" or food == "Oil, canola" or food == "Vegetable oil" or food == "Oil, corn and canola":
        return str("Canola oil")
    
    # Dairy & Eggs
    elif food == "Shredded mozzarella cheese by ROUNDY'S" or food == "Shredded mozzarella cheese" or food == "Cheese, shredded, part-skim, low moisture, mozzarella" or food == "Cheese, part skim milk, mozzarella" or food == "Cheese, part-skim, low moisture, mozzarella":
        return str("Shredded mozzarella cheese, low moisture part skim")
    elif food == "Unflavored Casein Protein Powder by PROMIX":
        return str("Casein protein powder, unflavored")
    elif food == "Plain nonfat greek yogurt by Foodtown, Inc." or food == "Yogurt, nonfat, plain, Greek" or food == "Yogurt, plain, nonfat milk" or food == "Yogurt, plain, nonfat milk, Greek" or food == "Plain greek nonfat yogurt by NOSTIMO":
        return str("Plain nonfat greek yogurt")
    elif food == "Buttermilk, low fat (1%)":
        return str("Buttermilk")
    elif food == "Eggs, egg whole, Large, Grade A" or food == "Large egg" or food == "Large Egg":
        return str("Egg")
    elif food == "100% liquid egg whites by KROGER":
        return str("Liquid egg whites")
    elif food == "Unflavored 100% whey protein isolate protein powder, unflavored by ISOPURE" or food == "Unflavored 100% whey protein isolate protein powder":
        return str("Whey protein powder, unflavored")
    elif food == "Nonfat cottage cheese by FRESH & EASY" or food == "Nonfat cottage cheese by HP Hood LLC" or food == "Nonfat cottage cheese by Dean Foods Company":
        return str("Nonfat cottage cheese")
    elif food == "Kraft Grated Parmesan Cheese" or food == "Grated parmesan cheese by POPE" or food == "Cheese, grated, parmesan":
        return str("Grated parmesan cheese")
    elif food == "Unsweetened original almond milk by Supervalu, Inc." or food == "Almond milk, unsweetened":
        return str("Unsweetened almond milk")
    elif food == "Unsweetened vanilla almond milk, unsweetened vanilla by Danone US, LLC" or food == "Unsweetened vanilla almondmilk by Target Stores" or food == "Unsweetened vanilla almond milk, unsweetened vanilla by Supervalu, Inc." or food == "Unsweetened vanilla almondmilk by Hy-Vee, Inc.":
        return str("Unsweetened vanilla almond milk")
    elif food == "Cheese, feta":
        return str("Feta cheese")   
    elif food == "Egg, fresh, raw, white":
        return str("Egg whites")
    elif food == "Eggs, egg yolk, Large, Grade A":
        return str("Egg yolk")
    elif food == "Shredded mild cheddar cheese by BORDEN":
        return str("Shredded cheddar cheese")
    elif food == "Milk, fat free (skim)":
        return str("Skim milk")

    # Fresh produce
    elif food == "Cabbage, raw" or food == "Cabbage, raw, green":
        return str("Cabbage")
    elif food == "Sweet potato, without skin, boiled, cooked":
        return str("Cooked sweet potato")
    elif food == "Bananas, raw, overripe":
        return str("Banana, overripe")
    elif food == "Onions, raw" or food == "Onions, raw, red" or food == "Onions, raw, yellow" or food == "Onions, raw, white":
        return str("Onion")
    elif food == "Apples, with skin, gala, raw" or food == "Apples, with skin, raw":
        return str("Apple, gala")
    elif food == "Carrots, raw, baby":
        return str("Baby carrots")
    elif food == "Avocados, California, raw":
        return str("Avocado")
    elif food == "Tomatoes, raw":
        return str("Tomato")
    elif food == "Peppers, raw, red, sweet" or food == "Pepper, raw, red, sweet":
        return str("Bell pepper")
    elif food == "Sweet potato, unprepared, raw" or food == "Sweet potato, washed":
        return str("Sweet potato")
    elif food == "Strawberries, raw":
        return str("Strawberries")
    elif food == "Ripe plantain, raw" or food == "Plantains, raw, yellow":
        return str("Plantain")
    elif food == "Carrots, raw":
        return str("Carrots")
    elif food == "Coleslaw mix by Bread & Circus Inc.":
        return str("Coleslaw mix")
    elif food == "Cucumber, raw" or food == "Cucumber, raw, with peel":
        return str("Cucumber")
    elif food == "Lettuce, raw" or food == "Lettuce, raw, cos or romaine" or food == "Romaine lettuce, raw":
        return str("Romaine lettuce")
    elif food == "Squash, raw, acorn, winter":
        return str("Acorn squash")    
    elif food == "Mushrooms, raw, white":
        return str("White Mushrooms")
    elif food == "Fruit peels apple banana by Target Stores":
        return str("Banana peel")
    elif food == "Ginger root, raw" or food == "Minced ginger by McCormick & Company, Inc.":
        return str("Ginger, fresh")
    elif food == "Cranberries, raw":
        return str("Cranberries")
    elif food == "Eggplant, raw":
        return str("Eggplant")
    elif food == "Fresh dill weed, fresh" or food == "Dill weed, fresh":
        return str("Dill, fresh")
    elif food == "Squash, raw, butternut, winter":
        return str("Butternut squash")
    elif food == "Squash, raw, includes skin, zucchini, summer":
        return str("Zucchini")
    elif food == "Squash, raw, spaghetti, winter":
        return str("Spaghetti squash")
    elif food == "Spinach, raw, or arugula" or food == "Spinach, raw":
        return str("Spinach, fresh")
    elif food == "Garlic, raw":
        return str("Garlic, fresh")
    elif food == "Pineapple, all varieties, raw":
        return str("Pineapple")
    elif food == "Mangos, raw":
        return str("Mango")
    elif food == "Beets, raw":
        return str("Beets")
    elif food == "Blackberries, raw":
        return str("Blackberries")
    elif food == "Summer squash, raw, yellow":
        return str("Yellow squash")
    elif food == "Red jalapeno salsa by The Kroger Co.":
        return str("Red jalapenos")
    elif food == "Cilantro, raw":
        return str("Cilantro, fresh")
    elif food == "Kiwi fruit":
        return str("Kiwi")
    
    # Frozen produce
    elif food == "Blueberries, frozen, wild":
        return str("Frozen blueberries")
    elif food == "Spinach, unprepared, chopped or leaf, frozen":
        return str("Frozen spinach, thawed")
    elif food == "Blackberries, unsweetened, frozen":
        return str("Frozen blackberries")
    elif food == "Strawberries, unsweetened, frozen":
        return str("Frozen strawberries")
    elif food == "Broccoli, unprepared, chopped, frozen" or food == "Frozen broccoli":
        return str("Frozen broccoli, thawed")
    elif food == "Fruit mixture, frozen":
        return str("Frozen fruit")
    elif food == "Brussels sprouts, unprepared, frozen":
        return str("Frozen brussel sprouts, thawed")
    elif food == "Cauliflower, unprepared, frozen":
        return str("Frozen cauliflower, thawed")
    elif food == "Kale, unprepared, frozen":
        return str("Frozen kale, thawed")
    elif food == "Vegetables, unprepared, frozen, mixed":
        return str("Vegetables")

    # Canned & jarred    
    elif food == "Tomato products, sauce, canned" or food == "Hunt's, pasta sauce, no added sugar, hunt's, pasta sauce, no added sugar by Conagra Brands, Inc.":
        return str("Unsweetened tomato sauce")
    elif food == "Artichoke hearts by MATIZ" or food == "Canned artichokes":
        return str("Artichokes")
    elif food == "Roasted red peppers by GALIL":
        return str("Roasted red peppers")
    elif food == "Tomatoes, diced, ripe, red, canned" or food == "Tomatoes, canned, diced" or food == "Fire roasted diced tomatoes by Raley's" or food == "Canned diced tomatoes":
        return str("Diced tomatoes")
    elif food == "Tomatoes, canned, crushed" or food == "Canned crushed tomatoes":
        return str("Crushed tomatoes")
    elif food == "Tomato paste by FIESTA" or food == "Tomato paste by REDPACK" or food == "Tomato products, paste, canned" or food == "Canned tomato paste" or food == "Tomato paste, canned":
        return str("Tomato paste")
    elif food == "Grape leaves, raw":
        return str("Grape leaves")
    elif food == "Minced clams in juice by Bumble Bee Foods, LLC" or food == "Canned clams":
        return str("Clams")
    elif food == "Fish, drained solids, canned in water, light, tuna" or food == "Canned tuna, in water":
        return str("Tuna, in water")
    elif food == "Pickles, sour, cucumber":
        return str("Pickles")
    elif food == "Capers by RALEY'S":
        return str("Capers")
    elif food == "Sardines in water":
        return str("Sardines, in water")
    elif food == "No salt added diced tomatoes by VINE RIPE":
        return str("Diced tomatoes, unsalted")
    elif food == "Diced green chiles by Raley's" or food == "Diced green chiles by HATCH" or food == "Diced green chile by Iga, Inc." or food == "Diced green chilies by SPARTAN" or food == "Diced green chilies by ELRIO":
        return str("Diced green chiles")
    elif food == "Chipotle peppers in adobo sauce by Goya Foods, Inc.":
        return str("Chipotle peppers in adobo sauce")
    elif food == "Kalamata olives, pitted":
        return str("Kalamata olives")
    
    # Nuts, chocolate, dried fruit
    elif food == "Almond butter by JUSTIN'S" or food == "Almond butter, lower sodium" or food == "Nuts, without salt added, plain, almond butter":
        return str("Almond butter")
    elif food == "Natural peanut butter by HAMPTON FARMS" or food == "Organic natural chunky peanut butter by The Federated Group, Inc." or food == "Natural peanut butter by Kohl Corporation":
        return str("Natural peanut butter")
    elif food == "Nuts, almonds" or food == "Nuts, with salt added, dry roasted, almonds" or food == "Nuts, without salt added, dry roasted, almonds":
        return str("Almonds")
    elif food == "Chopped peanuts by Raley's" or food == "Peanuts, raw, all types" or food == "Peanuts, unsalted, roasted" or food == "Peanuts, unsalted, dry roasted" or food == "Peanuts, lightly salted, dry roasted" or food == "Peanuts, salted, dry roasted" or food == "Peanuts, without salt, dry-roasted, all types":
        return str("Peanuts")
    elif food == "Dark chocolate baking chips, dark chocolate by LILYS" or food == "Hersheys Zero Sugar Chocolate Chips" or food == "Semisweet chocolate mini chips by Harris-Teeter Inc.":
        return str("Sugar free chocolate chips")
    elif food == str("90% cocoa dark chocolate by Lindt"):
        return str("90% chocolate")
    elif food == "Raw cashews" or food == "Nuts, raw, cashew nuts":
        return str("Cashews")
    elif food == "Raisins, seedless, dark":
        return str("Raisins")
    elif food == str("85% dark chocolate by Sinless Raw Food Inc"):
        return str("85% chocolate")
    elif food == "Chopped Walnuts, Great Value" or food == "Walnut chopped pieces" or food == "Chopped walnuts by DIAMOND":
        return str("Walnuts")
    elif food == "Walnut butter by Lyle Style":
        return str("Walnut butter")
    elif food == "Nuts, dried, pine nuts":
        return str("Pine nuts")
    elif food == "Nuts, pecans, or peanuts" or food == "Nuts, pecans":
        return str("Pecans")
    elif food == "Seeds, with salt added, dry roasted, sunflower seed kernels":
        return str("Sunflower kernels")
    elif food == "Nuts, with salt added, dry roasted, pistachio nuts" or food == "Dry roasted pistachios" or food == "Nuts, raw, pistachios":
        return str("Pistachios")
    elif food == "Raw hazelnuts" or food == "Nuts, hazelnuts or filberts":
        return str("Hazelnuts")
    elif food == "Roasted pumpkin seed butter, roasted by 88 ACRES" or food == "Pumpkin seed butter by Wilderness Poets LLC":
        return str("Pumpkin seed butter")
    elif food == "Baking chocolate, squares, unsweetened":
        return str("100% chocolate")
    
    # Carbs
    elif food == "Whole wheat protein tortillas by La Tortilla Factory Inc":
        return str("Whole wheat tortilla")
    elif food == "Bread, whole wheat":
        return str("Whole wheat bread")
    elif food == "Rice, raw, long-grain, brown":
        return str("Brown rice")
    elif food == "Pasta, dry, whole-wheat":
        return str("Whole wheat pasta")
    elif food == "Panko, crispy breadcrumbs by George DeLallo Co., Inc.":
        return str("Panko breadcrumbs")
    elif food == "Tortilla, whole wheat":
        return str("Whole wheat tortilla")
    elif food == "Chickpeas pasta by Banza LLC":
        return str("Chickpea pasta")
    elif food == "Cornmeal, yellow, whole-grain":
        return str("Cornmeal")
    
    # Meat & fish
    elif food == "Chicken, raw, meat only, boneless, skinless, breast, broiler or fryers":
        return str("Boneless skinless chicken breast")
    elif food == "Boneless skinless chicken thigh filets by PERDUE":
        return str("Boneless skinless chicken thighs")    
    elif food == "Chicken, raw, meat and skin, wing, broilers or fryers":
        return str("Chicken wings")
    elif food == "Chicken, raw, ground":
        return str("Ground chicken thighs")
    elif food == str("Turkey, raw, 7% fat, 93% lean, ground"):
        return str("Ground turkey, 93/7")    
    elif food == "Tilapia fillet" or food == "Fish, raw, tilapia":
        return str("Tilapia")
    elif food == "Fish, raw, pink, salmon" or food == "Salmon fillet by WILD ALASKAN SOCKEYE":
        return str("Salmon")
    elif food == "Peeled & deveined raw shrimp by PACIFIC SURF":
        return str("Frozen raw shrimp, peeled and deveined")    
    elif food == "Beef, raw, select, trimmed to 1/8 fat, separable lean only, steak, top sirloin":
        return str("Beef top sirloin")
    elif food == "Beef, raw, 93% lean meat / 7% fat, ground":
        return str("Ground beef, 93/7")    
    elif food == "Pork, raw, separable lean only, tenderloin, loin, fresh":
        return str("Pork tenderloin")
    elif food == "Shredded rotisserie chicken, rotisserie by Target Stores":
        return str("Shredded rotisserie chicken")
    
    # Else
    else:
        return food

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

if __name__ == '__main__':
    main()