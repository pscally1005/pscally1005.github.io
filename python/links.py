import os
import re
from html import escape, unescape
from bs4 import BeautifulSoup, NavigableString

POSTS_DIR = r"C:\Users\mets1\Documents\website\_posts\delete"

LINKS = {

  # RECIPES
  "banana ice cream": "/recipes/nice-cream",
  "salsa": "/recipes/salsa",
  "sugar free syrup": "/recipes/sugar-free-syrup",
  "sugar-free syrup": "/recipes/sugar-free-syrup",
  "natural peanut butter": "/recipes/natural-peanut-butter",
  "natural nut butter": "/recipes/natural-peanut-butter",

  # BEANS
  "black beans": "/misc/beans#black-beans",
  "black bean": "/misc/beans#black-beans",
  "black eyed peas": "/misc/beans#black-eyed-peas",
  "black eyed pea": "/misc/beans#black-eyed-peas",
  "brown lentils": "/misc/beans#brown-lentils",
  "brown lentil": "/misc/beans#brown-lentils",
  "cannellini beans": "/misc/beans#cannellini-beans",
  "cannellini bean": "/misc/beans#cannellini-beans",
  "cannellini": "/misc/beans#cannellini-beans",
  "chickpeas": "/misc/beans#chickpeas",
  "chickpea": "/misc/beans#chickpeas",
  "edamame": "/misc/beans#edamame",
  "fava beans": "/misc/beans#fava-beans",
  "fava bean": "/misc/beans#fava-beans",
  "fava": "/misc/beans#fava-beans",
  "great northern beans": "/misc/beans#great-northern-beans",
  "great northern bean": "/misc/beans#great-northern-beans",
  "great northern": "/misc/beans#great-northern-beans",
  "green lentils": "/misc/beans#green-lentils",
  "green lentil": "/misc/beans#green-lentils",
  "kidney beans": "/misc/beans#kidney-beans",
  "kidney bean": "/misc/beans#kidney-beans",
  "kidney": "/misc/beans#kidney-beans",
  "lima beans": "/misc/beans#lima-beans",
  "lima bean": "/misc/beans#lima-beans",
  "lima": "/misc/beans#lima-beans",
  "lupini beans": "/misc/beans#lupini-beans",
  "lupini bean": "/misc/beans#lupini-beans",
  "lupini": "/misc/beans#lupini-beans",
  "navy beans": "/misc/beans#navy-beans",
  "navy bean": "/misc/beans#navy-beans",
  "navy": "/misc/beans#navy-beans",
  "pink beans": "/misc/beans#pink-beans",
  "pink bean": "/misc/beans#pink-beans",
  "pinto beans": "/misc/beans#pinto-beans",
  "pinto bean": "/misc/beans#pinto-beans",
  "pinto": "/misc/beans#pinto-beans",
  "red lentils": "/misc/beans#red-lentils",
  "red lentil": "/misc/beans#red-lentils",
  "soy beans": "/misc/beans#soybeans",
  "soy bean": "/misc/beans#soybeans",
  "soybeans": "/misc/beans#soybeans",
  "soybean": "/misc/beans#soybeans",
  "soy": "/misc/beans#soybeans",
  "tofu": "/misc/beans#tofu",

  # DAIRY
  "unsweetened vanilla almond milk": "/misc/dairy#almond-milk",
  "unsweetened almond milk": "/misc/dairy#almond-milk",
  "almond milk": "/misc/dairy#almond-milk",
  "blue cheese": "/misc/dairy#blue-cheese",
  "butter": "/misc/dairy#butter",
  "casein protein powder": "/misc/dairy#casein",
  "casein proteins": "/misc/dairy#casein",
  "casein protein": "/misc/dairy#casein",
  "casein": "/misc/dairy#casein",
  "shredded cheese": "/misc/dairy#cheddar",
  "mexican cheese": "/misc/dairy#cheddar",
  "cheddar cheese": "/misc/dairy#cheddar",
  "cheddar": "/misc/dairy#cheddar",
  "coconut milk": "/misc/dairy#coconut-milk",
  "fat free cottage cheeses": "/misc/dairy#cottage-cheese",
  "nonfat cottage cheese": "/misc/dairy#cottage-cheese",
  "cottage cheese": "/misc/dairy#cottage-cheese",
  "whole milk cottage cheese": "/misc/dairy#cottage-cheese-whole-milk",
  "full fat cottage cheese": "/misc/dairy#cottage-cheese-whole-milk",
  "cream cheese": "/misc/dairy#cream-cheese",
  "feta cheese": "/misc/dairy#feta",
  "feta": "/misc/dairy#feta",
  "goat cheese": "/misc/dairy#goat-cheese",
  "plain nonfat greek yogurt": "/misc/dairy#yogurt",
  "nonfat greek yogurt": "/misc/dairy#yogurt",
  "greek yogurt": "/misc/dairy#yogurt",
  "yogurt": "/misc/dairy#yogurt",
  "plain whole milk greek yogurt": "/misc/dairy#yogurt-whole-milk",
  "plain full fat greek yogurt": "/misc/dairy#yogurt-whole-milk",
  "full fat greek yogurt": "/misc/dairy#yogurt-whole-milk",
  "kefir": "/misc/dairy#kefir",
  "skim milk": "/misc/dairy#skim-milk",
  "milk": "/misc/dairy#skim-milk",
  "whole milk": "/misc/dairy#whole-milk",
  "shredded mozzarella cheese": "/misc/dairy#mozzarella",
  "mozzarella cheese": "/misc/dairy#mozzarella",
  "mozzarella": "/misc/dairy#mozzarella",
  "parmesan cheese": "/misc/dairy#grated-cheese",
  "grated cheese": "/misc/dairy#grated-cheese",
  "parmesan": "/misc/dairy#grated-cheese",
  "swiss cheese": "/misc/dairy#swiss-cheese",
  "swiss": "/misc/dairy#swiss-cheese",
  "whey protein powder": "/misc/dairy#whey",
  "whey protein": "/misc/dairy#whey",
  "whey": "/misc/dairy#whey",

  # FISH
  "canned anchovies": "/misc/fish#anchovy",
  "anchovies": "/misc/fish#anchovy",
  "anchovy": "/misc/fish#anchovy",
  "clams": "/misc/fish#clam",
  "clam": "/misc/fish#clam",
  "cod": "/misc/fish#cod",
  "crabs": "/misc/fish#crab",
  "canned crab": "/misc/fish#crab",
  "crab": "/misc/fish#crab",
  "cuttlefish": "/misc/fish#cuttlefish",
  "haddock": "/misc/fish#haddock",
  "halibut": "/misc/fish#halibut",
  "herring": "/misc/fish#herring",
  "lobsters": "/misc/fish#lobster",
  "lobster": "/misc/fish#lobster",
  "mackerel": "/misc/fish#mackerel",
  "mahi mahi": "/misc/fish#mahi-mahi",
  "mussels": "/misc/fish#mussel",
  "mussel": "/misc/fish#mussel",
  "octopus": "/misc/fish#octopus",
  "octopi": "/misc/fish#octopus",
  "oysters": "/misc/fish#oyster",
  "oyster": "/misc/fish#oyster",
  "canned salmon": "/misc/fish#salmon",
  "salmon": "/misc/fish#salmon",
  "canned sardines": "/misc/fish#sardine",
  "sardines": "/misc/fish#sardine",
  "sardine": "/misc/fish#sardine",
  "scallops": "/misc/fish#scallop",
  "scallop": "/misc/fish#scallop",
  "shrimp": "/misc/fish#shrimp",
  "squid": "/misc/fish#squid",
  "tilapia": "/misc/fish#tilapia",
  "trout": "/misc/fish#trout",
  "canned tuna": "/misc/fish#tuna",
  "tuna": "/misc/fish#tuna",

  # FRUIT
  "unsweetened applesauce": "/misc/fruit#apple",
  "applesauce": "/misc/fruit#apple",
  "apples": "/misc/fruit#apple",
  "apple": "/misc/fruit#apple",
  "apricots": "/misc/fruit#apricot",
  "apricot": "/misc/fruit#apricot",
  "avocados": "/misc/fruit#avocado",
  "avocado": "/misc/fruit#avocado",
  "bananas": "/misc/fruit#banana",
  "banana": "/misc/fruit#banana",
  "blackberries": "/misc/fruit#blackberry",
  "blackberry": "/misc/fruit#blackberry",
  "blueberries": "/misc/fruit#blueberries",
  "blueberry": "/misc/fruit#blueberries",
  "boysenberries": "/misc/fruit#boysenberry",
  "boysenberry": "/misc/fruit#boysenberry",
  "cantaloupes": "/misc/fruit#cantaloupe",
  "cantaloupe": "/misc/fruit#cantaloupe",
  "cherries": "/misc/fruit#cherry",
  "cherry": "/misc/fruit#cherry",
  "clementines": "/misc/fruit#clementine",
  "clementine": "/misc/fruit#clementine",
  "cranberries": "/misc/fruit#cranberry",
  "cranberry": "/misc/fruit#cranberry",
  "dates": "/misc/fruit#dates",
  "date": "/misc/fruit#dates",
  "dried figs": "/misc/fruit#fig-dried",
  "dried fig": "/misc/fruit#fig-dried",
  "figs": "/misc/fruit#fig-dried",
  "fig": "/misc/fruit#fig-dried",
  "fresh figs": "/misc/fruit#fig-fresh",
  "fresh fig": "/misc/fruit#fig-fresh",
  "grapes": "/misc/fruit#grapes",
  "grape": "/misc/fruit#grapes",
  "grapefruits": "/misc/fruit#grapefruit",
  "grapefruit": "/misc/fruit#grapefruit",
  "guavas": "/misc/fruit#guava",
  "guava": "/misc/fruit#guava",
  "honeydews": "/misc/fruit#honeydew",
  "honeydew": "/misc/fruit#honeydew",
  "kiwis": "/misc/fruit#kiwi",
  "kiwi": "/misc/fruit#kiwi",
  "lemon juices": "/misc/fruit#lemon-juice",
  "lemon juice": "/misc/fruit#lemon-juice",
  "lemons": "/misc/fruit#lemon",
  "lemon": "/misc/fruit#lemon",
  "lime juices": "/misc/fruit#lime-juice",
  "lime juice": "/misc/fruit#lime-juice",
  "limes": "/misc/fruit#lime",
  "lime": "/misc/fruit#lime",
  "mandarins": "/misc/fruit#mandarin",
  "mandarin": "/misc/fruit#mandarin",
  "mangos": "/misc/fruit#mangos",
  "mango": "/misc/fruit#mangos",
  "olives": "/misc/fruit#olives",
  "olive": "/misc/fruit#olives",
  "oranges": "/misc/fruit#orange",
  "orange": "/misc/fruit#orange",
  "papayas": "/misc/fruit#papaya",
  "papaya": "/misc/fruit#papaya",
  "passion fruits": "/misc/fruit#passion-fruit",
  "passion fruit": "/misc/fruit#passion-fruit",
  "peaches": "/misc/fruit#peach",
  "peach": "/misc/fruit#peach",
  "pears": "/misc/fruit#pear",
  "pear": "/misc/fruit#pear",
  "persimmons": "/misc/fruit#persimmon",
  "persimmon": "/misc/fruit#persimmon",
  "pineapples": "/misc/fruit#pineapple",
  "pineapple": "/misc/fruit#pineapple",
  "plums": "/misc/fruit#plum",
  "plum": "/misc/fruit#plum",
  "pomegranates": "/misc/fruit#pomegranate",
  "pomegranate": "/misc/fruit#pomegranate",
  "prunes": "/misc/fruit#prune",
  "prune": "/misc/fruit#prune",
  "raisins": "/misc/fruit#raisins",
  "raisin": "/misc/fruit#raisins",
  "raspberries": "/misc/fruit#raspberry",
  "raspberry": "/misc/fruit#raspberry",
  "starfruits": "/misc/fruit#starfruit",
  "starfruit": "/misc/fruit#starfruit",
  "strawberries": "/misc/fruit#strawberries",
  "strawberry": "/misc/fruit#strawberries",
  "watermelons": "/misc/fruit#watermelon",
  "watermelon": "/misc/fruit#watermelon",

  # GRAINS
  "amaranth": "/misc/grains#amaranth",
  "barley": "/misc/grains#barley",
  "brown rice": "/misc/grains#brown-rice",
  "buckwheat": "/misc/grains#buckwheat",
  "corn": "/misc/grains#corn",
  "couscous": "/misc/grains#couscous",
  "farro": "/misc/grains#farro",
  "millet": "/misc/grains#millet",
  "oat flour": "/misc/grains#oats",
  "oats": "/misc/grains#oats",
  "oat": "/misc/grains#oats",
  "rolled oats": "/misc/grains#oats",
  "quick oats": "/misc/grains#oats",
  "popcorn": "/misc/grains#popcorn",
  "quinoa": "/misc/grains#quinoa",
  "rye": "/misc/grains#rye",
  "spelt": "/misc/grains#spelt",
  "vital wheat gluten": "/misc/grains#vital-wheat-gluten",
  "white flour": "/misc/grains#white-wheat",
  "all purpose flour": "/misc/grains#white-wheat",
  "flour": "/misc/grains#white-wheat",
  "white pasta": "/misc/grains#pasta-white",
  "white rice": "/misc/grains#white-rice",
  "whole wheat flour": "/misc/grains#whole-wheat",
  "whole wheat": "/misc/grains#whole-wheat",
  "whole wheat pasta": "/misc/grains#pasta",
  "pasta": "/misc/grains#pasta",
  "wild rice": "/misc/grains#wild-rice",

  # MEAT
  "bacon": "/misc/meat#bacon",
  "beef liver": "/misc/meat#liver",
  "bologna": "/misc/meat#bologna",
  "chicken breast": "/misc/meat#chicken-breast",
  "chicken breasts": "/misc/meat#chicken-breast",
  "chicken": "/misc/meat#chicken-breast",
  "chicken liver": "/misc/meat#chicken-liver",
  "chicken livers": "/misc/meat#chicken-liver",
  "chicken thighs": "/misc/meat#chicken-thighs",
  "egg": "/misc/meat#eggs",
  "eggs": "/misc/meat#eggs",
  "egg white": "/misc/meat#egg-whites",
  "egg whites": "/misc/meat#egg-whites",
  "ground beef": "/misc/meat#ground-beef",
  "ground turkey": "/misc/meat#ground-turkey",
  "ham": "/misc/meat#ham",
  "hot dog": "/misc/meat#hot-dogs",
  "hot dogs": "/misc/meat#hot-dogs",
  "lamb": "/misc/meat#lamb",
  "pepperoni": "/misc/meat#pepperoni",
  "pork liver": "/misc/meat#pork-liver",
  "pork tenderloin": "/misc/meat#pork-tenderloin",
  "salami": "/misc/meat#salami",
  "sausage": "/misc/meat#sausage",
  "sausages": "/misc/meat#sausage",
  "spam": "/misc/meat#spam",
  "steak": "/misc/meat#steak",
  "steaks": "/misc/meat#steak",
  "turkey breast": "/misc/meat#turkey-breast",
  "turkey breasts": "/misc/meat#turkey-breast",
  "veal": "/misc/meat#veal",
  "venison": "/misc/meat#venison",

  # NUTS
  "almond butter": "/misc/nuts#almond-butter",
  "almond flour": "/misc/nuts#almonds",
  "almonds": "/misc/nuts#almonds",
  "almond": "/misc/nuts#almonds",
  "brazil nuts": "/misc/nuts#brazil-nuts",
  "brazil nut": "/misc/nuts#brazil-nuts",
  "cashews": "/misc/nuts#cashews",
  "cashew butter": "/misc/nuts#cashew-butter",
  "cashew": "/misc/nuts#cashews",
  "chestnuts": "/misc/nuts#chestnuts",
  "chestnut": "/misc/nuts#chestnuts",
  "coconut flakes": "/misc/nuts#coconut",
  "coconut flour": "/misc/nuts#coconut",
  "coconut butter": "/misc/nuts#coconut",
  "coconut oil": "/misc/nuts#coconut",
  "coconut": "/misc/nuts#coconut",
  "hazelnuts": "/misc/nuts#hazelnuts",
  "hazelnut": "/misc/nuts#hazelnuts",
  "macadamia nuts": "/misc/nuts#macadamia-nuts",
  "macadamia nut butter": "/misc/nuts#macadamia-nuts",
  "macadamia nut": "/misc/nuts#macadamia-nuts",
  "peanut butter": "/misc/nuts#peanut-butter",
  "peanuts": "/misc/nuts#peanuts",
  "peanut": "/misc/nuts#peanuts",
  "pecans": "/misc/nuts#pecans",
  "pecan": "/misc/nuts#pecans",
  "pine nuts": "/misc/nuts#pine-nuts",
  "pine nut": "/misc/nuts#pine-nuts",
  "pignoli nuts": "/misc/nuts#pine-nuts",
  "pignoli": "/misc/nuts#pine-nuts",
  "pistachios": "/misc/nuts#pistachios",
  "pistachio butter": "/misc/nuts#pistachios",
  "pistachio": "/misc/nuts#pistachios",
  "walnuts": "/misc/nuts#walnuts",
  "walnut butter": "/misc/nuts#walnut-butter",
  "walnut": "/misc/nuts#walnuts",

  # SEEDS
  "chia seeds": "/misc/seeds#chia-seeds",
  "chia seed": "/misc/seeds#chia-seeds",
  "chia": "/misc/seeds#chia-seeds",
  "flax seeds": "/misc/seeds#flax-seeds",
  "flax seed": "/misc/seeds#flax-seeds",
  "flax": "/misc/seeds#flax-seeds",
  "hemp seeds": "/misc/seeds#hemp-seeds",
  "hemp seed": "/misc/seeds#hemp-seeds",
  "hemp": "/misc/seeds#hemp-seeds",
  "poppy seeds": "/misc/seeds#poppy-seeds",
  "poppy seed": "/misc/seeds#poppy-seeds",
  "poppy": "/misc/seeds#poppy-seeds",
  "pumpkin seeds": "/misc/seeds#pumpkin-seeds",
  "pumpkin seed butter": "/misc/seeds#pumpkin-seed-butter",
  "pumpkin seed": "/misc/seeds#pumpkin-seeds",
  "sesame seeds": "/misc/seeds#sesame-seeds",
  "sesame seed butter": "/misc/seeds#sesame-seeds",
  "sesame seed": "/misc/seeds#sesame-seeds",
  "tahini": "/misc/seeds#sesame-seeds",
  "sunflower seeds": "/misc/seeds#sunflower-seeds",
  "sunflower seed butter": "/misc/seeds#sunflower-seed-butter",
  "sunflower seed": "/misc/seeds#sunflower-seeds",
  "sunflower": "/misc/seeds#sunflower-seeds",

  # VEGGIES
  "acorn squash": "/misc/veggies#acorn-squash",
  "artichokes": "/misc/veggies#artichoke",
  "artichoke": "/misc/veggies#artichoke",
  "arugula": "/misc/veggies#arugula",
  "asparagus": "/misc/veggies#asparagus",
  "beets": "/misc/veggies#beets",
  "beet greens": "/misc/veggies#beet-greens",
  "beet green": "/misc/veggies#beet-greens",
  "beet": "/misc/veggies#beets",
  "bell peppers": "/misc/veggies#pepper",
  "bell pepper": "/misc/veggies#pepper",
  "pepper": "/misc/veggies#pepper",
  "bok choy": "/misc/veggies#bok-choy",
  "broccoli": "/misc/veggies#broccoli",
  "brussels sprouts": "/misc/veggies#brussel-sprout",
  "brussel sprouts": "/misc/veggies#brussel-sprout",
  "brussel sprout": "/misc/veggies#brussel-sprout",
  "butternut squash": "/misc/veggies#butternut-squash",
  "cabbage": "/misc/veggies#cabbage",
  "carrots": "/misc/veggies#carrots",
  "carrot": "/misc/veggies#carrots",
  "cauliflower": "/misc/veggies#cauliflower",
  "celery": "/misc/veggies#celery",
  "collard greens": "/misc/veggies#collard-green",
  "collard green": "/misc/veggies#collard-green",
  "cucumbers": "/misc/veggies#cucumber",
  "cucumber": "/misc/veggies#cucumber",
  "eggplants": "/misc/veggies#eggplant",
  "eggplant": "/misc/veggies#eggplant",
  "fennel": "/misc/veggies#fennel",
  "garlic": "/misc/veggies#garlic",
  "ginger": "/misc/veggies#ginger",
  "green beans": "/misc/veggies#green-bean",
  "green bean": "/misc/veggies#green-bean",
  "string bean": "/misc/veggies#green-bean",
  "kale": "/misc/veggies#kale",
  "kohlrabi": "/misc/veggies#kohlrabi",
  "lettuce": "/misc/veggies#lettuce",
  "mustard greens": "/misc/veggies#mustard-greens",
  "mustard green": "/misc/veggies#mustard-greens",
  "onions": "/misc/veggies#onion",
  "onion": "/misc/veggies#onion",
  "parsnips": "/misc/veggies#parsnips",
  "parsnip": "/misc/veggies#parsnips",
  "peas": "/misc/veggies#pea",
  "pea": "/misc/veggies#pea",
  "plantains": "/misc/veggies#plantain",
  "plantain": "/misc/veggies#plantain",
  "potatoes": "/misc/veggies#potato",
  "potato": "/misc/veggies#potato",
  "pumpkin": "/misc/veggies#pumpkin",
  "radicchio": "/misc/veggies#radicchio",
  "radishes": "/misc/veggies#radish",
  "radish": "/misc/veggies#radish",
  "spaghetti squash": "/misc/veggies#spaghetti-squash",
  "frozen spinach": "/misc/veggies#spinach-fresh",
  "spinach": "/misc/veggies#spinach-fresh",
  "sweet potatoes": "/misc/veggies#sweet-potato",
  "sweet potato": "/misc/veggies#sweet-potato",
  "swiss chard": "/misc/veggies#swiss-chard",
  "tomatoes": "/misc/veggies#tomato",
  "tomato": "/misc/veggies#tomato",
  "turnips": "/misc/veggies#turnip",
  "turnip": "/misc/veggies#turnip",
  "white mushrooms": "/misc/veggies#mushrooms",
  "mushrooms": "/misc/veggies#mushrooms",
  "mushroom": "/misc/veggies#mushrooms",
  "yellow squash": "/misc/veggies#yellow-squash",
  "zucchini": "/misc/veggies#zucchini",

  # NUTRIENTS (ABC)
  "micronutrients": "/misc/nutrient-alphabet",
  "micronutrient": "/misc/nutrient-alphabet",
  "micro nutrients": "/misc/nutrient-alphabet",
  "micro nutrient": "/misc/nutrient-alphabet",
  "nutrients": "/misc/nutrient-alphabet",
  "nutrient": "/misc/nutrient-alphabet",
  "vitamins and minerals": "/misc/nutrient-alphabet",
  "vitamins & minerals": "/misc/nutrient-alphabet",
  "vitamins": "/misc/nutrient-alphabet",
  "vitamin": "/misc/nutrient-alphabet",
  "minerals": "/misc/nutrient-alphabet",
  "mineral": "/misc/nutrient-alphabet",
  "vitamin a": "/misc/nutrient-alphabet#A",
  "beta carotene": "/misc/nutrient-alphabet#A",
  "beta-carotene": "/misc/nutrient-alphabet#A",
  "vitamin b6": "/misc/nutrient-alphabet#B",
  "pyridoxine": "/misc/nutrient-alphabet#B",
  "copper": "/misc/nutrient-alphabet#C",
  "vitamin d": "/misc/nutrient-alphabet#D",
  "vitamin e": "/misc/nutrient-alphabet#E",
  "folate": "/misc/nutrient-alphabet#F",
  "vitamin b9": "/misc/nutrient-alphabet#F",
  "iodine": "/misc/nutrient-alphabet#I",
  "vitamin k": "/misc/nutrient-alphabet#K",
  "lycopene": "/misc/nutrient-alphabet#L",
  "manganese": "/misc/nutrient-alphabet#M",
  "niacin": "/misc/nutrient-alphabet#N",
  "vitamin b3": "/misc/nutrient-alphabet#N",
  "omega-3": "/misc/nutrient-alphabet#O",
  "omega 3": "/misc/nutrient-alphabet#O",
  "EPA": "/misc/nutrient-alphabet#O",
  "DHA": "/misc/nutrient-alphabet#O",
  "ALA": "/misc/nutrient-alphabet#O",
  "vitamin b5": "/misc/nutrient-alphabet#P",
  "pantothenic acid": "/misc/nutrient-alphabet#P",
  "vitamin b2": "/misc/nutrient-alphabet#R",
  "riboflavin": "/misc/nutrient-alphabet#R",
  "selenium": "/misc/nutrient-alphabet#S",
  "vitamin b1": "/misc/nutrient-alphabet#T",
  "thiamin": "/misc/nutrient-alphabet#T",
  "zinc": "/misc/nutrient-alphabet#Z",

  # NUTRIENTS (OTHER)
  "calcium": "/misc/calcium",
  "choline": "/misc/choline",
  "cholesterol": "/misc/cholesterol",
  "fiber": "/misc/fiber",
  "iron": "/misc/iron",
  "magnesium": "/misc/magnesium",
  "phosphorus": "/misc/phosphorus",
  "potassium": "/misc/potassium",
  "sodium": "/misc/sodium",
  "vitamin b12": "/misc/vitamin-b12",
  "vitamin c": "/misc/vitamin-c",
  "added sugar": "/misc/hidden-sugar",
  "hidden sugar": "/misc/hidden-sugar",
  "sugar free": "/misc/hidden-sugar",
  "sugar-free": "/misc/hidden-sugar",
  "sugar": "/misc/hidden-sugar",
  "natural sweetness": "/misc/carbs",
  "carbohydrates": "/misc/carbs",
  "carbohydrate": "/misc/carbs",
  "low carb": "/misc/carbs",
  "high carb": "/misc/carbs",
  "net carbs": "/misc/carbs",
  "net carb": "/misc/carbs",
  "carb": "/misc/carbs",
  "heart healthy fats": "/misc/fats",
  "healthy fats": "/misc/fats",
  "monounsaturated fats": "/misc/fats",
  "monounsaturated fat": "/misc/fats",
  "polyunsaturated fats": "/misc/fats",
  "polyunsaturated fat": "/misc/fats",
  "saturated fats": "/misc/fats",
  "saturated fat": "/misc/fats",
  "trans fats": "/misc/fats",
  "trans fat": "/misc/fats",
  "fats": "/misc/fats",
  "fat": "/misc/fats",
  "protein": "/misc/protein",
  "high protein": "/misc/high-protein",
  "calories": "/misc/calories",
  "low calorie": "/misc/calories",
  "high calorie": "/misc/calories",
  "calorie": "/misc/calories",
  "creatine": "/misc/creatine",

  # DISEASES
  "gluten free": "/misc/gluten",
  "gluten": "/misc/gluten",
  "celiac": "/misc/gluten",
  "metabolic syndrome": "/misc/metabolic-syndrome",
  "type 2 diabetes": "/misc/diabetes",
  "type-2 diabetes": "/misc/diabetes",
  "diabetes": "/misc/diabetes",
  "glucose": "/misc/diabetes",
  "alzheimer's": "/misc/alzheimers",
  "alzheimer": "/misc/alzheimers",
  "dementia": "/misc/alzheimers",
  "sleep": "/misc/sleep",
  "exercise": "/misc/exercise",
  "pcos": "/misc/pcos",
  "polycystic ovary syndrome": "/misc/pcos",
  "insulin resistance": "/misc/insulin-resistance",
  "insulin": "/misc/insulin-resistance",
  "chronic inflammation": "/misc/chronic-inflammation",
  "inflammation": "/misc/chronic-inflammation",
  "anti inflammatory": "/misc/chronic-inflammation",
  "anti-inflammatory": "/misc/chronic-inflammation",
  "reduce inflammation": "/misc/chronic-inflammation",
  "antioxidant": "/misc/phytochemicals",
  "anti-oxidant": "/misc/phytochemicals",

  # KITCHEN
  "silicone spatula": "https://www.amazon.com/dp/B0C37QM1K3?ref=t_ac_view_request_product_image&campaignId=amzn1.campaign.1OO1S5W7ZMYBB&linkCode=tr1&tag=poormanprotei-20&linkId=amzn1.campaign.1OO1S5W7ZMYBB_1751469633605",
  "dough scraper": "https://amzn.to/44XmqKz",
  "bread lame": "https://amzn.to/43Cj65h",
  "razorblade": "https://amzn.to/43Cj65h",

  # MISC
  "processed foods": "/misc/processed-foods",
  "processed food": "/misc/processed-foods",
  "ultra processed foods": "/misc/processed-foods",
  "ultra-processed foods": "/misc/processed-foods",
  "ultra processed food": "/misc/processed-foods",
  "ultra-processed food": "/misc/processed-foods",
  "ultra processed": "/misc/processed-foods",
  "ultra-processed": "/misc/processed-foods",
  "apple cider vinegar": "/misc/apple-cider-vinegar",
  "acv": "/misc/apple-cider-vinegar",
  "prebiotic": "/misc/biotics",
  "probiotic": "/misc/biotics",
  "postbiotic": "/misc/biotics",

  # RECIPE CATEGORIES
  "beans": "/recipes/beans",
  "bean": "/recipes/beans",
  "dairy": "/recipes/dairy",
  "cheese": "/recipes/dairy",
  "fish": "/recipes/fish",
  "seafood": "/recipes/fish",
  "fruits": "/recipes/fruit",
  "fruit": "/recipes/fruit",
  "grains": "/recipes/grains",
  "grain": "/recipes/grains",
  "meats": "/recipes/meat",
  "meat": "/recipes/meat",
  "nuts": "/recipes/nuts",
  "nut": "/recipes/nuts",
  "seeds": "/recipes/seeds",
  "seed": "/recipes/seeds",
  "vegetables": "/recipes/veggies",
  "vegetable": "/recipes/veggies",
  "veggies": "/recipes/veggies",
  "veggie": "/recipes/veggies",

  # FOOD SECTIONS
  "hummus recipes": "/hummus",
  "hummus": "/hummus",
  "oatmeal recipes": "/oatmeal",
  "oatmeal": "/oatmeal",
  "overnight oats": "/oatmeal",
  "yogurt recipes": "/yogurt",
  "morning yogurt": "/yogurt",
  "yogurt bowl": "/yogurt",
  "nut butter recipes": "/nut-butter",
  "nut butter": "/nut-butter",
  "pesto recipes": "/pesto",
  "pesto": "/pesto",
  "soup and stew recipes": "/soup-stew",
  "soup and stew": "/soup-stew",
  "soup recipes": "/soup-stew",
  "soup": "/soup-stew",
  "stew recipes": "/soup-stew",
  "stew": "/soup-stew",
  "chili recipes": "/chili",
  "chili": "/chili",
  "salad recipes": "/salad",
  "salads": "/salad",
  "salad": "/salad",
  "salad dressing recipes": "/dressing",
  "salad dressings": "/dressing",
  "salad dressing": "/dressing",
  "dressing recipes": "/dressing",
  "dressing": "/dressing",
  "brownies": "/brownies",
  "brownie recipes": "/brownies",
  "brownie": "/brownies",
  "cookies": "/cookies",
  "cookie recipes": "/cookies",
  "cookie": "/cookies",
  "copycat recipes": "/copycat",
  "copycat": "/copycat",

  # RECIPE TYPES
  "bread": "/recipes/bread",
  "buns": "/recipes/bread",
  "bun": "/recipes/bread",
  "loaf": "/recipes/bread",
  "breakfast": "/recipes/breakfast",
  "drinks": "/recipes/drink",
  "drink": "/recipes/drink",
  "finger foods": "/recipes/finger-food",
  "finger food": "/recipes/finger-food",
  "ground meat": "/recipes/ground-meat",
  "healthier dessert": "/recipes/healthier-dessert",
  "dessert": "/recipes/healthier-dessert",
  "meatless": "/recipes/meatless",
  "meme recipes": "/recipes/meme",
  "meme recipe": "/recipes/meme",
  "meme": "/recipes/meme",
  "protein powder": "/recipes/protein-powder",
  "savory sauces": "/recipes/savory-sauces",
  "savory sauce": "/recipes/savory-sauces",
  "sides": "/recipes/sides",
  "side": "/recipes/sides",
  "sweet spreads": "/recipes/sweet-spreads",
  "sweet spread": "/recipes/sweet-spreads"
}

EXCLUDED_PHRASES = [
    "cookie sheets",
    "cookie sheet",
    "bread pans",
    "bread pan",
    "banana bread",
    "garlic powder",
    "onion powder",
    "monk fruit",
    "nutritional yeast",
    "minutes",
    "minute",
    "non fat",
    "nonfat",
    "fat free",
    "nutrition",
    "nutritious",
    "flours",
    "evaporated milk",
    "condensed milk",
    "carrot cake",
    "breaded"
    "fryer"
]

EXCLUDED_REGEXES = [
    re.compile(rf"\b{re.escape(p)}\b", re.IGNORECASE)
    for p in EXCLUDED_PHRASES
]

def should_skip_linking(text, key_start, key_end):
    for rx in EXCLUDED_REGEXES:
        for m in rx.finditer(text):
            phrase_start, phrase_end = m.span()

            # ONLY skip if the word is actually inside the phrase
            if key_start >= phrase_start and key_end <= phrase_end:
                return True

    return False

# -------------------------------------------------------------
# Helpers for Liquid and &emsp;
# -------------------------------------------------------------
def extract_liquid_blocks(text):
    blocks = []
    clean = []
    last = 0
    for match in re.finditer(r"{%.*?%}", text, flags=re.DOTALL):
        start, end = match.span()
        clean.append(text[last:start])
        blocks.append(match.group(0))
        clean.append(f"__LIQUID_{len(blocks)-1}__")
        last = end
    clean.append(text[last:])
    return "".join(clean), blocks

def restore_liquid_blocks(text, blocks):
    for i, block in enumerate(blocks):
        text = text.replace(f"__LIQUID_{i}__", block)
    return text

def protect_emsp(text):
    emsp_blocks = {}
    def replacer(m):
        key = f"__EMSP_{len(emsp_blocks)}__"
        emsp_blocks[key] = m.group(0)
        return key
    protected = re.sub(r"&emsp;", replacer, text)
    return protected, emsp_blocks

def restore_emsp(text, emsp_blocks):
    for key, val in emsp_blocks.items():
        text = text.replace(key, val)
    return text

# -------------------------------------------------------------
# Auto-link function
# -------------------------------------------------------------
def auto_link_html_safe_single_quotes(html, links, exclude_phrases=None):
    html, liquid_blocks = extract_liquid_blocks(html)
    html, emsp_blocks = protect_emsp(html)

    soup = BeautifulSoup(html, "html.parser")
    exclude_phrases = [p.lower() for p in (exclude_phrases or [])]

    # Prepare links sorted by length (longest first)
    keys = sorted(links.keys(), key=len, reverse=True)
    links_lower = {k.lower(): v for k, v in links.items()}

    # Build regex with named groups for deterministic longest match
    group_patterns = [
        f"(?P<L{i}>\\b{re.escape(k)}\\b)"
        for i, k in enumerate(keys)
    ]
    pattern = re.compile("|".join(group_patterns), re.IGNORECASE)

    def is_excluded(text, start, end):
        for phrase in exclude_phrases:
            phrase_lower = phrase.lower()
            phrase_start = text.lower().find(phrase_lower)
            if phrase_start != -1 and start >= phrase_start and end <= phrase_start + len(phrase_lower):
                return True
        return False

    def process_node(node):
        if isinstance(node, NavigableString):
            if node.parent.name in ("a", "script", "style"):
                return

            text = str(node)
            fragments = []
            last = 0
            last_end = 0

            for m in pattern.finditer(text):
                start, end = m.span()
                if start < last_end:
                    continue  # skip overlaps

                group_name = m.lastgroup
                key_index = int(group_name[1:])  # L{i} -> i
                key = keys[key_index]
                url = links_lower.get(key.lower())

                # === HARD RULE: skip butter/flour if previous sibling is a nut/seed/grain link ===
                if key.lower() in ("butter", "flour", "seeds"):
                    prev = node.previous_sibling
                    while prev:
                        if getattr(prev, "name", None) == "a":
                            href = prev.get("href", "")
                            if "nuts" in href or "seeds" in href or "grains" in href:
                                url = None  # skip linking butter/flour
                                break
                        prev = prev.previous_sibling

                    if is_excluded(text, start, end):
                        continue

                # === HARD RULE: skip ===
                if should_skip_linking(text, start, end):
                    url = None  # skip linking
                    continue

                if start > last:
                    fragments.append(text[last:start])

                if url:
                    tag = soup.new_tag("a", href=url)
                    tag.string = text[start:end]
                    fragments.append(tag)
                else:
                    fragments.append(text[start:end])

                last = end
                last_end = end

            if last < len(text):
                fragments.append(text[last:])

            for frag in reversed(fragments):
                node.insert_after(NavigableString(frag) if isinstance(frag, str) else frag)
            node.extract()

        elif node.name != "a":
            for child in list(node.contents):
                process_node(child)

    for child in list(soup.contents):
        process_node(child)

    html = "".join(str(c) for c in soup.contents)
    html = re.sub(r'href="([^"]+)"', r"href='\1'", html)
    html = html.replace("<br/>", "<br>")

    html = restore_emsp(html, emsp_blocks)
    html = restore_liquid_blocks(html, liquid_blocks)

    return html

# -------------------------------------------------------------
# Process front matter and body
# -------------------------------------------------------------
def process_front_matter(text, links, exclude_phrases=None):
    lines = text.splitlines(keepends=True)
    output = []
    front_matter_delims_seen = 0
    in_front_matter = False
    body_buffer = []

    for line in lines:
        if line.strip() == "---" and front_matter_delims_seen < 2:
            front_matter_delims_seen += 1
            in_front_matter = front_matter_delims_seen == 1
            output.append(line)
            continue

        if in_front_matter:
            if line.startswith("Description:"):
                key, value = line.split(":", 1)
                value = auto_link_html_safe_single_quotes(value, links, exclude_phrases).rstrip()
                output.append(f"{key}:{value}\n")
            else:
                output.append(line)
        else:
            body_buffer.append(line)

    if body_buffer:
        body = "".join(body_buffer)
        body = auto_link_html_safe_single_quotes(body, links, exclude_phrases)
        output.append(body)

    return "".join(output)

# -------------------------------------------------------------
# Main processing loop
# -------------------------------------------------------------
os.system('cls')
count = 0
for root, _, files in os.walk(POSTS_DIR):
    for file in files:
        if not file.startswith("2024"):
            continue
        if file.endswith((".md", ".html", ".markdown")):
            path = os.path.join(root, file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()

            content_no_liquid, liquid_blocks = extract_liquid_blocks(content)
            new_content = process_front_matter(content_no_liquid, LINKS, EXCLUDED_PHRASES)
            new_content = restore_liquid_blocks(new_content, liquid_blocks)

            if new_content != content:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                    print(f"Updated: {path}")
                    count += 1

print(f"Total files updated: {count}")
