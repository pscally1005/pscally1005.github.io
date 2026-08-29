import os
import re
from html import escape, unescape
from bs4 import BeautifulSoup, NavigableString
import time

POSTS_DIR = r"C:\Users\mets1\Documents\website\_posts"
# POSTS_DIR = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\_posts"

LINKS = {

    # RECIPES
    "/recipes/rosemary-sweet-potatoes": [
        "rosemary sweet potatoes",
        "rosemary sweet potato",
        "sweet potatoes with rosemary",
        "sweet potato with rosemary"
    ],
    "/recipes/no-nut-fudge-bars": [
        "no nut fudge bars",
        "no-nut fudge bars",
        "nut free fudge bars",
        "nut-free fudge bars"
        "no nut fudge bar",
        "no-nut fudge bar",
        "nut free fudge bar",
        "nut-free fudge bar"
    ],
    "/recipes/pea-butter": [
        "pea butter",
        "no-nut peanut butter",
        "no nut peanut butter",
        "nut free peanut butter",
        "nut-free peanut butter",
        "pea (no-nut) butter",
        "pea (no nut) butter",
        "pea-nut butter",
        "pea-not butter",
        "pea nut butter",
        "pea not butter"
    ],
    "/recipes/protein-shake-to-go": [
        "protein shake to go"
    ],
    "/recipes/milky-chocolate-spread": [
        "milky chocolate spread"
    ],
    "/recipes/pound-cake": [
        "pound cake",
        "lb cake",
        "1/4 lb cake",
        "1/4 pound cake",
        "quarter pound cake",
        "quarter lb cake",
        "the quarter pound cake",
        "the quarter lb cake",
        "the 1/4 pound cake",
        "the 1/4 lb cake"
    ],
    "/recipes/scones": [
        "lemon blueberry scones",
        "lemon blueberry scone",
        "blueberry lemon scones",
        "blueberry lemon scone",
        "scones",
        "scone",
        "whole wheat scones",
        "whole wheat scone",
        "whole wheat lemon blueberry scones",
        "whole wheat lemon blueberry scone",
        "whole wheat blueberry lemon scones",
        "whole wheat blueberry lemon scone",
        "lemon blueberry whole wheat scones",
        "lemon blueberry whole wheat scone",
        "blueberry lemon whole wheat scones",
        "blueberry lemon whole wheat scone"
    ],
    "/recipes/avocado-bread": [
        "avocado bread (sf)",
        "avocado bread",
        "sugar-free avocado bread",
        "sugar free avocado bread",
        "whole wheat avocado bread",
        "whole wheat avocado bread (sf)"
    ],
    "/recipes/nutty-veggies": [
        "nutty veggies",
        "nutty vegetables",
        "fatty veggies",
        "fatty vegetables"
    ],
    "/recipes/mug-brownie": [
        "microwave mug brownies",
        "microwave mug brownie",
        "healthy mug brownies",
        "healthy mug brownie",
        "low calorie mug brownies",
        "low calorie mug brownie",
        "low-calorie mug brownies",
        "low-calorie mug brownie",
        "sugar free mug brownies",
        "sugar-free mug brownies",
        "sugar-free mug brownie",
        "gluten free mug brownies",
        "gluten free mug brownie",
        "gluten-free mug brownies",
        "gluten free mug brownie"
    ],
    # "/recipes/homemade-electrolyte-powder": [
    #     "homemade electrolyte powder",
    # ],
    "/recipes/cottage-cheese-chips": [
        "cottage cheese chips",
        "cottage cheese chip",
        "high protein cottage cheese chips",
        "high protein cottage cheese chip",
        "1 ingredient cottage cheese chips",
        "1 ingredient cottage cheese chip",
        "one ingredient cottage cheese chips",
        "one ingredient cottage cheese chip"
    ],
    "/recipes/lentil-loaf": [
        "gluten free lentil loaf",
        "lentil loaf",
        "lentil loaf (gf)"
    ],
    "/recipes/english-muffin": [
        "microwave english muffins (gf)",
        "microwave english muffins",
        "microwave english muffin (gf)",
        "microwave english muffin",
        "english muffins (gf)",
        "english muffins",
        "english muffin (gf)",
        "english muffin",
        "low carb english muffins",
        "low carb english muffin",
        "low-carb english muffins",
        "low-carb english muffin",
        "low carb english muffins (gf)",
        "low carb english muffin (gf)",
        "low-carb english muffins (gf)",
        "low-carb english muffin (gf)"
    ],
    "/recipes/lentil-chips": [
        "lentil tortilla chips",
        "lentil chips",
        "baked lentil chips",
        "baked lentil tortilla chips",
        "red lentil tortilla chips",
        "red lentil chips",
        "baked red lentil chips",
        "baked red lentil tortilla chips",
        "red lentil wraps",
        "red lentil wrap",
        "lentil wraps",
        "lentil wrap",
        "red lentil tortillas",
        "red lentil tortilla",
        "lentil tortillas",
        "lentil tortilla"
    ],
    "/recipes/tomato-paste-sauce": [
        "tomato paste pasta sauce",
        "tomato paste sauce",
        "5 minute pasta sauce",
        "five minute pasta sauce"
    ],
    "/recipes/acai-bowl": [
        # "acai",
        # "Açaí"
        "acai bowl",
        "acai bowls",
        "acai yogurt bowl",
        "acai yogurt bowls",
        "healthy acai bowl",
        "healthy acai bowls",
        "healthy acai yogurt bowl",
        "healthy acai yogurt bowls",
        "Açaí bowl",
        "Açaí bowls",
        "Açaí yogurt bowl",
        "Açaí yogurt bowls",
        "healthy Açaí bowl",
        "healthy Açaí bowls",
        "healthy Açaí yogurt bowl",
        "healthy Açaí yogurt bowls",
    ],
    "/recipes/monk-fruit-cookies": [
        "granulated monk fruit cookies",
        "granulated monk fruit cookie",
        "granulated monkfruit cookies",
        "granulated monkfruit cookie",
        "monk fruit cookies",
        "monk fruit cookie",
        "monkfruit cookies",
        "monkfruit cookie"
    ],
    "/recipes/syrup-cookies": [
        "sugar free syrup cookies",
        "sugar free syrup cookie"
    ],
    "/recipes/cannoli-dip": [
        "cannoli dip",
        "cannoli",
        "high protein cannoli dip",
        "sugar free cannoli dip",
        "high protein sugar free cannoli dip",
        "sugar free high protein cannoli dip"
    ],
    "/recipes/protein-crumbles": [
        "vegan protein crumbles",
        "vegan protein crumble",
        "protein dressing"
    ],
    "/recipes/artificial-brownies": [
        "artificial brownies",
        "artificial brownie"
    ],
    "/recipes/put-milk-back-together-beans": [
        '"put the milk back together" beans',
        "put the milk back together beans"
    ],
    "/recipes/sweet-potato-toast": [
        "sweet potato toast"
    ],
    "/recipes/sludge-brick": [
        "peanut butter chocolate sludge brick",
        "peanut butter chocolate sludge bricks",
        "peanut butter sludge brick",
        "peanut butter sludge bricks",
        "peanut chocolate sludge brick",
        "peanut chocolate sludge bricks",
        "chocolate peanut sludge brick",
        "chocolate peanut sludge bricks",
        "chocolate sludge brick",
        "chocolate sludge bricks"
        "chocolate peanut butter sludge brick",
        "chocolate peanut butter sludge bricks",
        "sludge brick",
        "sludge bricks",
        "peanut butter chocolate sludge bar",
        "peanut butter chocolate sludge bars",
        "peanut butter sludge bar",
        "peanut butter sludge bars",
        "peanut chocolate sludge bar",
        "peanut chocolate sludge bars",
        "chocolate peanut sludge bar",
        "chocolate peanut sludge bars",
        "chocolate sludge bar",
        "chocolate sludge bars"
        "chocolate peanut butter sludge bar",
        "chocolate peanut butter sludge bars",
        "sludge bar",
        "sludge bars"
    ],
    "/recipes/chicken-biscuits": [
        "chicken biscuits",
        "chicken biscuit",
        # "biscuits",
        # "biscuit",
        "small batch o' chicken biscuits",
        "small batch o' chicken biscuit",
        "small batch of chicken biscuits",
        "small batch of chicken biscuit"
        "small batch chicken biscuits",
        "small batch chicken biscuit",
        "chicken fat biscuits",
        "chicken fat biscuit"
    ],
    "/recipes/vegan-biscuits": [
        # "biscuits",
        # "biscuit",
        "cauliflower biscuits (vegan, gf)",
        "cauliflower biscuit (vegan, gf)",
        "cauliflower biscuits",
        "cauliflower biscuit",
        "vegan biscuits",
        "vegan biscuit"
    ],
    "/recipes/cauliflower-cookies": [
        # "vegan cookies",
        # "vegan cookie",
        "cauliflower cookies (vegan, gf)",
        "cauliflower cookie (vegan, gf)",
        "cauliflower cookies",
        "cauliflower cookie",
        "cauliflower chocolate chip cookies",
        "cauliflower chocolate chip cookies",
        "vegan chocolate chip cookies",
        "vegan chocolate chip cookie"
    ],
    "/recipes/protein-cheesecake-brownies": [
        "high protein brownie cheesecake bars",
        "high protein brownie cheesecake bar",
        "high protein brownie cheesecake",
        "high protein cheesecake brownie bars",
        "high protein cheesecake brownie bar",
        "high protein cheesecake brownies",
        "high protein cheesecake brownie",
        "brownie cheesecake bars",
        "brownie cheesecake bar",
        "brownie cheesecake",
        "cheesecake brownie bars",
        "cheesecake brownie bar",
        "cheesecake brownies",
        "cheesecake brownie"
    ],
    "/recipes/protein-donuts": [
        "high protein donuts",
        "high protein donut",
        "air fryer protein donuts",
        "air fryer protein donut",
        "chocolate protein donuts",
        "chocolate protein donut",
        "protein donuts",
        "protein donut",
        "air fryer donuts",
        "air fryer donut",
        "air fried protein donuts",
        "air fried protein donut",
        "air fried donuts",
        "air fried donut",
        "chocolate donuts",
        "chocolate donut",
        "donuts",
        "donut"
    ],
    "/recipes/snickers-nice-cream-bar": [
        "snickers nice cream bar",
        "snickers ice cream bar",
        "snickers ice cream",
        "snickers nice cream",
        "snickers banana ice cream bar",
        "snickers banana ice cream",
        "snicker's nice cream bar",
        "snicker's ice cream bar",
        "snicker's ice cream",
        "snicker's nice cream",
        "snicker's banana ice cream bar",
        "snicker's banana ice cream"
    ],
    "/recipes/cherry-garcia": [
        "cherry garcia banana ice cream",
        "cherry garcia ice cream",
        "cherry garcia nice cream",
        "cherry garcia",
        "cherry ice cream"
    ],
    "/recipes/chunky-monkey": [
        "chunky monkey banana ice cream",
        "chunky monkey ice cream",
        "chunky monkey nice cream",
        "chunky monkey"
    ],
    "/recipes/sourdough-pizza-dough": [
        "sourdough pizza dough",
        "sourdough pizza crust",
        "sourdough pizza"
    ],
    "/recipes/sourdough-pizza-dough#skillet": [
        "cast iron pizza",
        "cast iron skillet pizza",
        "skillet pizza"
    ],
    "/recipes/cottage-cheese-pizza-bowls": [
        "high protein cottage cheese pizza bowl",
        "high protein cottage cheese pizza",
        "cottage cheese pizza bowl",
        "cottage cheese pizza",
        "high protein pizza bowls",
        "high protein pizza bowl"
    ],
    "/recipes/vegan-protein-bars": [
        "no-bake vegan protein bars",
        "no bake vegan protein bars",
        "no-bake vegan protein bar",
        "no bake vegan protein bar",
        "vegan protein bars",
        "vegan protein bar"
    ],
    "/recipes/sugar-free-chocolate-syrup": [
        "sugar free chocolate syrup recipe",
        "sugar free chocolate syrup",
        "chocolate syrup",
        "allulose chocolate syrup",
        "homemade chocolate syrup"
    ],
    "/recipes/protein-layer-cake": [
        "protein chocolate layer cake",
        "chocolate protein layer cake",
        "protein layer cake",
        "chocolate protein cake",
        "protein birthday cake",
        "protein birthday layer cake",
        "birthday protein layer cake",
        "birthday protein cake",
        "protein chocolate cake",
        "double chocolate protein cake"
    ],
    "/recipes/cottage-cheese-queso": [
        "high protein cottage cheese queso dip",
        "high protein cottage cheese queso",
        "cottage cheese queso dip",
        "cottage cheese queso",
        "queso dip",
        "queso",
        "high protein queso dip",
        "high protein queso"
    ],
    "/recipes/tabbouleh": [
        "tabbouleh",
        "tabouli",
        "tabbouli",
        "tabouleh",
        "lebanese tabbouleh salad",
        "lebanese tabbouleh",
        "tabbouleh salad"
    ],
    "/recipes/limeade": [
        "homemade sugar free limeade",
        "homemade limeade",
        "sugar free limeade",
        "limeade",
        "homemade sugar free lemonade",
        "homemade lemonade",
        "sugar free lemonade",
        "lemonade"
    ],
    "/recipes/fresh-mint-oat-bars": [
        "fresh mint oat bars",
        "fresh mint oat bar",
        "mint oat bars",
        "mint oat bar"
    ],
    "/recipes/honey-mustard": [
        "honey mustard dressing",
        "honey mustard",
        "homemade healthier honey mustard dressing",
        "homemade healthier honey mustard",
        "homemade honey mustard dressing",
        "homemade honey mustard"
    ],
    "/recipes/cubano-casserole": [
        "cubano casserole",
        "leaner cubano casserole",
        "cuban casserole",
        "leaner cuban casserole",
        "cubano",
        "cubano"
    ],
    "/recipes/mint-sauce": [
        "dairy free creamy mint sauce",
        "dairy free mint sauce",
        "creamy mint sauce",
        "mint sauce",
        "mint hummus",
        "creamy mint hummus",
        "dairy free creamy yogurt sauce",
    ],
    "/recipes/nojito": [
        "sugar free nohito",
        "sugar free no-hito",
        "nohito",
        "no-hito"
        "mohito",
        "sugar free nojito",
        "sugar free no-jito",
        "nojito",
        "no-jito"
        "mojito"
    ],
    "/recipes/recession-beans": [
        "recession beans: a $1 meal",
        "recession beans"
    ],
    "/misc/tea": [
        "herbal tea-r list",
        "herbal tea list",
        "herbal tea tier list",
        "teas",
        "tea"
        "herbal teas",
        "herbal tea"
    ],
    "/recipes/fiber-chocolate-milk": [
        "fiber chocolate milk",
        "fiber milk"
    ],
    "/misc/beans-are-carbs": [
        "beans are carbs",
        "beans are carbohydrates",
        "bean is a carb",
        "bean is a carbohydrate",
        "beans are a carb",
        "beans are a carbohydrate"
    ],
    "/recipes/coconut-blondies": [
        "air fryer coconut blondies",
        "air fryer coconut blondie",
        "air fried coconut blondies",
        "air fried coconut blondie",
        "coconut blondies",
        "coconut blondie"
    ],
    "/recipes/discard-whey-protein-bars": [
        "discard whey protein bars",
        "discard whey protein bar"
    ],
    "/misc/homemade-yogurt": [
        "homemade yogurt",
        "homemade plain nonfat greek yogurt",
        "homemade plain nonfat yogurt",
        "homemade plain yogurt",
        "homemade plain greek yogurt",
        "homemade greek yogurt",
        "homemade whey",
        "homemade liquid whey",
        "homemade yogurt whey",
        "homemade yogurt and whey",
        "homemade whey and yogurt",
        "liquid whey",
        "homemade liquid whey",
        "leftover liquid whey",
        "leftover homemade liquid whey",
        "homemade greek yogurt and liquid whey",
        "homemade yogurt and liquid whey",
        "homemade yogurt & liquid whey",
        "homemade yogurt & whey",
        "homemade greek yogurt & whey",
        "homemade greek yogurt and liquid whey",
        "homemade whey & yogurt"
    ],
    "/recipes/vic-noats": [
        "very vic novernight noats",
        "very vic noats",
        "vic noats",
        "vic novernight noats",
        "very vic n-overnight n-oats",
        "very vic n-oats",
        "vic n-overnight n-oats",
        "vic n-oats",
        "very vic no-vernight no-ats",
        "vic no-vernight no-ats",
        "very vic no-ats",
        "vic no-ats",
        "very vic no-overnight no-oats",
        "very vic no-oats",
        "vic no-overnight no-oats",
        "vic no-oats"
    ],
    "/recipes/oatmeal-cream-pies": [
        "protein oatmeal cream pies",
        "protein oatmeal cream pie",
        "oatmeal cream pies",
        "oatmeal cream pie"
    ],
    "/recipes/simple-soup": [
        "20 minute veggie soup",
        "20 minute vegetable soup",
        "20 minute simple soup",
        "20 minute soup",
        "simple soup"
    ],
    "/recipes/novernight-noats": [
        "novernight noats",
        "n-overnight n-oats",
        "no-vernight no-ats",
        "no-overnight no-oats"
    ],
    "/recipes/chicken-fat-cornbread": [
        "chicken fat cornbread"
    ],
    "/recipes/diy-yogurt": [
        "diy yogurt"
    ],
    "/recipes/nutella-cookie": [
        "single serving nutella cookie",
        "nutella cookie"
    ],
    "/recipes/pizza-beans": [
        "quick and easy pizza beans with spinach",
        "quick & easy pizza beans with spinach",
        "quick and easy pizza beans",
        "quick & easy pizza beans",
        "pizza beans with spinach",
        "pizza beans"
    ],
    "/recipes/fiber-protein-bar": [
        "high fiber protein bars",
        "fiber protein bars",
        "high fiber protein bar",
        "fiber protein bar"
    ],
    "/recipes/psyllium-wrap": [
        "high fiber psyllium wraps",
        "high fiber psyllium wrap",
        "high fiber wraps",
        "high fiber wrap",
        "psyllium wraps",
        "psyllium wrap"
    ],
    "/recipes/inulin-syrup": [
        "high fiber inulin syrup",
        "high fiber syrup",
        "inulin syrup",
        "chicory root syrup",
        "fiber syrup"
    ],
    "/recipes/high-fiber-jelly": [
        "high fiber jelly",
        "sugar free jelly",
        "psyllium husk jelly",
        "psyllium jelly"
    ],
    "/recipes/popped-quinoa": [
        "single serving popped quinoa",
        "popped quinoa"
    ],
    "/recipes/tomato-turkey-taco": [
        "tomato turkey tacos",
        "tomato turkey taco",
        "tomato tacos",
        "tomato taco",
        "ground turkey tacos",
        "ground turkey taco"
    ],
    "/recipes/cilantro-lime-rice": [
        "cilantro lime rice",
        "cilantro lime brown rice"
    ],
    "/recipes/fajita-peppers": [
        "fajita peppers",
        "fajita pepper",
        "fajita veggies",
        "fajits vegetables",
        "fajita veggie",
        "fajita vegetable",
        "sauteed fajita peppers",
        "sauteed fajita pepper",
        "sauteed fajita veggies",
        "sauteed fajita veggie",
        "sauteed fajita vegetables",
        "sauteed fajita vegetable"
    ],
    "/recipes/fro-yo": [
        "sugar free frozen yogurt",
        "sugar free fro yo",
        "sugar free fro-yo",
        "frozen yogurt",
        "fro yo",
        "fro-yo"
        "vanilla frozen yogurt",
        "vanilla fro yo",
        "vanilla fro-yo",
        "chocolate frozen yogurt",
        "chocolate fro yo",
        "chocolate fro-yo"
    ],
    "/recipes/ice-cream": [
        "lactose free no churn chocolate ice cream",
        "lactose free no churn ice cream",
        "lactose free ice cream",
        "no churn ice cream",
        "chocolate ice cream",
        "ice cream"
    ],
    "/recipes/spring-rolls": [
        "fresh veggie spring rolls",
        "fresh veggie spring roll",
        "spring rolls",
        "spring roll"
    ],
    "/recipes/chia-water": [
        "high fiber chia water",
        "high fiber chia seed water",
        "high fiber flax water",
        "high fiber flaxseed water",
        "high fiber flax seed water",
        "high fiber psyllium water",
        "high fiber psyllium husk water",
        "chia water",
        "chia seed water",
        "flax water",
        "flax seed water",
        "flaxseed water",
        "psyllium water",
        "psyllium husk water"
    ],
    "/recipes/chaos-rice": [
        "italian chaos rice",
        "chaos rice",
        "brown rice risotto"
    ],
    "/recipes/lazy-rainbow-cookies": [
        "Lazy rainbow cookies",
        "lazy rainbow cookie",
        "easy rainbow cookies",
        "easy rainbow cookie"
    ],
    "/recipes/butternut-yogurt": [
        "butternut squash yogurt"
    ],
    "/recipes/protein-frosting": [
        "protein frosting recipe",
        "protein frosting, vanilla",
        "protein frosting, chocolate",
        "protein frosting",
        "vanilla protein frosting",
        "chocolate protein frosting"
        "vanilla frosting",
        "chocolate frosting",
        "frosting"
    ],
    "/recipes/baklava": [
        "healthy baklava",
        "sugar free baklava",
        "gluten free baklava",
        "rice paper baklava",
        # "baklava with rice paper",
        "baklava",
        "baklava inspired",
        "baklava-inspired",
        "baklava inspired dessert",
        "baklava-inspired dessert",
        "gluten free baklava inspired dessert",
        "gluten free baklava-inspired dessert"
    ],
    "/recipes/white-chicken-chili": [
        "white chicken chili with greek yogurt",
        "greek yogurt white chicken chili",
        "white chicken chili"
    ],
    "/recipes/chocolate-cake": [
        # "cake",
        "chocolate cake from scratch",
        "chocolate cake",
        "homemade chocolate cake"
    ],
    "/recipes/protein-brownie-batter": [
        "edible protein brownie batter",
        "protein brownie batter"
    ],
    "/recipes/barlotto": [
        "barlotto, aka barley risotto",
        "barlotto aka barley risotto",
        "barlotto",
        "barley risotto"
    ],
    "/recipes/chocolate-chili": [
        "chocolate... chili?",
        "chocolate... chili",
        "chocolate chili?",
        "chocolate chili",
        "chocolaty... chili?",
        "chocolaty... chili",
        "chocolaty chili?",
        "chocolaty chili",
        "chocolatey... chili?",
        "chocolatey... chili",
        "chocolatey chili?",
        "chocolatey chili"
    ],
    "/recipes/dubai-chocolate": [
        "sugar free dubai chocolate",
        "homemade dubai chocolate",
        "dubai chocolate"
    ],
    "/recipes/pistachio-truffles": [
        "chocolate pistachio truffles",
        "pistachio chocolate truffles",
        "chocolate pistachio truffle",
        "pistachio chocolate truffle"
    ],
    "/recipes/chocolate-covered-marzipan": [
        "chocolate covered marzipan",
        "chocolate marzipan"
    ],
    "/recipes/chocolate-covered-marzipan#notes": [
        "homemade marzipan"
    ],
    "/recipes/mint-protien-bar": [
        "mint protein bars",
        "mint protein bar",
        "mint chocolate protein bars",
        "mint chocolate protein bar",
        "avocado mint protien bars",
        "avocado mint protein bar"
    ],
    "/recipes/best-healthy-brownies": [
        "the best healthy brownies recipe",
        "the best healthy brownies",
        "best healthy brownies recipe",
        "best healthy brownies"
    ],
    "/recipes/best-healthy-cookie-dough": [
        "the best healthy cookie dough recipe",
        "the best healthy cookie dough",
        "the best healthy cookies",
        "the best healthy cookie",
        "best healthy cookie dough recipe",
        "best healthy cookie dough",
        "best healthy cookies",
        "best healthy cookie",
        "best healthy cookies recipe",
        "best healthy cookie recipe",
        "the best healthy chocolate chip cookies recipe",
        "the best healthy chocolate chip cookie recipe",
        "the best healthy chocolate chip cookies",
        "the best healthy chocolate chip cookie",
        "best healthy chocolate chip cookies recipe",
        "best healthy chocolate chip cookie recipe",
        "best healthy chocolate chip cookies",
        "best healthy chocolate chip cookie"
    ],
    "/recipes/no-bake-white-chocolate-protein-brownies": [
        "no-bake white chocolate protein brownies",
        "no bake white chocolate protein brownies",
        "white chocolate no-bake protein brownies",
        "white chocolate no bake protein brownies",
        "white chocolate protein brownies",
        "white chocolate brownies",
        "no-bake white chocolate protein brownie",
        "no bake white chocolate protein brownie",
        "white chocolate no-bake protein brownie",
        "white chocolate no bake protein brownie",
        "white chocolate protein brownie",
        "white chocolate brownie"
    ],
    "/recipes/white-chocolate": [
        "tangy white chocolate",
        "homemade white chocolate",
        "white chocolate chips",
        "white chocolate chip",
        "white chocolate",
        "unsweetened white chocolate bar",
        "unsweetened white chocolate",
        "sugar free white chocolate chips",
        "sugar free white chocolate chunks",
        "sugar free white chocolate"
    ],
    "/recipes/chocolate-cloud-bars": [
        "chocolate cloud bars",
        "chocolate cloud protein bars",
        "chocolate cloud bar",
        "chocolate cloud protein bar"
    ],
    "/recipes/clif-bars": [
        "Copycat Peanut Butter Chocolate Clif Bars",
        "Copycat Peanut Butter Chocolate Clif Bar",
        "chocolate clif bars",
        "chocolate clif bar",
        "peanut butter chocolate clif bars",
        "peanut butter chocolate clif bar",
        "peanut chocolate clif bars",
        "peanut chocolate clif bar",
        "copycat chocolate clif bars",
        "copycat chocolate clif bar",
        "copycat clif bars",
        "copycat clif bar",
        "clif bars",
        "clif bar"
    ],
    "/recipes/peanut-coconut-curry": [
        "peanut coconut curry",
        "panang"
    ],
    "/recipes/gassy-assy": [
        "the gassy assy",
        "gassy assy"
    ],
    "/recipes/24-hour-chili": [
        "24 Hour Chili"
    ],
    "/recipes/4-ingredient-cookie-bars": [
        "4 Ingredient Cookie Bars"
    ],
    "/recipes/air-fried-falafel": [
        "Air Fryer Falafel (GF)",
        "Air Fryer Falafel",
        "falafel"
    ],
    "/recipes/air-fried-trail-mix": [
        "Air Fryer Trail Mix"
    ],
    "/recipes/almond-flour-empanadas": [
        "Almond Flour Empanada & Pierogi Dough",
        "almond flour empanadas",
        "almond flour pierogi",
        "almond flour empanada dough",
        "almond flour pierogi dough",
        "almond flour empanada",
        "ground beef empanadas",
        "ground beef empanada",
        "sweet potato pierogi",
        "spinach and feta hand pies",
        "spinach and feta hand pie",
        "spinach feta hand pies",
        "spinach feta hand pie",
        "spinach hand pies",
        "spinach hand pie",
        "spinach pies",
        "spinach pie",
        "cassatelle",
        "cassatella",
        "sicilian cassatelle",
        "sicilian cassatella"
    ],
    "/recipes/almond-flour-focaccia": [
        "Almond Flour Focaccia"
    ],
    "/recipes/amaretti": [
        "Amaretti Cookies with Monkfruit",
        "amaretti cookies",
        "amaretti cookie",
        "amaretti"
    ],
    "/recipes/amaretti-cookies-with-dates": [
        "Amaretti Cookies with Dates"
    ],
    "/recipes/apple-bread": [
        "Protein Apple Bread"
    ],
    "/recipes/apple-cinnamon-bread": [
        "Pumpkin Spice Apple Bread"
    ],
    "/recipes/apple-crumble": [
        "Apple Crumble with Oats",
        "apple crisp with oats"
    ],
    "/recipes/apple-pie": [
        "Sugar Free Apple Pie"
    ],
    "/recipes/apple-samoas": [
        "Apple Samoa Bites"
    ],
    "/recipes/aquafaba-ice-cream": [
        "Aquafaba Chocolate Ice Cream",
        "aquafaba ice cream"
        # "ice cream"
    ],
    "/recipes/avocado-pesto": [
        "Avocado Pesto - Vegan and Oil Free",
        "avocado pesto"
    ],
    "/recipes/avocado-protein-mousse": [
        "Avocado Protein Chocolate Mousse",
        "avocado protein mousse",
        "avocado chocolate mousse",
        "avocado mousse"
    ],
    "/recipes/avocado-tuna-salad": [
        "Avocado Tuna Salad"
    ],
    "/recipes/baked-chicken-thighs": [
        "Spiced Baked Chicken Thighs"
    ],
    "/recipes/baked-protein-bars": [
        "Baked Protein Bars"
    ],
    "/recipes/baked-rice-and-beans": [
        "Baked Rice and Beans with Vegetables",
        "baked rice and beans"
    ],
    "/recipes/balsamic-vinaigrette": [
        "Oil Free Balsamic Vinaigrette",
        "homemade balsamic vinaigrette"
    ],
    "/recipes/banana-bread": [
        "Oatmeal Banana Mini Muffins",
        "oatmeal banana muffins",
        "oatmeal banana bread"
    ],
    "/recipes/banana-bread-for-one": [
        "Protein Breakfast Banana Bread for One",
        "protein breakfast banana bread"
    ],
    "/recipes/banana-bread-hummus": [
        "banana bread hummus spread",
        "banana bread hummus",
        "homemade dessert hummus",
        "dessert hummus"
    ],
    "/recipes/banana-chimichanga": [
        "Healthy Banana Chimichanga",
        "banana chimichanga"
    ],
    "/recipes/banana-cream-pie": [
        "Banana No-Cream Pie",
        "banana cream pie"
    ],
    "/recipes/banana-protein": [
        "Protein Banana Nut Bread",
        "protein banana bread"
    ],
    "/recipes/banana-protein-pancakes": [
        "Banana Protein Pancakes",
        "banana pancakes"
        "banana protein pancake",
        "banana pancake"
    ],
    "/recipes/bbq-meatloaf": [
        "Classic BBQ Meatloaf and Lemon Roasted Broccoli"
        "classic bbq meatloaf",
        "meatloaf"
    ],
    "/recipes/bean-salad": [
        "Mediterranean 3 Bean Salad"
    ],
    "/recipes/beef-and-broccoli": [
        "Juicy and Healthy Beef and Broccoli",
        "beef and broccoli",
        "beef & broccoli",
        "juicy and healthy beef & broccoli",
        "juicy & healthy beef & broccoli"
        "juicy & healthy beef and broccoli"
    ],
    "/recipes/beef-liver": [
        "Making Liver Taste Good"
    ],
    "/recipes/big-boi": [
        "Bigger Boi Oatmeal"
    ],
    "/recipes/biscotti": [
        "Air Fryer Biscotti",
        "biscotti cookies",
        "biscotti cookie",
        "biscotti"
    ],
    "/recipes/black-bean-burger": [
        "Protein Black Bean Burgers",
        "protein black bean burger",
        "black bean burgers",
        "black bean burger",
        "protein bean burgers",
        "protein bean burger",
        "black bean patties",
        "black bean patty",
        "bean patties",
        "bean patty",
        "Protein chickpea Burgers",
        "protein chickpea burger",
        "chickpea burgers",
        "chickpea burger",
        "protein chickpea burgers",
        "protein chickpea burger",
        "chickpea patties",
        "chickpea patty"
    ],
    "/recipes/black-bean-date-brownies": [
        "Black Bean Date Brownies"
        "black bean date brownie",
        "black bean brownies",
        "black bean brownie",
        "bean brownies",
        "bean brownie"
    ],
    "/recipes/blue-cheese-dressing": [
        "White Bean Blue Cheese Dressing",
        "homemade blue cheese dressing",
        "homemade blue cheese"
    ],
    "/recipes/bolognese-oats": [
        "Turkey Oatmeal Bolognese"
    ],
    "/recipes/brain-boosting-bowl": [
        "Brain Boosting Bowl"
    ],
    "/recipes/brain-yogurt": [
        "Brain Boosting Yogurt"
    ],
    "/recipes/breaded-chicken": [
        "Italian Breaded Chicken with Bruschetta"
        "italian breaded chicken",
        "breaded chicken cutlets"
    ],
    "/recipes/broccoli-cheddar-soup": [
        "No Cream Broccoli Cheddar Soup",
        "broccoli cheddar soup"
    ],
    "/recipes/broccoli-fries": [
        "Air Fryer Broccoli Fries",
        "broccoli fries"
    ],
    "/recipes/broccoli-rabe": [
        "Garlic Lemon Broccoli Rabe"
    ],
    "/recipes/buffalo-chicken": [
        "Creamy Buffalo Chicken and Peppers"
    ],
    "/recipes/bulking-breakfast": [
        "1,000 Calorie Bulking Breakfast",
        "bulking breakfast"
    ],
    "/recipes/bulking-brownies": [
        "Clean Bulking Brownies",
        "bulking brownies"
    ],
    "/recipes/burger-bowl": [
        "Chopped Burger Bowl with Sweet Potatoes",
        "burger bowl"
    ],
    "/recipes/butter-chicken": [
        "No Butter Chicken with Quinoa",
        "butter chicken"
    ],
    "/recipes/butternut-squash": [
        "Roasted Butternut Squash with Onions"
        "roasted butternut squash",
    ],
    "/recipes/butternut-squash-risotto": [
        "Butternut Squash RisOATto",
        "butternut squash risotto"
    ],
    "/recipes/cabbage-bread": [
        "Cabbage Bread (4 Ingredients)",
        "cabbage bread"
    ],
    "/recipes/cacciatore": [
        "Stewed Chicken Cacciatore",
        "chicken cacciatore"
    ],
    "/recipes/caponata": [
        "Heavily Modified Sicilian Caponata",
        "sicilian caponata",
        "caponata"
    ],
    "/recipes/caprese-chicken": [
        "Balsamic Caprese Chicken with Roasted Artichokes",
        "balsamic caprese chicken",
        "caprese chicken"
    ],
    "/recipes/carrot-cake": [
        "Layered Protein Carrot Cake",
        "protein carrot cake",
        "carrot cake"
    ],
    "/recipes/carrot-cake-bites": [
        "Carrot Cake Energy Bites"
        "carrot cake energy bite",
    ],
    "/recipes/cheesecake": [
        "Sugar Free Peanut Butter Cheesecake",
        "peanut butter cheesecake"
    ],
    "/recipes/cheesecake-bars": [
        "No Bake Cheesecake Bars",
        "cheesecake bars",
        "no bake cheesecake bar",
        "cheesecake bar"
    ],
    "/recipes/cheesy-bean-dip": [
        "Cheesy Bean Dip",
        "bean dip"
    ],
    "/recipes/cheesy-cauliflower-rice-and-beans": [
        '"Cheesy" Cauliflower Rice & Beans',
        "'cheesy' cauliflower rice & beans",
        '"Cheesy" Cauliflower Rice and Beans',
        "'cheesy' cauliflower rice and beans",
        "cheesy cauliflower rice & beans",
        "cheese cauliflower rice and beans",
        "cauliflower rice & beans",
        "cauliflower rice and beans"
    ],
    "/recipes/cheesy-rice-and-broccoli": [
        "Cheesy Rice & Broccoli",
        "cheesy rice and broccoli"
    ],
    "/recipes/chicken-alfredo": [
        "Chicken Alfredo with Potatoes and Broccoli",
        "chicken alfredo"
    ],
    "/recipes/chicken-fingers": [
        "Gluten Free Chicken Fingers"
    ],
    "/recipes/chicken-florentine": [
        "No Cream Chicken Florentine",
        "chicken florentine",
    ],
    "/recipes/chicken-noodle-stew": [
        "Chicken Noodle Stew",
        "chicken noodle soup"
    ],
    "/recipes/chicken-nuggets": [
        "Freezer Chicken Nuggets"
    ],
    "/recipes/chicken-piccata": [
        "Quick, Easy, & Healthy Chicken Piccata",
        "chicken piccata"
    ],
    "/recipes/chicken-stew": [
        "Crockpot Chicken Stew",
        "chicken stew"
    ],
    "/recipes/chicken-wings": [
        "Gluten Free Baked Buffalo Wings",
        "buffalo chicken wings",
        "buffalo wings"
    ],
    "/recipes/chickpea-brownies": [
        "Protein Brownie Bars",
        "protein chickpea brownies",
        "protein brownies",
        "protein brownie",
        "protein brownie bar",
        "protein chickpea brownie"
    ],
    "/recipes/chickpea-chows": [
        "Chickpea Chows",
        "chickpea chow"
    ],
    "/recipes/chickpea-date-blondies": [
        "Chickpea Date Blondies",
        "chickpea date blondie",
        "chickpea blondies",
        "chickpea blondie"
    ],
    "/recipes/chickpea-date-brownies": [
        "Chickpea Date Brownies",
        "chickpea date brownie",
        "chickpea brownies",
        "chickpea brownie"
    ],
    "/recipes/chickpea-sandwich": [
        "Mashed Chickpea Sandwich"
    ],
    "/recipes/chickpea-wrap": [
        "Tomato Chickpea Wraps",
        "chana masala"
    ],
    "/recipes/chocolate-apple-cake": [
        "Chocolate Cake for One"
    ],
    "/recipes/chocolate-chip-cookie-skillet": [
        "Chocolate Chip Cookie Skillet",
        "cookie cake"
    ],
    "/recipes/chocolate-covered-garlic": [
        "Chocolate Covered Garlic Cloves"
    ],
    "/recipes/chocolate-electrolyte-bowls": [
        "Electrolyte Protein Breakfast Bowls"
    ],
    "/recipes/chocolate-kefir": [
        "Probiotic Chocolate Kefir",
        "chocolate kefir"
    ],
    "/recipes/chocolate-peanut-butter-mousse": [
        "Chocolate Peanut Butter Mousse",
        "chocolate mousse",
        "chickpea mousse",
        "peanut butter mousse",
        "mousse"
    ],
    "/recipes/chocolate-truffle": [
        "Chocolate Yogurt Kerfuffles",
        "chocolate yogurt truffles",
        "yogurt truffles",
    ],
    "/recipes/cinnamon-chickpea": [
        "Cinnamon Toast Chickpeas"
    ],
    "/recipes/cloud-bread": [
        "Low Carb Cloud Bread",
        "cloud bread"
    ],
    "/recipes/cocoa-bites": [
        "Peanut Butter Cocoa Bites"
    ],
    "/recipes/coconut-cookies": [
        "Sugar Free Coconut Cookies"
    ],
    "/recipes/coconut-macaroons": [
        "Coconut Macaroons with Honey",
        "coconut macaroons",
        "coconut macaroon"
    ],
    "/recipes/coffee-loaf": [
        "Decaf Coffee Loaf",
        "coffee loaf"
    ],
    "/recipes/congee": [
        "Brown Rice Congee Base",
        "congee"
    ],
    "/recipes/copycat-harvest-bowl": [
        "Copycat Sweetgreen Harvest Bowl",
        "harvest bowl"
    ],
    "/recipes/corn-on-the-cob": [
        "Roasted Corn on the Cob",
        "corn on the cobb"
    ],
    "/recipes/cottage-cheese-ice-cream": [
        "Cottage Cheese Ice Cream"
    ],
    "/recipes/cottage-cheese-peanut-butter": [
        "Cottage Cheese Peanut Butter"
    ],
    "/recipes/couscous": [
        "Tomato and Bean Couscous",
        "tomato & bean couscous"
    ],
    "/recipes/cranberry-sauce": [
        "Sugar Free Cranberry Sauce",
        "cranberry sauce"
    ],
    "/recipes/creamy-pesto-hummus": [
        "Creamy Pesto Hummus",
        "pesto hummus"
    ],
    "/recipes/crepe": [
        "Whole Wheat Breakfast Crepes",
        "whole wheat breakfast crepe",
        "crepes",
        "crepe"
    ],
    "/recipes/cuccidati": [
        "Date Cuccidati Cookies",
        "cuccidati",
        "fig cookies",
        "fig cookie"
    ],
    "/recipes/cucumber-salad": [
        "Kinda Asian Cucumber Salad",
        "cucumber salad"
    ],
    "/recipes/cut-out-cookies": [
        "Healthier Cut Out Cookies"
    ],
    "/recipes/date-brownie": [
        "Almond Butter Date Brownies",
        "date brownies",
        "almond butter date brownie",
        "date brownie"
    ],
    "/recipes/date-cookies": [
        "Almond Flour Cookies",
        "almond flour cookie",
        "date cookies",
        "date cookie"
    ],
    "/recipes/date-snickers": [
        "Date Snickers Bars",
        "date snickers bar",
        "date snickers"
    ],
    "/recipes/dead-simple-chili": [
        "Dead Simple Chili"
    ],
    "/recipes/deep-dish-pizza": [
        "Whole Wheat Deep Dish Pizza Pie",
        "deep dish pizza",
        "deep dish"
    ],
    "/recipes/double-pumpkin-brownies": [
        "Double Pumpkin Brownies",
        "pumpkin brownies"
    ],
    "/recipes/dual-bean-date-brookies": [
        "Dual Bean Date Brookies",
        "dual bean date brookie",
        "bean brookies",
        "bean brookie"
    ],
    "/recipes/easy-cheesecake": [
        "The Easiest (Healthy) Cheesecake",
        "easy cheesecake",
        "cheesecake"
    ],
    "/recipes/easy-cheesecake#lemon-blueberry": [
        "lemon blueberry cheesecake",
        "blueberry lemon cheesecake"
    ],
    "/recipes/easy-pizza-dough": [
        "Easy Pizza Dough"
    ],
    "/recipes/edible-cookie-dough-bites": [
        "Edible Cookie Dough Bites",
        "edible cookie dough"
    ],
    "/recipes/edible-cookie-dough-protein": [
        "Edible Cookie Dough with Protein"
    ],
    "/recipes/egg-roll-bowl": [
        "Egg Roll Skillet Bowls",
        "egg roll"
    ],
    "/recipes/eggplant-pizza": [
        "Mini Eggplant Pizzas",
        "mini eggplant pizza",
        "eggplant pizzas",
        "eggplant pizza"
    ],
    "/recipes/eggplant-salad": [
        "Grilled Eggplant and Chickpea Salad"
        "eggplant and chickpea salad"
    ],
    "/recipes/electrolyte-protein-shake": [
        "Electrolyte Protein Shake"
    ],
    "/recipes/energy-bites": [
        "No Bake Energy Bites",
        "energy bites"
    ],
    "/recipes/fajitas": [
        "Chicken Fajitas with Peppers",
        "chicken fajitas",
        "fajitas"
    ],
    "/recipes/farro-bowls": [
        "Chicken Farro Bowls with Goat Cheese"
    ],
    "/recipes/fatty-yogurt": [
        "Fatty Yogurt"
    ],
    "/recipes/feta-pasta": [
        "Viral Baked Feta Pasta",
        "feta pasta"
    ],
    "/recipes/fiber-one-brownies": [
        "Copycat Fiber One Brownies",
        "fiber one brownies",
        "copycat fiber one brownie",
        "fiber one brownie"
    ],
    "/recipes/fig-walnut-energy-bites": [
        "Fig & Walnut Energy Bites"
    ],
    "/recipes/fra-diavolo": [
        "Shrimp Fra Diavolo con Spinach",
        "shrimp fra diavolo",
        "fra diavolo"
    ],
    "/recipes/french-onion-miso-soup": [
        "French Onion & Miso Soup Crossover Event",
        "french onion miso soup",
        "french onino soup",
        "miso soup"
    ],
    "/recipes/frittata": [
        "Spinach and Onion Frittata",
        "frittata"
    ],
    "/recipes/greek-lemon-potatoes": [
        "Lower Oil Greek Lemon Potatoes",
        "greek lemon potatoes",
        "greek potatoes"
    ],
    "/recipes/greek-salad": [
        "Greek Salad with Chicken",
        "greek salad with grilled chicken",
        "greek salad"
    ],
    "/recipes/greek-yogurt-gnocchi": [
        "Greek Yogurt Whole Wheat Gnocchi",
        "whole wheat gnocchi",
        "gnocchi"
    ],
    "/recipes/green-bread": [
        "Green Bread - No Food Dye",
        "green bread"
    ],
    "/recipes/green-eggs-and-ham": [
        "Green Eggs & Ham (Kinda)",
        "green eggs and ham"
    ],
    "/recipes/green-smoothie": [
        "Green Hemp Smoothie",
        "green smoothie",
        "hemp smoothie"
    ],
    "/recipes/grilled-shrimp": [
        "Grilled Shrimp Skewers",
        "grille dshrimp"
    ],
    "/recipes/ground-thanksgiving": [
        "Ground Thanksgiving"
    ],
    "/recipes/haggis": [
        "My Take on Haggis",
        "haggis"
    ],
    "/recipes/hard-boiled-egg-mayo": [
        "Hard Boiled Egg Mayo"
    ],
    "/recipes/higher-protein-scrambled-eggs": [
        "Higher Protein Scrambled Eggs"
    ],
    "/recipes/home-fries": [
        "Sweet Potato Home Fries",
        "home fries"
    ],
    "/recipes/hot-honey-beef-bowls": [
        "Hot Honey Beef Bowls",
        "hot honey beef bowl"
    ],
    "/recipes/hot-honey-cornbread": [
        "Hot Honey Cornbread"
    ],
    "/recipes/hummus": [
        "Lemony Taco Inspired Hummus",
        "taco hummus"
    ],
    "/recipes/indian-chicken": [
        "Indian Chicken and Potatoes",
        "indian chicken",
        "indian potatoes"
    ],
    "/recipes/iron-bowl": [
        "The Iron Bowl",
        "iron bowl"
    ],
    "/recipes/italian-chicken": [
        "Roasted Italian Chicken Breast and Acorn Squash",
        "roasted italian chicken"
    ],
    "/recipes/italian-dressing": [
        "Homemade Sugar Free Italian Dressing",
        "homemade italian dressing"
    ],
    "/recipes/just-one-cookie": [
        "Just One Cookie"
    ],
    "/recipes/kale": [
        "Bean Kaled by Cheese"
    ],
    "/recipes/keto-brownies": [
        "Flourless Keto Brownies (2 g Net Carbs)",
        "flourless keto brownies",
        "keto brownies"
        "flourless keto brownie",
        "keto brownie"
    ],
    "/recipes/keto-chocolate-chip-cookies": [
        "Keto Chocolate Chip Cookies (3 g Net Carbs)",
        "keto chocolate chip cookies",
        "keto chocolate chip cookie",
        "keto cookies",
        "keto cookie"
    ],
    "/recipes/keto-fudge": [
        "Bittersweet Keto Fudge",
        "keto fudge"
    ],
    "/recipes/korean-chicken": [
        "Korean Inspired Chicken with Broccoli and Potatoes",
        "korean chicken"
    ],
    "/recipes/kung-pao-chicken": [
        "Nontraditional Kung Pao Chicken",
        "kung pao chicken"
    ],
    "/recipes/lactose-free-yogurt": [
        "Lactose Free, Sugar Free, Vanilla Greek Yogurt",
        "lactose free yogurt"
    ],
    "/recipes/lasagna-boats": [
        "Spaghetti Squash Lasagna Boats",
        "lasagna boats"
    ],
    "/recipes/lebanese-casserole": [
        "Lebanese Riced Cauliflower Casserole",
        "lebanese casserole"
    ],
    "/recipes/lemon-feta-bowl": [
        "Lemon Feta Chicken Bowls"
    ],
    "/recipes/lemon-ginger-tea": [
        "Lemon Ginger Tea",
        "homemade tea"
    ],
    "/recipes/low-carb-pb-cookies": [
        "Low Carb Peanut Butter Cookies",
        "keto peanut butter cookies",
        "low carb peanut butter cookie",
        "keto peanut butter cookie"
    ],
    "/recipes/low-fodmap-chili": [
        "Low FODMAP Chili"
    ],
    "/recipes/low-fodmap-tacos": [
        "Low FODMAP Chicken Tacos"
    ],
    "/recipes/maafe": [
        "Maafe (African Peanut Stew)",
        "maafe",
        "african peanut stew",
        "peanut chicken stew",
        "peanut stew"
    ],
    "/recipes/mac-and-cheese": [
        "High Protein Mac & Cheese",
        "high protein mac and cheese",
        "mac & cheese",
        "mac and cheese"
    ],
    "/recipes/manhattan-clam-chowder": [
        "(No Longer Allowed In) Manhattan Clam Chowder",
        "manhattan clam chowder"
    ],
    "/recipes/marinated-chicken": [
        "Marinated Chicken with Air Fried Plantains",
        "marinated chicken",
        "grilled chicken with plantains",
        "grilled chicken"
    ],
    "/recipes/meatballs": [
        "Zoodles and Meatballs"
    ],
    "/recipes/mediterranean-pasta-salad": [
        "Mediterranean Pasta Salad",
        "pasta salad"
    ],
    "/recipes/mediterranean-potato-salad": [
        "Mediterranean Sweet Potato Salad",
        "sweet potato salad",
        "potato salad"
    ],
    "/recipes/milkshake": [
        "Chocolate Nut Milkshake",
        "milkshake"
    ],
    "/recipes/miso-hummus": [
        "East Asian Miso Hummus",
        "miso hummus"
    ],
    "/recipes/mom-oatmeal": [
        "Hi Mom, Here's Your Oatmeal"
    ],
    "/recipes/mushroom-soup": [
        "No Cream of Mushroom Soup",
        "mushroom soup"
    ],
    "/recipes/nam-sod": [
        "Nam Sod (Thai Pork Salad)",
        "nam sod"
    ],
    "/recipes/neopolitan-banana-ice-cream": [
        "Neopolitan Banana Ice Cream",
        "neopolitan ice cream"
    ],
    "/recipes/new-england-clam-chowder": [
        "(I'm Banned From) New England Clam Chowder",
        "new england clam chowder"
    ],
    "/recipes/nice-cream-sandwiches": [
        "Nice Cream Sandwiches",
        "banana ice cream sandwiches",
        "nice cream sandwich",
        "banana ice cream sandwich",
        "ice cream sandwiches",
        "ice cream sandwich"
    ],
    "/recipes/no-bake-brownies": [
        "No Bake Protein Brownies",
        "no bake brownies"
    ],
    "/recipes/no-nut-protein-banana-bread": [
        "No Nut Protein Banana Bread",
        "nut free protein banana bread",
        "no nut banana bread",
        "nut free banana bread"
    ],
    "/recipes/no-protein-bar": [
        "The No-Protein Bar",
        "the no protein bar",
        "no-protein bar",
        "no protein bar"
    ],
    "/recipes/no-protein-powder-oatmeal": [
        "Overnight Oats with no Protein Powder",
        "overnight oats without protein powder"
    ],
    "/recipes/no-stir-peanut-butter": [
        "Homemade Skippy Peanut Butter",
        "homemade no stir peanut butter"
    ],
    "/recipes/no-yogurt-oatmeal": [
        "Yogurt Free Protein Oats",
        "yogurt free protein oatmeal"
    ],
    "/recipes/nordic-nut-loaf": [
        "Nordic Nut Loaf (GF)"
    ],
    "/recipes/oat-milk": [
        "Homemade Plant Based Milk",
        "homemade almond milk",
        "homemade oat milk",
        "homemade plant based milk",
        "homemade dairy free milk",
        "homemade nut milk",
        "homemade peanut milk"
    ],
    "/recipes/oatmeal-berry-bars": [
        "Oatmeal Berry Breakfast Bars",
        "raspberry oatmeal bars",
        "oatmeal raspberry bars",
        "blueberry oatmeal bars",
        "oatmeal blueberry bars",
        "strawberry oatmeal bars",
        "oatmeal strawberry bars"
    ],
    "/recipes/oatmeal-chocolate-cookies": [
        "Oatmeal Chocolate Chip Cookies",
        "oatmeal chocolate chip cookie",
        "oatmeal cookies",
        "oatmeal cookie",
        "oatmeal chocolate cookies",
        "oatmeal chocolate cookie"
    ],
    "/recipes/oatmeal-fudge-bars": [
        "Peanut Butter Fudge Bars",
        "oatmeal fudge bars",
        "peanut butter oatmeal fudge bars",
        "peanut butter fudge oatmeal bars",
        "oatmeal peanut butter fudge bars",
        "oatmeal fudge peanut butter bars",
        "fudge bars",
        "peanut butter fudge bar"
    ],
    "/recipes/oats-banana": [
        "Banana Nut Bread Protein Overnight Oats",
        "banana protein overnight oats",
        "banana oatmeal"
    ],
    "/recipes/oats-berry": [
        "Berry Delicious Protein Overnight Oats",
        "berry protein overnight oats",
        "berry oatmeal"
    ],
    "/recipes/oats-pb": [
        "Peanut Butter Punch Protein Overnight Oats",
        "peanut butter protein overnight oats",
        "peanut butter oatmeal"
    ],
    "/recipes/oats-pumpkin": [
        "Pumpkin Pie Protein Overnight Oats",
        "pumpkin protein overnight oats",
        "pumpkin oatmeal"
    ],
    "/recipes/oats-reeses": [
        "Reese's Protein Overnight Oats",
        "peanut butter chocolate overnight oats",
        "chocolate peanut butter overnight oats",
        "peanut butter chocolate oatmeal",
        "chocolate peanut butter oatmeal"
    ],
    "/recipes/oil-free-basil-pesto": [
        "Oil Free Basil Pesto",
        "basil pesto"
    ],
    "/recipes/olivcado": [
        "Olivcado Salad Dressing",
        "homemade caesar dressing",
        "homemade caesar",
        "olivcado dressing"
    ],
    "/recipes/olive-dip": [
        "Balsamic Olive Spread",
        "olive spread",
        "olive dip"
    ],
    "/recipes/omega-3-yogurt-bowl": [
        "Omega-3 Yogurt Bowl",
        "omega 3 yogurt bowl"
    ],
    "/recipes/onion-soup-bread": [
        "Onion Soup Bread"
    ],
    "/recipes/pad-thai": [
        "Chicken Pad Thai with Spaghetti Squash",
        "chicken pad thai",
        "pad thai"
    ],
    "/recipes/pan-de-higo": [
        "Pan de Higo / Larabars",
        "larabars",
        "larabar",
        "pan de higo"
    ],
    "/recipes/pancake": [
        "Pumpkin Protein Pancakes",
        "pumpkin protein pancake",
        "pumpkin pancakes",
        "pumpkin pancake"
    ],
    "/recipes/parmesan-broccoli": [
        "Parmesan Crusted Roasted Broccoli",
        "parmesan broccoli"
    ],
    "/recipes/pb-bread": [
        "Peanut Butter Bread"
    ],
    "/recipes/pb-cups": [
        "Low Cal PB Cups",
        "low calorie peanut butter cups",
        "low calorie pb cups",
        "low cal peanut butter cups",
        "Low Cal PB Cup",
        "low calorie peanut butter cup",
        "low calorie pb cup",
        "low cal peanut butter cup"
    ],
    "/recipes/pbj-muffin": [
        "Peanut Butter & Jelly Muffins",
        "peanut butter and jelly muffins",
        "peanut butter & jelly muffin",
        "peanut butter and jelly muffin",
        "pb&j muffins",
        "pb&j muffin"
        "pb & j muffins",
        "pb & j muffin"
    ],
    "/recipes/peanut-butter-banana-bake": [
        "Peanut Butter Banana Bars",
        "peanut butter banana bar",
        "banana oatmeal bars",
        "banana oatmeal bar",
        "oatmeal banana bars",
        "oatmeal banana bar",
        "peanut butter oatmeal bars",
        "peanut butter oatmeal bar"
    ],
    "/recipes/peanut-butter-bars": [
        "No Bake Peanut Butter Bars",
        "peanut butter bars",
        "no bake peanut butter bar",
        "peanut butter bars"
    ],
    "/recipes/peanut-butter-chili": [
        "High Protein Peanut Butter Chili",
        "peanut butter chili"
    ],
    "/recipes/peanut-butter-cookies": [
        "Honey Sweetened Peanut Butter Cookies",
        "honey peanut butter cookies",
        "honey sweetened peanut butter cookie",
        "honey peanut butter cookies",
        "peanut butter honey cookies",
        "peanut butter honey cookie",
        "peanut butter cookies",
        "Peanut butter cookie"
    ],
    "/recipes/peanut-butter-pie": [
        "Peanut Butter Banana Pie",
        "peanut butter pie"
    ],
    "/recipes/peanut-chicken": [
        "Peanut Chili Chicken Skillet",
        "peanut chicken chili skillet"
    ],
    "/recipes/peanut-chili-salad-dressing": [
        "Peanut Chili Salad Dressing",
        "peanut salad dressing",
        "peanut dressing"
    ],
    "/recipes/pecan-cream-cheese-cookies": [
        "Pecan Cream Cheese Cookies",
        "pecan cookies",
        "pecan cream cheese cookie",
        "pecan cookie"
    ],
    "/recipes/pecan-pie-bars": [
        "No Bake Pecan Pie Bars",
        "no bake pecan pie bar",
        "no bake pecan pie",
        "pecan pie"
    ],
    "/recipes/penne-casserole": [
        "Penne and Meat Casserole Bake",
        "penne & meat casserole bake",
        "penne and meat casserole",
        "penne & meat casserole",
        "Penne and beef Casserole Bake",
        "penne & beef casserole bake",
        "penne and beef casserole",
        "penne & beef casserole"
    ],
    "/recipes/pesto-goat-cheese-mac-and-cheese": [
        "Pesto Goat Cheese Mac & Cheese",
        "pesto goat cheese"
    ],
    "/recipes/pickle-ketchup": [
        "Pickle Ketchup with Hot Honey",
        "pickle ketchup"
    ],
    "/recipes/plantain-chips": [
        "Air Fryer Plantain Chips"
    ],
    "/recipes/poor-mans-ice-cream": [
        "Poor Man's Ice Cream"
    ],
    "/recipes/popcorn": [
        "Healthy Microwave Popcorn",
        "homemade popcorn"
    ],
    "/recipes/pork-tenderloin": [
        "Roasted Pork Tenderloin & Veggies"
    ],
    "/recipes/protein-candy-bars": [
        "Caramel Protein Candy Bars",
        "protein candy bars",
        "caramel protein candy bar",
        "protein candy bar"
    ],
    "/recipes/protein-chocolate-bar": [
        "Protein Chocolate Bar"
    ],
    "/recipes/protein-cinnamon-rolls": [
        "Fluffy Protein Cinnamon Rolls",
        "protein cinnamon rolls",
        "fluffy protein cinnamon roll",
        "protein cinnamon roll",
        "homemade cinnamon rolls",
        "homemade cinnamon roll"
    ],
    "/recipes/protein-cookie-dough": [
        "Edible Protein Cookie Dough"
    ],
    "/recipes/protein-cookie-dough-bowl": [
        "Protein Cookie Dough Bowl"
    ],
    "/recipes/protein-mug-cake": [
        "Microwave Protein Mug Cake",
        "protein mug cake",
        "protien mug brownie",
        "microwave protein mug brownie",
        "mug cakes"
    ],
    "/recipes/protein-poptart": [
        "PB&J Protein PopTart",
        "homemade poptarts",
        "homemade poptart",
        "homemade pop tarts",
        "homemade pop tart"
    ],
    "/recipes/protein-pudding": [
        "Chocolate Protein Pudding",
        "protein pudding",
        "pudding"
    ],
    "/recipes/protein-slop": [
        "Protein Slop with Sweet Potatoes",
        "protein slop"
    ],
    "/recipes/protein-wrap": [
        "High Protein Flatbread Wrap",
        "protein wrap",
        "protein flatbread"
    ],
    "/recipes/pumpkin-bread": [
        "Protein Pumpkin Loaf",
        "protein pumpkin bread",
        "pumpkin bread",
        "pumpkin loaf"
    ],
    "/recipes/pumpkin-cake": [
        "Frosted Pumpkin Cake",
        "pumpkin cake"
    ],
    "/recipes/pumpkin-muffins": [
        "Pumpkin Chocolate Chip Mini Muffins",
        "pumpkin chocolate chip muffins"
        "pumpkin chocolate chip mini muffin",
        "pumpkin chocolate chip muffin",
        "pumkin chocolate mini muffins",
        "pumpkin chocolate muffins",
        "pumpkin chocolate mini muffin",
        "pumpkin chocolate muffin",
        "pumpkin mini muffins",
        "pumpkin mini muffin",
        "pumpkin muffins",
        "pumpkin muffin"
    ],
    "/recipes/pumpkin-pie": [
        "Perfect Protein Packed Pumpkin Pie",
        "protein pumpkin pie",
        "pumpkin pie"
    ],
    "/recipes/puree-veggie-soup": [
        "Pureed Roasted Veggie Soup",
        "tomato soup",
        "butternut squash soup"
    ],
    "/recipes/rainbow-cookies-v1": [
        "Monk Fruit Rainbow Cookies",
        "rainbow cookies v1",
        "monk fruit rainbow cookies"
    ],
    "/recipes/rainbow-cookies-v2": [
        "Dye Free Rainbow Cookies",
        "rainbow cookies v2",
        "dye free rainbow cookies"
    ],
    "/recipes/rainbow-cookies-v3": [
        "Rainbow Cookies v3",
        "rainbow cookies",
        "rainbow cookie",
        "homemade rainbow cookies",
        "homemade rainbow cookie",
        "italian rainbow cookies",
        "italian rainbow cookie",
        "homemade italian rainbow cookies",
        "homemade italian rainbow cookie"
    ],
    "/recipes/raspberry-brownies": [
        "Chocolate Raspberry Brownies",
        "raspberry brownies",
        "chocolate raspberry brownie",
        "raspberry brownie"
    ],
    "/recipes/ratatouille": [
        "Simple Ratatouille Stew",
        "ratatouille stew",
        "ratatouille"
    ],
    "/recipes/reconstituted-peanut-butter": [
        "Reconstituted Peanut Butter"
    ],
    "/recipes/red-lentils": [
        "Easy Red Lentils"
    ],
    "/recipes/refried-beans": [
        "Refried Pinto Beans"
    ],
    "/recipes/roasted-beet-hummus": [
        "Creamy Roasted Beet Hummus",
        "beet hummus"
    ],
    "/recipes/roasted-eggplant-hummus": [
        "Mediterranean Roasted Eggplant Hummus",
        "eggplant hummus"
    ],
    "/recipes/roasted-garlic-hummus": [
        '"Cheesy" Garlic Hummus',
        "'Cheesy' Garlic Hummus",
        "cheesy garlic hummus",
        "garlic hummus"
    ],
    "/recipes/roasted-onion": [
        "You Can Roast a Whole Onion",
        "roasted onion"
    ],
    "/recipes/roasted-red-pepper-hummus": [
        "Roasted Red Pepper Hummus"
        "red pepper hummus",
        "roasted pepper hummus",
        "pepper hummus"
    ],
    "/recipes/running-club-broccoli": [
        "Running Club Broccoli"
    ],
    "/recipes/salad-base": [
        "Salad Base For Your Fridge",
        "salad base"
    ],
    "/recipes/salmon-and-crunchy-salad": [
        "Simply Baked Salmon and Crunchy Salad",
        "crunchy salad",
        "simply baked salmon",
        "grilled salmon"
    ],
    "/recipes/salsa-chicken": [
        "Two Ingredient Salsa Chicken",
        "2 ingredient salsa chicken",
        "salsa chicken"
    ],
    "/recipes/secret-truffles": [
        "Secret Truffles"
    ],
    "/recipes/seven-layer-bars": [
        "7-Layer Bars",
        "hello dollies",
        "magic cookie bars",
        "7 layer bars"
    ],
    "/recipes/shakshuka": [
        "Tomato and Egg Shakshuka",
        "shakshuka"
    ],
    "/recipes/shawarma-turkey-kebabs": [
        "Shawarma Turkey Kebabs",
        "turkey kebabs",
        "shwarma turkey kebab",
        "turkey kebabs",
        "kebebs",
        "kebab"
    ],
    "/recipes/shepards-pie": [
        "Cauliflower Mash Shepard's Pie",
        "shepard's pie",
        "shepards pie"
    ],
    "/recipes/shredded-chicken": [
        "Simple Shredded Chicken",
        "shredded chicken",
        "leftover cooked chicken"
        "shredded cooked chicken",
        "cooked chicken"
    ],
    "/recipes/sleepy-smoothie": [
        "Golden Milk, aka Sleepy Smoothie",
        "sleepy smoothie",
        "golden milk"
    ],
    "/recipes/sloppy-joe": [
        "Sloppy Joe Skillets",
        "sloppy joe's",
        "sloppy joes"
    ],
    "/recipes/sourdough-flatbread": [
        "Sourdough Discard Flatbread",
        "sourdough discard flatbreads",
        "sourdough flatbread",
        "sourdough flatbreads",
        "discard flatbread",
        "discard flatbreads"
    ],
    "/recipes/soy-sauce-chicken": [
        "Soy Sauce Chicken and Brussel Sprouts",
        "soy sauce chicken"
    ],
    "/recipes/spaghetti-and-meatballs": [
        "Spaghetti (Squash) & (Gluten Free) Meatballs",
        "spaghetti squash & gluten free meatballs",
        "Spaghetti (Squash) and (Gluten Free) Meatballs",
        "spaghetti squash and gluten free meatballs",
        "Spaghetti & Meatballs",
        "spaghetti and meatballs",
        "Spaghetti squash & Meatballs",
        "spaghetti squash and meatballs"
    ],
    "/recipes/spaghetti-taco": [
        "Spaghetti Tacos with Zoodles",
        "spaghetti tacos",
        "spaghetti taco"
    ],
    "/recipes/spinach-mushroom-scrambled-eggs": [
        "Spinach & Mushroom Scrambled Eggs"
    ],
    "/recipes/steamed-veggies": [
        "Steamed Vegetables That Don't Suck",
        "steamed vegetables"
    ],
    "/recipes/stovetop-oatmeal": [
        "Stovetop Apple Oatmeal",
        "apple oatmeal"
    ],
    "/recipes/strawberry-chia-oatmeal": [
        "Strawberry Chia Protein Oatmeal",
        "strawberry oatmeal",
        "strawberry chia overnight oats"
    ],
    "/recipes/stuffed-grape-leaves": [
        "Dolmas (Stuffed Grape Leaves)",
        "dolmas",
        "dolma",
        "stuffed grape leaves",
        "stuffed grape leaf"
    ],
    "/recipes/stuffed-peppers": [
        "Turkey & Rice Stuffed Bell Peppers",
        "stuffed bell peppers",
        "stuffed peppers"
    ],
    "/recipes/styrofoam-cookies": [
        "Nut Butter Styrofoam Cookies",
        "styrofoam cookies",
        "nut butter styrofoam cookie",
        "styrofoam cookie"
    ],
    "/recipes/sugar-free-fudge": [
        # "fudge",
        "3 Ingredient Sugar Free Fudge",
        "three ingredient sugar free fudge",
        "sugar free fudge"
    ],
    "/recipes/three-ingredient-fudge": [
        "3 ingredient fudge",
        "three ingredient fudge",
        "peanut butter chocolate fudge",
        "chocolate peanut butter fudge",
        "bulking fudge",
        "weight gain fudge",
        "clean bulking fudge",
        "bittersweet fudge",
        "bittersweet chocolate fudge",
        "bitter fudge",
        "bitter chocolate fudge"
    ],
    "/recipes/superfood-bowls": [
        "Date Night Superfood Bowls",
        "superfood bowls",
        "superfood bowl"
    ],
    "/recipes/sweet-potato-banana-muffins": [
        "Sweet Potato Banana Muffins",
        "sweet potato banana mini muffins",
        "sweet potato banana mini-muffins",
        "sweet potato banana muffin",
        "sweet potato muffins",
        "sweet potato mini-muffins",
        "sweet potato mini muffins",
        "sweet potato muffin",
        "sweet potato mini muffin",
        "sweet potato mini-muffins"
    ],
    "/recipes/sweet-potato-blondies": [
        "Sweet Potato Blondies",
        "sweet potato blondie"
    ],
    "/recipes/sweet-potato-bread": [
        "Whole Wheat Sweet Potato Loaf",
        "whole wheat sweet potato bread",
        "sweet potato loaf",
        "sweet potato bread",
        "potato loaf",
        "potato bread"
    ],
    "/recipes/sweet-potato-brownies": [
        "Sweet Potato Brownies (SF)",
        "sweet potato brownies",
        "sweet potato brownie"
    ],
    "/recipes/sweet-potato-hummus": [
        "Golden Sweet Potato Hummus",
        "sweet potato hummus"
    ],
    "/recipes/sweet-potato-pie": [
        "Crustless Sweet Potato Pie",
        "sweet potato pie"
    ],
    "/recipes/sweet-potato-yogurt": [
        "Sweet Potato Yogurt with Sliced Strawberries",
        "sweet potato yogurt"
    ],
    "/recipes/thin-mints": [
        "Homemade Thin Mint Cookies",
        "homemade thin mints",
        "homemade thin mint"
    ],
    "/recipes/three-ingredient-brownies": [
        "Three Ingredient Brownie Bites",
        "3 ingredient brownie bites",
        "brownie bites",
        "brownie bite"
    ],
    "/recipes/three-sisters": [
        "Three Sisters - Squash, Beans, and Corn",
        "3 sisters - squash, beans, and corn",
        "three sisters",
        "3 sisters"
    ],
    "/recipes/tilapia": [
        "Air Fried Tilapia from Frozen",
        "air fried tilapia"
    ],
    "/recipes/tiramisu": [
        "No Bake Homemade Tiramisù",
        "homemade Tiramisù",
        "No Bake Homemade Tiramisu",
        "homemade Tiramisu",
        "Tiramisù",
        "Tiramisu",
    ],
    "/recipes/tofu-scramble": [
        "Vegan Tofu Scramble",
        "tofu scramble"
    ],
    "/recipes/tomato-pesto": [
        "Tomato Paste-o",
        "tomato pesto"
    ],
    "/recipes/trail-mix-balls": [
        "Trail Mix Balls",
        "trail mix ball"
    ],
    "/recipes/tropical-salsa": [
        "Tropical Fruit Salsa",
        "fruit salsa"
    ],
    "/recipes/truffles": [
        "Chocolate Covered Truffles",
        "oreo balls",
        "chocolate covered truffle",
        "oreo ball",
        "cottage cheese truffles",
        "cottage cheese truffle"
    ],
    "/recipes/tuna-salad": [
        "No-Mayo Tuna Salad",
        "tuna salad"
    ],
    "/recipes/turkey-pesto-pita": [
        "Tomato Pesto Turkey Pitas"
    ],
    "/recipes/two-ingredient-oat-cookies": [
        "Two Ingredient Oat Cookies",
        "2 ingredient oat cookies",
        "two ingredient oat cookie",
        "2 ingredient oat cookie",
        "Two Ingredient Oatmeal Cookies",
        "2 ingredient Oatmeal cookies",
        "two ingredient Oatmeal cookie",
        "2 ingredient Oatmeal cookie"
    ],
    "/recipes/vegan-chili": [
        "Creamy Vegan White Bean Chili",
        "vegan chili"
    ],
    "/recipes/vegan-chocolate-cheesecake": [
        # "cheesecake",
        "Vegan Chocolate Cheesecake Bars",
        "vegan cheesecake bars",
        "vegan chocolate cheesecake bar",
        "vegan cheesecake bars",
        "vegan cheesecake",
        "chocolate cheesecake bars",
        "chocolate cheesecake bar",
        "chocolate cheesecake"
    ],
    "/recipes/vegan-cornbread": [
        "Vegan Cajun Cornbread",
        "vegan cornbread",
        "cajun cornbread"
    ],
    "/recipes/vegan-mac-and-cheese": [
        '"Mac" & "Cheese"',
        "'Mac' & 'Cheese'",
        '"Mac" and "Cheese"',
        "'Mac' and 'Cheese'"
    ],
    "/recipes/vegan-pasta-salad": [
        "Sun Dried Tomato Pasta Salad"
    ],
    "/recipes/vegetable-medley": [
        "Spinach & Onion Vegetable Medley"
    ],
    "/recipes/vegetarian-meal": [
        "A Complete Vegetarian Meal"
    ],
    "/recipes/vegetarian-soup": [
        "Vegetarian Dump & Go Soup",
        "dump & go soup",
        "Vegetarian Dump and Go Soup",
        "dump and go soup"
    ],
    "/recipes/vic-oats": [
        "Very Vic",
        "vic oatmeal",
        "vic oats"
    ],
    "/recipes/vic-yogurt": [
        "Yogurt - For Those Who Hate It",
        "yogurt for those who hate it"
    ],
    "/recipes/wacky-cake": [
        "The Wacky Cake",
        "wacky cake"
    ],
    "/recipes/waffle-fries": [
        "Sweet Potato Waffle Fries",
        "waffle fries"
    ],
    "/recipes/whipped-cream": [
        "Aquafaba Whipped Cream (Sugar Free and Vegan)",
        "aquafaba whipped cream",
        "sugar free whipped cream",
        "vegan whipped cream",
        "dairy free whipped cream"
    ],
    "/recipes/whipped-feta-spread": [
        "Whipped Feta Spread",
        "feta spread"
    ],
    "/recipes/white-bean-croutons": [
        "White Bean Croutons",
        "gluten free croutons"
    ],
    "/recipes/white-bean-milkshake": [
        "White Bean Milkshake"
    ],
    "/recipes/whole-wheat-beer-bread": [
        "Whole Wheat Beer Bread",
        "beef bread"
    ],
    "/recipes/yellow-rice": [
        "Anti-Inflammatory Yellow(ish) Rice",
        "Anti-Inflammatory Yellow Rice",
        "yellow rice"
    ],
    "/recipes/yogurt-apple": [
        "Apple Pie Yogurt Bowl",
        "apple yogurt bowl"
    ],
    "/recipes/yogurt-banana": [
        "Peanut Butter Banana Yogurt Bowl",
        "peanut butter yogurt bowl"
    ],
    "/recipes/yogurt-bark": [
        "Blueberry Yogurt Bark",
        "yogurt bark"
    ],
    "/recipes/yogurt-choc": [
        "Chocolate Almond Yogurt Bowl",
        "chocolate yogurt bowl"
    ],
    "/recipes/yogurt-pbj": [
        "Peanut Butter and Jelly Yogurt Bowl",
        "peanut butter & jelly yogurt bowl"
    ],
    "/recipes/zero-calorie-cookies": [
        "Zero Calorie Cookies",
        "0 calorie cookies"
    ],
    "/recipes/zucchini-wedges": [
        "Parmesan Crusted Zucchini Wedges",
        "zucchini wedges",
        "zucchini fries"
    ],
    "/recipes/chocolate-free-chocolate": [
        "Chocolate Free Chocolate",
        "carob chocolate bar"
    ],
    "/recipes/pecan-butter-bars": [
        "carob pecan butter bars",
        "carob pecan butter bar",
        "pecan butter bars",
        "pecan butter bar"
    ],
    "/recipes/cornbread": [
        # "homemade cornbread",
        # "healthier cornbread",
        # "healthy cornbread",
        "cheesy protein cornbread",
        "sugar free cornbread",
        "sugar-free cornbread"
    ],
    "/recipes/cottage-cheese-rolls": [
        "cottage cheese oat rolls",
        "cottage cheese oat roll",
        "cottage cheese rolls",
        "cottage cheese roll",
        "oat rolls",
        "oat roll"
    ],
    "/recipes/hot-honey": [
        "homemade hot honey",
        "hot honey"
    ],
    "/recipes/trail-mix": [
        "homemade trail mix",
        "mixed nuts & chocolate trail mix"
    ],
    "/recipes/granola": [
        "homemade granola",
        "low sugar granola"
    ],
    "/recipes/almond-flour-loaf": [
        "almond flour sandwich loaf",
        "almond flour loaf",
        "almond flour bread",
        "gluten free bread"
    ],
    "/recipes/almond-flour-rolls": [
        "almond flour rolls & bagels",
        "almond flour rolls",
        "almond flour roll",
        "almond flour bagels",
        "almond flour bagel"
        "gluten free rolls",
        "gluten free roll",
        "gluten free bagels",
        "gluten free bagel"
    ],
    "/recipes/triscuits": [
        "homemade crackers",
        "homemade cracker",
        "homemade triscuits",
        "homemade triscuit",
        "copycat triscuits",
        "copycat triscuit",
        "whole wheat crackers",
        "whole wheat cracker"
    ],
    "/recipes/flaxseed-crackers": [
        "gluten free flaxseed crackers",
        "gluten free flaxseed cracker",
        "gluten free flax seed crackers",
        "gluten free flax seed cracker",
        "gluten free crackers",
        "gluten free cracker",
        "flaxseed crackers",
        "flaxseed cracker",
        "flax seed crackers",
        "flax seed cracker"
    ],
    "/recipes/granola-bars": [
        "homemade granola bars",
        "homemade granola bar",
        "peanut butter banana granola bars",
        "peanut butter banana granola bar"
    ],
    "/recipes/pie-crust": [
        "healthier graham cracker pie crust, chocolate",
        "healthier graham cracker pie crust",
        "graham cracker pie crust",
        "graham cracker crust",
        "homemade pie crust",
        "homemade graham cracker crust"
    ],
    "/recipes/nutella": [
        "homemade nutella",
        "roasted hazelnut nutella (sf)",
        "roasted hazelnut nutella",
        "hazelnut nutella",
        "healthier nutella",
        "healthy nutella",
        "sugar free nutella",
        "sugar-free nutella"
    ],
    "/recipes/chickpea-nutella": [
        "no-nut chickpea nutella",
        "no nut chickpea nutella",
        "nut free nutella",
        "chickpea nutella",
        "low fat nutella",
        "fat free nutella"
    ],
    "/recipes/quick-nutella": [
        "single serving quick nutella",
        "quick nutella",
        "powdered peanut butter nutella",
        # "chocolate spread",
        "sugar free chocolate spread",
        "sugar-free chocolate spread"
    ],
    "/recipes/protein-nutella": [
        "protein nutella",
        "high protein nutella",
        "high protein chocolate spread",
        "high protein nutella copycat",
        "protein nutella copycat",
        "protein copycat nutella",
        "high protein copycat nutella",
        "yogurt nutella"
    ],
    "/recipes/gf-crackers": [
        "gluten free graham crackers",
        "gluten free graham cracker",
        "homemade graham crackers",
        "homemade graham cracker",
        "healthier graham crackers",
        "healthier graham cracker",
        "healthy graham crackers",
        "healthy graham cracker"
    ],
    "/recipes/pizza": [
        # "pizza",
        # "pizza dough",
        "home oven baked pizza",
        "homemade pizza dough",
        "homemade pizza"
    ],
    "/recipes/slow-cooked-beans": [
        "slow cooker dried beans",
        "homemade beans",
        "crockpot beans",
        "make the beans from scratch",
        "beans from scratch"
    ],
    "/misc/homemade-cheese#labneh": [
        "labneh cheese, whole milk",
        "labneh cheese, skim",
        "labneh cheese",
        "labneh"
    ],
    "/misc/ground-chicken": [
        "ground chicken",
        "ground chicken thighs",
        "ground chicken breasts",
        "how to make ground chicken"
    ],
    "/recipes/tortilla": [
        "oat-wheat tortillas",
        "oat wheat tortillas",
        "whole wheat tortillas",
        "whole wheat tortilla",
        "tortillas",
        "tortilla"
    ],
    "/recipes/apple-spread": [
        "apple spread",
        "appe butter",
        "no sugar added apple spread",
        "unsweetened apple spread",
        "unsweetened apple butter"
    ],
    "/recipes/chocolate-almond-butter": [
        "chocolate almond butter"
    ],
    "/recipes/maple-cinnamon-peanut-butter": [
        "maple cinnamon peanut butter"
    ],
    "/recipes/white-chocolate-walnut-butter": [
        "white chocolate walnut butter"
    ],
    "/recipes/mint-pistachio-butter": [
        "mint pistachio butter"
    ],
    "/recipes/cashew-cookie-butter": [
        "cashew cookie butter"
    ],
    "/recipes/super-seed-butter": [
        "super seed butter"
    ],
    "/recipes/protein-shake": [
        "simple protein shake",
        "protein shake",
        "protein shakes"
    ],
    "/recipes/protein-bar": [
        "100 calorie protein bars"
    ],
    "/recipes/taco": [
        "taco",
        "tacos"
    ],
    "/recipes/pita": [
        "pita",
        "pita bread",
        "pocket pita",
        "whole wheat pita bread",
        "whole wheat pita"
    ],
    "/recipes/pretzel": [
        "whole wheat hot pretzels",
        "whole wheat hot pretzel",
        "hot pretzels",
        "hot pretzel",
        "homemade hot pretzels",
        "homemade hot pretzel"
        "homemade pretzels",
        "homemade pretzel"
    ],
    "/recipes/gluten-free-pretzels": [
        "gluten free savory pretzels",
        "gluten free savory pretzel",
        "gluten free pretzels",
        "gluten free pretzel",
        "savory pretzels",
        "savory pretzel",
        "almond flour pretzels",
        "almond flour pretzel",
        "homemade gluten free pretzels",
        "homemade gluten free pretzel"
    ],
    "/recipes/chia-pudding": [
        "chia pudding"
    ],
    "/recipes/berry-jam": [
        "homemade jam",
        "homemade jelly",
        "homemade blackberry jam",
        "low sugar berry jam",
        "no sugar berry jam",
        "sugar free berry jam",
        "low sugar jam",
        "no sugar jam",
        "sugar free jam",
        "berry jam",
        "raspberry jam",
        "raspberry jelly",
        "blackberry jam",
        "blackberry jelly",
        "jam",
        "jelly"
    ],
    "/recipes/strawberry-chia-jam": [
        "strawberry jam",
        "blueberry jam",
        "chia jam",
        "strawberry jelly",
        "blueberry jelly",
        "chia jelly",
        "strawberry chia jam",
        "strawberry chia jelly",
        "blueberry chia jam",
        "blueberry chia jelly",
        "homemade chia jam",
        "homemade chia jelly"
    ],
    "/misc/whole-wheat-sourdough#starter": [
        "starter",
        "sourdough starter",
        "whole wheat sourdough starter",
        "sourdough discard"
    ],
    "/misc/whole-wheat-sourdough#bread-recipe": [
        "sourdough",
        "sourdough bread",
        "whole wheat sourdough bread",
        "sourdough loaf",
        "whole wheat sourdough loaf"
    ],
    "/misc/slow-cooker-chicken": [
        "chicken fat",
        "shmaltz",
        "homemade broth",
        "bone broth",
        "homemade chicken broth",
        "chicken bone broth",
        "slow cooking a whole chicken",
        "chicken broth",
        "homemade chicken fat",
        "rendered out chicken fat"
    ],
    "/recipes/seitan": [
        "seitan"
    ],
    "/recipes/pasta-sauce": [
        "simple pasta sauce",
        "pasta sauce",
        "marinara sauce"
    ],
    "/recipes/nice-cream": [
        "banana nice cream",
        "banana ice cream",
        "nice cream",
        "healthy ice cream",
        "homemade nice cream",
        "homemade ice cream",
        "chocolate banana nice cream",
        "chocolate banana ice cream"
    ],
    "/recipes/double-chocolate-banana-bread": [
        "double chocolate banana bread",
        "chocolate chip banana bread",
        "chocolate banana bread"
    ],
    "/recipes/cookie-bar": [
        "no bake cookie bars",
        "no bake cookie bar",
        "cookie bars",
        "cookie bar",
        "oat flour cookie bars",
        "oat flour cookie bar",
        "peanut butter banana cookie bars",
        "peanut butter banana cookie bar"
    ],
    "/recipes/salsa": [
        "five minute salsa (no garlic/onion)",
        "five minute salsa",
        "5 minute salsa (no garlic/onion)",
        "5 minute salsa",
        "homemade salsa",
        "salsa"
    ],
    "/recipes/guacamole": [
        "holy guacamole",
        "homemade guacamole",
        "homemade guac",
        "guacamole",
        "guac"
    ],
    "/recipes/hot-sauce": [
        "red jalapeno louisiana hot sauce",
        "homemade hot sauce",
        "hot sauce"
    ],
    "/recipes/sugar-free-syrup": [
        "homemade sugar free syrup",
        "homemade sugar-free syrup",
        "sugar free syrup",
        "sugar-free syrup",
        "sf syrup",
        "syrup",
        "sfs",
        "liquid sweeteners",
        "liquid sweetener",
        "liquid zero calorie sweetener",
        "sugar free sweeteners",
        "sugar free sweetener"
    ],
    "/recipes/natural-peanut-butter": [
        "homemade natural peanut butters",
        "homemade natural peanut butter",
        "homemade peanut butters",
        "homemade peanut butter",
        "homemade natural nut butters",
        "homemade natural nut butter",
        "homemade nut butters",
        "homemade nut butter",
        "homemade natural seed butters",
        "homemade natural seed butter",
        "homemade seed butters",
        "homemade seed butter",
        "natural peanut butters",
        "natural peanut butter",
        "nut/seed butters",
        "natural nut or seed butters",
        "natural nut or seed butter",
        "nut or seed butters",
        "nut/seed butter",
        "nut or seed butter",
        "real peanut butter",
        "natural nut butters",
        "natural seed butters",
        "natural nut butter",
        "homemade tahini",
        "natural seed butter",
        "nut butters",
        "seed butters",
        "nut butter",
        "seed butter",
        "'nut' butter",
        "pb"
    ],
    "/recipes/monkfruit-chocolate-chunks": [
        # "sugar free chocolate chips",
        # "sugar free chocolate chip",
        "sugar free chocolate"
        "sugar free chocolate chunks",
        "sugar free chocolate chunk",
        "monk fruit chocolate chips",
        "monk fruit chocolate chip",
        "monk fruit chocolate chunks",
        "monk fruit chocolate chunk",
        "sugar-free chocolate chips",
        "sugar-free chocolate chip",
        "sugar-free chocolate"
        "sugar-free chocolate chunks",
        "sugar-free chocolate chunk",
        "monkfruit chocolate chips",
        "monkfruit chocolate chip",
        "monkfruit chocolate chunks",
        "monkfruit chocolate chunk",
        "monk fruit chocolate",
        "monkfruit chocolate",
        "homemade sugar free chocolate"
    ],
    "/recipes/pumpkin-puree": [
        "roasted pumpkin puree",
        "homemade pumpkin puree",
        "pumpkin puree"
    ],
    "/recipes/sweet-potato-puree": [
        "roasted sweet potato puree",
        "homemade sweet potato puree",
        "sweet potato puree"
    ],
    "/recipes/roasted-butternut-squash-puree": [
        "roasted butternut squash puree",
        "homemade butternut squash puree",
        "butternut squash puree",
        "butternut puree"
    ],
    "/recipes/cottage-cheese-flatbread": [
        "cottage cheese flatbread",
        "cottage cheese flatbreads"
    ],
    "/recipes/cashew-ricotta-cheese": [
        "dairy free cashew ricotta cheese",
        "cashew ricotta cheese",
        "dairy free ricotta cheese",
        "dairy free ricotta",
        "cashew ricotta"
    ],
    "/recipes/smoothie": [
        "protein fruit smoothies",
        "protein fruit smoothie",
        "fruit smoothies",
        "fruit smoothie",
        "smoothies",
        "smoothie",
        "smoothie bowls",
        "smoothie bowl",
        "protein smoothie bowls",
        "protein smoothie bowl",
        "fruit smoothie bowls",
        "fruit smoothie bowl"
    ],
    "/recipes/ww-bread": [
        "my classic bread recipe",
        "whole wheat bread",
        "100% whole wheat bread",
        "homemade whole wheat bread"
    ],
    "/recipes/whole-wheat-bagels": [
        "whole wheat bagles",
        "whole wheat bagel"
    ],
    "/recipes/roasted-vegetables": [
        "roasted vegetables",
        "roasted vegetable",
        "roasted veggies",
        "roasted veggie",
        "roasted red peppers",
        "roasted red pepper",
        "roasted broccoli",
        "roasted cauliflower",
        "roasted butternut squash",
        "roasted brussel sprouts",
        "roasted acorn squash",
        "roasted spaghetti squash",
        "roasted beets",
        "roasted squash",
        "roasted beet",
        "roasted garlic",
        "roasted asparagus",
        "simply roasted vegetables",
        "simply roasted veggies",
        "simply roasted vegetable",
        "simply roasted veggie"
    ],
    "/misc/homemade-cheese#ricotta": [
        "ricotta cheese",
        "ricotta"
    ],
    "/recipes/bbq-sauce": [
        "homemade bbq sauce",
        "unsweetened bbq sauce",
        "sugar-free bbq sauce",
        "sugar free bbq sauce",
        "homemade barbeque sauce",
        "unsweetened barbeque sauce",
        "sugar-free barbeque sauce",
        "sugar free barbeque sauce"
    ],
    "/recipes/ketchup": [
        "sugar free ketchup",
        "date sweetened ketchup",
        "date-sweetened ketchup",
        "unsweetened ketchup"
    ],
    "/recipes/ketchup": [
        "pickle ketchup with hot honey",
        "pickle ketchup",
        "hot honey ketchup",
        "honey ketchup"
    ],
    "/recipes/chili": [
        "slow cooker chili",
        "crockpot chili",
        "homemade chili",
        "my chili recipe",
        "chili"
    ],
    "/recipes/creamy-pesto": [
        "creamy pesto dip",
        "creamy pesto",
        "cottage cheese pesto",
        "no oil pesto",
        "oil free pesto",
        "oil-free pesto",
        "spinach pesto"
    ],
    "/recipes/cheese-sauce": [
        "gooey cheese sauce",
        "cheese sauce",
        "homemade cheese sauce"
    ],
    "/recipes/two-ingredient-mac-and-cheese": [
        "two ingredient mac & cheese",
        "two ingredient mac and cheese",
        "homemade mac & cheese",
        "homemade mac and cheese"
    ],
    "/recipes/eggplant-rollatini": [
        "leaner eggplant rollatini",
        "eggplant rollatini",
        "rollatini"
        "gluten free eggplant rollatini",
        "gluten free rollatini",
        "manicotti"
    ],
    "/recipes/eggplant-parm": [
        "hassle free eggplant parm",
        "hassle free eggplant parmesan",
        "hassle free eggplant parmesean",
        "eggplant parmesan",
        "eggplant parmesean",
        "eggplant parm"
        "gluten free eggplant parmesean",
        "gluten free eggplant parmesan",
        "gluten free eggplant parm"
    ],
    "/recipes/vegetarian-protein-lasagna": [
        "vegetarian protein lasagna",
        "homemade lasagna",
        "protein lasagna",
        "vegetarian lasagna",
        "gluten free lasagna"
    ],
    "/recipes/mayo": [
        "lighter mayo substitute",
        "homemade mayo",
        "homemade mayonnaise",
        "homemade light mayo",
        "homemade mayonnaise",
        "greek yogurt mayonnaise",
        "greek yogurt mayo",
        "yogurt mayonnaise",
        "yogurt mayo"
    ],
    "/recipes/hollandaise": [
        "homemade hollandaise",
        "greek yogurt hollandaise sauce",
        "greek yogurt hollandaise",
        "yogurt hollandaise sauce",
        "yogurt hollandaise",
        "hollandaise sauce",
        "hollandaise"
    ],
    "/misc/garlic-paste": [
        "roasted garlic paste for your freezer",
        "roasted garlic paste",
        "garlic paste"
    ],
    "/recipes/date-frosting": [
        # "frosting",
        "date sweetened frosting",
        "sugar free frosting",
        "sugar-free frosting",
        "healthier frosting",
        "healthy frosting",
        "date frosting",
        "yogurt frosting",
        "cottage cheese frosting",
        "low fat frosting",
        "fat free frosting"
    ],
    "/recipes/pasta-with-clam-sauce": [
        "pasta with healthier clam sauce",
        "pasta with clam sauce",
        "clam sauce"
    ],
    "/recipes/babaganoush": [
        "lemon baba ganoush without oil",
        "lemon babaganoush without oil",
        "lemon babaganoush",
        "lemon baba ganoush",
        "eggplant babaganoush",
        "eggplant baba ganoush",
        "babaganoush",
        "baba ganoush"
    ],
    "/recipes/salmon-and-tzatziki": [
        "roasted salmon and sprouts with tzatziki",
        "roasted salmon and sprouts",
        "roasted salmon"
    ],
    "/recipes/tzatziki": [
        "tzatziki sauce",
        "greek yogurt tzatziki",
        "yogurt tzatziki",
        "tzatziki",
        "homemade tzatziki",
        "homemade tzatziki sauce"
    ],
    "/recipes/shrimp-oreganata": [
        "gluten free shrimp oreganata",
        "shrimp oreganata",
        "homemade breadcrumbs",
        "gluten free breadcrumbs",
        "breadcrumb mix",
        "gluten free breadcrumb mix",
        "homemade breadcrumb mix",
        "oat flour breadcrumb mix",
        "oat flour breadcrumbs"
    ],
    "/recipes/whole-wheat-baguettes": [
        "whole wheat baguettes",
        "whole wheat baguette",
        "homemade baguettes",
        "homemage baguette",
        "french bread",
        "french baguette",
        "italian bread",
        "club roll"
    ],
    "/recipes/core-power-milkshake": [
        "copycat core power protein milkshake",
        "copycat core power milkshake",
        "core power protein milkshake",
        "copycat core powder",
        "protein milkshake",
        "core power protein milkshake",
        "core power",
        "homemade core power milkshake",
        "homemade core power protein milkshake",
        "homemade protein core cpower milkshake",
        "homemade core powder",
        "homemade protein milkshake"
    ],
    "/recipes/rx-bars": [
        "copycat chocolate rx bars",
        "copycat rx bars",
        "chocolate rx bars",
        "copycat chocolate rx bar",
        "copycat rx bar",
        "chocolate rx bar",
        "homemade rx bars",
        "homemade rx bar",
        "rx bars",
        "rx bar"
    ],
    "/recipes/copycat-barebell": [
        "copycat barebell protein bars",
        "copycat barebell protein bar",
        "barebell protien bars",
        "barebell protein bar",
        "copycat barebell",
        "barebell",
        "homemade barebell protein bars",
        "homemade barebell protein bar",
        "homemade barebell"
        "barebell bars",
        "barebell bar",
        "barebell"
    ],
    "/recipes/copycat-quest-bars": [
        "copycat quest protein bars",
        "copycat quest protein bar",
        "quest protein bars",
        "quest protein bar",
        "homemade quest protein bars",
        "homemade quest protein bar",
        "homemade quest",
        "copycat quest",
        "quest bars",
        "quest bar",
        "quest"
    ],
    "/recipes/copycat-quest-cookie": [
        "copycat quest protein cookies",
        "copycat quest protein cookie",
        "copycat quest cookies",
        "copycat quest cookie",
        "quest protein cookies",
        "quest protein cookie",
        "homemade quest protein cookies",
        "homemade quest protein cookie",
        "homemade quest cookie",
        "homemade quest cookies",
        "quest cookies",
        "quest cookie"
        "protein cookies",
        "protein cookie"
    ],
    "/recipes/chobani-yogurt-drink": [
        "copycat chobani yogurt drink",
        "chobani yogurt drink",
        "copycat chobani",
        "homemade chobani yogurt drink"
    ],
    "/recipes/electrolyte-powder": [
        "copycat LMNT electrolyte powder",
        "homemade electrolyte powder",
        "LMNT",
        "electrolyte powder",
        "homemade electrolyte drink mix",
        "homemade electrolyte drink",
    ],
    "/misc/rotisserie-chicken-cost-analysis": [
        "store-bought rotisserie chicken",
        "storebought rotisserie chicken",
        "store bought rotisserie chicken",
        "rotisserie chicken",
        "💵 Rotisserie Chicken Cost Analysis",
        "Rotisserie Chicken Cost Analysis",
        "rotisserie chickens",
        "rotisserie chicken",
        "rotisserie"
    ],
    "/misc/chicken-thighs-cost-analysis": [
        "💲 Chicken Thighs Cost Analysis",
        "chicken thighs cost analysis"
    ],
    "/misc/bone-broth": [
        "homemade bone broth + veggie soup",
        "veggie soup",
        "homemade bone broth",
        "bone broth",
        "broth"
    ],
    "/recipes/gluten-free-millet-bread": [
        "gluten free millet bread",
        "millet bread"
    ],
    "/recipes/classic-tahini-hummus": [
        "classic tahini hummus",
        "classic hummus",
        "tahini hummus"
    ],
    "/recipes/veggie-ground": [
        "high protein veggie ground",
        "protein veggie ground",
        "veggie ground"
    ],
    "/recipes/baked-beans": [
        "no added sugar baked beans",
        "sugar free baked beans",
        "sugar-free baked beans",
        "homemade baked beans",
        "unsweetened baked beans"
    ],
    "/recipes/smores": [
        "indoor roasted s'mores",
        "indoor roasted smores",
        "indoor roasted s'more",
        "indoor roasted smore",
        "s'mores",
        "smores",
        "s'more",
        "smore"
    ],
    "/recipes/chicken-fat-chocolate-chip-cookies": [
        "chicken fat chocolate chip cookies",
        "chicken fat cookies",
        "chicken fat brownies",
        "chicken fat cookie",
        "chicken fat brownie",
        "chicken fat chocolate chip cookie"
    ],
    "/recipes/pretzel-nuggets": [
        "homemade peanut butter pretzel nuggets",
        "homemade peanut butter pretzel nugget",
        "peanut butter pretzel nuggets",
        "peanut butter pretzel nugget",
        "homemade pretzel nuggets",
        "homemade pretzel nugget"
    ],
    "/recipes/sugar-cookies": [
        "decorative sugar cookies",
        "decorative sugar cookie"
    ],
    "/recipes/coconut-banana-rum-cake": [
        "coconut banana rum cake",
        "coconut rum cake",
        "banana rum cake",
        "rum cake"
    ],
    "/recipes/classic-fudge": [
        "traditional fudge recipe",
        "traditional fudge",
        "classic fudge"
    ],
    "/recipes/brownies": [
        "classic fudgy brownies",
        "classic brownies",
        "classic fudgy brownie",
        "classic fudgy brownie",
        "traditional brownies",
        "traditional brownie",
        "my standard brownie recipe",
        "standard brownie recipe",
        "standard brownies",
        "standard brownie",
        "standard version of brownies"
    ],
    "/recipes/chocolate-chip-cookies": [
        "classic chocolate chip cookies",
        "classic cookies",
        "classic chocolate chip cookie",
        "classic cookie",
        "traditional chocolate chip cookies",
        "traditional cookies",
        "traditional chocolate chip cookie",
        "traditional cookie",
        "my standard chocolate chip cookie recipe",
        "my standard cookie recipe",
        "standard chocolate chip cookies",
        "standard cookies",
        "standard chocolate chip cookie",
        "standard cookie",
        "standard cookie dough",
        "traditional cookie dough",
        "classic cookie dough",
        "typical homemade cookie",
        "standard version of cookies",
    ],
    "/recipes/chocolate-chip-date-cookies": [
        "chocolate chip date cookies",
        "date cookies",
        "chocolate chip date cookie",
        "date cookie"
    ],
    "/recipes/double-chocolate-date-cookies": [
        "double chocolate date cookies",
        "double chocolate date cookie",
        "chocolate cookies",
        "chocolate cookie"
    ],
    "/recipes/peanut-butter-date-cookies": [
        "peanut butter date cookies",
        "peanut butter date cookie",
        "pb date cookies",
        "pb date cookie"
    ],
    "/recipes/mint-chocolate-chip-date-cookies": [
        "Mint Chocolate Chip Date Cookies",
        # "mint chocolate chip cookies",
        # "mint chocolate chip cookie",
        "mint date cookies",
        "mint date cookie",
        "mint chocolate date cookies",
        "mint chocolate date cookie",
        "mint cookies",
        "mint cookie",
        "mint chocolate cookies",
        "mint chocolate cookie",
        "mint chocolate chip date cookie"
    ],
    "/recipes/oatmeal-raisin-cookies": [
        "naturally sweetened oatmeal raisin cookies",
        "naturally sweetened oatmeal raisin cookie",
        "oatmeal raisin cookies",
        "oatmeal raisin cookie"
    ],
    "/recipes/cauliflower-rice": [
        "simple cauliflower rice",
        "cauliflower rice"
    ],
    "/recipes/burger-patties": [
        "simple burger patties",
        "simple burger patty",
        "burger patties",
        "burger patty",
        "burgers",
        "burger"
    ],
    "/recipes/burger-buns": [
        "no yeast whole wheat burger buns",
        "no yeast whole wheat burger bun",
        "no yeast burger buns",
        "no yeast burger bun",
        "whole wheat burger buns",
        "whole wheat burger bun",
        "burger buns",
        "burger bun"
    ],
    "/recipes/oat-wraps": [
        "gluten free oat wraps",
        "gluten free oat wrap",
        "gluten free wraps",
        "gluten free wrap",
        "oat wraps",
        "oat wrap",
        "wraps",
        "wrap"
    ],
    "/recipes/coconut-bread": [
        "gluten and grain free coconut bread",
        "gluten free coconut bread",
        "grain free coconut bread",
        "keto coconut bread",
        "coconut bread"
    ],
    "/recipes/irish-soda-bread": [
        "whole wheat and oat flour irish soda bread",
        "whole wheat irish soda bread",
        "oat flour irish soda bread",
        "irish soda bread",
        "soda bread"
    ],
    "/recipes/unsweetened-hot-cocoa": [
        "unsweetened hot cocoa",
        "unsweetened hot chocolate",
        "sugar-free hot cocoa",
        "sugar-free hot chocolate",
        "sugar free hot cocoa",
        "sugar free hot chocolate",
        "hot cocoa",
        # "healthy chocolate milk",
        "hot chocolate"
    ],
    "/recipes/hot-chocolate": [
        "high protein hot cocoa",
        "high protein hot chocolate",
        "protein hot cocoa",
        "protein hot chocolate"
    ],"/recipes/rice-and-beans": [
        "classic rice and beans",
        "classic rice & beans",
        "rice and beans",
        "rice & beans"
    ],
    "/recipes/avocado-toast": [
        "versatile avocado toast",
        "avocado toast"
    ],
    "/recipes/baked-sweet-potato": [
        "baked sweet potatoes",
        "baked sweet potato",
        "baked potatoes",
        "baked potato"
    ],
    "/recipes/pulled-chicken": [
        "bbq pulled chicken and coleslaw",
        "bbq pulled chicken",
        "pulled chicken",
        "pulled pork",
        "bbq chicken",
        "barbeque chicken",
        "barbeque pulled chicken and coleslaw",
        "barbeque pulled chicken"
    ],
    "/recipes/sweet-potato-fries": [
        "spices sweet potato fries",
        "sweet potato fries"
    ],
    "/recipes/chicken-jerky": [
        # "beef jerky",
        "air fryer chicken jerky",
        "chicken jerky"
    ],
    "/recipes/pickled-onions": [
        "quick pickled red onions",
        "pickled red onions",
        "quick pickled red onion",
        "pickled red onion",
        "quick pickled onions",
        "quick pickled onion",
        "pickled onions",
        "pickled onion",
        "pickled red onions",
        "pickled red onion"
    ],
    "/recipes/bolognese": [
        "dutch oven bolognese sauce",
        "homemade bolognese sauce",
        "homemade bolognese",
        "bolognese sauce",
        "bolognese"
    ],
    "/recipes/hard-boiled-egg": [
        "hard boiled eggs: stovetop or air fryer",
        "hard boiled egg: stovetop or air fryer"
        "hard boiled eggs",
        "hard boiled egg",
        "eggs, hard boiled",
        "egg, hard boiled"
    ],
    "/recipes/chocolate-bar": [
        "sugar free chocolate bar",
        "sugar-free chocolate bar",
        # "homemade chocolate bar",
        "unsweetened chocolate bar",
        "unsweetened 100% chocolate bar",
    ],
    "/misc/chocolate-percentages": [
        "make your own dark chocolate",
        "homemade dark chocolate",
        "homemade chocolate bars",
        "homemade chocolate bar",
        "homemade chocolate"
    ],
    "/misc/pinto-bean-cake": [
        "improving the pinto bean cake",
        "pinto bean cake"
    ],
    "/recipes/sugar-cookies": [
        "decorative sugar cookies",
        "decorative sugar cookie",
        "decorating sugar cookies",
        "decorating sugar cookie",
        "sugar cookies",
        "sugar cookie"
    ],
    "/misc/homemade-flours": [
        "homemade flours",
        "homemade flour"
    ],
    "/recipes/spaghetti-squash": [
        "spaghetti squash cooked 3 ways",
        "spaghetti squash cooked three ways",
        "cooked spaghetti squash"
    ],
    "/recipes/cloud-bread-loaf": [
        "cloud bread loaf",
        "cloud bread"
    ],
    "/recipes/keto-bread-loaf": [
        "keto bread loaf recipe",
        "keto bread loaf",
        "keto bread"
    ],
    "/recipes/cauliflower-pizza": [
        "gluten free pizza crust",
        "gluten free pizza",
        "cauliflower flaxseed pizza crust",
        "cauliflower flax seed pizza crust",
        "cauliflower flaxseed pizza",
        "cauliflower flax seed pizza",
        "cauliflower pizza"
    ],
    "/recipes/pico-de-gallo": [
        "simple pico de gallo",
        "homemade pico de gallo",
        "pico de gallo"
    ],
    "/recipes/no-honey-mustard": [
        "no-honey mustard dressing",
        "no honey mustard dressing",
        "honey mustard dressing",
        "no-honey mustard",
        "no honey mustard"
    ],
    "/recipes/buffalo-chicken-dip": [
        "high protein buffalo chicken dip",
        "homemade buffalo chicken dip",
        "buffalo chicken dip",
        "buffalo dip"
    ],
    "/recipes/spinach-artichoke-dip": [
        "lightened up spinach artichoke dip",
        "homemade spinach artichoke dip",
        "spinach artichoke dip",
        "spinach artichoke"
    ],
    "/recipes/cheese-bean-dip": [
        "cheesy bean dip",
        "homemade bean dip",
        "bean dip"
    ],
    "/recipes/greek-yogurt-caesar-dressing": [
        "greek yogurt caesar dressing",
        "yogurt carsear dressing",
        "greek yogurt casesar",
        "healthier caesar dressing",
        "healthy caesar dressing",
        "homemade caesar dressing"
    ],
    "/recipes/french-onion-dip": [
        "low fat french onion dip",
        "homemade french onion dip"
    ],
    "/recipes/caramelized-onions": [
        "slow cooker caramelized onions",
        "slow cooker caramelized onion",
        "caramelized onions",
        "caramelized onion"
    ],
    "/recipes/evoo-pesto": [
        "lightened extra virgin olive oil pesto",
        "lightened evoo pesto",
        "extra virgin olive oil pesto",
        "evoo pesto",
        "olive oil pesto"
    ],
    "/recipes/pesto-classico": [
        "pesto classico",
        "classic pesto",
        "traditional pesto",
        "basil pesto"
    ],

    # DISEASES
    "/misc/stats": [
        "chronic disease",
        "chronic diseases"
    ],
    "/misc/celiac": [
        "gluten allergy",
        "wheat allergy",
        "gluten free",
        "gluten-free",
        "gf",
        "gluten intolerance",
        "gluten sensitivity",
        "gluten intolerant",
        "no gluten",
        "gluten",
        "celiac disease",
        "celiacs",
        "celiac"
    ],
    "/misc/metabolic-syndrome": [
        "metabolic issues",
        "metabolic issue",
        "metabolic syndrome",
        "metabolically unfit",
        "metabolic health issues",
        "metabolic healthy",
        "poor metabolic health",
        "metabolic health",
        "metabolic function",
        "metabolic"
    ],
    "/misc/diabetes": [
        "prediabetes",
        "pre-diabetes",
        "prediabetics",
        "pre-diabetics",
        "prediabetic",
        "pre-diabetic",
        "diabetics",
        "diabetic",
        "type-2 diabetics",
        "type-2 diabetic",
        "type 2 diabetics",
        "type 2 diabetic",
        "type 2 diabetes",
        "type-2 diabetes",
        "diabetes (type 2)",
        "diabetes (type ii)",
        "diabetes",
        "impaired glucose metabolism",
        "impaired glucose",
        "metabolism of glucose",
        "fasting glucose",
        "high glucose",
        "glucose spikes",
        "glucose spike",
        "glucose curve",
        "elevated glucose",
        "glucose metabolism",
        "spikes in glucose",
        "spike in glucose",
        "chronic glucose",
        "reducing glucose",
        "spike your glucose",
        "body's glucose",
        "spike glucose",
        "glucose levels",
        "glucose level",
        "high in glucose",
        "waves of glucose",
        "stable glucose levels",
        "stable glucose level",
        "stable glucose",
        "blood sugar regulation",
        "blood sugar control",
        "blood sugar",
        "glycemic index",
        "glycemic",
        "high-glycemic",
        "high glycemic",
        "low-glycemic",
        "low glycemic",
        "blood glucose control",
        "blood glucose regulation",
        "blood glucose"
    ],
    "/misc/alzheimers": [
        "alzheimer's disease",
        "alzheimers disease",
        "alzheimer's",
        "alzheimers",
        "alzheimer",
        "memory problems",
        "memory problem",
        "cognitive decline or memory issues",
        "cognitive decline",
        "cognitive impairment",
        "memory issues",
        "memory issue",
        "memory loss",
        "dementia"
    ],
    "/misc/sleep": [
        "sleep apnea",
        "sleep"
    ],
    "/misc/exercise": [
        "physical exercises",
        "physical exercise",
        "exercises",
        "exercise",
        "sedentary lifestyle",
        "sedentary"
    ],
    "/misc/pcos": [
        "pcos",
        "polycystic ovary syndrome",
        "polycystic ovarian syndrome"
    ],
    "/misc/insulin-resistance": [
        "elevated insulin",
        "insulin resistance",
        "insulin resistant",
        "insulin sensitivity",
        "insulin sensitive",
        "fasting insulin",
        "insulin"
    ],
    "/misc/chronic-inflammation": [
        "inflammatory",
        "chronic inflammation",
        "inflammation",
        "anti inflammatory",
        "anti-inflammatory",
        "reduced inflammation",
        "reduce inflammation",
        "reducing inflammation",
        "carotenoids astaxanthin",
        "carotenoid astaxanthin",
        "oxidative stress",
        "oxidation",
        "free-radicals",
        "free radicals",
        "free-radical",
        "free radical"
    ],
    "/misc/phytochemicals": [
        "oleocanthal",
        "oleuropein",
        "polyphenolic compounds",
        "polyphenolic compound",
        "polyphenolics",
        "polyphenols",
        "polyphenols apigen, chologenic acid, and quercetin",
        "allicin, s-allyl cysteine (SAC), and diallyl disulfide (DADS)",
        "gingerol",
        "shogoal",
        "s-allyl cysteine (SAC)",
        "diallyl disulfide (DADS)",
        "s-allyl cysteine",
        "diallyl disulfide",
        "onionin A (ONA)",
        "onionin A",
        "sulfur compounds",
        "sulfur compound",
        "anthocyanins nasunin",
        "antioixdant compounds",
        "antioxidant compound",
        "anthocyanin nasunin",
        "nasunin",
        "carotenoids capsanthin",
        "carotenoid capsanthin",
        "antioxidants capsanthin",
        "antioxidant capsanthin",
        "capsanthin",
        "antioxidants sulforaphane and I3C",
        "antioxidant sulforaphane and I3C",
        "antioxidants I3C and sulforaphane",
        "antioxidant I3C and sulforaphane",
        "antioxidants I3C",
        "antioxidant I3C",
        "indole-3-carbinol (I3C)",
        "indole-3-carbinol",
        "I3C",
        "antioxidants sulforaphane",
        "antioxidant sulforaphane",
        "sulforaphane",
        "astaxanthin",
        "plant compounds",
        "plant compound",
        "anthocyanins, and glucosinolates",
        "anthocyanins and glucosinolates",
        "isothiocyanates, and glucosinolates",
        "isothiocyanates and glucosinolates",
        "isothiocyanates",
        "glucosinolates",
        "glucosinolate",
        "antioxidants kaempferol",
        "antioxidant kaempferol",
        "antioxidants sulpforaphane, kaempferol, and quercetin",
        "kaempferol",
        "antioxidants protodioscin",
        "antioxidant protodioscin",
        "protodioscin",
        "antioxidants apigenin",
        "antioxidant apigenin",
        "apigenin, quercetin, and kaempferol",
        "apigenin",
        "antioxidantsrutin",
        "antioxidant rutin",
        "rutin",
        "antioxidants quercetin and kaempferol",
        "antioxidant quercetin and kaempferol",
        "antioxidants quercetin",
        "antioxidant quercetin",
        "glucosinolates, quercetin, kaempferol, and indole-3-carbinol",
        "quercetin, kaempferol, and indole-3-carbinol",
        "quercetin",
        "antioxidants avenathramides",
        "antioxidant avenathramides",
        "avenathramides",
        "avenathramide",
        "antioxidants lutein and zeaxanthin",
        "antioxidant lutein and zeaxanthin",
        "carotenoids lutein and zeaxanthin",
        "carotenoid lutein and zeaxanthin",
        "lutein and zeaxanthin",
        "lutein, and zeaxanthin",
        "lutein, zeaxanthin",
        "antioxidants lutein",
        "antioxidants zeaxanthin",
        "antioxidant lutein",
        "antioxidant zeaxanthin",
        "carotenoids lutein",
        "carotenoids zeaxanthin",
        "carotenoid lutein",
        "carotenoid zeaxanthin",
        "lutein",
        "zeaxanthin",
        "antioxidants resveratrol",
        "antioxidant resveratrol",
        "resveratrol",
        "antioxidants carotenoids",
        "antioxidant carotenoids",
        "antioxidants carotenoid",
        "antioxidant carotenoid",
        "carotenoids",
        "carotenoid",
        "flavonoids",
        "flavonoid",
        "antioxidants punicalagins",
        "antioxidant punicalagins",
        "antioxidants punicalagin",
        "antioxidant punicalagin",
        "punicalagins",
        "punicalagin",
        "antioxidants rutin, kaemferol, vitexin, and quercetin",
        "antioxidants vitexin",
        "antioxidant vitexin",
        "antioxidants proanthocyanidins",
        "antioxidant proanthocyanidins",
        "antioxidants proanthocyanidin",
        "antioxidants proanthocyanidin",
        "proanthocyanidins",
        "proanthocyanidin",
        "antioxidants anthocyanins",
        "antioxidant anthocyanins",
        "antioxidants anthocyanin",
        "antioxidant anthocyanin",
        "anthocyanins",
        "anthocyanin",
        "antioxidants",
        "anti-oxidants",
        "antioxidant",
        "anti-oxidant",
        "polyphenols",
        "polyphenol",
        "phytochemicals",
        "phytochemical",
        "phyto-chemicals",
        "phyto-chemical",
        "phyto chemicals",
        "phyto chemical",
        "phytonutrients",
        "phytonutrient",
        "phyto-nutrients",
        "phyto-nutrient",
        "phyto nutrients",
        "phyto nutrient"
    ],
    "/misc/depression": [
        "depression"
    ],

    # BEANS
    "/misc/beans": [
        "Beans Beans The Musical Fruit",
        "beans",
        "bean",
        "legumes",
        "legume",
        "dried beans",
        "dried bean"
    ],
    "/misc/beans#black-beans": [
        "black beans",
        "black bean",
        "black"
    ],
    "/misc/beans#black-eyed-peas": [
        "black eyed peas",
        "black eyed pea"
    ],
    "/misc/beans#brown-lentils": [
        "brown lentils",
        "brown lentil"
    ],
    "/misc/beans#red-lentils": [
        "lentils",
        "lentil",
        "red lentil pasta",
        "red lentils",
        "red lentil"
    ],
    "/misc/beans#cannellini-beans": [
        "cannellini beans",
        "cannellini bean",
        "cannellini"
    ],
    "/misc/beans#chickpeas": [
        "chickpea pasta",
        "chickpeas",
        "garbanzo beans",
        "garbanzos",
        "garbanzo",
        "chickpea flours",
        "chickpea flour",
        "chickpea"
    ],
    "/misc/beans#edamame": [
        "edamame"
    ],
    "/misc/beans#fava-beans": [
        "fava beans",
        "fava bean",
        "fava"
    ],
    "/misc/beans#great-northern-beans": [
        "great northern beans",
        "great northern bean",
        "great northern"
    ],
    "/misc/beans#green-lentils": [
        "green lentils",
        "green lentil"
    ],
    "/misc/beans#kidney-beans": [
        "light red kidney beans",
        "dark red kidney beans",
        "light red kidney bean",
        "dark red kidney bean",
        "red kidney beans",
        "red kidney bean",
        "kidney beans",
        "kidney bean",
        "kidney"
    ],
    "/misc/beans#lima-beans": [
        "lima beans",
        "lima bean",
        "lima"
    ],
    "/misc/beans#lupini-beans": [
        "lupini beans",
        "lupini bean",
        "lupinis",
        "lupini"
    ],
    "/misc/beans#navy-beans": [
        "navy beans",
        "navy bean",
        "navy",
        "white beans",
        "white bean"
    ],
    "/misc/beans#pink-beans": [
        "pink beans",
        "pink bean"
    ],
    "/misc/beans#pinto-beans": [
        "pinto beans",
        "pinto bean",
        "pinto"
    ],
    "/misc/beans#soybeans": [
        "soy beans",
        "soy bean",
        "soybeans",
        "soybean",
        "soy"
    ],
    "/misc/beans#tofu": [
        "tofu"
    ],

    # DAIRY
    "/misc/dairy": [
        "I'm Dying For Dairy",
        "dairy"
    ],
    "/misc/dairy#almond-milk": [
        "plant based milks",
        "plant based milk",
        "non-dairy milks",
        "non-dairy milk",
        "non dairy milks",
        "non dairy milk",
        "unsweetened vanilla almond milk",
        "unsweetened almond milk",
        "unsweetened plant milks",
        "unsweetened plant milk",
        "plant milks",
        "plant milk",
        "almond milk"
    ],
    "/misc/dairy#blue-cheese": [
        "blue cheese"
    ],
    "/misc/dairy#brie": [
        "brie cheese",
        "brie"
    ],
    "/misc/dairy#butter": [
        "butter"
    ],
    "/misc/dairy#buttermilk": [
        "buttermilk",
        "butter milk"
    ],
    "/misc/dairy#casein": [
        "protein powder (unflavored casein)",
        "protein powder (casein)",
        "protein powder (vanilla casein)",
        "protein powder (chocolate casein)",
        "casein protein powder",
        "casein proteins",
        "casein protein",
        "casein",
        "vanilla casein protein powder",
        "chocolate casein protein powder"
    ],
    "/misc/dairy#cheddar": [
        "shredded cheese",
        "mexican cheese",
        "cheddar cheese",
        "shredded cheddar cheese",
        "shredded cheddar",
        "cheddar"
    ],
    "/misc/dairy#coconut-milk": [
        "coconut milks",
        "coconut milk"
    ],
    "/misc/dairy#cottage-cheese": [
        "fat free cottage cheeses",
        "fat free cottage cheese",
        "nonfat cottage cheeses",
        "nonfat cottage cheese",
        "cottage cheeses",
        "cottage cheese",
        "non fat cottage cheeses",
        "non fat cottage cheese"
    ],
    "/misc/dairy#cottage-cheese-whole-milk": [
        "whole milk cottage cheese",
        "full fat cottage cheese"
    ],
    "/misc/dairy#cream-cheese": [
        "full fat cream cheese",
        "reduced fat cream cheese",
        "cream cheese"
    ],
    "/misc/dairy#feta": [
        "feta cheese",
        "feta"
    ],
    "/misc/dairy#goat-cheese": [
        "goat cheese"
    ],
    "/misc/dairy#yogurt": [
        "plain nonfat greek yogurt",
        "nonfat greek yogurt",
        "plain greek yogurt",
        "greek yogurt",
        "yogurt"
    ],
    "/misc/dairy#yogurt-whole-milk": [
        "plain whole milk greek yogurt",
        "whole milk greek yogurt",
        "plain full fat greek yogurt",
        "full fat greek yogurt"
    ],
    "/misc/dairy#kefir": [
        "kefir (milk)",
        "kefir"
    ],
    "/misc/dairy#skim-milk": [
        "low fat milks",
        "low fat milk",
        "cow's milk",
        "cows milk",
        "cow milk",
        "skim milk",
        "skim",
        "milk",
        "dairy milks",
        "dairy milk",
        "animal based milks",
        "animal based milk",
        "animal milks",
        "animal milk"
    ],
    "/misc/dairy#whole-milk": [
        "whole milk"
    ],
    "/misc/dairy#mozzarella": [
        "shredded mozzarella cheese",
        "mozzarella cheese",
        "shredded mozzarella",
        "mozzarella",
        "cheese"
    ],
    "/misc/dairy#grated-cheese": [
        "parmesan cheese",
        "grated cheese",
        "pre grated cheese",
        "pre-grated cheese",
        "parmesan",
        "parm",
        "grated parmesan cheese",
        "grated parmesan",
        "grated parm",
        "grated parm cheese"
    ],
    "/misc/dairy#swiss-cheese": [
        "swiss cheese",
        "swiss"
    ],
    "/misc/dairy#whey": [
        "protein powder (unflavored whey)",
        "protein powder (whey)",
        "protein powder (vanilla whey)",
        "protein powder (chocolate whey)",
        "vanilla whey protein powder",
        "chocolate whey protein powder",
        # "vanilla protein powder",
        # "chocolate protein powder",
        "whey protein powder",
        "whey protein",
        "whey",
        "protein powders",
        "protein powder"
    ],

    #  FISH
    "/misc/fish": [
        "I'm Hooked On Fish",
        "fish & seafood",
        "fish and seafood",
        "fish",
        "seafood",
        "shellfish"
    ],
     "/misc/fish#anchovy": [
        "canned anchovies",
        "anchovies",
        "anchovy"
    ],
    "/misc/fish#clam": [
        "clams",
        "clam"
    ],
    "/misc/fish#cod": [
        "cod"
    ],
    "/misc/fish#crab": [
        "crabs",
        "canned crab",
        "crab"
    ],
    "/misc/fish#cuttlefish": [
        "cuttlefish"
    ],
    "/misc/fish#haddock": [
        "haddock"
    ],
    "/misc/fish#halibut": [
        "halibut"
    ],
    "/misc/fish#herring": [
        "herring"
    ],
    "/misc/fish#lobster": [
        "lobsters",
        "lobster"
    ],
    "/misc/fish#mackerel": [
        "mackerel"
    ],
    "/misc/fish#mahi-mahi": [
        "mahi mahi"
    ],
    "/misc/fish#mussel": [
        "mussels",
        "mussel"
    ],
    "/misc/fish#octopus": [
        "octopus",
        "octopi"
    ],
    "/misc/fish#oyster": [
        "oysters",
        "oyster"
    ],
    "/misc/fish#salmon": [
        "canned salmon",
        "salmon",
        "lox"
    ],
    "/misc/fish#sardine": [
        "canned sardines",
        "sardines",
        "sardine"
    ],
    "/misc/fish#scallop": [
        "scallops",
        "scallop"
    ],
    "/misc/fish#shrimp": [
        "shrimp"
    ],
    "/misc/fish#squid": [
        "squid"
    ],
    "/misc/fish#swordfish": [
        "swordfish",
        "sword fish"
    ],
    "/misc/fish#tilapia": [
        "tilapia"
    ],
    "/misc/fish#trout": [
        "trout"
    ],
    "/misc/fish#tuna": [
        "canned tuna",
        "tuna"
    ],

    # FRUIT
    "/misc/fruit": [
        "Going Bananas For Bananas",
        "whole fruits",
        "whole fruit",
        "fruits",
        "fruit",
        "citrus fruits",
        "citrus fruit"
    ],
     "/misc/fruit#apple": [
        "unsweetened applesauce",
        "applesauce",
        "apples",
        "apple"
    ],
    "/misc/fruit#apricot": [
        "apricots",
        "apricot"
    ],
    "/misc/fruit#avocado": [
        "avocados",
        "avocado"
    ],
    "/misc/fruit#banana": [
        "bananas",
        "banana"
    ],
    "/misc/fruit#blackberry": [
        "blackberries",
        "blackberry",
        "frozen blackberries",
        "frozen blackberry"
    ],
    "/misc/fruit#blueberries": [
        "blueberries",
        "blueberry",
        "berries",
        "berry",
        "frozen blueberries",
        "frozen blueberry"
    ],
    "/misc/fruit#boysenberry": [
        "boysenberries",
        "boysenberry"
    ],
    "/misc/fruit#cantaloupe": [
        "cantaloupes",
        "cantaloupe"
    ],
    "/misc/fruit#cherry": [
        "cherries",
        "cherry"
    ],
    "/misc/fruit#clementine": [
        "clementines",
        "clementine"
    ],
    "/misc/fruit#cranberry": [
        # "dried cranberries",
        # "dried cranberry"
        "cranberries",
        "cranberry",
        "crasins",
        "crasin"
    ],
    "/misc/fruit#dates": [
        "dates",
        "date"
    ],
    "/misc/fruit#fig-dried": [
        "dried figs",
        "dried fig",
        "figs",
        "fig"
    ],
    "/misc/fruit#fig-fresh": [
        "fresh figs",
        "fresh fig"
    ],
    "/misc/fruit#grapes": [
        "grapes",
        "grape"
    ],
    "/misc/fruit#grapefruit": [
        "grapefruits",
        "grapefruit"
    ],
    "/misc/fruit#guava": [
        "guavas",
        "guava"
    ],
    "/misc/fruit#honeydew": [
        "honeydews",
        "honeydew"
    ],
    "/misc/fruit#kiwi": [
        "kiwis",
        "kiwi"
    ],
    "/misc/fruit#lemon-juice": [
        "lemon juices",
        "lemon juice"
    ],
    "/misc/fruit#lemon": [
        "lemons",
        "lemon"
    ],
    "/misc/fruit#lime-juice": [
        "lime juices",
        "lime juice"
    ],
    "/misc/fruit#lime": [
        "limes",
        "lime"
    ],
    "/misc/fruit#mandarin": [
        "mandarin oranges",
        "mandarin orange",
        "mandarins",
        "mandarin"
    ],
    "/misc/fruit#mangos": [
        "mangos",
        "mango"
    ],
    "/misc/fruit#nectarine": [
        "nectarines",
        "nectarine"
    ],
    "/misc/fruit#olives": [
        "olives",
        "olive"
    ],
    "/misc/fruit#orange": [
        # "citrus fruits",
        # "citrus fruit",
        "oranges",
        "orange"
    ],
    "/misc/fruit#papaya": [
        "papayas",
        "papaya"
    ],
    "/misc/fruit#passion-fruit": [
        "passion fruits",
        "passion fruit"
    ],
    "/misc/fruit#peach": [
        "peaches",
        "peach"
    ],
    "/misc/fruit#pear": [
        "pears",
        "pear"
    ],
    "/misc/fruit#persimmon": [
        "persimmons",
        "persimmon"
    ],
    "/misc/fruit#pineapple": [
        "pineapples",
        "pineapple"
    ],
    "/misc/fruit#plum": [
        "plums",
        "plum"
    ],
    "/misc/fruit#pomegranate": [
        "pomegranates",
        "pomegranate seeds",
        "pomegranate seed",
        "pomegranate"
    ],
    "/misc/fruit#prune": [
        "prunes",
        "prune"
    ],
    "/misc/fruit#raisins": [
        "unsweetened dried fruits",
        "unsweetened dried fruit",
        "raisins",
        "raisin"
    ],
    "/misc/fruit#raspberry": [
        "raspberries",
        "raspberry",
        "frozen raspberries",
        "frozen raspberry"
    ],
    "/misc/fruit#starfruit": [
        "starfruits",
        "starfruit"
    ],
    "/misc/fruit#strawberries": [
        "strawberries",
        "strawberry",
        "frozen strawberries",
        "frozen strawberry"
    ],
    "/misc/fruit#watermelon": [
        "watermelons",
        "watermelon",
        "melons",
        "melon"
    ],

    # GRAINS
    "/misc/grains": [
        "A Grain Of Truth",
        "whole grains",
        "whole grain",
        "grains",
        "grain",
        "grain free",
        "grain-free"
    ],
    "/misc/grains#amaranth": [
        "amaranth"
    ],
    "/misc/grains#barley": [
        "barley"
    ],
    "/misc/grains#brown-rice": [
        "brown rice flours",
        "brown rice flour",
        "brown rice",
        "rice"
    ],
    "/misc/grains#buckwheat": [
        "buckwheat",
        "buck wheat"
    ],
    "/misc/grains#bulgur": [
        "bulgur wheat",
        "bulgur"
    ],
    "/misc/grains#corn": [
        "corn"
    ],
    "/misc/grains#couscous": [
        "couscous"
    ],
    "/misc/grains#farro": [
        "farro"
    ],
    "/misc/grains#millet": [
        "millet flours",
        "millet flour",
        "millet"
    ],
    "/misc/grains#oats": [
        "oat flours",
        "oat flour",
        "unsweetened oat milk",
        "oat milk",
        "oats",
        # "oatmeal",
        "oat",
        "old-fashioned oats",
        "old-fashioned oat",
        "old fashioned oats",
        "old fashioned oat",
        "rolled oats",
        "quick oats"
    ],
    "/misc/grains#popcorn": [
        "popcorn"
    ],
    "/misc/grains#quinoa": [
        "quinoa"
    ],
    "/misc/grains#rye": [
        "rye flours",
        "rye flour",
        "rye"
    ],
    "/misc/grains#spelt": [
        "spelt flours",
        "spelt flour",
        "spelt"
    ],
    "/misc/grains#vital-wheat-gluten": [
        "vital wheat gluten",
        "vwg"
    ],
    "/misc/grains#white-wheat": [
        "white flours",
        "white flour",
        "enriched flours",
        "enriched flour",
        "enriched wheat flours",
        "enriched wheat flour",
        "enriched white flours",
        "enriched white flour",
        "highly processed white flours",
        "highly processed white flour",
        "heavily processed white flours",
        "heavily processed white flour",
        "processed white flours",
        "processed white flour",
        "highly processed flours",
        "highly processed flour",
        "heavily processed flours",
        "heavily processed flour",
        "processed flours",
        "processed flour",
        "refined white flours",
        "refined white flour",
        "refined flours",
        "refined flour",
        "all purpose white flours",
        "all purpose white flour",
        "all purpose flours",
        "all purpose flour",
        "self-rising flour",
        "self rising flour",
        "typical flours",
        "typical flour",
        "all-purpose flours",
        "all-purpose flour",
        "ap flour",
        "standard flour",
        "regular flour",
        "all purpose",
        # "flours",
        "flour",
        "wheat flours",
        "wheat flour",
        "refined flour free",
        "free of refined flours",
        "free of refined flour"
    ],
    "/misc/grains#pasta-white": [
        "white pasta"
    ],
    "/misc/grains#white-rice": [
        "white rice",
        "white arborio rice",
        "arborio rice",
        "sushi rice"
    ],
    "/misc/grains#whole-wheat": [
        "whole wheat flours",
        "whole wheat flour",
        "wheat based flours",
        "wheat based flour",
        "wheat-based flours",
        "wheat-based flour",
        "wheat based",
        "wheat grain",
        "wheat kernel",
        "whole wheat",
        "wheat"
    ],
    "/misc/grains#pasta": [
        "whole wheat pasta",
        "wheat pasta",
        "pasta",
        "penne"
    ],
    "/misc/grains#wild-rice": [
        "wild rice"
    ],

    # MEAT
    "/misc/meat": [
        "Let's Meet The Meats",
        "meats",
        "meat",
        "lean meats"
    ],
    "/misc/meat#bacon": [
        "bacon"
    ],
    "/misc/meat#liver": [
        "beef liver",
        "organ meats",
        "organ meat",
        "liver"
    ],
    "/misc/meat#bologna": [
        "bologna"
    ],
    "/misc/meat#chicken-breast": [
        "boneless skinless chicken breasts",
        "boneless skinless chicken breast",
        "skinless chicken breasts",
        "skinless chicken breast",
        "boneless skinless breasts",
        "boneless skinless breast",
        "skinless breasts",
        "skinless breast",
        "chicken breast",
        "chicken breasts",
        "breasts",
        "breast",
        "chickens",
        "chicken"
    ],
    "/misc/meat#chicken-liver": [
        "chicken liver",
        "chicken livers"
    ],
    "/misc/meat#chicken-thighs": [
        "boneless skinless chicken thighs",
        "boneless skinless chicken thigh",
        "boneless skinless thighs",
        "boneless skinless thigh",
        "skinless chicken thighs",
        "skinless chicken thigh",
        "skinless thighs",
        "skinless thigh",
        "bone-in skin-on chicken thighs",
        "bone-in skin-on chicken thigh",
        "bone in skin on chicken thighs",
        "bone in skin on chicken thigh",
        "bone-in skin-on thighs",
        "bone-in skin-on thigh",
        "bone in skin on thighs",
        "bone in skin on thigh",
        "chicken thighs",
        "thighs",
        "thigh meat",
        "thigh",
        "bone-in, skin-on thighs",
        "bone-in, skin-on thigh",
        "bone-in and skin-on thighs",
        "bone-in and skin-on thigh",
        "bone in, skin on thighs",
        "bone in, skin on thigh",
        "bone in and skin on thighs",
        "bone in and skin on thigh"
    ],
    "/misc/meat#eggs": [
        "whole eggs",
        "whole egg",
        "egg yolks",
        "egg yolk",
        "yolks",
        "yolk",
        "egg",
        "eggs"
    ],
    "/misc/cooking-eggs#fried": [
        "fried eggs",
        "fried egg"
    ],
    "/misc/meat#egg-whites": [
        "liquid egg whites",
        "liquid egg white",
        "carton egg whites",
        "carton egg white",
        "egg whites",
        "egg white",
        "whites"
    ],
    "/misc/meat#ground-beef": [
        "93% lean ground beef",
        "93 % ground beef",
        "93/7 ground beef",
        "ground beef",
        # "ground meat",
        "red meat",
        "beef",
        "93 % lean beef"
    ],
    "/misc/meat#ground-turkey": [
        "93% lean ground turkey",
        "93% ground turkey",
        "93/7 ground turkey",
        "ground turkey",
        "turkey",
        "93% lean meat",
        "93% meat",
        "93% lean turkey"
    ],
    "/misc/meat#ham": [
        "ham steak",
        "ham"
    ],
    "/misc/meat#hot-dogs": [
        "hot dog",
        "hot dogs"
    ],
    "/misc/meat#lamb": [
        "lamb"
    ],
    "/misc/meat#pepperoni": [
        "pepperoni"
    ],
    "/misc/meat#pork-liver": [
        "pork liver"
    ],
    "/misc/meat#pork-tenderloin": [
        "pork tenderloin",
        "ground pork",
        "pork"
    ],
    "/misc/meat#salami": [
        "salami"
    ],
    "/misc/meat#sausage": [
        "sausage",
        "sausages",
        "breakfast sausages",
        "breakfast sausage"
    ],
    "/misc/meat#spam": [
        "spam"
    ],
    "/misc/meat#steak": [
        "steak",
        "steaks",
        "sirloin"
    ],
    "/misc/meat#turkey-breast": [
        "turkey breast",
        "turkey breasts"
    ],
    "/misc/meat#veal": [
        "veal"
    ],
    "/misc/meat#venison": [
        "venison"
    ],

    # NUTS
    "/misc/nuts": [
        "I'm Nuts For Nuts",
        "nuts",
        "nut"
    ],
    "/misc/nuts#almonds": [
        "almond butter",
        "almond flours",
        "almond flour",
        "nut flour",
        "almond meals",
        "almond meal",
        "almonds",
        "almond"
    ],
    "/misc/nuts#brazil-nuts": [
        "brazil nuts",
        "brazil nut"
    ],
    "/misc/nuts#cashews": [
        "unsweetened cashew milk",
        "cashew milk",
        "cashews",
        "cashew butter",
        "cashew"
    ],
    "/misc/nuts#chestnuts": [
        "chestnuts",
        "chestnut"
    ],
    "/misc/nuts#coconut": [
        "unsweetened shredded coconut flakes",
        "unsweetened coconut flakes",
        "shredded coconut flakes",
        "unsweetened shredded coconut flake",
        "unsweetened coconut flake",
        "shredded coconut flake",
        "shredded coconut",
        "coconut flakes",
        "coconut flake",
        "coconut flour",
        "coconut butter",
        "extra-virgin coconut oil",
        "extra virgin coconut oil",
        "unrefined coconut oil",
        "virgin coconut oil",
        "coconut oil",
        "coconuts",
        "coconut's",
        "coconut"
    ],
    "/misc/nuts#hazelnuts": [
        "hazelnut butter",
        "hazelnuts",
        "hazelnut"
    ],
    "/misc/nuts#macadamia-nuts": [
        "macadamia nuts",
        "macadamia nut butter",
        "macadamia nut"
    ],
    "/misc/nuts#peanuts": [
        "peanut butter",
        "peanuts",
        "peanut"
    ],
    "/misc/nuts#pecans": [
        "pecan butter",
        "pecans",
        "pecan"
    ],
    "/misc/nuts#pine-nuts": [
        "pine nuts",
        "pine nut",
        "pine",
        "pignoli nuts",
        "pignoli"
    ],
    "/misc/nuts#pistachios": [
        "pistachios",
        "pistachio butter",
        "pistachio"
    ],
    "/misc/nuts#walnuts": [
        "walnuts",
        "walnut butter",
        "walnut"
    ],

    # SEEDS
    "/misc/seeds": [
        "I See Seeds In Your Future",
        "seeds",
        "seed"
    ],
    "/misc/seeds#chia-seeds": [
        "chia seeds",
        "chia seed",
        "chia eggs",
        "chia egg",
        "chia"
    ],
    "/misc/seeds#flax-seeds": [
        "flax eggs",
        "flax egg",
        "ground flax seeds",
        "ground flaxseeds",
        "ground flax seed",
        "ground flaxseed",
        "ground flax",
        "flaxseed meal",
        "flax seed meal",
        "flax meal",
        "flaxmeal",
        "flax seeds",
        "flax seed",
        "flaxseeds",
        "flaxseed",
        "flax"
    ],
    "/misc/seeds#hemp-seeds": [
        "hemp seeds",
        "hemp seed",
        "hemp eggs",
        "hemp egg",
        "hemp"
    ],
    "/misc/seeds#poppy-seeds": [
        "poppy seeds",
        "poppy seed",
        "poppy"
    ],
    "/misc/seeds#pumpkin-seeds": [
        "pumpkin seeds",
        "pumpkin seed butter",
        "pumpkin seed"
    ],
    "/misc/seeds#sesame-seeds": [
        "sesame seeds",
        "sesame seed butter",
        "sesame seed",
        "tahini"
    ],
    "/misc/seeds#sunflower-seeds": [
        "sunflower seeds",
        "sunflower seed butter",
        "sunflower butter",
        "sun butter",
        "sunflower seed",
        "sunflower"
    ],

    #  VEGGIES
    "/misc/veggies": [
        "Lettuce Turnip The Beet",
        "vegetables",
        "vegetable",
        "veggies",
        "veggie",
        "dark leafy greens",
        "dark leafy green",
        "leafy greens",
        "leafy green",
        "dark leafy vegetables",
        "dark leafy vegetable",
        "leafy vegetables",
        "leafy vegetable",
        "greens"
    ],"/misc/veggies#acorn-squash": [
        "acorn squash"
    ],
    "/misc/veggies#artichoke": [
        "artichokes",
        "artichoke"
    ],
    "/misc/veggies#arugula": [
        "arugula"
    ],
    "/misc/veggies#asparagus": [
        "asparagus"
    ],
    "/misc/veggies#beets": [
        "beets",
        "beet"
    ],
    "/misc/veggies#beet-greens": [
        "beet greens",
        "beet green"
    ],
    "/misc/veggies#pepper": [
        "red bell peppers",
        "red bell pepper",
        "orange bell peppers",
        "orange bell pepper",
        "yellow bell peppers",
        "yellow bell pepper",
        "green bell peppers",
        "green bell pepper",
        "bell peppers",
        "bell pepper",
        "peppers",
        "pepper"
    ],
    "/misc/veggies#bok-choy": [
        "bok choy"
    ],
    "/misc/veggies#broccoli": [
        "broccoli"
    ],
    "/misc/veggies#brussel-sprout": [
        "brussels sprouts",
        "brussel sprouts",
        "brussel sprout"
    ],
    "/misc/veggies#butternut-squash": [
        "butternut squash noodles",
        "butternut squash",
        "orange vegetables",
        "orange vegetable",
        "squash"
    ],
    "/misc/veggies#cabbage": [
        "shredded cabbage",
        "cabbage"
    ],
    "/misc/veggies#carrots": [
        "baby carrots",
        "baby carrot",
        "carrots",
        "carrot"
    ],
    "/misc/veggies#cauliflower": [
        "mashed cauliflower",
        "cauliflower"
    ],
    "/misc/veggies#celery": [
        "celery"
    ],
    "/misc/veggies#collard-green": [
        "collard greens",
        "collard green",
        "collards",
        "collard"
    ],
    "/misc/veggies#cucumber": [
        "cucumbers",
        "cucumber"
    ],
    "/misc/veggies#eggplant": [
        "eggplants",
        "eggplant"
    ],
    "/misc/veggies#fennel": [
        "fennel"
    ],
    "/misc/veggies#garlic": [
        "fresh garlic",
        "garlic cloves",
        "minced garlic",
        "garlic"
    ],
    "/misc/veggies#ginger": [
        "ginger"
    ],
    "/misc/veggies#green-bean": [
        "green beans",
        "green bean",
        "string beans",
        "string bean"
    ],
    "/misc/veggies#kale": [
        "kale"
    ],
    "/misc/veggies#kohlrabi": [
        "kohlrabi"
    ],
    "/misc/veggies#lettuce": [
        "romaine lettuce",
        "iceberg lettuce",
        "romaine",
        "iceberg",
        "lettuce"
    ],
    "/misc/veggies#mustard-greens": [
        "mustard greens",
        "mustard green"
    ],
    "/misc/veggies#onion": [
        "onions",
        "onion",
        "yellow onions",
        "yellow onion",
        "red onions",
        "red onion",
        "white onions",
        "white onion"
    ],
    "/misc/veggies#parsnips": [
        "parsnips",
        "parsnip"
    ],
    "/misc/veggies#pea": [
        "peas",
        "pea"
    ],
    "/misc/veggies#plantain": [
        "plantains",
        "plantain"
    ],
    "/misc/veggies#potato": [
        "potatoes",
        "potato"
    ],
    "/misc/veggies#pumpkin": [
        "pumpkin"
    ],
    "/misc/veggies#radicchio": [
        "radicchio"
    ],
    "/misc/veggies#radish": [
        "radishes",
        "radish"
    ],
    "/misc/veggies#spaghetti-squash": [
        "spaghetti squash"
    ],
    "/misc/veggies#spinach-fresh": [
        "frozen spinach",
        "spinach"
    ],
    "/misc/veggies#sweet-potato": [
        "sweet potatoes",
        "sweet potato",
        "yams",
        "yam"
    ],
    "/misc/veggies#swiss-chard": [
        "swiss chard"
    ],
    "/misc/veggies#tomato": [
        "tomatoes",
        "tomato",
        "cherry tomatoes",
        "cherry tomato",
        "grape tomatoes",
        "grape tomato",
        "tomato paste",
        "crushed tomatoes",
        "diced tomatoes"
    ],
    "/misc/veggies#turnip": [
        "turnips",
        "turnip"
    ],
    "/misc/veggies#mushrooms": [
        "white mushrooms",
        "mushrooms",
        "mushroom"
    ],
    "/misc/veggies#yellow-squash": [
        "yellow squash"
    ],
    "/misc/veggies#zucchini": [
        "zucchini noodles",
        "zucchini noodle",
        "zoodles",
        "zoodle",
        "zucchini"
    ],

    # NUTRIENTS (ABC)
    "/misc/nutrient-alphabet": [
        "The ABCs of Nutrients",
        "multi-vitamin",
        "multivitamin",
        "micronutrients",
        "micronutrient",
        "micronutritionally",
        "macro",
        "micro",
        "macronutrients",
        "macronutrient",
        "nutrient-dense",
        "nutrient dense",
        "nutrient rich",
        "nutrient-rich",
        "macro and micro nutrients",
        "macro and micro nutrient",
        "micro nutrients",
        "micro nutrient",
        "micro-nutrients",
        "micro-nutrient",
        "micro-nutritionally",
        "macro nutrients",
        "macro nutrient",
        "macro-nutrients",
        "macro-nutrient",
        "essential nutrients",
        "essential nutrient",
        "essential micronutrients",
        "essential micronutrient",
        "nutrients",
        "nutrient",
        "vitamins/minerals",
        "vitamin/mineral",
        "vitamins and minerals",
        "vitamins, minerals",
        "vitamins, and minerals",
        "vitamin, and mineral",
        "vitamin and mineral",
        "vitamins & minerals",
        "vitamins",
        "vitamin contents",
        "vitamin content",
        "essential vitamins",
        "essential minerals",
        "essential vitamin",
        "essential mineral",
        "vitamin",
        "minerals",
        "mineral contents",
        "mineral content",
        "mineral"
    ],
    "/misc/nutrient-alphabet#A": [
        "vitamins a",
        "vitamin a",
        "beta carotene",
        "beta-carotene",
        "betacarotene"
    ],
    "/misc/nutrient-alphabet#B": [
        "b vitamins",
        "b vitamin",
        "pyridoxine",
        "vitamins b6 (pyridoxine)",
        "vitamins b6",
        "vitamin b6 (pyridoxine)",
        "b6 (pyridoxine)",
        "pyridoxine (vitamin b6)",
        "pyridoxine (b6)",
        "vitamin b6",
        "b6"
    ],
    "/misc/nutrient-alphabet#C": [
        "minerals copper",
        "mineral copper",
        "copper"
    ],
    "/misc/nutrient-alphabet#D": [
        "vitamins d",
        "vitamin d",
        "d"
    ],
    "/misc/nutrient-alphabet#E": [
        "vitamins e",
        "vitamin e",
        "e"
    ],
    "/misc/nutrient-alphabet#F": [
        "vitamins b9 (folate)",
        "vitamins b9",
        "vitamin b9 (folate)",
        "b9 (folate)",
        "folate (vitamin b9)",
        "folate (b9)",
        "b9",
        "folate",
        "vitamin b9"
    ],
    "/misc/nutrient-alphabet#G": [
        "glucose"
    ],
    "/misc/nutrient-alphabet#I": [
        "iodine"
    ],
    "/misc/nutrient-alphabet#K": [
        "vitamins k",
        "vitamin k",
        "k"
    ],
    "/misc/nutrient-alphabet#L": [
        "lycopene"
    ],
    "/misc/nutrient-alphabet#M": [
        "minerals manganese",
        "mineral manganese",
        "manganese"
    ],
    "/misc/nutrient-alphabet#N": [
        "niacin",
        "vitamins b3 (niacin)",
        "vitamins b3",
        "vitamin b3 (niacin)",
        "b3 (niacin)",
        "niacin (vitamin b3)",
        "niacin (b3)",
        "vitamin b3",
        "b3"
    ],
    "/misc/nutrient-alphabet#O": [
        "omega-3 fish oils",
        "omega 3 fish oils",
        "omega-3 fish oil",
        "omega 3 fish oil",
        "omega 3 fatty acids",
        "omega-3 fatty acids",
        "omega 3 fatty acid",
        "omega-3 fatty acid",
        "fish oils",
        "fish oil",
        "omega-3",
        "omega 3",
        "omega-3s",
        "omega 3s",
        "omega 3 fats",
        "omega 3 fat",
        "omega-3 fats",
        "omega-3 fat",
        "EPA omega-3 fatty acids",
        "EPA omega 3 fatty acids",
        "EPA omega-3 fatty acid",
        "EPA omega 3 fatty acid",
        "DHA omega-3 fatty acids",
        "DHA omega 3 fatty acids",
        "DHA omega-3 fatty acid",
        "DHA omega 3 fatty acid",
        "ALA omega-3 fatty acids",
        "ALA omega 3 fatty acids",
        "ALA omega-3 fatty acid",
        "ALA omega 3 fatty acid",
        "omega-3 fatty acids EPA",
        "omega 3 fatty acids EPA",
        "omega-3 fatty acid EPA",
        "omega 3 fatty acid EPA",
        "omega-3 fatty acids DHA",
        "omega 3 fatty acids DHA",
        "omega-3 fatty acid DHA",
        "omega 3 fatty acid DHA",
        "omega-3 fatty acids ALA",
        "omega 3 fatty acids ALA",
        "omega-3 fatty acid ALA",
        "omega 3 fatty acid ALA",
        "alpha-linolenic acid",
        "docosahexaenoic acid",
        "eicosapentaenoic acid",
        "ALA (alpha-linolenic acid)",
        "DHA (docosahexaenoic acid)",
        "EPA (eicosapentaenoic acid)",
        "alpha-linolenic acid (ALA)",
        "docosahexaenoic acid (DHA)",
        "eicosapentaenoic acid (EPA)",
        "EPA",
        "DHA",
        "ALA"
    ],
    "/misc/nutrient-alphabet#P": [
        "vitamins b5",
        "vitamin b5",
        "vitamin b5 (pantothenic acid)",
        "b5 (pantothenic acid)",
        "pantothenic acid (vitamin b5)",
        "pantothenic acid (b5)",
        "pantothenic acid",
        "b5"
    ],
    "/misc/nutrient-alphabet#R": [
        "vitamins b2 (riboflavin)",
        "vitamins b2",
        "vitamin b2 (riboflavin)",
        "b2 (riboflavin)",
        "riboflavin (b2)",
        "riboflavin (vitamin b2)",
        "vitamin b2",
        "b2",
        "riboflavin"
    ],
    "/misc/nutrient-alphabet#S": [
        "minerals selenium",
        "mineral selenium",
        "selenium"
    ],
    "/misc/nutrient-alphabet#T": [
        "vitamins b1 (thiamin)",
        "vitamins b1",
        "vitamin b1 (thiamin)",
        "thiamin (vitamin b1)",
        "thiamin (b1)",
        "b1 (thiamin)",
        "vitamin b1",
        "b1",
        "thiamin"
    ],
    "/misc/nutrient-alphabet#Z": [
        "minerals zinc",
        "mineral zinc",
        "zinc"
    ],

    # NUTRIENTS (Dedicated posts)
    "/misc/calcium": [
        "Got Calcium?",
        "minerals calcium",
        "mineral calcium",
        "calcium"
    ],
    "/misc/choline": [
        "minerals choline",
        "mineral choline",
        "choline"
    ],
    "/misc/cholesterol": [
        "cholesterol"
    ],
    "/misc/fiber": [
        "high fiber",
        "high-fiber",
        "fiber",
        "dietary fiber",
        "soluble fiber",
        "insoluble fiber",
        "Fiber: Happiness is a Good Poop",
        "fibers"
    ],
    "/misc/iron": [
        "I Run on Iron",
        "plant based iron",
        "plant-based iron",
        "minerals iron",
        "mineral iron",
        "iron",
        "'heme' iron",
        "'heme-iron'",
        "heme iron",
        "heme-iron",
        "non heme-iron",
        "non heme iron",
        "'non-heme-iron'",
        "'non-heme' iron",
        "non-heme-iron",
        "non-heme iron",
        "heme",
        "non heme",
        "non-heme"
    ],
    "/misc/magnesium": [
        "Mag-nificent: The Mighty Mineral for Muscles and Mind",
        "minerals magnesium",
        "mineral magnesium",
        "magnesium"
    ],
    "/misc/phosphorus": [
        "Phosphorus: Fuel For Bones & Beyond",
        "minerals phosphorus",
        "mineral phosphorus",
        "phosphorus"
    ],
    "/misc/potassium": [
        "A Monkey Never Cramps: Why You Need Potassium",
        "minerals potassium",
        "mineral potassium",
        "potassium"
    ],
    "/misc/sodium": [
        "minerals sodium",
        "mineral sodium",
        "sodium"
    ],
    "/misc/vitamin-b12": [
        "B-Ware the Deficiency: The Power of B12",
        "vitamins b12 (cobalamin)",
        "vitamins b12",
        "vitamin b12",
        "vitamin b12 (cobalamin)",
        "b12 (cobalamin)",
        "cobalamin (vitamin b12)",
        "cobalamin (b12)",
        "b12",
        "cobalamin"
    ],
    "/misc/vitamin-c": [
        "(Vitamin) C You Later, Sickness!",
        "vitamins c",
        "vitamin c",
        "c"
    ],
    "/misc/hidden-sugar": [
        "table sugar",
        "white granulated sugar",
        '"refined" sugars',
        '"refined" sugar',
        "sugary sauces",
        "sugar sauce",
        "glazes",
        "glaze",
        "sugary",
        "sugar-filled",
        "sugar filled",
        "high sugar",
        "low sugar",
        "sugar consumption",
        "sugar bombs",
        "sugar bomb",
        "simple sugars",
        "simple sugar",
        "added sugars",
        "added sugar",
        "high fructose corn syrup (hfcs)",
        "high fructose corn syrup",
        "hfcs (high fructose corn syrup)",
        "hfcs",
        "corn syrup",
        "no sugars",
        "no sugar",
        "sugar spreads",
        "sugar spread",
        "sugar-loaded",
        "sugar loaded",
        "sugar full",
        "full of sugars",
        "full of sugar",
        "full of added sugars",
        "full of added sugar",
        "hidden sugars",
        "hidden sugar",
        "refined sugars",
        "refined sugar free",
        "refined sugar",
        "sugar free",
        "sf",
        "sugar-free",
        "sugars",
        "sugar",
        "white sugar",
        "brown sugar",
        "white and brown sugars",
        "brown and white sugars",
        "white and brown sugar",
        "brown and white sugar",
        "white or brown sugars",
        "brown or white sugars",
        "white or brown sugar",
        "brown or white sugar",
        "sugar sweetened beverages",
        "sugar sweetened beverage",
        "sweetened almond milks"
    ],
    "/misc/carbs": [
        "whole food sources of sugar",
        "carbohydrate-rich",
        "carb-rich",
        "whole food carbohydrates",
        "whole food carbs",
        "whole food carbohydrate",
        "whole food carb",
        "whole food sugars",
        "whole food sugar",
        "refined carbs",
        "refined carb",
        # "natural sweetness",
        # "natural sweeteners",
        # "natural sweetener",
        # "natural sugars",
        # "natural sugar",
        "carbohydrates",
        "carbohydrate",
        "low carb",
        "high carb",
        "total carbohydrates",
        "total carbohydrate",
        "total carbs",
        "total carb",
        "net carbs",
        "net carb",
        "complex carbs",
        "complex carb",
        "carbs",
        "carb",
        "refined starches",
        "refined starch",
        "refined grains",
        "refined grain",
        "starches",
        "starchy",
        "starch",
        "Carbs: The Devil in Disguise?",
        "complex starches",
        "complex starch"
    ],
    "/misc/fats": [
        "Fat: The Innocent Criminal?",
        # "leaner",
        # "lean",
        "full fat",
        "reduced fat",
        "fat free",
        "hydrogenated fats",
        "hydrogenated fat",
        "hydrogenated oils",
        "hydrogenated oil",
        "heart healthy fats",
        "healthiest fats",
        "healthiest fat",
        "healthy fats",
        "healthy fat",
        "unhealthy fats",
        "healthier fats",
        "unhealthy fat",
        "unhealthy oils",
        "unhealthy oil",
        "essential fatty acids",
        "essential fatty acid",
        "fatty acids",
        "fatty acid",
        "fatty foods",
        "fatty food",
        "fatty",
        # "fattier",
        "fattiest",
        "heart-healthy monounsaturated fats",
        "heart healthy monounsaturated fats",
        "heart-healthy monounsaturated fat",
        "heart healthy monounsaturated fat",
        "heart-healthy mono-unsaturated fats",
        "heart healthy mono-unsaturated fats",
        "heart-healthy mono-unsaturated fat",
        "heart healthy mono-unsaturated fat",
        "heart-healthy mono unsaturated fats",
        "heart healthy mono unsaturated fats",
        "heart-healthy mono unsaturated fat",
        "heart healthy mono unsaturated fat",
        "high fat",
        "low fat",
        "lowfat",
        "nonfat",
        "monounsaturated fats",
        "monounsaturated fat",
        "mono-unsaturated fats",
        "mono-unsaturated fat",
        "mono unsaturated fats",
        "mono unsaturated fat",
        "polyunsaturated fats",
        "polyunsaturated fat",
        "poly-unsaturated fats",
        "poly-unsaturated fat",
        "poly unsaturated fats",
        "poly unsaturated fat",
        "saturated fats",
        "saturated fat",
        "saturated",
        "unsaturated fats",
        "unsaturated fat",
        "unsaturated",
        "trans fats",
        "trans fat",
        "added fats",
        "added fat",
        "fats",
        "fat",
        "added oils",
        "added oil",
        # "highly refined oils",
        # "highly refined oil",
        # "heavily refined oils",
        # "heavily refined oil",
        # "refined oils",
        # "refined oil",
        "refined fats",
        "refined fat",
        "oils",
        # "oil",
        "low-fat",
        "heart-healthy fats",
        "no oil",
        "oil free",
        "dietary fat"
    ],
    "/misc/protein": [
        "protein quality",
        "plant based protein",
        "plant-based protein",
        "branched-chain amino acids (BCAAs)",
        "branched-chain amino acid (BCAA)",
        "branched chain amino acids (BCAAs)",
        "branched chain amino acid (BCAA)",
        "BCAAs",
        "BCAA",
        "branched chain amino acids",
        "branched chain amino acid",
        "branched-chain amino acids",
        "branched-chain amino acid",
        "essential amino acids",
        "essential amino acid",
        "amino acids",
        "amino acid",
        "proteins",
        "protein",
        '"protein"',
        "complete proteins",
        "complete protein",
        "Protein: The Essential Building Blocks",
        "What is the Best Protein Source?",
        "lean protein",
        "protein rich",
        "protein-rich",
        "protein dense",
        "protein-dense"
    ],
    "/misc/high-protein": [
        "high protein foods",
        "high protein food",
        "high-protein foods",
        "high protein",
        "high-protein",
        "protein ratio"
        "protein to calorie ratio",
        "protein ratios"
    ],
    "/misc/calories": [
        "It's About More Than Calories",
        "calorie dense",
        "calorically dense",
        "calorically",
        "caloric",
        "calorie-dense",
        "calorie dense",
        "low calories",
        "high calories",
        "low-calories",
        "high-calories",
        "low calorie",
        "high calorie",
        "low-calorie",
        "high-calorie",
        "zero calories",
        "zero-calories",
        "zero calorie",
        "0 calories",
        "0 calorie",
        "zero-calorie",
        "calories",
        "calorie"
    ],
    "/misc/creatine": [
        "creatine"
    ],

    # AMAZON
    "https://amzn.to/4qQYEc4": [
        '5.5 x 3.3"',
        '5.5" x 3.3"',
        "plastic meal prep containers",
        "plastic meal prep container"
    ],
    "https://amzn.to/3Sg1Z7p": [
        "pure granulated monk fruit",
    ],
    "https://amzn.to/4wFerfa": [
        "shaker bottle",
        "blender bottle"
    ],
    "https://amzn.to/4zMyIm3": [
        "powdered milk, skim",
        "powdered milk, nonfat",
        "powdered milk, non fat",
        "powdered milk",
        "milk powder, skim",
        "milk powder, nonfat",
        "milk powder, non fat",
        "milk powder"
    ],
    "https://amzn.to/4wzvob5": [
        "small ramekins",
        "small ramekin",
        "ramekins",
        "ramekin"
    ],
    "https://amzn.to/4cBNvpn": [
        "Açaí",
        "acai",
        "frozen acai puree",
        "unsweetened acai",
        "frozen acai packets",
        "frozen acai packets unsweetened",
        "frozen acai packets unsweetened puree",
        "frozen acai puree packets",
        "frozen acai puree packets unsweetened",
        "frozen acai puree packets unsweetened puree",
        "acai packets",
        "acai packets unsweetened",
        "acai packets unsweetened puree",
        "acai puree packets",
        "acai puree packets unsweetened",
        "acai puree packets unsweetened puree",
        "frozen Açaí",
        "unsweetened Açaí puree",
        "unsweetened Açaí packets",
        "unsweetened Açaí packets puree",
        "unsweetened Açaí puree packets",
        "frozen Açaí puree",
        "unsweetened Açaí",
        "frozen Açaí packets",
        "frozen Açaí packets unsweetened",
        "frozen Açaí packets unsweetened puree",
        "frozen Açaí puree packets",
        "frozen Açaí puree packets unsweetened",
        "frozen Açaí puree packets unsweetened puree",
        "Açaí packets",
        "Açaí packets unsweetened",
        "Açaí packets unsweetened puree",
        "Açaí puree packets",
        "Açaí puree packets unsweetened",
        "Açaí puree packets unsweetened puree",
        "frozen Açaí",
        "unsweetened Açaí puree",
        "unsweetened Açaí packets",
        "unsweetened Açaí packets puree",
        "unsweetened Açaí puree packets",
        "Açaí puree",
        "acai puree"
    ],
    "https://amzn.to/43wLkhB": [
        "nutritional yeast"
    ],
    "https://amzn.to/44VXByC": [
        "soy sauce",
        "tamari",
        "low sodium soy sauce",
        "gluten free soy sauce",
        "soy sauce, low sodium, gluten free",
        "soy sauce, gluten free, low sodium",
        "soy sauce, gluten free",
        "soy sauce, low sodium"
    ],
    "https://amzn.to/4khDgIM": [
        "almond extract"
    ],
    "https://amzn.to/43MkDqr": [
        "vanilla extract",
        "vanilla"
    ],
    "https://amzn.to/4bGjSTE": [
        "coconut extract"
    ],
    "https://amzn.to/4xtISFR": [
        "mint extract"
    ],
    "https://amzn.to/4xor2nH": [
        "maple extract"
    ],
    "https://amzn.to/3TIq7QF": [
        "rum extract"
    ],
    "https://amzn.to/4gl7OK1": [
        "butter extract"
    ],
    "https://amzn.to/45Oxbha": [
        "walden farms chocolate syrup",
        "zero calorie chocolate syrup"
    ],
    "https://amzn.to/4ggGWuF": [
        "walden farms peanut butter",
        "walden farms peanut butter spread",
        "walden farms peanut spread",
        "walden farms whipped peanut spread",
        "zero calorie peanut spread"
    ],
    "https://amzn.to/40gmjGE": [
        "everything bagel seasoning",
        "everything bagel seasoning mix",
        "everything bagel seasoning blend",
        "everything bagel seasoning spice",
        "everything bagel spice",
        "everything bagel spice mix",
        "everything bagel spice blend",
        "everything bagel spice seasoning",
        "everything bagel spice seasoning mix",
        "everything bagel spice seasoning blend"
        "everything seasoning"
    ],
    'https://amzn.to/4pw27vM': [
        "yeast extract spread",
        "yeast extract",
        "marmite",
        "marmite yeast extract",
        "marmite spread",
        "marmite yeast extract spread"
    ],
    'https://amzn.to/4hqp55w': [
        # "yeast extract spread",
        # "yeast extract",
        "vegemite",
        "vegemite yeast extract",
        "vegemite spread",
        "vegemite yeast extract spread"
    ],
    "https://amzn.to/4wPTDC8": [
        "donut mold",
        "donut molds",
        "donut pan",
        "donut pans"
        "silicone donut molds",
        "silicone donut mold",
        "silicone donut pans",
        "silicone donut pan",
        "air fryer donut molds",
        "air fryer donut mold",
        "air fryer donut pans",
        "air fryer donut pan",
        "donut liners",
        "donut liner",
        "silicone donut liners",
        "silicone donut liner",
        "air fryer donut liners",
        "air fryer donut liner"
    ],
    "https://amzn.to/4vamaBm": [
        "mason jars",
        "mason jar",
        "small mason jars",
        "small mason jar",
    ],
    "https://amzn.to/4vedGsO": [
        "large mason jars",
        "large mason jar"
    ],
    "https://amzn.to/4bidRMq": [
        "hershey's zero sugar chocolate syrup",
        "hershey's sugar free chocolate syrup",
        "hershey's chocolate syrup",
        "sugar free chocolate syrup, storebought"
    ],
    "https://amzn.to/4aXnK21": [
        "pea protein powder",
        "pea protein isolate",
        "pea protein",
        "pea powder",
        "vegan protein powder",
        "vegan protein isolate"
    ],
    "https://amzn.to/4a5ULZB": [
        "standard lemonade",
        "storebought lemonade",
        "lemonade sweetened with sugar"
    ],
    "https://amzn.to/4enTf6c": [
        "standard limeade",
        "storebought limeade",
        "limeade sweetened with sugar"
    ],
    "https://amzn.to/4uJsVK5": [
        "storebought honey mustard dressing",
        "storebought honey mustard",
        "store bought honey mustard dressing",
        "storebought honey mustard",
        "commercial honey mustard dressings"
    ],
    "https://amzn.to/4obDT9v": [
        "aleias italian style",
        "aleia's italian style"
    ],
    "https://amzn.to/49FHMxv": [
        "metamucil psyllium husk powder",
        "metamucil psyllium husks",
        "metamucil psyllium husk",
        "metamucil psyllium",
        "metamucil"
    ],
    "https://amzn.to/4wVWdYl": [
        "fage yogurt",
        "fage"
    ],
    "https://amzn.to/4v01SLH": [
        "cheesecloth",
        "cheese cloth"
    ],
    "https://amzn.to/43IY4C9": [
        "duncan hines keto brownie mix",
        "duncan hines keto brownies",
        "duncan hines keto brownie",
        "duncan hines keto boxed brownie mix",
        "duncan hines keto boxed brownies",
        "duncan hines keto boxed brownie",
        "keto box",
        "keto mix"
    ],
    "https://amzn.to/4dNQWdX": [
        "duncan hines dark chocolate fudge brownie mix",
        "duncan hines dark chocolate fudge brownies",
        "duncan hines dark chocolate fudge brownie"
        "duncan hines dark chocolate brownie mix",
        "duncan hines dark chocolate brownies",
        "duncan hines dark chocolate brownie",
        "duncan hines boxed brownie mix",
        "duncan hines brownie mix",
        "duncan hines brownies",
        "duncan hines brownie",
        "duncan hines dark chocolate boxed brownie mix",
        "duncan hines dark chocolate boxed brownies",
        "duncan hines dark chocolate boxed brownie",
        "standard duncan hines brownies"
    ],
    "https://amzn.to/4wdSyoe": [
        "zero net carb tortillas",
        "zero net carb tortilla",
        "carb balance tortillas",
        "carb balanace tortilla",
        "zero net carb wraps",
        "zero net carb wrap",
        "carb balance wraps",
        "carb balanace wrap"
    ],
    "https://amzn.to/4w2GB4Q": [
        "kettle and fire bone broth",
        "kettle & fire bone broth",
        "kettle and fire broth",
        "kettle & fire broth",
        "kettle and fire",
        "kettle & fire"
    ],
    # "https://amzn.to/4vLldRa": [
    #     "psyllium husks",
    #     "psyllium husk",
    #     "psyllium",
    #     "psyllium's",
    #     "unflavored psyllium husks",
    #     "unflavored psyllium husk",
    #     "unflavored psyllium",
    #     "plain psyllium husks",
    #     "plain psyllium husk",
    #     "plain psyllium"
    #     "unflavored, plain psyllium husks",
    #     "unflavored, plain psyllium husk",
    #     "unflavored, plain psyllium"
    #     "plain, unflavored psyllium husks",
    #     "plain, unflavored psyllium husk",
    #     "plain, unflavored psyllium"
    # ],
    "https://amzn.to/4dGuPpJ": [
        "rice paper",
        "rice paper wrap"
    ],
    "https://amzn.to/4uKqFT3": [
        "phyllo dough",
        "phyllo",
        "filo dough",
        "filo",
        "fillo dough",
        "fillo",
        "phyllo pastry",
        "filo pastry",
        "fillo pastry",
        "phyllo dough sheets",
        "phyllo sheets",
        "filo dough sheets",
        "filo sheets",
        "fillo dough sheets",
        "fillo sheets"
    ],
    'https://amzn.to/3TbDFnv': [
        "veggie better than bouillon",
        "vegetable better than bouillon",
        "better than bouillon vegetable",
        "better than bouillon veggie"
    ],
    "https://amzn.to/4c6GlII": [
        "chicken better than bouillon",
        "better than bouillon chicken",
        "better than bouillon"
    ],
    "https://amzn.to/3QiSinj": [
        "chicken bouillon powder",
        "bouillon powder"
    ],
    "https://amzn.to/4sUCq9c": [
        "chicken bouillon cubes",
        "chicken bouillon cube",
        "bouillon cubes",
        "bouillon cube"
    ],
    "https://amzn.to/4uVLBYm": [
        "standard dubai chocolate bar",
        "standard dubai chocolate"
    ],
    "https://amzn.to/4kGEfC5": [
        "sugar free chocolate chips",
        "sugar free chocolate chip"
    ],
    "https://amzn.to/43lbOE5": [
        "magnesium glycinate",
        "magnesium <i>glycinate</i>",

    ],
    "https://amzn.to/4jl3nx0": [
        "magnesium malate",
        "magnesium <i>malate</i>"
    ],
    "https://amzn.to/43xsRBI": [
        "sodium chloride"
    ],
    "https://amzn.to/3P2NFNU": [
        "potassium chloride"
    ],
    "https://amzn.to/414BfHP": [
        "cooking gloves",
        "kitchen gloves",
        "cooking glove",
        "kitchen glove"
    ],
    "https://amzn.to/4bu23Gx": [
        "manuka honey",
        "manuka",
        "50+"
    ],
    "https://amzn.to/3N5x2k1": [
        "10+"
    ],
    "https://amzn.to/4uxIiqc": [
        "850+"
    ],
    "https://amzn.to/4rhYDwh": [
        "carob powder",
        "carob"
    ],
    "https://amzn.to/46PSfov": [
        "instant pot",
        "pressure cooker"
    ],
    "https://amzn.to/3Ffts2R": [
        "small glass meal prep containers",
        "small glass meal prep container",
        "glass meal prep container",
        "meal prep container",
        "6.2 x 4.5\"",
        "6.2\" x 4.5\"",
        "glass containers",
        "glass container",
        "glass meal prep containers",
        "glass meal prep container",
        "meal prep containers",
        "meal prep container"
    ],
    "https://amzn.to/4hcIXsT": [
        "large glass container",
        "large glass containers",
        "large glass meal prep container",
        "large glass meal prep containers",
        "large meal prep containers",
        "large meal prep container"
    ],
    "https://amzn.to/3O5nlSH": [
        "pizza wheel",
        "pizza cutter"
    ],
    "https://amzn.to/4ccXgLm": [
        "baking stone",
        "pizza stone",
        "stone"
    ],
    "https://amzn.to/4raSjqy": [
        "metal spatula"
    ],
    "https://amzn.to/40F2aK0": [
        "silicone spatula",
        "spatula"
    ],
    "https://amzn.to/4xxgT8z": [
        "silicone tongs",
        "silicone tong",
        "tongs",
        "tong"
    ],
    "https://amzn.to/4w9zEO1": [
        "metal tongs",
        "metal tong"
    ],
    "https://amzn.to/44XmqKz": [
        "dough scraper"
    ],
    "https://amzn.to/43Cj65h": [
        "bread lame",
        "razorblade"
    ],
    "https://amzn.to/3SqwsMO": [
        "liquid monk fruit",
        # "liquid stevia or monk fruit",
        # "liquid monk fruit or stevia",
        # "liquid monk fruit (or stevia)",
        # "liquid stevia (or monk fruit)",
        # "liquid stevia",
        # "liquid stevia/monk fruit",
        # "liquid monk fruit/stevia"
        "monk fruit",
        "monk fruit extract",
    ],
    "https://amzn.to/45wOzIv": [
        "liquid stevia"
    ],
    "https://amzn.to/4sgDH9S": [
        "powdered peanut butter",
        "peanut flour",
        "powdered peanuts"
    ],
    "https://amzn.to/4ceFnvP": [
        "granulated monk fruit",
        "granulated sweeteners",
        "granulated sweetener",
        "granulated zero calorie sweeteners",
        "granular zero calorie sweeteners",
        "granulated zero calorie sweetener",
        "granular zero calorie sweetener",
        "granular sweeteners",
        "granular sweetener"
        "zero calorie sweetener",
        "low calorie sweetener"
    ],
    "https://amzn.to/43vQs5E": [
        "powdered monk fruit",
        "powdered sweeteners",
        "powdered sweetener",
        "powdered zero calorie sweeteners",
        "powder zero calorie sweeteners",
        "powdered zero calorie sweetener",
        "powder zero calorie sweetener",
        "powdered sweeteners",
        "powdered sweetener"
    ],
    "https://amzn.to/4mzsH5p": [
        "allulose"
    ],
    "https://amzn.to/4lkg3Hr": [
        "erythritol"
    ],
    "https://amzn.to/4beiNlT": [
        "granulated stevia",
        "stevia"
    ],
    "https://amzn.to/4layTR1": [
        "stevia sweetened electrolyte mix",
        "flavored electrolyte mix",
        "electrolyte mix",
        "electrolyte powder"
    ],
    "https://amzn.to/43ycqF2": [
        "lactase enzyme powder",
        "lactase enzyme"
    ],
    "https://amzn.to/47w8h7R": [
        "inulin"
    ],
    "https://amzn.to/45yjx2X": [
        "food scale",
        "kitchen scale",
        "scale"
    ],
    "https://amzn.to/4q0AUjI": [
        "food processor"
    ],
    "https://amzn.to/3VHhgMM": [
        "hand blender",
        "small blender or food processor",
        "small blender or food chopper",
        "small food processor",
        "small food chopper",
        "small blender",
        "immersion blender",
        "chopper"
    ],
    "https://amzn.to/3SsDLn7": [
        "large blender",
        "blender"
    ],
    "https://amzn.to/3FuWETp": [
        "air frying",
        "air fryers",
        "air fryer",
        "air fried",
        "air fry"
    ],
    "https://amzn.to/43AzcfI": [
        "silicone air fryer liner",
        "air fryer liner"
    ],
    "https://amzn.to/44T3n3X": [
        "silicone liner",
        "silicone baking mat",
        "silicone mat"
    ],
    "https://amzn.to/3YY2H9q": [
        "9\" square baking dishes",
        "9\" square baking dish",
        "9\" square baking pans",
        "9\" square baking pan",
        "9\" square pans",
        "9\" square pan",
        "9\" baking pans",
        "9\" baking pan",
        "9x9 square baking pans",
        "9x9 square baking pan",
        "9 inch square baking pans",
        "9 inch square baking pan",
        "9 in square baking pans",
        "9 in square baking pan",
        '9" square baking pan',
        '9" square pan',
        '9" square'
    ],
    "https://amzn.to/4aiCsjh": [
        "9x13in pans",
        "9x13in pan",
        "9x13\" casserole dishes",
        "9x13\" casserole dish",
        "9x13\" casserole pans",
        "9x13\" casserole pan",
        "9x13\" baking dishes",
        "9x13\" baking dish",
        "9x13\" baking pans",
        "9x13\" baking pan",
        "9x13\" pans",
        "9x13\" pan",
        "9 x 13\" casserole dishes",
        "9 x 13\" casserole dish",
        "9 x 13\" casserole pans",
        "9 x 13\" casserole pan",
        "9 x 13\" baking dishes",
        "9 x 13\" baking dish",
        "9 x 13\" baking pans",
        "9 x 13\" baking pan",
        "9 x 13\" pans",
        "9 x 13\" pan",
        '7x11"',
        '11x7"',
        '7 x 11"',
        '11 x 7"'
    ],
    "https://amzn.to/4mxxkxl": [
        "9\" cake pans",
        "9\" cake pan",
        "9\" circlular cake pans",
        "9\" circlular cake pan",
        "9\" circle cake pans",
        "9\" circle cake pan",
        "9\" circle pans",
        "9\" circle pan"
    ],
    "https://amzn.to/4q0gY0f": [
        "9\" pie pans",
        "9\" pie pan",
        "9\" circlular pie pans",
        "9\" circlular pie pan",
        "9\" circle pie pans",
        "9\" circle pie pan"

    ],
    "https://amzn.to/3YUjIkN": [
        "9x5\" bread pans",
        "9x5\" bread pan",
        "9 x 5\" bread pans",
        "9 x 5\" bread pan",
        "9x5\" loaf pans",
        "9x5\" loaf pan",
        "9 x 5\" loaf pans",
        "9 x 5\" loaf pan",
        "loaf pans",
        "loaf pan",
        "bread pans",
        "bread pan"
    ],
    "https://amzn.to/45sRAsB": [
        "cookie sheets",
        "cookie sheet",
        "baking trays",
        "baking tray",
        "baking sheets",
        "baking sheet",
        "baking pans",
        "baking pan"
    ],
    "https://amzn.to/3T1ymDy": [
        "mini muffin pans",
        "mini muffin pan",
        "mini-muffin pans",
        "mini-muffin pan",
        "mini muffin tins",
        "mini muffin tin",
        "mini-muffin tins",
        "mini-muffin tin"
    ],
    "https://amzn.to/4mzzEDl": [
        "muffin pans",
        "muffin pan"
    ],
    "https://amzn.to/3Fw6MeC": [
        "wooden spoons",
        "wooden spoon",
        "wooden spatulas",
        "wooden spatula"
    ],
    "https://amzn.to/4kmobG2": [
        "food thermometer",
        "instant thermometer",
        "thermometer",
        "internal temperature",
        # "registering",
        # "registered",
        "register",
        "130F",
        "135F",
        "140F",
        "145F",
        "150F",
        "155F",
        "160F",
        "165F",
        "170F",
        "175F",
        "180F",
        "185F",
        "190F",
        "195F",
        "200F",
        "205F",
        "210F",
        "215F",
        "inside temperature",
        "registered a temperature"
    ],
    "https://amzn.to/3Hdg0gk": [
        "spray of olive oil",
        "spray of oil",
        "spray the paper with oil",
        "spray the pan with oil",
        "spray with oil",
        "cooking spray",
        "oil spray",
        "spray",
        "lightly grease with oil",
        "lightly grease the paper with oil",
        "grease the paper with oil",
        "lightly spray with oil",
        "lightly spray",
        "grease with oil",
        "lightly oil",
        "refillable spray bottle",
        "spray bottle",
        "spray it with oil",
        "grease it with oil",
        "lightly grease it with oil",
        "lightly grease",
        "lightly oiled",
        "lightly greased"
    ],
    "https://amzn.to/4zyFnzN": [
        "large glass bowls",
        "large glass bowl",
        "medium glass bowls",
        "medium glass bowl",
        "small glass bowls",
        "small glass bowl",
        "glass bowls",
        "glass bowl",
        "large bowls",
        "large bowl",
        "medium bowls",
        "medium bowl",
        "small bowls",
        "small bowl",
        "small microwave safe bowls",
        "small microwave safe bowl",
        "small microwave-safe bowls",
        "small microwave-safe bowl",
        "microwave safe bowls",
        "microwave safe bowl",
        "microwave-safe bowls",
        "microwave-safe bowl",
        "large microwave safe bowls",
        "large microwave safe bowl",
        "large microwave-safe bowls",
        "large microwave-safe bowl",
        "medium microwave safe bowls",
        "medium microwave safe bowl",
        "medium microwave-safe bowls",
        "medium microwave-safe bowl"
    ],
    "https://amzn.to/4rb3CiD": [
        "metal bowls",
        "metal bowl"
    ],
    "https://amzn.to/45yqsbM": [
        "electric hand mixer",
        "electric mixer",
        "hand mixer"
    ],
    "https://amzn.to/4dFeyPZ": [
        "salad spinner"
    ],
    "https://amzn.to/4rdR0HI": [
        "12\" nonstick pans",
        "12\" nonstick pan",
        "12\" non-stick pans",
        "12\" non-stick pan",
        "12\" pans",
        "12\" pan",
        "12\"",
        "large pans",
        "large pan"
    ],
    "https://amzn.to/465aAxx": [
        "10\" cast iron pan",
        "10\" cast iron",
        "cast iron pan",
        "cast iron",
        "10\" cast iron skillet",
        "cast iron skillet",
        "10\" cast iron frying pan",
        "cast iron frying pan",
        "10\" cast iron fry pan",
        "cast iron fry pan",
        "cast-iron",
        "10\" cast-iron pan",
        "10\" cast-iron",
        "cast-iron pan",
    ],
    "https://amzn.to/4dBv5Ga": [
        "10\" nonstick pans",
        "10\" nonstick pan",
        "10\" non stick pans",
        "10\" non stick pan",
        "10\" non-stick pans",
        "10\" non-stick pan",
        "10\" pans",
        "10\" pan",
        "10\"",
        "medium nonstick pans",
        "medium nonstick pan",
        "medium non stick pans",
        "medium non stick pan",
        "mednium non-stick pans",
        "medium non-stick pan"
    ],
    "https://amzn.to/4qFE9y3": [
        "small pans",
        "small pan",
        "8\" pans",
        "8\" pan",
        "8\""
    ],
    "https://amzn.to/4pREQ61": [
        "stainless steel pans",
        "stainless steel pan"
    ],
    "https://amzn.to/49DLg42": [
        "stainless steel pots",
        "stainless steel pot"
    ],
    "https://amzn.to/46ccg8m": [
        "small sauce pot",
        "small sauce-pot",
        "small saucepot",
        "small sauce pots",
        "small sauce-pots",
        "small saucepots",
        "small pot",
        "small pots",
        "medium saucepot",
        "medium pot"
        "medium sauce pot",
        "medium sized saucepot",
        "medium sized pot",
        "medium sized sauce pot",
        "medium sized sauce-pot",
        "medium sized sauce pot",
    ],
    "https://amzn.to/3LNGdVy": [
        "dutch oven"
    ],
    "https://amzn.to/4bOh0on": [
        # "10\" pans",
        # "10\" pan",
        # "10\"",
        "10\" stainless steel pans",
        "10\" stainless steel pan",

    ],
    "https://amzn.to/4r5boL0": [
        "potato masher"
    ],
    "https://amzn.to/4q2FwWu": [
        "fine mesh strainer",
        "mesh strainer",
        "sift"
    ],
    "https://amzn.to/49ZXQcQ": [
        "spider"
    ],
    "https://amzn.to/4qQNmn2": [
        "wire racks",
        "wire rack",
        "cooling racks",
        "cooling rack"
    ],
    "https://amzn.to/44T3gFz": [
        "knife sharpener"
    ],
    "https://amzn.to/4jlDKwc": [
        "chef knife",
        "knives",
        "knife"
    ],
    "https://amzn.to/43gNqmY": [
        "cutting board"
    ],
    "https://amzn.to/4dHwY2G": [
        "measuring spoons",
        "measuring spoon"
    ],
    "https://amzn.to/4dFNtMP": [
        "measuring cups",
        "measuring cup"
    ],
    "https://amzn.to/49TUS9E": [
        "large slow cooker",
        "large slowcooker",
        "large crockpot",
        "large crock pot",
        "slow cooker",
        "slow cooked",
        "slowcooker",
        "crockpot",
        "crock pot"
    ],
    "https://amzn.to/4q3nlQz": [
        "mandoline"
    ],
    "https://amzn.to/4qZKHI9": [
        "chocolate bar mold",
        "chocolate mold"
    ],
    "https://amzn.to/40XU6EF": [
        "thick chocolate bar mold",
        "thick chocolate mold",
        "dubai chocolate bar mold",
        "dubai chocolate mold",
        "thick chocolate bar"
    ],

    # MISC
    "/misc/meat-cost-analysis": [
        "is fattier meat actually cheaper?",
        "is fattier meat actually cheaper",
        "ground meat cost analysis",
        "meat cost analysis"
    ],
    "/misc/psyllium-husk": [
        "psyllium husks",
        "psyllium husk",
        "psyllium",
        "psyllium's",
        "psyllium husk fiber",
        "psyllium fiber",
        "psyllium husk: hype or healthy?",
        "psyllium husk: hype or healthy"
    ],
    "/misc/caffeine": [
        "caffeine",
        "coffee",
        "caffeine: productivity tool or daily dependence?",
        "tea",
        "espresso"
    ],
    "/misc/costs": [
        # "costs",
        # "cost",
        "cost analysis"
    ],
    "/misc/chicken-leg-quarters": [
        "chicken leg quarters",
        "chicken leg quarter",
        "chicken legs",
        "chicken leg",
        "you should get chicken leg quarters",
        "you should be getting chicken leg quarters",
        "roasting chicken leg quarters",
        "roasting chicken leg quarter",
        "roasting chicken legs",
        "roasting chicken leg",
        "roasted chicken leg quarters",
        "roasted chicken leg quarter",
        "roasted chicken legs",
        "roasted chicken leg",
        "leg quarters",
        "leg quarter"
    ],
    "/misc/healthier-brownies-and-cookies-experiment": [
        "healthier brownies & cookies experiment",
        "healthier brownies & cookies",
        "healthy brownies & cookies experiment",
        "healthy brownies & cookies",
        "healthier brownies and cookies experiment",
        "healthier brownies and cookies",
        "healthy brownies and cookies experiment",
        "healthy brownies and cookies"
    ],
    "/misc/olive-oil": [
        "extra-virgin olive oil",
        "extra virgin olive oil",
        "virgin olive oil",
        "olive oil",
        "EVOO",
        "oil",
        "olive oils",
        "extra-virgin oils",
        "extra virgin oils",
        "extra-virgin oil",
        "extra virgin oil",
        "olive oil's",
        "extra-virgin olive oil's",
        "extra virgin olive oil's"
    ],
    "/misc/natural-sweeteners": [
        "natural sweeteners",
        "natural sweetener",
        "natural sugars",
        "natural sugar",
        "unrefined sugars",
        "unrefined sugar",
        '"natural" sugars',
        '"natural" sugar',
        '"natural" (or "unrefined") sugars',
        '"natural" (or "unrefined") sugar'
    ],
    "/misc/natural-sweeteners#sugar-free": [
        "zero calorie natural sweeteners",
        "zero calorie natural sweetener",
        "zero-calorie natural sweeteners",
        "zero-calorie natural sweetener",
        "sugar free natural sweeteners",
        "sugar freee natural sweetener",
        "sugar-free natural sweeteners",
        "sugar-free natural sweetener",
        "zero-calorie sugar substitutes",
        "zero calorie sugar substitutes",
        "zero-calorie sugar substitute",
        "zero calorie sugar substitute"
    ],
    "/misc/natural-sweeteners#honey": [
        "honey"
    ],
    "/misc/natural-sweeteners#maple-syrup": [
        "maple syrup"
    ],
    "/misc/natural-sweeteners#agave": [
        "agave syrup",
        "agave"
    ],
    "/misc/natural-sweeteners#coconut-sugar": [
        "coconut sugar"
    ],
    "/misc/natural-sweeteners#date-sugar": [
        "date sugar",
        "date syrup"
    ],
    "/misc/processed-foods": [
        "processed stuff",
        "processed foods",
        "processed food",
        "highly processed",
        "ultra processed snacks",
        "ultraprocessed snacks",
        "ultra-processed snacks",
        "ultra processed snack",
        "ultraprocessed snack",
        "ultra-processed snack",
        "ultra processed junk",
        "ultraprocessed junk",
        "ultra-processed junk",
        "ultra processed",
        "ultraprocessed",
        "ultra-processed",
        "processed",
        "ultraprocessed \"foods\"",
        "ultraprocessed \"food\"",
        "ultra processed \"foods\"",
        "ultra-processed \"foods\"",
        "ultra processed \"food\"",
        "ultra-processed \"food\"",
        "ultraprocessed foods",
        "ultraprocessed food",
        "ultra processed foods",
        "ultra-processed foods",
        "ultra processed food",
        "ultra-processed food",
        "ultra processed",
        "ultra-processed",
        "heavily processed",
        "processed"
    ],
    "/misc/apple-cider-vinegar": [
        "apple cider vinegar",
        "acv"
    ],
    "/misc/biotics": [
        "prebiotic",
        "probiotic",
        "postbiotic"
    ],
    "/misc/water-absorption": [
        "flour replacement",
        "flour alternative",
        "alternative flour",
        "flour substitute",
        "water absorption of different flours",
        "water absorption",
        "absorbs much more liquid",
        "absorbs more liquid",
        "absorbs much more water",
        "absorbs more water",
        "absorbs much less liquid",
        "absorbs less liquid",
        "absorbs much less water",
        "absorbs less water",
        "absorbs much more liquid",
        "absorb more liquid",
        "absorb much more water",
        "absorb more water",
        "absorb much less liquid",
        "absorb less liquid",
        "absorb much less water",
        "absorb less water"
    ],

    # FOOD SECTIONS
    "/hummus": [
        "hummus recipes here",
        "hummuses",
        "hummus recipes",
        "hummus",
        "hummus-like recipes",
        "hummus-like recipe",
        "hummus-like",
        "hummus like"
    ],
    "/oatmeal": [
        # "oats",
        "oatmeal recipes here",
        "oatmeal recipes",
        "oatmeal",
        "overnight oats recipes",
        "overnight oats recipe",
        "overnight oats",
        "overnight oat",
        "bowl of oatmeal",
        "bowl of oats"
    ],
    "/yogurt": [
        # "yogurt",
        "yogurt recipes here",
        "yogurt recipes",
        "morning yogurt",
        "yogurt bowl",
        "bowl of yogurt"
    ],
    "/nut-butter": [
        # "nut butter",
        "nut butter recipes here",
        "nut butter recipes"
    ],
    "/pesto": [
        "pesto recipes here",
        "pesto recipes",
        "pesto"
    ],
    "/soups-and-stews": [
        "soup and stew recipes here",
        "soup recipes here",
        "stew recipes here",
        "soup and stew recipes",
        "soups, stews",
        "soups and stews",
        "soup and stew",
        "soup recipes",
        "soups",
        "soup",
        "stew recipes",
        "stews",
        "stew",
        "chili recipes here",
        "chili recipes",
        "chili recipe"
    ],
    "/salad": [
        "salad recipes here",
        "salad recipes",
        "salads",
        "salad"
    ],
    "/salad-dressings": [
        "salad dressing recipes here",
        "dressing recipes here",
        "salad toppings",
        "salad dressing recipes",
        "homemade salad dressings",
        "homemade salad dressing",
        "homemade dressings",
        "homemade dressing",
        "salad dressings",
        "salad dressing",
        "dressing recipes",
        "dressing"
    ],
    "/brownies": [
        "brownie recipes here",
        "brownies",
        "brownie recipes",
        "brownie",
        "brookies",
        "brookie",
        "blondies",
        "blondie",
        "healthy brownies recipes",
        "healthy brownie recipe",
        "brownie recipe",
        "healthy brownies",
        "healthy brownie",
        "healthier brownies",
        "healthier brownie"
    ],
    "/cookies": [
        "cookie recipes here",
        "cookies",
        "cookie recipes",
        "cookie",
        "healthy cookie recipes",
        "healthy cookie recipe",
        "cookie recipe",
        "healthy cookies",
        "healthy cookie",
        "healthier cookies",
        "healthier cookie"
    ],
    "/copycat": [
        "copycat recipes here",
        "recreated",
        "copycat recipes",
        "copycat drinks",
        "copycat"
    ],
    "/vic": [
        "vic's",
        "vic"
    ],
    "/protein-bar": [
        "protein bar recipes",
        "protein bar recipe",
        "protein bars",
        "protein bar",
        '"protein" bars',
        '"protein" bar',
        '"protein" bar recipes',
        '"protein" bar recipe'
    ],
    "/beans": [
        "bean recipes here",
        "bean recipes",
        "bean recipe"
    ],

    # RECIPE TYPES
    "/recipes/bread": [
      # "flatbreads",
      # "flatbread",
      # "buns",
      # "bun",
      # "bagels",
      # "bagel",
      # "rolls",
      # "roll",
      "breadmaking",
      "bread making",
      "baking breads",
      "baking bread",
      "real breads",
      "real bread",
      "bread recipes",
      "bread recipe",
      "breads",
      "bread"
    ],
    "/recipes/breakfast": [
        "breakfasts",
        "breakfast"
    ],
    "/recipes/drinks": [
        "drinks",
        "drink"
    ],
    "/recipes/finger-food": [
        "finger foods",
        "finger food"
    ],
    "/recipes/ground-meat": [
        "ground meat"
    ],
    "/recipes/healthier-dessert": [
        "healthier desserts",
        "healthier dessert",
        "healthier baking",
        "healthy baking dessert",
        "healthy baking",
        "healthy baked goods",
        "healthy baked good",
        "baked goods",
        "baked good",
        "healthy desserts",
        "healthy dessert",
        "mildly sweetened desserts",
        "mildly sweetened dessert",
        "mildly-sweetened desserts",
        "mildly-sweetened dessert",
        "baking",
        "desserts",
        "dessert"
    ],
    "/recipes/meatless": [
        "meatless dish",
        "meatless",
        "meatless meals",
        "meatless meal",
        "vegetarian meals",
        "vegetarian meal",
        "vegetarian",
        "vegetarians",
        "vegetarian dishes",
        "plant-based meals",
        "plant-based meal",
        "plant-based",
        "plant based meals",
        "plant based meal",
        "plant based",
        "plant-based dishes",
        "plant based dishes"
    ],
    "/recipes/meme": [
        "meme recipes",
        "meme recipe",
        "meme"
    ],
    "/recipes/protein-powder": [
        # "protein powder",
        "protein powder desserts",
        "protein powder dessert",
        "protein based desserts",
        "protein based dessert",
        "protein packed desserts",
        "protein packed dessert",
        "protein desserts",
        "protein dessert",
        "protein snacks",
        "protein snack",
        "protein desserts",
        "protein dessert",
        "high-protein desserts",
        "high-protein dessert",
        "high protein desserts",
        "high protein dessert"
    ],
    "/recipes/savory-sauces": [
        # "sauce",
        "sauces and dips",
        "savory sauces",
        "savory sauce",
        "savory sauce recipes",
        "sauce recipes",
        "savory sauce recipe",
        "sauce recipe",
        "sauces"
    ],
    "/recipes/sides": [
      "sides",
      "on the side",
      "side dishes",
      "side dish",
      "side"
    ],
    "/recipes/sweet-spreads": [
      "sweet spreads",
      "sweet spread",
      "spreads"
    ],

    # OVERSHADOWED
    # "/misc/overshadowed-healthy-foods#chocolate": [
    #     "real dark chocolate",
    #     "true dark chocolate",
    #     "dark chocolate (at least 85%)",
    #     "dark chocolate (100%)",
    #     "dark chocolate",
    #     "100% chocolate",
    #     "100% bar",
    #     "95% chocolate",
    #     "95% bar",
    #     "85-90% chocolate",
    #     "90% chocolate",
    #     "90% bar",
    #     "85% chocolate",
    #     "85% bar",
    #     "72% chocolate",
    #     "72% bar",
    #     "super dark chocolate",
    #     "unsweetened chocolate",
    #     "cocoa powder",
    #     "cocoa",
    #     "cacao powder",
    #     "cacao"
    # ],

    # COCOA
    "/misc/chocolate-benefits": [
        "real dark chocolate",
        "true dark chocolate",
        "dark chocolate (at least 85%)",
        "dark chocolate (100%)",
        "dark chocolate",
        "100% chocolate",
        "100% bar",
        "95% chocolate",
        "95% bar",
        "85-90% chocolate",
        "90% chocolate",
        "90% bar",
        "85% chocolate",
        "85% bar",
        "72% chocolate",
        "72% bar",
        "super dark chocolate",
        "unsweetened chocolate",
        "cocoa powder",
        "cocoa",
        "cacao powder",
        "cacao",
        # "chocolate chips",
        "chocolate"
    ],

    # FAKE HEALTHY FOODS
    "/misc/fake-healthy-foods": [
        "healthy trap foods",
        "healthy trap food",
        "healthy foods",
        "healthy food",
        "healthier foods",
        "healthier food",
        "trap foods",
        "trap food",
        "junk foods",
        "junk food"
    ],
    "/misc/fake-healthy-foods#rice-cakes": [
        "flavored rice cakes",
        "flavored rice cake",
        "rice cakes",
        "rice cake"
    ],
    "/misc/fake-healthy-foods#dips": [
        # "dips",
        # "dessert hummus",
        "mayonnaise",
        "light mayo",
        "honey mustard",
        "ranch dressing",
        "ranch",
        "french onion dip",
        "mayo-based",
        "mayo",
        "ketchup",
        "commercial bbq sauces",
        "commercial bbq sauce",
        "bbq sauces",
        "bbq sauce",
        "barbeque sauces",
        "barbeque sauce"
    ],
    "/misc/fake-healthy-foods#sauces": [
        "jarred pasta sauces",
        "jarred pasta sauce",
        "jarred sauces",
        "jarred sauce",
        "bottled sauces",
        "bottled sauce",
        "pasta sauces",
        "cocktail sauce",
        "pizza sauce",
        "tartar sauce",
        "storebought pesto",
        "alfredo"
    ],
    "/misc/fake-healthy-foods#chocolate": [
        # "dark chocolate",
        "chocolate (less than 70%)"
    ],
    "/misc/fake-healthy-foods#sugar-substitutes": [
        # "sugar alcohols erythritol",
        # "sugar alcohol erythritol",
        # "erythritol",
        "sugar alcohols maltitol",
        "sugar alcohol maltitol",
        "maltitol",
        "sugar alcohols xylitol",
        "sugar alcohol xylitol",
        "xylitol",
        "sugar alcohols sorbitol",
        "sugar alcohol sorbitol",
        "sorbitol",
        "sugar alcohols",
        "sugar alcohol",
        "sugar substitutes",
        "sugar substitute",
        "artificial sweeteners sucralose",
        "artificial sweetener sucralose",
        "sucralose",
        "artificial sweeteners aspartame",
        "artificial sweetener aspartame",
        "aspartame",
        "artificial sweeteners saccharin",
        "artificial sweetener saccharin",
        "saccharin",
        # "allulose",
        "artificial sweeteners",
        "artificial sweetener"
    ],
    "/misc/fake-healthy-foods#cereal": [
        "cereal bars",
        "cereal bar",
        "breakfast cereals",
        "breakfast cereal",
        "cereals",
        "cereal"
    ],
    "/misc/fake-healthy-foods#dried-fruit": [
        "sweetened canned fruits",
        "sweetened dried fruits",
        "sweetened canned fruit",
        "sweetened dried fruit",
        "canned fruits",
        "canned fruit",
        "dried fruits",
        "dried fruit"
    ],
    "/misc/fake-healthy-foods#nutella": [
        "nutella"
    ],
    "/misc/fake-healthy-foods#nuts": [
        "flavored nuts"
    ],
    "/misc/fake-healthy-foods#sports-drinks": [
        "flavored drinks",
        "flavored drink",
        "sports drinks",
        "sports drink",
        "drink mixes",
        "drink mix",
        "electrolyte drinks",
        "electrolyte drink"
    ],
    "/misc/fake-healthy-foods#energy-drinks": [
        "energy drinks",
        "energy drink"
    ],
    "/misc/fake-healthy-foods#coffee": [
        "sweetened drinks",
        "sweetened drink",
        "sweetened coffees",
        "sweetened coffee",
        # "coffees",
        # "caffeine additions",
        # "caffeine adiction",
        # "caffeine addicts",
        # "caffeine addict",
        # "caffeine",
        # "coffee",
        "coffee addictions",
        "coffee addiction",
        "coffee addicts",
        "coffee addict"
    ],
    "/misc/fake-healthy-foods#iced-tea": [
        "sweetened teas",
        "sweetened tea",
        "iced teas",
        "iced tea"
    ],
    "/misc/fake-healthy-foods#diet-soda": [
        "diet drinks",
        "diet drink",
        "diet sodas",
        "diet soda",
        "diet coke",
        "sodas",
        "soda"
    ],
    "/misc/fake-healthy-foods#muffins": [
        "mini muffins",
        "mini-muffins",
        "mini muffin",
        "muffins",
        "muffin"
    ],
    "/misc/fake-healthy-foods#banana-bread": [
        "banana bread"
    ],
    "/misc/fake-healthy-foods#pancakes": [
        "waffles and pancakes",
        "waffles or pancakes",
        "waffles",
        "pancakes",
        "pancake",
        "waffle",
        "waffles/pancakes",
        "waffle/pancake"
    ],
    "/misc/fake-healthy-foods#seed-oil": [
        "inflammatory oils",
        "inflammatory fats",
        "palm or vegetable oils",
        "palm or vegetable oil",
        "peanut oil",
        "rice bran oil",
        "inflammatory oil",
        "vegetable oils",
        "vegetable oil",
        "refined seed oils",
        "refined seed oil",
        "seed oils",
        "seed oil",
        "canola oil",
        "corn oil",
        "cottonseed oil",
        "vegetable/seed oils",
        "vegetable/seed oil",
        "grapeseed oil",
        "safflower oil",
        "soybean oil",
        "palm oil",
        "sunflower oil",
        "highly refined oils",
        "highly refined oil",
        "heavily refined oils",
        "heavily refined oil",
        "refined oils",
        "refined oil"
    ],
    "/misc/fake-healthy-foods#frozen-meals": [
        "pre-prepared processed meals",
        "pre-prepared processed meal",
        "prepared processed meals",
        "prepared processed meal",
        "processed meals",
        "processed meal",
        "frozen meals",
        "frozen meal",
        "pre-prepared meals",
        "pre-prepared meal",
        "preprepared meals",
        "preprepared meal",
        "pre prepared meals",
        "pre prepared meal",
        "prepared meals",
        "prepared meal",
        "canned soup",
        "ramen cups",
        "ramen cup",
        "instant ramen",
        "ramen"
    ],
    "/misc/fake-healthy-foods#processed-meats": [
        "processed meats",
        "processed meat",
        "cured meats",
        "cured meat",
        "beef jerky",
        "deli meats",
        "deli meat",
        "sandwich meats",
        "sandwich meat",
        "lunch meats",
        "lunch meat",
        "cold cuts",
        "cold cut"
    ],
    "/misc/fake-healthy-foods#yogurt": [
        "flavored yogurts",
        "flavored yogurt",
        "vanilla yogurt",
        "strawberry yogurt",
        "sweetened yogurt"
    ],
    "/misc/fake-healthy-foods#granola": [
        "breakfast bars",
        # "breakfast bar",
        "granola bars",
        "granola bar",
        "granolas",
        "granola"
    ],
    "/misc/fake-healthy-foods#trail-mix": [
        "trail mix"
    ],
    "/misc/fake-healthy-foods#pretzels": [
        "pretzels",
        "pretzel"
    ],
    "/misc/fake-healthy-foods#crackers": [
        "graham crackers",
        "graham cracker",
        "crackers",
        "cracker"
    ],
    "/misc/fake-healthy-foods#chips": [
        "doritos",
        "dorito",
        "tortilla chips",
        "tortilla chip",
        "potato chips",
        "potato chip",
        "veggie straws",
        "veggie straw",
        "plantain chips",
        "plantain chip",
        "banana chips",
        "banana chip",
        "chips",
        "chip"
    ],
    "/misc/fake-healthy-foods#bread": [
        "white breads",
        "white bread",
        "storebought bread"
    ],
    "/misc/fake-healthy-foods#peanut-butter": [
        "processed no-stir peanut butters",
        "processed no stir peanut butters",
        "processed no stir peanut butter",
        "processed peanut butters",
        "processed peanut butter",
        "conventional peanut butters",
        "conventional peanut butter",
        "no-stir peanut butters",
        "no stir peanut butters",
        "no-stir peanut butter",
        "no stir peanut butter",
        "no-stir",
        "no stir",
        "peanut butters"
    ],
    "/misc/fake-healthy-foods#jelly": [
        # "jelly",
        # "jam",
        "grape jelly",
        "grape jam",
        "jam and jelly",
        "jelly and jam",
        "most fruit jams",
        "most fruit jam",
        "most fruit jellies",
        "most fruit jelly",
        "fruit jams",
        "fruit jam",
        "fruit jellies",
        "fruit jelly"
    ],
    "/misc/fake-healthy-foods#cornbread": [
        "cornbread"
    ],
    "/misc/fake-healthy-foods#potatoes": [
        "french fries",
        "french fry",
        "fries"
    ],
    "/misc/fake-healthy-foods#juice": [
        "fruit juices",
        "fruit juice",
        # "lemonade",
        "juice"
    ],
    "/misc/fake-healthy-foods#oats": [
        "flavored instant oatmeal",
        "flavored instant oats",
        "instant oatmeal",
        "oatmeal packets",
        "instant oats",
        "flavored oatmeal",
        "flavored oats"
    ],
    "/misc/fake-healthy-foods#baked-beans": [
        "canned baked beans",
        "pre-prepared baked beans",
        "preprepared beans",
        "prepared baked beans",
        "baked beans"
    ],
    "/misc/beans#refried-beans": [
        "canned refried beans",
        "refried beans"
    ],
    "/misc/fake-healthy-foods#salad-dressing": [
        "bottled salad dressings",
        "bottled salad dressing",
        "balsamic vinaigrette",
        "raspberry vinaigrette",
        "italian dressing",
        "thousand island dressing",
        "thousand island",
        "caesar dressing",
        "caesar"
    ],
    "/misc/fake-healthy-foods#milk": [
        "sweetened almond milk",
        "chocolate almond milk",
        "chocolate milk",
        "sweetened milks",
        "sweetened milk",
        "flavored milks",
        "flavored kefirs",
        "flavored milk",
        "flavored kefir",
        "commercial almond milks",
        "commercial almond milk",
        "strawberry milk",
        "sweetened almond milk",
        "sweetened milk"
    ],
    "/misc/fake-healthy-foods#low-fat": [
        "low fat peanut butter",
        "low fat salad dressing",
        "low fat crackers"
    ],
    "/misc/fake-healthy-foods#popcorn": [
        "movie theater or microwave popcorn",
        "movie theater popcorn",
        "movie popcorn",
        "theater popcorn",
        "microwave popcorn",
        "microwave bags of popcorn"
    ],
    "/misc/fake-healthy-foods#margarine": [
        "margarine",
        "low fat butter",
        "lowfat",
        "shortening",
        "vegetable oil spreads",
        "vegetable oil spread"
    ],
    "/misc/fake-healthy-foods#fake-meat": [
        "ultraprocessed fake meat",
        "ultra processed fake meat",
        "ultra-processed fake meat",
        "processed fake meat",
        "fake meat"
    ]

}

EXCLUDED_PHRASES = [
    "certainly be baking",
    "oat layer",
    "with some monk fruit extract",
    "the monk fruit is there to add additional sweetness that the <a href='https://amzn.to/4lkg3Hr'>erythritol</a> lacks",
    "the monk fruit is there to add additional sweetness that the erythritol lacks",
    "(monk fruit only)",
    "<a href='https://amzn.to/4lkg3Hr'>erythritol</a> + monk fruit",
    "erythritol + monk fruit",
    "the former is a granulated sweetener",
    "<i>only</i> monk fruit",
    "lemon, lime, grapefruit, hot chocolate, and pumpkin spice",
    "tortilla into 96 chips",
    "wrap it",
    "chocolate chunk",
    "chocolate chunks",
    "wrap in",
    "homemade electrolyte powder!  This is a bulk base recipe",
    "<i>Lemon</i>",
    "INGREDIENTS(electrolyte-lemon)",
    "<i>Lime</i>",
    "INGREDIENTS(electrolyte-lime)",
    "<i>Grapefruit</i>",
    "INGREDIENTS(electrolyte-grapefruit)",
    "<i>Hot Chocolate</i>",
    "INGREDIENTS(electrolyte-cocoa)",
    "<i>Pumpkin Spice</i>",
    "INGREDIENTS(electrolyte-spice)",
    "added sugar free sweetener",
    "to make an electrolyte drink",
    "<b>10 g</b> serving of electrolyte powder",
    "added sugar-free sweetener",
    "similar (but sweetened) fudge recipe",
    "96 chips",
    "these tortilla chips",
    "return the chips",
    "most frozen acai",
    "chocolate mixture",
    "<b>Cheese</b>",
    "leave the bread in the oven",
    "until the sides",
    "if using chocolate",
    "if you're using chocolate",
    "savory bread",
    "sweet bread",
    "chocolate bread",
    "cheese ingredients",
    "cheese mix",
    "on top of the cheese",
    "noodles, cheese, and sauce",
    "leaner cuts of ground meat",
    # "exactly 93% meat and 7% fat",
    "although 93% lean beef",
    "85% lean and 80% lean beef",
    "the 93% lean beef costs",
    "fattier ground meat",
    "85% lean",
    "80% and 85% beef",
    "80% lean",
    "that 93% lean beef",
    "than 80% beef",
    "than 85% beef",
    "and 93% lean beef",
    "peanut butter on top",
    "chocolate brownies",
    "donut batter",
    "protein glaze",
    "only glaze",
    "then glaze",
    "chocolate brownie",
    "cheesecake layer",
    "cheesecake ingredients",
    "cheesecake batter",
    "cheesecake filling",
    "brownie layer",
    "brownie and cheesecake",
    "creamy ice cream",
    "like ice cream",
    "ice cream bar",
    "ice cream bars",
    "hard ice cream",
    "short-chain fatty acids",
    # "some don't have protein powder",
    # "happens to have protein powder",
    "have your cake",
    "this cake",
    "the cake",
    "one cake",
    "other cake",
    "in the cake itself",
    "bulgur wheat",
    "juice that is",
    "coffee beans",
    "coffee bean",
    "cacao pods",
    "cacao pod",
    "kola nuts",
    "kola nut",
    "fat utilization",
    "Black:",
    "juice not from",
    "soda water",
    "chocolate baked oats",
    "baked oats",
    "this honey mustard recipe",
    "club soda",
    "your cookie dough",
    "hemoglobin, a protein",
    "apple cinnamon",
    "pistachio chocolate",
    "pistachio mix",
    "pistachio mint",
    "cranberry apple",
    "red raspberry",
    "lemon ginger",
    "C TIER",
    "D TIER",
    "turmeric ginger"
    "pink/orange",
    "don't overbake, as cookies",
    "and whey to airtight containers",
    "baked sweet potato brownies",
    "starter culture",
    "baked sweet potato brownie",
    "as the sweet potato brownies were",
    "bowl with oil",
    "larger test of sweet potato brownies",
    "traditional brownie texture",
    "dry baked good",
    "swapping the oil",
    "instead of oil until",
    "baking one half",
    "even over the oil",
    "sugar brownies",
    "sweet potato traditional brownies",
    "same cannot be said for traditional brownies",
    "and oil.  The batter",
    "1 cup oil",
    "4 tbsp oil",
    "the standard brownies were great",
    "bowl with the oil",
    "oil in a box of brownie mix",
    "instead of oil",
    "baked as mini muffins",
    "time for mini muffins",
    "4 mini muffins",
    "bean brownie recipes",
    "larger scale",
    "then scale",
    "cookie batter",
    "for some healthy cornbread recipes",
    "this healthy cornbread",
    "the cornbread",
    "this cornbread",
    "sandwich cookies",
    "sandwich cookie",
    "6 cookies",
    "couple of healthy cornbread recipes",
    "corn cake",
    "bodily fat",
    "body fat",
    "pizza crust",
    "1 dessert",
    "double chocolate",
    "cookie is set",
    "chocolate is melty",
    "one dessert",
    "1 medium sized tortilla",
    "tortilla or crepe",
    "this sugar free syrup is also",
    "let the syrup rest at room temperature",
    "10\" circle",
    "1 side",
    "crepes, wraps, sandwiches, quesadillas, or even pizza",
    "pliable wraps",
    "each wrap's batter",
    "any wrap after the",
    "crepe batter",
    "keep the protein powder",
    "this is the juice",
    "mix together fruit juice",
    "thickens the juice",
    "mango/peach fruit juice",
    "jelly recipe",
    "of jelly today",
    "chicken, beef, turkey, veggie, etc.",
    "chocolate quinoa crisps",
    '"pancake"',
    "without any oil",
    "trail mixes and granola",
    "quinoa seeds",
    "raw quinoa",
    "quinoa scotcheroos",
    "taco spices",
    "taco night",
    "homemade broth, and delicious chicken fat",
    "chicken fat jar",
    "we essentially get chicken broth and chicken fat for free",
    "rendered out chicken fat",
    "1 cup (24 g) bone broth",
    "1 cup (240 g) of bone broth",
    "real bone broth is quite costly",
    "and then the sides",
    "milk mixture",
    "ice cream maker",
    "chicken at 250F",
    "the chicken should be thoroughly cooked through",
    "when the chicken is done",
    "after the chicken is done baking",
    "bits of chicken starting to fry",
    "lean chicken meat",
    "different cuts of chicken",
    "chicken drumsticks",
    "chicken drumstick",
    "cheapest cut of chicken",
    "of raw chicken",
    "of cooked chicken meat",
    "leftover cooked chicken with some",
    "some of my cooked chicken to make my",
    "for some recipes using leftover cooked chicken",
    "time intensive part is just shredding the chicken",
    "just combine all your shredded meat",
    "separate the lean meat",
    "split chicken breasts",
    "split breasts",
    "split chicken breast",
    "split breast",
    "raw meat weight",
    "factor in the raw meat weight",
    "how much does it cost",
    "of raw meat",
    "but net meat isn't",
    "net meat",
    "per pound of cooked meat",
    "cost per pound",
    "skim the fat",
    "assuming that meat loses about",
    "cooked meat corresponds to",
    "that makes the meat from leg quarters",
    "kettle and fire bone broth",
    "rendered out fat",
    "solidify the fat",
    "mason jars of fat",
    "both the jars of fat",
    "golden colored fat",
    "and then there's the fat",
    "(142 g) of fat",
    "grilled cheese",
    "fried rice",
    "ginger (ground)",
    "flour blend",
    "side by side",
    "cupcakes, muffins",
    "delicious and healthy frosting for all",
    "wrap in foil",
    "shaved chocolate",
    "oil, and vanilla",
    "pistachio mixture",
    "in the syrup you pour",
    "coat it in chocolate",
    "delicious and rich edible cookie dough",
    "dubai style chocolate",
    "coconut palm",
    "palm sap",
    "thick chocolate bar",
    "plain shredded wheat cereal",
    "shredded wheat cereal",
    "your wheat cereal",
    "combine the cereal",
    "remaining chocolate",
    # "chocolate outside",
    "almond paste",
    "pistachio dough",
    "in the chocolate",
    "chocolate candies",
    "excess chocolate",
    "blends of oils",
    "actual baked cookies",
    "canola, corn",
    "safflower, soybean",
    "and sunfower oils",
    '"vegetable" oil',
    "animal fats",
    "animal fat",
    "making this edible cookie dough",
    "If you're a fan of edible cookie dough",
    "crunchy cookies",
    "crunchy cookie",
    "the cookies and the brownies",
    "mint chocolate chip cookie or mint chocolate brownie",
    "mint chocolate chip cookies",
    "mint chocolate chip cookie",
    "mint chocolate brownies",
    "mint chocolate brownie",
    "peanut butter chocolate chip cookies",
    "peanut butter chocolate chip cookie",
    "baked brownies",
    "raw cookie dough",
    "these cookies",
    "fairly small cookie",
    "tate's cookie",
    "these brownies",
    "fairly small brownie",
    "true for cookies",
    "passable cookies",
    "passable cookie",
    "experimental brownies",
    "experimental brownie",
    "experimental cookies",
    "experimental cookie"
    "baking with",
    "standard chocolate chips",
    "into chocolate chips",
    "and oil, as",
    "amount of oil",
    "with the oil",
    # "oil, vinegar",
    # "vinegar, oil",
    # "oil, and warm",
    # "oil, baking",
    "more oil",
    "less oil",
    "packed in oil",
    "for the oil",
    "all the oil",
    "in oil",
    "oil, and sour cream",
    "oil or water",
    "<a href='/misc/dairy#butter'>butter</a> and oil",
    "<a href='/misc/dairy#butter'>butter</a> or oil",
    "<a href='/misc/dairy#butter'>butter</a>/oil",
    "oil and <a href='/misc/dairy#butter'>butter</a>",
    "oil or <a href='/misc/dairy#butter'>butter</a>",
    "oil/<a href='/misc/dairy#butter'>butter</a>",
    "<a href='/misc/dairy#butter'>butter</a>, oil",
    "oil, <a href='/misc/dairy#butter'>butter</a>",
    "oil to seperate",
    "nor oil"
    "the oil can",
    "off the oil",
    "top is just oil",
    "out the oil",
    "oil off",
    "oil on the top",
    "oil pressed",
    "oil press"
    "layer of oil",
    "because oil and water",
    "of oil gets",
    "an oil",
    "tons of oil",
    "lower oil",
    "tablespoons of oil",
    "your oil",
    "amounts of oil",
    "excess oil",
    "need for oil",
    "omitted the oil",
    "cut back on a bit of oil",
    "a bit of the oil",
    "tablespoon of oil",
    "oil replacements",
    "oil substitutes",
    "oil replacement",
    "oil substitute",
    "as opposed to oil",
    "chocolate flavor",
    "olive trees",
    "stone wheels",
    "high-quality oils",
    "higher-quality oils",
    "low-quality oils",
    "lower-quality oils",
    "lower-grade oils",
    "lower grade oils",
    "higher-grade oils",
    "higher grade oils",
    "high-quality oil",
    "higher-quality oil",
    "low-quality oil",
    "lower-quality oil",
    "177 - 210 C",
    "lower-grade oil",
    "lower grade oil",
    "higher-grade oil",
    "cooking fat",
    "higher grade oil",
    "olive tree",
    "culinary oils",
    "culinary oil",
    "brownie base",
    "entire brownie",
    "melted chocolate",
    "milk sugars",
    "honey-like",
    "honey-like consistency",
    "honey like consistency",
    "honey consistency",
    "consistency of honey",
    "sugar maple",
    "vanilla or chocolate",
    "chocolate or vanilla",
    "vanilla (or chocolate)",
    "chocolate (or vanilla)"
    "chocolate is firm",
    "chocolate on the other side",
    "harden the chocolate",
    "frozen berries",
    "beet juice",
    "pickled beet juice",
    "pickled beets",
    "pickled beet",
    "cookie layers",
    "cookie layer",
    "chocolate spread",
    "chocolate coating",
    "large scale",
    "large-scale",
    "cocoa beans",
    "cocoa bean",
    "cacao beans",
    "cacao bean",
    "carob beans",
    "carob bean",
    "cocoa plants",
    "cocoa plant",
    "cacao plants",
    "cacao plant",
    "carob plants",
    "carob plant",
    "cocoa trees",
    "cocoa tree",
    "cacao trees",
    "cacao tree",
    "carob trees",
    "carob tree",
    "vegetable steam",
    "wrap each",
    # "maple syrup",
    # "honey",
    "potato bread",
    "potato buns",
    "potato bun",
    "PB&J",
    "PBJ",
    "strawberry jam",
    "cranberry sauce",
    "scale it up",
    "shortening the",
    "cucumber salad",
    "flour, baking powder",
    "honey cornbread",
    "squash meat",
    "scale the recipe",
    "the same flour",
    "broccoli rabe",
    "yellow rice",
    "concentrate the starch",
    "and the cheese",
    "lemon potatoes",
    "as some desserts",
    '"rice"',
    "arrange fries",
    "arrange the fries",
    "bean salad",
    "cheese substitute",
    "fruit salsa",
    "orange color",
    "sodium citrate",
    "american cheese",
    "blue cheese dressing",
    "homemade mayo",
    "deviled eggs",
    "egg salad",
    "macaroni salad",
    "400 g of ketchup",
    "favorite spreads and sauces",
    "peanut chili",
    "store-bought hummus",
    "storebought hummus",
    "store bought hummus",
    "orange hue",
    "stems (and seeds",
    "my bbq sauce",
    "the banana bread should",
    "the glaze",
    "non-protein",
    "your flour",
    "spread to",
    "apple bread",
    "chickpea chows",
    # "dessert hummus",
    "banana brownies",
    "2 cookies",
    "be baking",
    "oat cookies",
    "oat cookie",
    "cookie ingredients",
    "brownie ingredients",
    "bread ingredients",
    # "traditional brownies",
    # "traditional brownie",
    # "traditional cookies",
    # "traditional cookie",
    "black bean brownies",
    "black bean brownie",
    "chickpea brownies",
    "chickpea brownie",
    "chickpea blondies",
    "chickpea blondie",
    "bean brownies",
    "bean brownie",
    "garlic or onion powders",
    "garlic or onion powder",
    "onion or garlic powders",
    "onion or garlic powder",
    "taco shell",
    "taco seasoning",
    "spaghetti tacos",
    "spaghetti taco",
    "cocoa fat",
    "coffee cake",
    "baking yesteryear",
    "onion flakes",
    "onion soup",
    "soda bread",
    "quick bread",
    "milk or white",
    "smooth butter forms",
    "tuna-salad-salad",
    "tuna-salad",
    "french onion soup",
    # "french onion dip",
    # "spinach artichoke",
    '"meat"-loaf',
    "by baking for",
    "cheesy rice",
    "pasta salad",
    "potato salad",
    'ground "meat"',
    "baking enough",
    "taco meat",
    "chipotle peppers",
    "chipotle pepper",
    "pecan pie",
    "combo of low fat",
    "store cookies",
    "24 cookies",
    "to baking",
    "standard full fat",
    "chocolate chip muffins",
    "chocolate chip muffin",
    "banana chocolate chip",
    "banana muffins",
    "banana muffin",
    "pumpkin blondies",
    "sized muffins",
    "sized muffin",
    "muffin tins",
    "48 mini muffins",
    "36 mini muffins",
    "pumpkin muffins",
    "pumpkin muffin",
    "pumpkin topping",
    "cooled brownies",
    "24 brownies",
    "16 brownies",
    "pumpkin brownies",
    "leftover brownies",
    "leftover brownie",
    "line a small pan with parchment paper",
    '10" x 6"',
    "flatten the cookies",
    "flatten the cookie",
    "air fry setting",
    "mint cookies",
    "mint cookie",
    "square cookies",
    "a lot of cookies",
    '"cookie" layers',
    "per cookie",
    "coating the cookies",
    "each baked cookie",
    "and baking at",
    "instant coffee",
    "mascarpone cheese",
    "layers of coffee",
    "also coffee and",
    "italian dessert",
    "fig newton",
    "peanut butter chips",
    "butterscotch chips",
    "dessert built",
    "chocolate graham crackers instead",
    "raw crackers",
    "you're baking",
    "bottom and sides",
    "blend the graham crackers",
    "pumpkin cake",
    "yogurt filling",
    "oatmeal crust",
    "oatmeal fudge",
    "oatmeal berry breakfast bars",
    "oatmeal berry breakfast bar",
    "finished cookies",
    "these cookies won't flatten",
    "milk chocolate",
    "other sugar free chocolate chip",
    "favorite sugar free chocolate chips",
    "chocolate peanut butter",
    "chocolate chip peanut butter",
    "up the sides",
    "and baking in",
    "24 mini muffins",
    "3 mini muffins",
    "6 mini muffins",
    "16 mini muffins",
    "look black",
    "left side",
    "right side",
    "vanilla (or almond)",
    "mini muffin liners",
    "mini muffin cups",
    "pecan butter chocolate truffles",
    "chocolate chip cookies",
    "chocolate chip cookie",
    # "graham cracker pie crust",
    # "graham cracker crust",
    "peanut butter pie",
    "into cookies",
    "peanut butter cookies",
    "peanut butter cookie",
    "thin cookie",
    "oatmeal cookies",
    "oatmeal cookie",
    "cookie dough",
    "coconut macaroons",
    "coconut macarons",
    "coconut macaroon",
    "coconut macaron"
    "either mini muffins",
    "cookie cake",
    "split peas",
    "split pea",
    "hour brownies",
    "hour pizza",
    "sheep hearts, lung, and liver",
    "the only organ meat",
    "honey beef",
    "sun dried tomatoes",
    "sun dried tomato",
    "pasta water",
    "if baking",
    "cheese sauce",
    "lemon zest",
    "lime zest",
    "orange zest",
    "fish sauce",
    "oyster sauce",
    "seal the sides",
    "some oil",
    "baking later",
    "baking now",
    "meat filling",
    "with the grain",
    "against the grain",
    "cookie scoop",
    "hummus ingredients",
    "sauce ingredients",
    "pesto ingredients",
    "touch of oil",
    "egg rolls",
    "egg roll",
    "when baking",
    "pasta parties",
    "pasta party",
    "clam juice",
    "top and sides",
    '"cookies"',
    "boxed cookies",
    "girl scout cookies",
    "girl scout cookie",
    "black mission",
    "each cracker",
    "vanilla, mint, or almond",
    "vanilla or almond",
    "spanish fig",
    "fig cake",
    "fig bread",
    "cinnamon sugar",
    "remove the seeds",
    "remove seeds",
    "ribs and seeds",
    "waffle fries",
    "waffle fry",
    "flour the",
    "cracker dough",
    "caesar salad",
    "granola mixture",
    "in the sides",
    "rice and meat mixtures",
    "grape leaves",
    "grape leaf",
    "the crackers",
    "the fries",
    "sweet potato fries",
    "sweet potato fry",
    "into crackers",
    "golden milk",
    "whole milk (3.25%",
    "and drink",
    "strain the milk",
    ") milk",
    "squeeze the milk",
    "nut milk bag",
    "chicken pad thai",
    "rice noodles",
    "rice noodle",
    "chicken francese",
    "chicken piccata",
    "chicken juice",
    # "grilled chicken",
    # "greek salad",
    "after baking",
    # "rotisserie chickens",
    # "rotisserie chicken",
    "butter chicken",
    "egg noodles",
    "egg noodle",
    "egg pasta",
    # "oatmeal raisin",
    "<b>oatmeal raisin</b>",
    "<b>peanut chocolate</b>",
    "<b>almond</b>",
    "<b>coconut</b>",
    "noodle soup",
    "as its flour",
    "noodle stew",
    "chicken noodle",
    # "salsa chicken",
    "baking them",
    "tomato paste mixture",
    # "tomato paste",
    # "crushed tomatoes",
    # "diced tomatoes",
    "trim the fat",
    "cut the fat",
    "excess fat",
    "italian chicken",
    "indian chicken",
    "korean chicken",
    "hunter's chicken",
    "chicken cacciatore",
    "celery seeds",
    "celery seed",
    "dressing ingredients",
    "oil and vinegar",
    "mode at 170F",
    "chicken florentine",
    "buffalo chicken",
    # "buffalo chicken dip",
    "barbeque chicken",
    "bbq chicken",
    "lemon chicken",
    "chili paste",
    "chili sauce",
    "'d",
    "oat mixture",
    "oat base",
    "oatmeal mixture",
    "oatmeal base",
    "raspberry oatmeal bars",
    "and toast until",
    "apple picking",
    "apple spice",
    "pumpkin spice",
    "pumpkin pie",
    "muffin batter",
    "not a dessert",
    "banana muffins",
    "banana muffin",
    "toast your",
    "toast until",
    "apple pie",
    "muffin holes",
    "muffin hole",
    "PB banana",
    "with some oil",
    # "with oil",
    "40 mini muffins",
    "small pancakes",
    "blueberry muffins",
    "blueberry muffin",
    "peanut butter bread",
    "great depression",
    "size muffins",
    "as mini muffins",
    "the muffins",
    "like a pancake",
    "of full fat",
    # "graham cracker crust",
    "bake the pretzels",
    "pretzel pan",
    "savory pretzel",
    "pretzels are low in",
    "baking dish",
    "freezing this bread",
    "serrated knife",
    "bread dough",
    "bake or toast",
    "traditional bread",
    "this bread is",
    "typical bread",
    "slices of bread",
    "slice of bread",
    "sandwich or toast",
    "rice-like",
    "rice like",
    "dusted flour",
    "sifted flour",
    # "pizza dough",
    "leftover bread",
    "so toast",
    "- flour",
    # "the bread",
    "before baking",
    # "savory cornbread",
    # "this cornbread",
    "done baking",
    "baking powder and soda",
    "baking soda and powder",
    "smaller bread",
    "make tortilla chips",
    "part-skim",
    "part skim",
    "while baking",
    "continue baking",
    # "irish soda",
    "remaining pretzels",
    "the pretzel",
    "each pretzel",
    "add as much soda",
    "place pretzels",
    "into pretzels",
    "move the soda",
    "washing soda",
    "healthier pretzels",
    "healthier pretzel",
    "hot pretzels",
    "hot pretzel",
    "any baking recipes",
    "beef tallow",
    "cookie scooop",
    "the dessert",
    # "peanut butter pretzel",
    "pretzel nuggets",
    "pretzel nugget",
    "each cookies",
    "each cookie",
    "your cookies",
    "your cookie",
    "your brownies",
    "your brownie",
    "cookie cutters",
    "cookie cutter",
    # "decorative cookies",
    # "decorating cookies",
    # "decorative cookie",
    # "decorating cookie",
    "sugar cookies",
    "sugar cookie",
    "and oil a",
    "cookies and cream",
    "cookies & cream",
    "scrape the sides",
    "scrape the side",
    "scraping the sides",
    "scraping the side",
    "bottom, sides",
    "brownie skin",
    "bigger brownies",
    "24 brownies",
    "brownie batter",
    "brownie texture",
    "sugar dissolve",
    "sugar crystals",
    "sugar crystal",
    "dissolves the sugar",
    "developing the gluten",
    "develop the gluten",
    "since brownies",
    "the brownies",
    "the cookies",
    "center of the brownies",
    "the brownies to stick",
    # "pan with oil",
    "standard dessert",
    "to the cookie dough",
    "scoop the cookies",
    "a fine dessert",
    "corn muffins",
    "corn muffin",
    "secretly a dessert",
    "another dessert that",
    "really a dessert",
    "meat replacement",
    "fake meat",
    "meat substitute",
    "types of sauces",
    "bran, and peanut",
    "rice bran",
    "canola, sunflower",
    "cottonseed, corn",
    "corn, soybean",
    "lean towards",
    "lean toward",
    "zero calorie natural sweeteners",
    "zero calorie natural sweetener",
    "vanilla bean",
    "sugar cane",
    "sugarcane",
    "sugar beets",
    "sugar beet",
    "banana waffles",
    "banana waffle",
    "banana muffins",
    "banana muffin",
    "banana pancakes",
    "banana pancake",
    "the same dessert in a",
    "breakfast, bread, or a",
    "not a breakfast",
    "is just a brownie",
    "is just a cookie",
    "still a dessert",
    "fine dessert",
    "of dessert",
    '"breakfast"',
    "breakfast foods",
    "breakfast food",
    '"bread"',
    "american breads",
    "american bread",
    "grocery store breads",
    "store-bought breads",
    "storebought breads",
    "store bought breads",
    "grocery store bread",
    "store-bought bread",
    "storebought bread",
    "store bought bread",
    "whole wheat breads",
    "loaves of bread",
    # "loaf of bread",
    "bread products",
    "bread product",
    # "protein cookies",
    # "protein cookie",
    "alongside",
    "along side",
    "cookies like",
    "dehydrated vegetables",
    "dehydrated vegetable",
    "cookies and candy",
    "cookies and candies",
    "wheat thins",
    "wheat thin",
    "packaged cookies",
    "packaged cookie",
    "baked desserts",
    "baked dessert",
    "fruit cups",
    "fruit cup",
    "fruit chunks",
    "fruit chunk",
    "fruit flavors",
    "fruit flavor",
    "ever drink",
    "skim off",
    "two sides",
    "2 sides",
    "sipping drink",
    "apple juice",
    "juice concentrate",
    "peanut spread",
    "breakfast is the most important meal of the day",
    "isn't the healthiest breakfast",
    "puffed rice",
    'part of a complete breakfast',
    "transport fats",
    "transport fat",
    "metabolize fats",
    "metabolize fat",
    "vitamin-like",
    "vitamin b4",
    "liver toxicity",
    "dark chocolate bar",
    "allulose dark chocolate",
    "sugar free dark chocolate",
    "melted dark chocolate",
    "chunks of dark chocolate",
    "gooey dark chocolate",
    "dark chocolate chips",
    "dark chocolate chip",
    "dark chocolate chunks",
    "dark chocolate chunk",
    "chopped dark chocolate",
    "dark chocolate candies",
    "dark chocolate candy",
    "cocoa butter",
    "exercise bands",
    "exercise band",
    "make you fat",
    "fat-like",
    "calcium phosphate",
    "kidney waste",
    "kidney tuble",
    "mineral deposits",
    "mineral deposit",
    "fat-free mass",
    "orange juice",
    "the protein needed",
    "combines with a protein",
    "black olives",
    "black olive",
    "black tea",
    "black or green tea",
    "black coffee",
    "black and white",
    "black-and-white",
    "kidney stones",
    "kidney stone",
    "kidney disease",
    "kidney failure",
    "liver disease",
    "liver or kidney damage",
    "liver or kidney",
    "kidney, liver",
    "liver, kidney",
    "kidney or liver",
    "liver damage",
    "liver failure",
    "nutrient transfer",
    "transfer nutrients",
    "transfer nutrient",
    "kidney problems",
    "kidney problem",
    "structures of proteins",
    "structures of protein",
    "formation of proteins",
    "formation of protein",
    "structure of proteins",
    "structure of protein",
    "protein structure",
    "protein formation",
    "get fat",
    "apple watch",
    "as fat",
    "synthesis of DNA and proteins",
    "synthesis of DNA and protein",
    "synthesis of proteins",
    "synthesis of protein",
    "your liver",
    "your kidneys",
    "your kidney",
    "the liver",
    "the kidneys",
    "the kidney",
    "orange foods",
    "orange food",
    "80% lean",
    "vegetarian protein powders",
    "vegetarian protein powder",
    "vegan protein powders",
    "vegan protein powder",
    "fat metabolism",
    "fruit concentrate",
    "confectioner's sugar",
    "confectioners sugar",
    # "extra virgin coconut oil",
    "sugar from an",
    "sugar from a",
    "fatty liver",
    "chocolate covered fruit and nuts",
    "chocolate covered fruit",
    "chocolate covered raisins",
    "chocolate covered raisin",
    "chocolate covered nuts",
    "chocolate covered nut",
    "chocolate covered almonds",
    "chocolate covered almond",
    "packaged baked goods",
    "mushroom rice",
    "sugar pumpkin",
    "resistant starch",
    "mustard seeds",
    "mustard seed",
    "fat soluble",
    "water soluble",
    "roll the",
    "eggplant parmesean",
    "eggplant parmesan",
    "eggplant parm",
    "chicken parmesean",
    "chicken parmesan",
    "pulled chicken",
    "chicken wings",
    "chicken wing",
    "coconut shrimp",
    "general tso's chicken",
    "kung pao chicken",
    "chicken alfredo",
    "pulled pork",
    "chicken parm",
    "tuna salad",
    "tuna fish",
    "tomato sauce",
    "protein synthesis",
    "crab meat",
    "coconut meat",
    "cake flour",
    "bread flour",
    "D-Chiro-Inositol",
    "whatever starch",
    "these seeds",
    "redish/purplish juice",
    # "unsweetened dried fruits",
    # "unsweetened dried fruit",
    "jelly beans",
    "jelly bean",
    "baking powder",
    "baking soda",
    "butter-able",
    "non-butter-able",
    "caprese salad",
    "side note",
    "milk drink",
    "milk sugar",
    "olive or coconut",
    "butter beans",
    "butter bean",
    "poor man protein",
    "'breakfast'",
    "'breakfast",
    "beakfast'",
    "breakfast burger",
    "breakfast pizza",
    "minimally processed meats",
    "opposite side",
    "sense of scale",
    "red bean paste",
    "barley malt",
    "corn sweetener",
    "cane juice",
    "liquid glucose",
    "glucose solids",
    "grape sugar",
    "coconut nectar",
    "coconut aminos",
    "maraschino cherries",
    "maraschino cherry",
    # "chia pudding",
    "curry sauces",
    "curry sauce",
    "coconut water",
    "coconut yogurt",
    # "english muffins",
    # "english muffin",
    # "smoothie bowls",
    # "smoothie bowl",
    # "protein shakes",
    # "protein shake",
    # "protein bars",
    # "protein bar",
    "flavored rice dishes",
    "traditional desserts",
    "traditional dessert",
    "classic desserts",
    "classic dessert",
    "most desserts",
    "most dessert",
    "these are desserts",
    "drink a glass",
    "drink it",
    "fermented juice",
    "rice vinegars",
    "rice vinegar",
    # "nut free",
    # "nut-free",
    # "dairy free",
    "dairy-free",
    "quail eggs",
    "quail egg",
    "kidney function",
    "kidney health",
    "juniper berries",
    "juniper berry",
    "inca berries",
    "inca berry",
    "iced tea (unsweetened)",
    "unsweetened ice tea",
    "dragon fruit",
    "dessert toppings",
    "dessert topping",
    "mac & cheese",
    "mac and cheese",
    "rice crispies",
    "frozen breakfasts",
    "frozen breakfast",
    "egg sandwiches",
    "cinnamon rolls",
    "cinnamon roll",
    # '"protein"',
    '"whole-grain"',
    # "rice cakes",
    # "rice cake",
    "bakery desserts",
    "bakery dessert",
    "home fries",
    "twice baked potatoes",
    "scalloped potatoes",
    "potato skins",
    "potato salad",
    "potato rolls",
    "mashed potatoes",
    "mashed potato",
    "kidney damage",
    "kidneys",
    "musical fruit",
    "pumpkin pie",
    "bean water",
    "bean skins",
    "bean skin",
    "lemon essential oils",
    "lemon essential oil",
    "pancakes; see my",
    "waffle; that thing",
    "two ingredient waffles",
    "two ingredient waffle",
    "of waffles",
    "six waffles",
    "keto waffles",
    "waffles have nearly",
    "waffles, these are",
    "waffles before",
    "the waffles",
    "have waffles with",
    "waffles.  they are the",
    "waffles are a great source",
    "waffles or pancakes to boost",
    "waffles won't cook",
    "each waffle",
    "these waffles",
    "all waffles on an",
    "each waffle",
    "extra waffles",
    "worst waffles",
    "this waffle tasted",
    "not a waffle",
    "solid waffle",
    "waffles, but with a",
    "good waffle",
    "waffle shape",
    "waffles, but still",
    "pancakes: you can also make pancakes",
    "waffle sundae",
    "chicken and waffles",
    "waffles are the highest",
    "waffles are also a",
    "flavor of waffles/pancakes",
    "waffle, which was",
    "pancakes and waffles for years",
    "pancake or waffle, and I",
    "waffle was cheesy",
    "this waffle going",
    "waffles are definitely the way to go",
    "work as waffles",
    "pancakes for a brunch",
    "savory waffles",
    "sweet waffles",
    "savory waffle",
    "sweet waffle",
    "waffles falling",
    "top side",
    "bottom side",
    "top (raw) side",
    "per side",
    "heavily oil",
    "oil between making",
    "oil for about",
    "out of the iron",
    "chocolate chips",
    "chocolate chip",
    "later date",
    "waffle iron",
    "waffle maker",
    "cheese waffles",
    "cheese waffle",
    "cheese cloth",
    "with a knife",
    "pulp and juice",
    "fruit syrup",
    "with a syrup",
    "skins and seeds",
    "the juice",
    "squeezed juice",
    "grape juice",
    "grape pulp",
    "grape skins",
    "grape skin",
    "cheese to make",
    "brownie batter",
    "milk flavor",
    "milk hit",
    "cheese done",
    "milk solids",
    "milk solid",
    '"cheese"',
    "making cheese",
    "cheese somehow",
    "curds (cheese)",
    "cheese making",
    "made cheese",
    "whey syrup",
    "cheese curds",
    "cheese curd",
    "liquid (whey)",
    # "liquid whey",
    "acid whey",
    "inside",
    "aside",
    "still side",
    "fiber one brownie",
    "brownie mix",
    "boxed brownies",
    "frankenstein cookie dough",
    "so cookie dough",
    "much flour",
    "flour name",
    '"flour"',
    "I'd",
    "additional flour",
    "handle and roll",
    "roll into",
    "brownie colored",
    "brownie color",
    "sole flour",
    "final flour",
    "flour that",
    "e. coli",
    "less flour",
    "flour of",
    "is flour",
    "than bread dough",
    "than cookie dough",
    "represent bread dough",
    "represent cookie dough",
    "dryer flour",
    "drier flour",
    "cookie dough like",
    "cookie dough consistency",
    "feel like cookie dough",
    "cookie dough texture",
    "each flour",
    "e.",
    "i.e.",
    "you'd",
    "chicken or the egg",
    "toxic soup",
    "a drink",
    "to drink",
    "fat mailman",
    "coffee brews",
    "burn fat",
    "don't drink",
    "essential oils",
    "essential oil",
    # "minimally processed",
    # "less processed",
    "corn dogs",
    "corn dog",
    "corndogs",
    "corndog",
    "fried chicken",
    "mozzarella sticks",
    "mozzarella stick",
    "potassium sorbate",
    # "potassium chloride",
    # "sodium chloride",
    # "magnesium malate",
    # "magnesium glycinate",
    # "magnesium citrate",
    "sodium benzoate",
    "mixed drinks",
    "olive or canola",
    "plastic knife",
    "banana peppers",
    "banana pepper",
    # "banana bread",
    "garlic powder",
    "onion powder",
    "garlic and onion powders",
    "garlic and onion powder",
    "garlic and onion",
    "garlic, onion",
    "onion and garlic powders",
    "onion and garlic powder",
    "onion and garlic",
    "onion, garlic",
    # "monk fruit",
    # "nutritional yeast",
    "minutes",
    "minute",
    # "non fat",
    # "nonfat",
    # "full fat",
    # "fat free",
    "nutrition",
    "nutritious",
    "flours",
    "evaporated milk",
    "condensed milk",
    "carrot cake",
    "breaded",
    "fryer",
    # "olive oil",
    "flaxseed oil",
    # "peanut oil",
    "avocado oil",
    "almond oil",
    "sesame oil",
    # "extra virgin olive oil",
    "soy sauce, low sodium, gluten free",
    "low sodium",
    "lemon pepper",
    "lime pepper",
    "mango pepper",
    "cut side",
    "flip side",
    "sleep on",
    "first side",
    "other side",
    "side down",
    "side up",
    "seam side",
    "almond extract",
    "butter extract",
    "coconut extract",
    "side effects",
    "side effect",
    "corn starch",
    "cornstarch",
    # "cast iron",
    # "cast-iron",
    "non dairy",
    "non-dairy",
    "all sides",
    "all 4 sides",
    "4 sides",
    "both sides",
    "soy sauce",
    "the flour",
    "a flour",
    "finer flour",
    "fine flour",
    "coarser flour",
    "coarse flour",
    "homemade flour",
    "own flour",
    "together flour",
    "lightly flour",
    "flour the bowl",
    "flour your bowl",
    "with flour",
    "of flour",
    "more flour",
    "flour and water",
    "flour +",
    "60 g flour",
    "each side",
    "down the sides",
    "down the side",
    "pan on the side",
    "off the sides",
    "the side of the",
    "to the side",
    "on the side of",
    "and the sides",
    "on the sides",
    "tapped on the side",
    "when the side",
    "of the sides",
    "of the side",
    "around the sides",
    "the side",
    "one side",
    "scoop out the seeds",
    "the seeds",
    "the seed",
    "black pepper",
    "cayenne pepper",
    "chicken bouillon",
    # "chicken broth",
    "veggie broth",
    "vegetable broth",
    "chicken or veggie broth",
    "veggie or chicken broth",
    "beef broth",
    "chicken bone",
    "chicken skin",
    "skin chips",
    "red pepper flakes",
    # "red pepper",
    "chili powder",
    "scale up",
    "scale down",
    "scale this",
    "to scale",
    "easily scale",
    "grains of",
    "butter knife",
    "butter knives",
    '8" long',
    '1/8" thick',
    '1/8"',
    '1/8" - 1/4"',
    # "gluten free flour",
    "type of flour",
    "bean sprouts",
    '2% milk',
    '2 % milk',
    '1% milk',
    '1 % milk',
    "rice milk",
    "pea milk",
    "soy milk",
    "fat greek yogurt",
    "fat cottage cheese",
    "a grain",
    "grain of",
    "grain of rice",
    "grain of salt",
    "white meat",
    "dark meat",
    "salt and pepper",
    "pepper and salt",
    "salt, and pepper",
    "salt, pepper",
    "pepper, salt",
    "pepper, and salt",
    # "date syrup",
    # "date sugar",
    # "coconut sugar",
    # "agave syrup",
    "glucose syrup",
    "invert sugar",
    "rice syrup",
    "beet sugar",
    "syrupy",
    "maple<br>syrup",
    "brown rice syrup",
    "cane sugar",
    "cane syrup",
    "powdered sugar",
    "honey nut",
    "raisin bran",
    # "corn syrup",
    "until the syrup",
    "sugar syrup",
    "homemade syrup",
    "into a syrup",
    "homemade syrup to use",
    "making the syrup",
    "using the syrup",
    "put syrup on",
    "lite syrup",
    "malt syrup",
    "golden syrup",
    "carob syrup",
    "sorghum syrup",
    "sorgum syrup",
    "sweet syrup remains",
    "colored syrup",
    "milk syrup",
    "tasted the syrup",
    "caramel syrup",
    "microwaved the syrup",
    "fruit juice concentrate",
    "desserts for breakfast",
    "dessert for breakfast",
    "kneading bread",
    "knead bread",
    "bready",
    "bread-y",
    "bread-like",
    "bread like"
    "garlic-y",
    "garlicy",
    "wheat starch",
    "chicken nuggets",
    "chicken nugget",
    "chicken fingers",
    "chicken finger",
    "fish sticks",
    "fish stick",
    "immitation crab",
    "onion rings",
    "onion ring",
    "veggie burgers",
    "veggie burger",
    "fat loss",
    "soup bases",
    "soup base",
    "not fat",
    "being fat",
    "skinny-fat",
    "fat inside",
    "breast cancer",
    "breast and colon cancer"
    "kidney disease",
    "kidneys",
    "c-reactive protein",
    "kidney stone",
    "or orange",
    "meat mix",
    "meat's",
    "dry side",
    "wet side",
    "side-by-side",
    "phenylethylamine (PEA)"

]
EXCLUDED_PHRASES = list(dict.fromkeys(EXCLUDED_PHRASES))

REMOVE_CATEGORIES = [
    "/misc/homemade-yogurt",
    "/misc/bone-broth",
    "/misc/costs",
    "/misc/olive-oil",
    "/misc/natural-sweeteners",
    "/misc/chocolate-benefits",
    "/misc/whole-wheat-sourdough",
    "/misc/beans",
    "/misc/dairy",
    "/misc/fish",
    "/misc/fruit",
    "/misc/grains",
    "/misc/meat",
    "/misc/nuts",
    "/misc/seeds",
    "/misc/veggies",
    "/misc/celiac",
    "/misc/metabolic-syndrome",
    "/misc/diabetes",
    "/misc/alzheimers",
    "/misc/sleep",
    "/misc/exercise",
    "/misc/pcos",
    "/misc/insulin-resistance",
    "/misc/chronic-inflammation",
    "/misc/phytochemicals",
    "/misc/depression",
    "/misc/nutrient-alphabet",
    "/misc/calcium",
    "/misc/choline",
    "/misc/cholesterol",
    "/misc/fiber",
    "/misc/iron",
    "/misc/magnesium",
    "/misc/phosphorus",
    "/misc/potassium",
    "/misc/sodium",
    "/misc/vitamin-b12",
    "/misc/vitamin-c",
    "/misc/hidden-sugar",
    "/misc/carbs",
    "/misc/fats",
    "/misc/protein",
    "/misc/high-protein",
    "/misc/calories",
    "/misc/creatine",
    "/recipes/natural-peanut-butter",
    "/hummus",
    "/oatmeal",
    "/yogurt",
    "/nut-butter",
    "/pesto",
    "/soups-and-stews",
    "/chili",
    "/salad",
    "/dressing",
    "/salad-dressings",
    "/brownies",
    "/cookies",
    "/copycat",
    "/recipes/bread",
    "/recipes/breakfast",
    "/recipes/chicken",
    "/recipes/drinks",
    "/recipes/finger-food",
    "/recipes/fish",
    "/recipes/ground-meat",
    "/recipes/healthier-dessert",
    "/recipes/meatless",
    "/recipes/meme",
    "/recipes/protein-powder",
    "/recipes/savory-sauces",
    "/recipes/sides",
    "/recipes/sweet-spreads",
    "/misc/fake-healthy-foods",
    "/misc/processed-foods",
    "/misc/overshadowed-healthy-foods",

]

EXCLUDED_REGEXES = [
    re.compile(rf"\b{re.escape(p)}\b", re.IGNORECASE)
    for p in EXCLUDED_PHRASES
]

# Convert new LINKS format (url -> [aliases]) into old format (alias -> url)
def build_alias_lookup(links_by_url):
    alias_to_url = {}
    for url, aliases in links_by_url.items():
        for alias in aliases:
            alias_lower = alias.lower()
            # optional: warn if duplicate alias
            if alias_lower in alias_to_url and alias_to_url[alias_lower] != url:
                print(f"Warning: alias '{alias}' maps to multiple URLs: '{alias_to_url[alias_lower]}' vs '{url}'")
            alias_to_url[alias_lower] = url
    return alias_to_url

ALIAS_LOOKUP = build_alias_lookup(LINKS)


# -------------------------------------------------------------
# Core skip logic (unchanged)
# -------------------------------------------------------------
def should_skip_linking(text, key_start, key_end):
    for rx in EXCLUDED_REGEXES:
        for m in rx.finditer(text):
            phrase_start, phrase_end = m.span()
            if key_start >= phrase_start and key_end <= phrase_end:
                return True
    return False

def remove_existing_links(html, categories):
    escaped = [re.escape(cat) for cat in categories]

    # Match:
    # - exact category (/misc/nuts)
    # - OR category + fragment (/misc/nuts#almonds)
    # - BUT NOT extra path chars like /misc/meatloaf-experiment
    pattern = re.compile(
        rf"<a\s+href=['\"](?:{'|'.join(escaped)})(?:#[^'\"/]*)?['\"]>(.*?)</a>",
        re.IGNORECASE
    )

    return pattern.sub(r"\1", html)

# -------------------------------------------------------------
# Generic block protector
# -------------------------------------------------------------
def protect_blocks(text, patterns):
    blocks = []
    def repl(m):
        key = f"__BLOCK_{len(blocks)}__"
        blocks.append(m.group(0))
        return key

    combined = re.compile("|".join(patterns), re.DOTALL | re.IGNORECASE)
    return combined.sub(repl, text), blocks


def restore_blocks(text, blocks):
    for i, block in enumerate(blocks):
        text = text.replace(f"__BLOCK_{i}__", block)
    return text

# -------------------------------------------------------------
# Liquid protection (shared everywhere)
# -------------------------------------------------------------
LIQUID_PROTECT = [
    r"{%\s*assign\b.*?%}",            # assign blocks (multi-line safe)
    r"{%\s*capture\b.*?{%\s*endcapture\s*%}",  # capture blocks
    r"{%.*?%}",                       # other Liquid tags
]

# -------------------------------------------------------------
# Auto-linker (PURE TEXT, NO PARSING)
# -------------------------------------------------------------
def auto_link_html_safe_single_quotes(html, links, exclude_phrases=None, skip_links_to=None):

    exclude_phrases = [p.lower() for p in (exclude_phrases or [])]

    # ---------------------------------------------------------
    # Protect regions that must NEVER be touched
    # ---------------------------------------------------------
    PROTECTED_PATTERNS = [
        r"{%\s*assign\b.*?%}",   # Protect full assign blocks
        r"{%.*?%}",              # Other Liquid tags
        r"<a\b[^>]*>.*?</a>",             # Existing links
        r"<script\b[^>]*>.*?</script>",
        r"<style\b[^>]*>.*?</style>",
        # r"<ul\b[^>]*>.*?</ul>",
        # r"<ol\b[^>]*>.*?</ol>",
        r"<ul\b[^>]*>",
        r"</ul>",
        r"<ol\b[^>]*>",
        r"</ol>",
        r"<div\b[^>]*>.*?</div>",
        r"<img\b[^>]*>",
        r"&emsp;",
        r"<font\b[^>]*>.*?</font>",
    ]

    html, protected_blocks = protect_blocks(html, PROTECTED_PATTERNS)

    # ---------------------------------------------------------
    # Prepare longest-first regex (no \b boundaries)
    # ---------------------------------------------------------
    # Use the alias lookup instead of the old links dict
    links_lower = ALIAS_LOOKUP
    keys = sorted(links_lower.keys(), key=len, reverse=True)
    pattern = re.compile(
        r"(?<!\w)(" + "|".join(map(re.escape, keys)) + r")(?!\w)",
        re.IGNORECASE
    )

    # ---------------------------------------------------------
    # Replace matches safely
    # ---------------------------------------------------------
    def replacer(m):
        word = m.group(0)
        start, end = m.span()
        lower = word.lower()
        url = links_lower.get(lower)

        if not url:
            return word

        # Skip if the match is inside an excluded phrase
        for phrase in exclude_phrases:
            idx = html.lower().find(phrase)
            if idx != -1 and start >= idx and end <= idx + len(phrase):
                return word

        # Skip if should_skip_linking logic applies
        if should_skip_linking(html, start, end):
            return word

        # **Skip linking if URL matches current page permalink**
        # if skip_links_to and url == skip_links_to:
        if skip_links_to and url.startswith(skip_links_to):
            return word

        return f"<a href='{url}'>{word}</a>"

    html = pattern.sub(replacer, html)

    # ---------------------------------------------------------
    # Restore protected regions EXACTLY
    # ---------------------------------------------------------
    html = restore_blocks(html, protected_blocks)

    return html


# -------------------------------------------------------------
# Front matter processor (minimal change)
# -------------------------------------------------------------
def process_front_matter(text, links, exclude_phrases=None):
    lines = text.splitlines(keepends=True)
    output = []
    in_front_matter = False
    delims = 0
    body = []

    current_section = None  # Description / Instructions / Notes
    current_permalink = None
    in_compare_block = False  # For COMPARE()/INGREDIENTS()/FACTS() macros

    for line in lines:
        if line.startswith("permalink:"):
            current_permalink = line.split(":", 1)[1].strip()
            break

    for line in lines:
        if line.strip() == "---" and delims < 2:
            delims += 1
            in_front_matter = delims == 1
            output.append(line)
            continue

        if in_front_matter:
            # Section headers
            if line.startswith(("Description:", "Instructions:", "Notes:")):
                key, value = line.split(":", 1)
                current_section = key

                value, blocks = protect_blocks(value, LIQUID_PROTECT)
                value = remove_existing_links(value, REMOVE_CATEGORIES)
                value = restore_blocks(value, blocks)

                value = auto_link_html_safe_single_quotes(
                    value,
                    links,
                    exclude_phrases,
                    skip_links_to=current_permalink
                )

                output.append(f"{key}:{value}")
                continue

            # Inside Description / Instructions / Notes, but skip COMPARE/INGREDIENTS/FACTS macros
            if current_section in ("Description", "Instructions", "Notes"):
                stripped = line.lstrip()

                # If we're already inside a COMPARE/INGREDIENTS/FACTS block, just copy through
                if in_compare_block:
                    output.append(line)
                    if ")" in stripped:
                        in_compare_block = False
                    continue

                # Detect start of COMPARE/INGREDIENTS/FACTS blocks
                if stripped.startswith(("COMPARE(", "INGREDIENTS(", "FACTS(")):
                    in_compare_block = True
                    output.append(line)
                    # Handle single-line macro case
                    if ")" in stripped:
                        in_compare_block = False
                    continue

                # Normal content in these sections gets auto-linked
                processed, blocks = protect_blocks(line, LIQUID_PROTECT)
                processed = remove_existing_links(processed, REMOVE_CATEGORIES)
                processed = restore_blocks(processed, blocks)

                processed = auto_link_html_safe_single_quotes(
                    processed,
                    links,
                    exclude_phrases,
                    skip_links_to=current_permalink
                )

                output.append(processed)
                continue

            # Any other front-matter line
            output.append(line)
        else:
            body.append(line)

    # Process body normally
    if body:
        html_body = "".join(body)
        html_body, blocks = protect_blocks(html_body, LIQUID_PROTECT)
        html_body = remove_existing_links(html_body, REMOVE_CATEGORIES)
        html_body = restore_blocks(html_body, blocks)

        output.append(auto_link_html_safe_single_quotes(
            html_body,
            links,
            exclude_phrases,
            skip_links_to=current_permalink
        ))

    return "".join(output)

# -------------------------------------------------------------
# Main processing loop (NO BeautifulSoup)
# -------------------------------------------------------------
def main():
    start_time = time.perf_counter()
    os.system("cls")
    print("-------------------")

    count = 0

    for root, _, files in os.walk(POSTS_DIR):
        for file in files:
            if not file.endswith((".md", ".html", ".markdown")):
                continue

            # optional filename filter (keep or remove)
            if not file.startswith(("2026-09-03")):
                continue

            # exclude some files
            # if file.startswith("2025-11-03-cheese"):
            #     continue

            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                original = f.read()

            updated = process_front_matter(
                original,
                ALIAS_LOOKUP,
                EXCLUDED_PHRASES
            )

            if updated != original:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(updated)

                print(f"Updated: {path}")
                count += 1

    print(f"Total files updated: {count}")

    elapsed = time.perf_counter() - start_time
    print(f"Elapsed time: {elapsed:.3f} seconds")

if __name__ == "__main__":
    main()
