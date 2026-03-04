import os
import importlib
import sys


def main() -> None:
    root = os.getcwd()
    if root not in sys.path:
        sys.path.insert(0, root)

    recipe_links_mod = importlib.import_module("python.testing.recipeLinks")
    links_module = importlib.import_module("python.links")

    RECIPE_LINKS = getattr(recipe_links_mod, "RECIPE_LINKS", {})
    links = getattr(links_module, "LINKS", {})

    existing_recipe_urls = {url for url in links.keys() if isinstance(url, str) and url.startswith("/recipes/")}

    new_items: dict[str, list[str]] = {}
    for url, titles in RECIPE_LINKS.items():
        if not isinstance(url, str) or not url.startswith("/recipes/"):
            continue
        if url in existing_recipe_urls:
            continue
        new_items[url] = titles

    out_dir = os.path.join(root, "python", "testing")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "new_recipe_links_for_links_py.txt")

    with open(out_path, "w", encoding="utf-8", errors="ignore") as f:
        for url in sorted(new_items):
            titles = new_items[url]
            title = titles[0] if titles else ""
            # Simple title escaping for quotes
            title = title.replace("\\", "\\\\").replace('"', '\\"')

            f.write(f'    "{url}": [\n')
            f.write(f'        "{title}",\n')
            f.write("    ],\n")


if __name__ == "__main__":
    main()

