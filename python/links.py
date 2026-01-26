import os
import re
from html import escape, unescape
from bs4 import BeautifulSoup, NavigableString

POSTS_DIR = r"C:\Users\mets1\Documents\website\_posts\misc\cooking"
# POSTS_DIR = r"C:\Users\mets1\Documents\GitHub\pscally1005.github.io\_posts\delete"

LINKS = {

  # RECIPES
  "banana ice cream": "/recipes/nice-cream",
  "salsa": "/recipes/salsa",
  "hot sauce": "/recipes/hot-sauce",
  "sugar free syrup": "/recipes/sugar-free-syrup",
  "sugar-free syrup": "/recipes/sugar-free-syrup",
  "natural peanut butter": "/recipes/natural-peanut-butter",
  "natural nut butter": "/recipes/natural-peanut-butter",
  "natural seed butter": "/recipes/natural-peanut-butter",
  "nut butters": "/recipes/natural-peanut-butter",
  "seed butters": "/recipes/natural-peanut-butter",
  "nut butter": "/recipes/natural-peanut-butter",
  "seed butter": "/recipes/natural-peanut-butter",
  "sugar free chocolate chips": "/recipes/monkfruit-chocolate-chunks",
  "sugar free chocolate": "/recipes/monkfruit-chocolate-chunks",
  "pumpkin puree": "/recipes/pumpkin-puree",
  "sweet potato puree": "/recipes/sweet-potato-puree",
  "butternut squash puree": "/recipes/roasted-butternut-squash-puree",
  "cottage cheese flatbread": "/recipes/cottage-cheese-flatbread",
  "smoothies": "/recipes/smoothie",
  "smoothie": "/recipes/smoothie",

  # BEANS
  "black beans": "/misc/beans#black-beans",
  "black bean": "/misc/beans#black-beans",
  "black eyed peas": "/misc/beans#black-eyed-peas",
  "black eyed pea": "/misc/beans#black-eyed-peas",
  "brown lentils": "/misc/beans#brown-lentils",
  "brown lentil": "/misc/beans#brown-lentils",
  "lentils": "/misc/beans#brown-lentils",
  "lentil": "/misc/beans#brown-lentils",
  "cannellini beans": "/misc/beans#cannellini-beans",
  "cannellini bean": "/misc/beans#cannellini-beans",
  "cannellini": "/misc/beans#cannellini-beans",
  "chickpea pasta": "/misc/beans#chickpeas",
  "chickpeas": "/misc/beans#chickpeas",
  "garbanzo beans": "/misc/beans#chickpeas",
  "garbanzos": "/misc/beans#chickpeas",
  "garbanzo": "/misc/beans#chickpeas",
  "chickpea flour": "/misc/beans#chickpeas",
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
  "red lentil pasta": "/misc/beans#red-lentils",
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
  "protein powder": "/misc/dairy#whey",

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
  "rice": "/misc/grains#brown-rice",
  "buckwheat": "/misc/grains#buckwheat",
  "corn": "/misc/grains#corn",
  "couscous": "/misc/grains#couscous",
  "farro": "/misc/grains#farro",
  "millet": "/misc/grains#millet",
  "oat flour": "/misc/grains#oats",
  "unsweetened oat milk": "/misc/grains#oats",
  "oat milk": "/misc/grains#oats",
  "oats": "/misc/grains#oats",
  "oat": "/misc/grains#oats",
  "rolled oats": "/misc/grains#oats",
  "quick oats": "/misc/grains#oats",
  "popcorn": "/misc/grains#popcorn",
  "quinoa": "/misc/grains#quinoa",
  "rye flour": "/misc/grains#rye",
  "rye": "/misc/grains#rye",
  "spelt flour": "/misc/grains#spelt",
  "spelt": "/misc/grains#spelt",
  "vital wheat gluten": "/misc/grains#vital-wheat-gluten",
  "vwg": "/misc/grains#vital-wheat-gluten",
  "white flour": "/misc/grains#white-wheat",
  "refined flour": "/misc/grains#white-wheat",
  "all purpose flour": "/misc/grains#white-wheat",
  "flour": "/misc/grains#white-wheat",
  "white pasta": "/misc/grains#pasta-white",
  "white rice": "/misc/grains#white-rice",
  "white arborio rice": "/misc/grains#white-rice",
  "arborio rice": "/misc/grains#white-rice",
  "sushi rice": "/misc/grains#white-rice",
  "whole wheat flour": "/misc/grains#whole-wheat",
  "wheat based": "/misc/grains#whole-wheat",
  "wheat grain": "/misc/grains#whole-wheat",
  "wheat flour": "/misc/grains#white-wheat",
  "whole wheat": "/misc/grains#whole-wheat",
  "whole wheat pasta": "/misc/grains#pasta",
  "wheat flour": "/misc/grains#pasta-white",
  "pasta": "/misc/grains#pasta",
  "wild rice": "/misc/grains#wild-rice",

  # MEAT
  "bacon": "/misc/meat#bacon",
  "beef liver": "/misc/meat#liver",
  "bologna": "/misc/meat#bologna",
  "boneless skinless chicken breasts": "/misc/meat#chicken-breast",
  "boneless skinless chicken breast": "/misc/meat#chicken-breast",
  "chicken breast": "/misc/meat#chicken-breast",
  "chicken breasts": "/misc/meat#chicken-breast",
  "breasts": "/misc/meat#chicken-breast",
  "breast": "/misc/meat#chicken-breast",
  "chicken": "/misc/meat#chicken-breast",
  "chicken liver": "/misc/meat#chicken-liver",
  "chicken livers": "/misc/meat#chicken-liver",
  "boneless skinless chicken thighs": "/misc/meat#chicken-thighs",
  "boneless skinless chicken thigh": "/misc/meat#chicken-thighs",
  "bone-in skin-on chicken thighs": "/misc/meat#chicken-thighs",
  "bone-in skin-on chicken thigh": "/misc/meat#chicken-thighs",
  "bone in skin on chicken thighs": "/misc/meat#chicken-thighs",
  "bone in skin on chicken thigh": "/misc/meat#chicken-thighs",
  "chicken thighs": "/misc/meat#chicken-thighs",
  "thighs": "/misc/meat#chicken-thighs",
  "thigh meat": "/misc/meat#chicken-thighs",
  "thigh": "/misc/meat#chicken-thighs",
  "egg yolks": "/misc/meat#eggs",
  "egg yolk": "/misc/meat#eggs",
  "egg": "/misc/meat#eggs",
  "eggs": "/misc/meat#eggs",
  "egg whites": "/misc/meat#egg-whites",
  "egg white": "/misc/meat#egg-whites",
  "whites": "/misc/meat#egg-whites",
  "ground beef": "/misc/meat#ground-beef",
  "beef": "/misc/meat#ground-beef",
  "ground turkey": "/misc/meat#ground-turkey",
  "turkey": "/misc/meat#ground-turkey",
  "ham": "/misc/meat#ham",
  "hot dog": "/misc/meat#hot-dogs",
  "hot dogs": "/misc/meat#hot-dogs",
  "lamb": "/misc/meat#lamb",
  "pepperoni": "/misc/meat#pepperoni",
  "pork liver": "/misc/meat#pork-liver",
  "pork tenderloin": "/misc/meat#pork-tenderloin",
  "ground pork": "/misc/meat#pork-tenderloin",
  "pork": "/misc/meat#pork-tenderloin",
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
  "almond butter": "/misc/nuts#almonds",
  "almond flour": "/misc/nuts#almonds",
  "almonds": "/misc/nuts#almonds",
  "almond": "/misc/nuts#almonds",
  "brazil nuts": "/misc/nuts#brazil-nuts",
  "brazil nut": "/misc/nuts#brazil-nuts",
  "unsweetened cashew milk": "/misc/nuts#cashews",
  "cashew milk": "/misc/nuts#cashews",
  "cashews": "/misc/nuts#cashews",
  "cashew butter": "/misc/nuts#cashews",
  "cashew": "/misc/nuts#cashews",
  "chestnuts": "/misc/nuts#chestnuts",
  "chestnut": "/misc/nuts#chestnuts",
  "unsweetened coconut flakes": "/misc/nuts#coconut",
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
  "peanut butter": "/misc/nuts#peanuts",
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
  "walnut butter": "/misc/nuts#walnuts",
  "walnut": "/misc/nuts#walnuts",

  # SEEDS
  "chia seeds": "/misc/seeds#chia-seeds",
  "chia seed": "/misc/seeds#chia-seeds",
  "chia": "/misc/seeds#chia-seeds",
  "ground flax seeds": "/misc/seeds#flax-seeds",
  "ground flaxseeds": "/misc/seeds#flax-seeds",
  "ground flax seed": "/misc/seeds#flax-seeds",
  "ground flaxseed": "/misc/seeds#flax-seeds",
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
  "pumpkin seed butter": "/misc/seeds#pumpkin-seeds",
  "pumpkin seed": "/misc/seeds#pumpkin-seeds",
  "sesame seeds": "/misc/seeds#sesame-seeds",
  "sesame seed butter": "/misc/seeds#sesame-seeds",
  "sesame seed": "/misc/seeds#sesame-seeds",
  "tahini": "/misc/seeds#sesame-seeds",
  "sunflower seeds": "/misc/seeds#sunflower-seeds",
  "sunflower seed butter": "/misc/seeds#sunflower-seeds",
  "sun butter": "/misc/seeds#sunflower-seeds",
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
  "peppers": "/misc/veggies#pepper",
  "pepper": "/misc/veggies#pepper",
  "bok choy": "/misc/veggies#bok-choy",
  "broccoli": "/misc/veggies#broccoli",
  "brussels sprouts": "/misc/veggies#brussel-sprout",
  "brussel sprouts": "/misc/veggies#brussel-sprout",
  "brussel sprout": "/misc/veggies#brussel-sprout",
  "butternut squash noodles": "/misc/veggies#butternut-squash",
  "butternut squash": "/misc/veggies#butternut-squash",
  "shredded cabbage": "/misc/veggies#cabbage",
  "cabbage": "/misc/veggies#cabbage",
  "baby carrots": "/misc/veggies#carrots",
  "baby carrot": "/misc/veggies#carrots",
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
  "fresh garlic": "/misc/veggies#garlic",
  "garlic cloves": "/misc/veggies#garlic",
  "minced garlic": "/misc/veggies#garlic",
  "garlic": "/misc/veggies#garlic",
  "ginger": "/misc/veggies#ginger",
  "green beans": "/misc/veggies#green-bean",
  "green bean": "/misc/veggies#green-bean",
  "string bean": "/misc/veggies#green-bean",
  "kale": "/misc/veggies#kale",
  "kohlrabi": "/misc/veggies#kohlrabi",
  "romaine lettuce": "/misc/veggies#lettuce",
  "iceberg lettuce": "/misc/veggies#lettuce",
  "romaine": "/misc/veggies#lettuce",
  "iceberg": "/misc/veggies#lettuce",
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
  "yams": "/misc/veggies#sweet-potato",
  "yam": "/misc/veggies#sweet-potato",
  "swiss chard": "/misc/veggies#swiss-chard",
  "tomatoes": "/misc/veggies#tomato",
  "tomato": "/misc/veggies#tomato",
  "turnips": "/misc/veggies#turnip",
  "turnip": "/misc/veggies#turnip",
  "white mushrooms": "/misc/veggies#mushrooms",
  "mushrooms": "/misc/veggies#mushrooms",
  "mushroom": "/misc/veggies#mushrooms",
  "yellow squash": "/misc/veggies#yellow-squash",
  "zucchini noodles": "/misc/veggies#zucchini",
  "zucchini noodle": "/misc/veggies#zucchini",
  "zoodles": "/misc/veggies#zucchini",
  "zoodle": "/misc/veggies#zucchini",
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
  "b6": "/misc/nutrient-alphabet#B",
  "b vitamins": "/misc/nutrient-alphabet#B",
  "pyridoxine": "/misc/nutrient-alphabet#B",
  "copper": "/misc/nutrient-alphabet#C",
  "vitamin d": "/misc/nutrient-alphabet#D",
  "vitamin e": "/misc/nutrient-alphabet#E",
  "folate": "/misc/nutrient-alphabet#F",
  "vitamin b9": "/misc/nutrient-alphabet#F",
  "b9": "/misc/nutrient-alphabet#F",
  "iodine": "/misc/nutrient-alphabet#I",
  "vitamin k": "/misc/nutrient-alphabet#K",
  "lycopene": "/misc/nutrient-alphabet#L",
  "manganese": "/misc/nutrient-alphabet#M",
  "niacin": "/misc/nutrient-alphabet#N",
  "vitamin b3": "/misc/nutrient-alphabet#N",
  "b3": "/misc/nutrient-alphabet#N",
  "omega-3": "/misc/nutrient-alphabet#O",
  "omega 3": "/misc/nutrient-alphabet#O",
  "EPA": "/misc/nutrient-alphabet#O",
  "DHA": "/misc/nutrient-alphabet#O",
  "ALA": "/misc/nutrient-alphabet#O",
  "vitamin b5": "/misc/nutrient-alphabet#P",
  "pantothenic acid": "/misc/nutrient-alphabet#P",
  "vitamin b2": "/misc/nutrient-alphabet#R",
  "b2": "/misc/nutrient-alphabet#R",
  "riboflavin": "/misc/nutrient-alphabet#R",
  "selenium": "/misc/nutrient-alphabet#S",
  "vitamin b1": "/misc/nutrient-alphabet#T",
  "b1": "/misc/nutrient-alphabet#T",
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
  "refined sugar": "/misc/hidden-sugar",
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
  "added fats": "/misc/fats",
  "added fat": "/misc/fats",
  "fats": "/misc/fats",
  "fat": "/misc/fats",
  "refined oils": "/misc/fats",
  "refined oil": "/misc/fats",
  "seed oils": "/misc/fats",
  "seed oil": "/misc/fats",
  "vegetable oils": "/misc/fats",
  "vegetable oil": "/misc/fats",
  "oils": "/misc/fats",
  "oil": "/misc/fats",
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

  # AMAZON
  "metal spatula": "https://amzn.to/4raSjqy",
  "silicone spatula": "https://www.amazon.com/dp/B0C37QM1K3?ref=t_ac_view_request_product_image&campaignId=amzn1.campaign.1OO1S5W7ZMYBB&linkCode=tr1&tag=poormanprotei-20&linkId=amzn1.campaign.1OO1S5W7ZMYBB_1751469633605",
  "spatula": "https://www.amazon.com/dp/B0C37QM1K3?ref=t_ac_view_request_product_image&campaignId=amzn1.campaign.1OO1S5W7ZMYBB&linkCode=tr1&tag=poormanprotei-20&linkId=amzn1.campaign.1OO1S5W7ZMYBB_1751469633605",
  "dough scraper": "https://amzn.to/44XmqKz",
  "bread lame": "https://amzn.to/43Cj65h",
  "razorblade": "https://amzn.to/43Cj65h",
  "liquid monk fruit": "https://amzn.to/3SqwsMO",
  "powdered peanut butter": "https://www.amazon.com/dp/B07SXBL1GF?ref=t_ac_view_request_product_image&campaignId=amzn1.campaign.2L4DOI4F1KV3G&linkCode=tr1&tag=poormanprotei-20&linkId=amzn1.campaign.2L4DOI4F1KV3G_1767022097417",
  "granulated monk fruit": "https://www.amazon.com/dp/B0DD4YY92R?ref=t_ac_view_request_product_image&campaignId=amzn1.campaign.3UEEUG24MBC1R&linkCode=tr1&tag=poormanprotei-20&linkId=amzn1.campaign.3UEEUG24MBC1R_1767021852598",
  "lactase enzyme": "https://amzn.to/43ycqF2",
  "inulin": "https://amzn.to/47w8h7R",
  "food scale": "https://amzn.to/45yjx2X",
  "kitchen scale": "https://amzn.to/45yjx2X",
  "scale": "https://amzn.to/45yjx2X",
  "food processor": "https://amzn.to/4q0AUjI",
  "blender": "https://amzn.to/4bO4VQ3",
  "small food processor": "https://amzn.to/3VHhgMM",
  "small food chopper": "https://amzn.to/3VHhgMM",
  "immersion blender": "https://amzn.to/3VHhgMM",
  "chopper": "https://amzn.to/3VHhgMM",
  "air fryers": "https://amzn.to/3FuWETp",
  "air fryer": "https://amzn.to/3FuWETp",
  "air fried": "https://amzn.to/3FuWETp",
  "air fry": "https://amzn.to/3FuWETp",
  "air fryer liner": "https://amzn.to/43AzcfI",
  "silicone liner": "https://amzn.to/44T3n3X",
  "silicone baking mat": "https://amzn.to/44T3n3X",
  "silicone mat": "https://amzn.to/44T3n3X",
  '9" square baking pans': "https://amzn.to/3YY2H9q",
  '9" square baking pan': "https://amzn.to/3YY2H9q",
  '9" square pans': "https://amzn.to/3YY2H9q",
  '9" square pan': "https://amzn.to/3YY2H9q",
  "9x9 square baking pans": "https://amzn.to/3YY2H9q",
  "9x9 square baking pan": "https://amzn.to/3YY2H9q",
  "9 inch square baking pans": "https://amzn.to/3YY2H9q",
  "9 inch square baking pan": "https://amzn.to/3YY2H9q",
  "9 in square baking pans": "https://amzn.to/3YY2H9q",
  "9 in square baking pan": "https://amzn.to/3YY2H9q",
  "9x13in pans": "https://amzn.to/4aiCsjh",
  "9x13in pan": "https://amzn.to/4aiCsjh",
  '9x13" casserole dishes': "https://amzn.to/4aiCsjh",
  '9x13" casserole dish': "https://amzn.to/4aiCsjh",
  '9x13" casserole pans': "https://amzn.to/4aiCsjh",
  '9x13" casserole pan': "https://amzn.to/4aiCsjh",
  '9x13" baking dishes': "https://amzn.to/4aiCsjh",
  '9x13" baking dish': "https://amzn.to/4aiCsjh",
  '9x13" baking pans': "https://amzn.to/4aiCsjh",
  '9x13" baking pan': "https://amzn.to/4aiCsjh",
  '9x13" pans': "https://amzn.to/4aiCsjh",
  '9x13" pan': "https://amzn.to/4aiCsjh",
  "9x13in pans": "https://amzn.to/4aiCsjh",
  "9x13in pan": "https://amzn.to/4aiCsjh",
  '9 x 13" casserole dishes': "https://amzn.to/4aiCsjh",
  '9 x 13" casserole dish': "https://amzn.to/4aiCsjh",
  '9 x 13" casserole pans': "https://amzn.to/4aiCsjh",
  '9 x 13" casserole pan': "https://amzn.to/4aiCsjh",
  '9 x 13" baking dishes': "https://amzn.to/4aiCsjh",
  '9 x 13" baking dish': "https://amzn.to/4aiCsjh",
  '9 x 13" baking pans': "https://amzn.to/4aiCsjh",
  '9 x 13" baking pan': "https://amzn.to/4aiCsjh",
  '9 x 13" pans': "https://amzn.to/4aiCsjh",
  '9 x 13" pan': "https://amzn.to/4aiCsjh",
  '9" pie pans': "https://amzn.to/4q0gY0f",
  '9" pie pan': "https://amzn.to/4q0gY0f",
  '9" cake pans': "https://amzn.to/4q0gY0f",
  '9" cake pan': "https://amzn.to/4q0gY0f",
  '9" circlular pie pans': "https://amzn.to/4q0gY0f",
  '9" circlular pie pan': "https://amzn.to/4q0gY0f",
  '9" circlular cake pans': "https://amzn.to/4q0gY0f",
  '9" circlular cake pan': "https://amzn.to/4q0gY0f",
  '9" circle pie pans': "https://amzn.to/4q0gY0f",
  '9" circle pie pan': "https://amzn.to/4q0gY0f",
  '9" circle cake pans': "https://amzn.to/4q0gY0f",
  '9" circle cake pan': "https://amzn.to/4q0gY0f",
  '9" circle pans': "https://amzn.to/4q0gY0f",
  '9" circle pan': "https://amzn.to/4q0gY0f",
  '9x5" bread pans': "https://amzn.to/3YUjIkN",
  '9x5" bread pan': "https://amzn.to/3YUjIkN",
  '9 x 5" bread pans': "https://amzn.to/3YUjIkN",
  '9 x 5" bread pan': "https://amzn.to/3YUjIkN",
  '9x5" loaf pans': "https://amzn.to/3YUjIkN",
  '9x5" loaf pan': "https://amzn.to/3YUjIkN",
  '9 x 5" loaf pans': "https://amzn.to/3YUjIkN",
  '9 x 5" loaf pan': "https://amzn.to/3YUjIkN",
  "bread pans": "https://amzn.to/3YUjIkN",
  "bread pan": "https://amzn.to/3YUjIkN",
  "cookie sheets": "https://amzn.to/45sRAsB",
  "cookie sheet": "https://amzn.to/45sRAsB",
  "baking pans": "https://amzn.to/45sRAsB",
  "baking pan": "https://amzn.to/45sRAsB",
  "mini muffin pans": "https://amzn.to/3T1ymDy",
  "mini muffin pan": "https://amzn.to/3T1ymDy",
  "mini-muffin pans": "https://amzn.to/3T1ymDy",
  "mini-muffin pan": "https://amzn.to/3T1ymDy",
  "mini muffin tins": "https://amzn.to/3T1ymDy",
  "mini muffin tin": "https://amzn.to/3T1ymDy",
  "mini-muffin tins": "https://amzn.to/3T1ymDy",
  "mini-muffin tin": "https://amzn.to/3T1ymDy",
  "muffin pans": "https://amzn.to/4mzzEDl",
  "muffin pan": "https://amzn.to/4mzzEDl",
  "wooden spoons": "https://amzn.to/3Fw6MeC",
  "wooden spoon": "https://amzn.to/3Fw6MeC",
  "wooden spatulas": "https://amzn.to/3Fw6MeC",
  "wooden spatula": "https://amzn.to/3Fw6MeC",
  "food thermometer": "https://amzn.to/4kmobG2",
  "instant thermometer": "https://amzn.to/4kmobG2",
  "thermometer": "https://amzn.to/4kmobG2",
  "internal temperature": "https://amzn.to/4kmobG2",
  "spray of oil": "https://amzn.to/3Hdg0gk",
  "spray the paper with oil": "https://amzn.to/3Hdg0gk",
  "spray the pan with oil": "https://amzn.to/3Hdg0gk",
  "spray with oil": "https://amzn.to/3Hdg0gk",
  "cooking spray": "https://amzn.to/3Hdg0gk",
  "oil spray": "https://amzn.to/3Hdg0gk",
  "spray": "https://amzn.to/3Hdg0gk",
  "grease with oil": "https://amzn.to/3Hdg0gk",
  "glass containers": "https://amzn.to/4mPZcMW",
  "glass container": "https://amzn.to/4mPZcMW",
  "glass meal prep containers": "https://amzn.to/4mPZcMW",
  "glass meal prep container": "https://amzn.to/4mPZcMW",
  "meal prep containers": "https://amzn.to/4mPZcMW",
  "meal prep container": "https://amzn.to/4mPZcMW",
  "large glass bowls": "https://amzn.to/4adxMft",
  "large glass bowl": "https://amzn.to/4adxMft",
  "medium glass bowls": "https://amzn.to/4adxMft",
  "medium glass bowl": "https://amzn.to/4adxMft",
  "small glass bowls": "https://amzn.to/4adxMft",
  "small glass bowl": "https://amzn.to/4adxMft",
  "glass bowls": "https://amzn.to/4adxMft",
  "glass bowl": "https://amzn.to/4adxMft",
  "large bowls": "https://amzn.to/4adxMft",
  "large bowl": "https://amzn.to/4adxMft",
  "medium bowls": "https://amzn.to/4adxMft",
  "medium bowl": "https://amzn.to/4adxMft",
  "small bowls": "https://amzn.to/4adxMft",
  "small bowl": "https://amzn.to/4adxMft",
  "metal bowls": "https://amzn.to/4rb3CiD",
  "metal bowl": "https://amzn.to/4rb3CiD",
  "hand mixer": "https://amzn.to/45yqsbM",
  "salad spinner": "https://amzn.to/4dFeyPZ",
  '12" nonstick pans': "https://amzn.to/4rdR0HI",
  '12" nonstick pan': "https://amzn.to/4rdR0HI",
  '12" non-stick pans': "https://amzn.to/4rdR0HI",
  '12" non-stick pan': "https://amzn.to/4rdR0HI",
  '12" pans': "https://amzn.to/4rdR0HI",
  '12" pan': "https://amzn.to/4rdR0HI",
  '12"': "https://amzn.to/4rdR0HI",
  "large pans": "https://amzn.to/4rdR0HI",
  "large pan": "https://amzn.to/4rdR0HI",
  "cast iron pan": "https://amzn.to/465aAxx",
  "cast iron": "https://amzn.to/465aAxx",
  "small pans": "https://amzn.to/4qFE9y3",
  "small pan": "https://amzn.to/4qFE9y3",
  '8" pans': "https://amzn.to/4qFE9y3",
  '8" pan': "https://amzn.to/4qFE9y3",
  '8"': "https://amzn.to/4qFE9y3",
  "stainless steel pans": "https://amzn.to/4pREQ61",
  "stainless steel pan": "https://amzn.to/4pREQ61",
  "stainless steel pots": "https://amzn.to/49DLg42",
  "stainless steel pot": "https://amzn.to/49DLg42",
  "medium saucepot": "https://amzn.to/46ccg8m",
  "medium pot": "https://amzn.to/46ccg8m",
  "dutch oven": "https://amzn.to/3LNGdVy",
  '10" pans': "https://amzn.to/4bOh0on",
  '10" pan': "https://amzn.to/4bOh0on",
  '10"': "https://amzn.to/4bOh0on",
  "potato masher": "https://amzn.to/4r5boL0",
  "fine mesh strainer": "https://amzn.to/4q2FwWu",
  "mesh strainer": "https://amzn.to/4q2FwWu",
  "sift": "https://amzn.to/4q2FwWu",
  "spider": "https://amzn.to/49ZXQcQ",
  "wire racks": "https://amzn.to/4qQNmn2",
  "wire rack": "https://amzn.to/4qQNmn2",
  "cooling racks": "https://amzn.to/4qQNmn2",
  "cooling rack": "https://amzn.to/4qQNmn2",
  "knife sharpener": "https://amzn.to/44T3gFz",
  "chef knife": "https://amzn.to/4jlDKwc",
  "knives": "https://amzn.to/4jlDKwc",
  "knife": "https://amzn.to/4jlDKwc",
  "cutting board": "https://amzn.to/43gNqmY",
  "measuring spoons": "https://amzn.to/4dHwY2G",
  "measuring spoon": "https://amzn.to/4dHwY2G",
  "measuring cups": "https://amzn.to/4dFNtMP",
  "measuring cup": "https://amzn.to/4dFNtMP",
  "large slow cooker": "https://amzn.to/49TUS9E",
  "large slowcooker": "https://amzn.to/49TUS9E",
  "large crockpot": "https://amzn.to/49TUS9E",
  "large crock pot": "https://amzn.to/49TUS9E",
  "slow cooker": "https://amzn.to/49TUS9E",
  "slowcooker": "https://amzn.to/49TUS9E",
  "crockpot": "https://amzn.to/49TUS9E",
  "crock pot": "https://amzn.to/49TUS9E",
  "mandoline": "https://amzn.to/4q3nlQz",
  "chocolate bar mold": "https://amzn.to/4qZKHI9",
  "chocolate mold": "https://amzn.to/4qZKHI9",

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
  "flour replacement": "/misc/water-absorption",
  "flour substitute": "/misc/water-absorption",

  # RECIPE CATEGORIES
  "beans": "/misc/beans",
  "bean": "/misc/beans",
  "dairy": "/misc/dairy",
  "cheese": "/misc/dairy",
  "fish": "/misc/fish",
  "seafood": "/misc/fish",
  "fruits": "/misc/fruit",
  "fruit": "/misc/fruit",
  "grains": "/misc/grains",
  "grain": "/misc/grains",
  "meats": "/misc/meat",
  "meat": "/misc/meat",
  "nuts": "/misc/nuts",
  "nut": "/misc/nuts",
  "seeds": "/misc/seeds",
  "seed": "/misc/seeds",
  "vegetables": "/misc/veggies",
  "vegetable": "/misc/veggies",
  "veggies": "/misc/veggies",
  "veggie": "/misc/veggies",
  "dark leafy greens": "/misc/veggies",
  "leafy greens": "/misc/veggies",
  "greens": "/misc/veggies",

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
  "soups and stews": "/soup-stew",
  "soup and stew": "/soup-stew",
  "soup recipes": "/soup-stew",
  "soups": "/soup-stew",
  "soup": "/soup-stew",
  "stew recipes": "/soup-stew",
  "stews": "/soup-stew",
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
  "breads": "/recipes/bread",
  "bread": "/recipes/bread",
  "buns": "/recipes/bread",
  "bun": "/recipes/bread",
  "breakfast": "/recipes/breakfast",
  "drinks": "/recipes/drink",
  "drink": "/recipes/drink",
  "finger foods": "/recipes/finger-food",
  "finger food": "/recipes/finger-food",
  "ground meat": "/recipes/ground-meat",
  "healthier desserts": "/recipes/healthier-dessert",
  "healthier dessert": "/recipes/healthier-dessert",
  "desserts": "/recipes/healthier-dessert",
  "dessert": "/recipes/healthier-dessert",
  "meatless": "/recipes/meatless",
  "meme recipes": "/recipes/meme",
  "meme recipe": "/recipes/meme",
  "meme": "/recipes/meme",
  # "protein powder": "/recipes/protein-powder",
  "protein snacks": "/recipes/protein-powder",
  "protein snack": "/recipes/protein-powder",
  "protein desserts": "/recipes/protein-powder",
  "protein dessert": "/recipes/protein-powder",
  "savory sauces": "/recipes/savory-sauces",
  "savory sauce": "/recipes/savory-sauces",
  "sides": "/recipes/sides",
  "side dish": "/recipes/sides",
  "side": "/recipes/sides",
  "sweet spreads": "/recipes/sweet-spreads",
  "sweet spread": "/recipes/sweet-spreads"
}

EXCLUDED_PHRASES = [""

    "banana peppers",
    "banana pepper",
    "banana bread",
    "garlic powder",
    "onion powder",
    "garlic and onion powders",
    "garlic and onion powder",
    "garlic and onion",
    "onion and garlic powders",
    "onion and garlic powder",
    "onion and garlic",
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
    "breaded",
    "fryer",
    "olive oil",
    "peanut oil",
    "avocado oil",
    "lemon pepper",
    "lime pepper",
    "mango pepper",
    "cut side",
    "the side",
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
    "cast iron",
    "cast-iron",
    "non dairy",
    "non-dairy",
    "all sides",
    "all 4 sides",
    "4 sides",
    "both sides",
    "soy sauce",
    "the flour",
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
    "the sides",
    "the side",
    "one side",
    "scoop out the seeds",
    "the seeds",
    "the seed",
    "black pepper",
    "cayenne pepper",
    "chicken bouillon",
    "chicken broth",
    "chicken bone",
    "chicken skin",
    "red pepper flakes",
    "red pepper",
    "chili powder",
    "scale up",
    "scale down",
    "scale this",
    "easily scale",
    "grains of",
    "butter knife",
    '8" long',
    '1/8" thick',
    '1/8"',
    '1/8" - 1/4"',
    "gluten free flour",
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
    "low sodium",
    "date syrup",
]

REMOVE_CATEGORIES = [
    "/misc/beans",
    "/misc/dairy",
    "/misc/fish",
    "/misc/fruit",
    "/misc/grains",
    "/misc/meat",
    "/misc/nuts",
    "/misc/seeds",
    "/misc/veggies",
]

EXCLUDED_REGEXES = [
    re.compile(rf"\b{re.escape(p)}\b", re.IGNORECASE)
    for p in EXCLUDED_PHRASES
]

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
# Auto-linker (PURE TEXT, NO PARSING)
# -------------------------------------------------------------
def auto_link_html_safe_single_quotes(html, links, exclude_phrases=None):

    exclude_phrases = [p.lower() for p in (exclude_phrases or [])]

    # ---------------------------------------------------------
    # Protect regions that must NEVER be touched
    # ---------------------------------------------------------
    PROTECTED_PATTERNS = [
        r"{%.*?%}",                       # Liquid
        r"<a\b[^>]*>.*?</a>",             # Existing links
        r"<script\b[^>]*>.*?</script>",
        r"<style\b[^>]*>.*?</style>",
        # r"<ul\b[^>]*>.*?</ul>",
        # r"<ol\b[^>]*>.*?</ol>",
        r"<div\b[^>]*>.*?</div>",
        r"<img\b[^>]*>",
        r"&emsp;",
        r"<font\b[^>]*>.*?</font>",
    ]

    html, protected_blocks = protect_blocks(html, PROTECTED_PATTERNS)

    # ---------------------------------------------------------
    # Prepare longest-first regex
    # ---------------------------------------------------------
    keys = sorted(links.keys(), key=len, reverse=True)
    links_lower = {k.lower(): v for k, v in links.items()}

    pattern = re.compile(
        r"\b(" + "|".join(map(re.escape, keys)) + r")\b",
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

        # excluded phrases
        for phrase in exclude_phrases:
            idx = html.lower().find(phrase)
            if idx != -1 and start >= idx and end <= idx + len(phrase):
                return word

        if should_skip_linking(html, start, end):
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

                value = remove_existing_links(value, REMOVE_CATEGORIES)
                value = auto_link_html_safe_single_quotes(value, links, exclude_phrases)

                output.append(f"{key}:{value}")
                continue

            # Bullet points inside Instructions / Notes
            if current_section in ("Instructions", "Notes") and line.lstrip().startswith("-"):
                line = remove_existing_links(line, REMOVE_CATEGORIES)

                linked = auto_link_html_safe_single_quotes(
                    line,
                    links,
                    exclude_phrases
                )

                output.append(linked)
                continue

            # Any other front-matter line
            output.append(line)
        else:
            body.append(line)

    # Process body normally
    if body:
        html_body = "".join(body)
        html_body = remove_existing_links(html_body, REMOVE_CATEGORIES)
        output.append(auto_link_html_safe_single_quotes(html_body, links, exclude_phrases))

    return "".join(output)

# -------------------------------------------------------------
# Main processing loop (NO BeautifulSoup)
# -------------------------------------------------------------
def main():
    os.system("cls")
    print("-------------------")

    count = 0

    for root, _, files in os.walk(POSTS_DIR):
        for file in files:
            if not file.endswith((".md", ".html", ".markdown")):
                continue

            # optional filename filter (keep or remove)
            # if not file.startswith("2024"):
                # continue

            # exclude some files
            if file.startswith("2025-11-03-cheese") or file.startswith("2024-04-01-fish-chips") or file.startswith("2024-08-23-kitchen"):
                continue

            path = os.path.join(root, file)

            with open(path, "r", encoding="utf-8") as f:
                original = f.read()

            updated = process_front_matter(
                original,
                LINKS,
                EXCLUDED_PHRASES
            )

            if updated != original:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(updated)

                print(f"Updated: {path}")
                count += 1

    print(f"Total files updated: {count}")


if __name__ == "__main__":
    main()
