import os
import json


def collect_recipe_links(posts_root: str) -> dict[str, list[str]]:
    recipes_dir = os.path.join(posts_root, "_posts", "recipes")
    links: dict[str, list[str]] = {}

    for dirpath, _, filenames in os.walk(recipes_dir):
        for fname in filenames:
            if not fname.endswith((".md", ".markdown", ".html")):
                continue

            path = os.path.join(dirpath, fname)
            with open(path, encoding="utf-8") as f:
                in_front_matter = False
                delims = 0
                title = None
                permalink = None

                for line in f:
                    if line.strip() == "---":
                        delims += 1
                        if delims == 2:
                            break
                        in_front_matter = True
                        continue

                    if not in_front_matter:
                        continue

                    ls = line.lstrip()

                    if ls.startswith("title:") and title is None:
                        val = ls.split(":", 1)[1].strip()
                        val = val.strip().strip("'").strip('"')
                        title = val
                    elif ls.startswith("permalink:") and permalink is None:
                        val = ls.split(":", 1)[1].strip()
                        permalink = val

                if permalink and title:
                    links[permalink] = [title]

    return links


def write_recipe_links_file(posts_root: str, out_path: str) -> None:
    links = collect_recipe_links(posts_root)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("RECIPE_LINKS = {\n")
        for permalink in sorted(links):
            title = links[permalink][0]
            permalink_literal = json.dumps(permalink)
            title_literal = json.dumps(title)

            f.write(f"    {permalink_literal}: [\n")
            f.write(f"        {title_literal},\n")
            f.write("    ],\n")

        f.write("}\n")


def main() -> None:
    root = os.getcwd()
    out_dir = os.path.join(root, "python", "testing")
    os.makedirs(out_dir, exist_ok=True)

    out_path = os.path.join(out_dir, "recipeLinks.py")
    write_recipe_links_file(root, out_path)


if __name__ == "__main__":
    main()

