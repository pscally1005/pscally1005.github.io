import os
import re
from html import escape, unescape
from bs4 import BeautifulSoup

POSTS_DIR = r"C:\Users\mets1\Documents\website\_posts\archive"

LINKS = {
  # BEANS
  "black bean": "/misc/beans#black-beans",
  "black eyed pea": "/misc/beans#black-eyed-peas",
  "brown lentil": "/misc/beans#brown-lentils",
  "cannellini bean": "/misc/beans#cannellini-beans",
  "cannellini": "/misc/beans#cannellini-beans",
  "chickpea": "/misc/beans#chickpeas",
  "edamame": "/misc/beans#edamame",
  "fava bean": "/misc/beans#fava-beans",
  "fava": "/misc/beans#fava-beans",
  "great northern bean": "/misc/beans#great-northern-beans",
  "great northern": "/misc/beans#great-northern-beans",
  "green lentil": "/misc/beans#green-lentils",
  "kidney bean": "/misc/beans#kidney-beans",
  "kidney": "/misc/beans#kidney-beans",
  "lima bean": "/misc/beans#lima-beans",
  "lima": "/misc/beans#lima-beans",
  "lupini bean": "/misc/beans#lupini-beans",
  "lupini": "/misc/beans#lupini-beans",
  "navy bean": "/misc/beans#navy-beans",
  "navy": "/misc/beans#navy-beans",
  "pink bean": "/misc/beans#pink-beans",
  "pinto bean": "/misc/beans#pinto-beans",
  "pinto": "/misc/beans#pinto-beans",
  "red lentil": "/misc/beans#red-lentils",
  "soy bean": "/misc/beans#soybeans",
  "soybean": "/misc/beans#soybeans",
  "soy": "/misc/beans#soybeans",
  "tofu": "/misc/beans#tofu",

  # DAIRY
  "almond milk": "/misc/dairy#almond-milk",
  "blue cheese": "/misc/dairy#blue-cheese",
  "butter": "/misc/dairy#butter",
  "casein protein powder": "/misc/dairy#casein",
  "casein protein": "/misc/dairy#casein",
  "casein": "/misc/dairy#casein",
  "cheddar cheese": "/misc/dairy#cheddar",
  "cheddar": "/misc/dairy#cheddar",
  "coconut milk": "/misc/dairy#coconut-milk",
  "nonfat cottage cheese": "/misc/dairy#cottage-cheese",
  "cottage cheese": "/misc/dairy#cottage-cheese",
  "whole milk cottage cheese": "/misc/dairy#cottage-cheese-whole-milk",
  "cream cheese": "/misc/dairy#cream-cheese",
  "feta cheese": "/misc/dairy#feta",
  "feta": "/misc/dairy#feta",
  "goat cheese": "/misc/dairy#goat-cheese",
  "plain nonfat greek yogurt": "/misc/dairy#yogurt",
  "greek yogurt": "/misc/dairy#yogurt",
  "yogurt": "/misc/dairy#yogurt",
  "plain whole milk greek yogurt": "/misc/dairy#yogurt-whole-milk",
  "kefir": "/misc/dairy#kefir",
  "skim milk": "/misc/dairy#skim-milk",
  "milk": "/misc/dairy#skim-milk",
  "whole milk": "/misc/dairy#whole-milk",
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
  "anchovy": "/misc/fish#anchovy",
  "clam": "/misc/fish#clam",
  "cod": "/misc/fish#cod",
  "crab": "/misc/fish#crab",
  "cuttlefish": "/misc/fish#cuttlefish",
  "haddock": "/misc/fish#haddock",
  "halibut": "/misc/fish#halibut",
  "herring": "/misc/fish#herring",
  "lobster": "/misc/fish#lobster",
  "mackerel": "/misc/fish#mackerel",
  "mahi mahi": "/misc/fish#mahi-mahi",
  "mussels": "/misc/fish#mussel",
  "octopus": "/misc/fish#octopus",
  "oyster": "/misc/fish#oyster",
  "salmon": "/misc/fish#salmon",
  "sardine": "/misc/fish#sardine",
  "scallop": "/misc/fish#scallop",
  "shrimp": "/misc/fish#shrimp",
  "squid": "/misc/fish#squid",
  "tilapia": "/misc/fish#tilapia",
  "trout": "/misc/fish#trout",
  "tuna": "/misc/fish#tuna",

  # FRUIT
  "apple": "/misc/fruit#apple",
  "apricot": "/misc/fruit#apricot",
  "avocado": "/misc/fruit#avocado",
  "banana": "/misc/fruit#banana",
  "blackberry": "/misc/fruit#blackberry",
  "blueberry": "/misc/fruit#blueberries",
  "boysenberry": "/misc/fruit#boysenberry",
  "cantaloupe": "/misc/fruit#cantaloupe",
  "cherry": "/misc/fruit#cherry",
  "clementine": "/misc/fruit#clementine",
  "cranberry": "/misc/fruit#cranberry",
  "date": "/misc/fruit#dates",
  "dried fig": "/misc/fruit#fig-dried",
  "fig": "/misc/fruit#fig-dried",
  "fresh fig": "/misc/fruit#fig-fresh",
  "grape": "/misc/fruit#grapes",
  "grapefruit": "/misc/fruit#grapefruit",
  "guava": "/misc/fruit#guava",
  "honeydew": "/misc/fruit#honeydew",
  "kiwi": "/misc/fruit#kiwi",
  "lemon juice": "/misc/fruit#lemon-juice",
  "lemon": "/misc/fruit#lemon",
  "lime juice": "/misc/fruit#lime-juice",
  "lime": "/misc/fruit#lime",
  "mandarin": "/misc/fruit#mandarin",
  "mango": "/misc/fruit#mangos",
  "olive": "/misc/fruit#olives",
  "orange": "/misc/fruit#orange",
  "papaya": "/misc/fruit#papaya",
  "passion fruit": "/misc/fruit#passion-fruit",
  "peach": "/misc/fruit#peach",
  "pear": "/misc/fruit#pear",
  "persimmon": "/misc/fruit#persimmon",
  "pineapple": "/misc/fruit#pineapple",
  "plum": "/misc/fruit#plum",
  "pomegranate": "/misc/fruit#pomegranate",
  "prune": "/misc/fruit#prune",
  "raisin": "/misc/fruit#raisins",
  "raspberry": "/misc/fruit#raspberry",
  "starfruit": "/misc/fruit#starfruit",
  "strawberry": "/misc/fruit#strawberries",
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
  "quick oats": "/misc/grains#oats",
  "rolled oats": "/misc/grains#oats",
  "oat": "/misc/grains#oats",
  "popcorn": "/misc/grains#popcorn",
  "quinoa": "/misc/grains#quinoa",
  "rye": "/misc/grains#rye",
  "spelt": "/misc/grains#spelt",
  "vital wheat gluten": "/misc/grains#vital-wheat-gluten",
  "white flour": "/misc/grains#white-wheat",
  "all purpose flour": "/misc/grains#white-wheat",
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
  "chicken": "/misc/meat#chicken-breast",
  "chicken liver": "/misc/meat#chicken-liver",
  "chicken thighs": "/misc/meat#chicken-thighs",
  "egg": "/misc/meat#eggs",
  "egg white": "/misc/meat#egg-whites",
  "ground beef": "/misc/meat#ground-beef",
  "ground turkey": "/misc/meat#ground-turkey",
  "ham": "/misc/meat#ham",
  "hot dogs": "/misc/meat#hot-dogs",
  "lamb": "/misc/meat#lamb",
  "pepperoni": "/misc/meat#pepperoni",
  "pork liver": "/misc/meat#pork-liver",
  "pork tenderloin": "/misc/meat#pork-tenderloin",
  "salami": "/misc/meat#salami",
  "sausage": "/misc/meat#sausage",
  "spam": "/misc/meat#spam",
  "steak": "/misc/meat#steak",
  "turkey breast": "/misc/meat#turkey-breast",
  "veal": "/misc/meat#veal",
  "venison": "/misc/meat#venison",

  # NUTS
  "almond": "/misc/nuts#almonds",
  "brazil nut": "/misc/nuts#brazil-nuts",
  "cashew": "/misc/nuts#cashews",
  "chestnut": "/misc/nuts#chestnuts",
  "coconut flakes": "/misc/nuts#coconut",
  "coconut flour": "/misc/nuts#coconut",
  "coconut": "/misc/nuts#coconut",
  "hazelnut": "/misc/nuts#hazelnuts",
  "macadamia nut": "/misc/nuts#macadamia-nuts",
  "peanut": "/misc/nuts#peanuts",
  "pecan": "/misc/nuts#pecans",
  "pine nut": "/misc/nuts#pine-nuts",
  "pistachio": "/misc/nuts#pistachios",
  "walnut": "/misc/nuts#walnuts",

  # SEEDS
  "chia seed": "/misc/seeds#chia-seeds",
  "chia": "/misc/seeds#chia-seeds",
  "flax seed": "/misc/seeds#flax-seeds",
  "flax": "/misc/seeds#flax-seeds",
  "hemp seed": "/misc/seeds#hemp-seeds",
  "hemp": "/misc/seeds#hemp-seeds",
  "poppy seed": "/misc/seeds#poppy-seeds",
  "poppy": "/misc/seeds#poppy-seeds",
  "pumpkin seed": "/misc/seeds#pumpkin-seeds",
  "sesame seed": "/misc/seeds#sesame-seeds",
  "tahini": "/misc/seeds#sesame-seeds",
  "sunflower seed": "/misc/seeds#sunflower-seeds",
  "sunflower": "/misc/seeds#sunflower-seeds",

  # VEGGIES
  "acorn squash": "/misc/veggies#acorn-squash",
  "artichoke": "/misc/veggies#artichoke",
  "arugula": "/misc/veggies#arugula",
  "asparagus": "/misc/veggies#asparagus",
  "beet": "/misc/veggies#beets",
  "beet green": "/misc/veggies#beet-greens",
  "bell pepper": "/misc/veggies#pepper",
  "bok choy": "/misc/veggies#bok-choy",
  "broccoli": "/misc/veggies#broccoli",
  "brussel sprout": "/misc/veggies#brussel-sprout",
  "butternut squash": "/misc/veggies#butternut-squash",
  "cabbage": "/misc/veggies#cabbage",
  "carrot": "/misc/veggies#carrots",
  "cauliflower": "/misc/veggies#cauliflower",
  "celery": "/misc/veggies#celery",
  "collard green": "/misc/veggies#collard-green",
  "cucumber": "/misc/veggies#cucumber",
  "eggplant": "/misc/veggies#eggplant",
  "fennel": "/misc/veggies#fennel",
  "garlic": "/misc/veggies#garlic",
  "ginger": "/misc/veggies#ginger",
  "green bean": "/misc/veggies#green-bean",
  "kale": "/misc/veggies#kale",
  "kohlrabi": "/misc/veggies#kohlrabi",
  "lettuce": "/misc/veggies#lettuce",
  "mustard green": "/misc/veggies#mustard-greens",
  "onion": "/misc/veggies#onion",
  "parsnip": "/misc/veggies#parsnips",
  "pea": "/misc/veggies#pea",
  "plantain": "/misc/veggies#plantain",
  "potato": "/misc/veggies#potato",
  "pumpkin": "/misc/veggies#pumpkin",
  "radicchio": "/misc/veggies#radicchio",
  "radish": "/misc/veggies#radish",
  "spaghetti squash": "/misc/veggies#spaghetti-squash",
  "spinach": "/misc/veggies#spinach-fresh",
  "sweet potato": "/misc/veggies#sweet-potato",
  "swiss chard": "/misc/veggies#swiss-chard",
  "tomato": "/misc/veggies#tomato",
  "turnip": "/misc/veggies#turnip",
  "white mushroom": "/misc/veggies#mushrooms",
  "mushroom": "/misc/veggies#mushrooms",
  "yellow squash": "/misc/veggies#yellow-squash",
  "zucchini": "/misc/veggies#zucchini",

  # NUTRIENTS (ABC)
  "vitamin a": "/misc/nutrient-alphabet#A",
  "beta carotene": "/misc/nutrient-alphabet#A",
  "beta-carotene": "/misc/nutrient-alphabet#A",
  "vitamin b6": "/misc/nutrient-alphabet#B",
  "pyroxidine": "/misc/nutrient-alphabet#B",
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
  "sugar": "/misc/hidden-sugar",
  "carbohydrate": "/misc/carbs",
  "carb": "/misc/carbs",
  "healthy fats": "/misc/fats",
  "fat": "/misc/fats",
  "protein": "/misc/protein",
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
  "processed food": "/misc/processed-foods",
  "ultra processed": "/misc/processed-foods",
  "ultra-processed": "/misc/processed-foods",
  "apple cider vinegar": "/misc/apple-cider-vinegar",
  "acv": "/misc/apple-cider-vinegar",
  "prebiotic": "/misc/biotics",
  "probiotic": "/misc/biotics",
  "postbiotic": "/misc/biotics",

  # RECIPE CATEGORIES
  "bean": "/recipes/beans",
  "dairy": "/recipes/dairy",
  "fish": "/recipes/fish",
  "seafood": "/recipes/fish",
  "fruit": "/recipes/fruit",
  "grain": "/recipes/grains",
  "meat": "/recipes/meat",
  "nut": "/recipes/nuts",
  "seed": "/recipes/seeds",
  "vegetable": "/recipes/veggies",
  "veggie": "/recipes/veggies",

  # FOOD SECTIONS
  "hummus": "/hummus",
  "oatmeal": "/oatmeal",
  "overnight oats": "/oatmeal",
  "yogurt": "/yogurt",
  "natural nut butter": "/nut-butter",
  "nut butter": "/nut-butter",
  "pesto": "/pesto",
  "soup": "/soup-stew",
  "stew": "/soup-stew",
  "chilli": "/chilli",
  "salad": "/salad",
  "salad dressing": "/dressing",
  "dressing": "/dressing",
  "brownie": "/brownie",
  "cookie": "/cookie",
  "copycat": "/copycat",

  # RECIPE TYPES
  "bread": "/recipes/bread",
  "breakfast": "/recipes/breakfast",
  "drink": "/recipes/drink",
  "finger food": "/recipes/finger-food",
  "ground meat": "/recipes/ground-meat",
  "healthier dessert": "/recipes/healthier-dessert",
  "dessert": "/recipes/healthier-dessert",
  "meatless": "/recipes/meatless",
  "meme recipe": "/recipes/meme",
  "meme": "/recipes/meme",
  "protein powder": "/recipes/protein-powder",
  "savory sauce": "/recipes/savory-sauces",
  "side": "/recipes/sides",
  "sweet spread": "/recipes/sweet-spreads"
}

def normalize(text):
    return text.replace("\r\n", "\n").strip() + "\n"

def auto_link_safe(text, links):
    """
    Auto-link exact words/phrases in text while skipping existing <a> tags.
    No pluralization, only exact matches.
    """
    sorted_keys = sorted(links.keys(), key=len, reverse=True)
    segments = re.split(r'(<a\s+[^>]*>.*?</a>)', text, flags=re.IGNORECASE | re.DOTALL)

    for i, seg in enumerate(segments):
        if seg.lower().startswith("<a"):
            continue

        for key in sorted_keys:
            url = links[key]
            pattern = re.compile(rf"\b{re.escape(key)}\b", re.IGNORECASE)
            seg = pattern.sub(lambda m: f"<a href='{url}'>{m.group(0)}</a>", seg)

        segments[i] = seg

    return "".join(segments)

def protect_blocks(text, pattern, token, flags=0):
    protected = []

    def replacer(match):
        protected.append(match.group(0))
        return f"__{token}_{len(protected)-1}__"

    text = re.sub(pattern, replacer, text, flags=flags)
    return text, protected

def restore_blocks(text, protected, token):
    for i, block in enumerate(protected):
        text = text.replace(f"__{token}_{i}__", block)
    return text

def process_front_matter(front_matter):
    lines = front_matter.splitlines()
    output = []

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith("Description:"):
            key, value = line.split(":", 1)
            linked = auto_link_safe(value, LINKS)
            output.append(f"{key}:{linked}")
            i += 1
            continue

        if line.startswith("Instructions:"):
            output.append(line)
            i += 1
            while i < len(lines) and lines[i].lstrip().startswith("-"):
                output.append(auto_link_safe(lines[i], LINKS))
                i += 1
            continue

        output.append(line)
        i += 1

    return "\n".join(output) + "\n"

def split_front_matter(text):
    if text.startswith("---"):
        delim_indices = [m.start() for m in re.finditer(r'^---\s*$', text, re.MULTILINE)]
        if len(delim_indices) >= 2:
            start = delim_indices[0] + 4
            end = delim_indices[1]
            front_matter = text[:end].rstrip("\n") + "\n"
            body = text[end + 4:]
            return front_matter, body
    return "", text

def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    front_matter, body = split_front_matter(content)

    if front_matter:
        fm_body_text = front_matter.strip("-\n")
        fm_body_text = process_front_matter(fm_body_text)
        front_matter = "---\n" + fm_body_text.strip("\n") + "\n---\n"

    body, code_blocks = protect_blocks(body, r"```[\s\S]*?```", "CODE")
    body, inline_code = protect_blocks(body, r"`[^`]*`", "INLINE")
    body, quotes = protect_blocks(body, r"(['\"])(?:\\.|(?!\1).)*\1", "QUOTE")
    body, bullets = protect_blocks(body, r"(?m)^(?:\s*(?:[-*+]|[0-9]+\.)\s+.*$)", "BULLET", flags=re.MULTILINE)

    body = auto_link_safe(body, LINKS)

    body = restore_blocks(body, bullets, "BULLET")
    body = restore_blocks(body, quotes, "QUOTE")
    body = restore_blocks(body, inline_code, "INLINE")
    body = restore_blocks(body, code_blocks, "CODE")

    new_content = front_matter + body

    if normalize(new_content) != normalize(content):
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated: {path}")

os.system('cls')
for root, _, files in os.walk(POSTS_DIR):
    for file in files:
        if file.endswith((".md", ".html", ".markdown")):
            process_file(os.path.join(root, file))
