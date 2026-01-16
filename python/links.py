import os
import re

POSTS_DIR = r"C:\Users\mets1\Documents\website\_posts\archive"

LINKS = {
    "nuts": "/misc/nuts",
    "fiber": "/misc/fiber",
    "iron": "/misc/iron",
}

# --------------------------------------------------

def split_front_matter(text):
    """Separates Jekyll front matter from body."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) == 3:
            return "---" + parts[1] + "---", parts[2]
    return "", text

def protect_code_blocks(text):
    """Temporarily remove code blocks and inline code."""
    protected = []

    def replacer(match):
        protected.append(match.group(0))
        return f"__CODE_BLOCK_{len(protected)-1}__"

    text = re.sub(r"```[\s\S]*?```", replacer, text)
    text = re.sub(r"`[^`]*`", replacer, text)

    return text, protected

def restore_code_blocks(text, protected):
    for i, block in enumerate(protected):
        text = text.replace(f"__CODE_BLOCK_{i}__", block)
    return text

def auto_link(text):
    for word, url in LINKS.items():
        pattern = re.compile(
            rf"(?<!<a[^>]*>)\b({re.escape(word)})\b(?![^<]*</a>)",
            re.IGNORECASE
        )

        text = pattern.sub(
            rf"<a href='{url}'>\1</a>",
            text
        )

    return text

def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    front_matter, body = split_front_matter(content)
    body, protected = protect_code_blocks(body)

    new_body = auto_link(body)

    new_body = restore_code_blocks(new_body, protected)

    if new_body != body:
        with open(path, "w", encoding="utf-8") as f:
            f.write(front_matter + new_body)
        print(f"Updated: {path}")

# --------------------------------------------------

for root, _, files in os.walk(POSTS_DIR):
    for file in files:
        if file.endswith((".md", ".html")):
            process_file(os.path.join(root, file))
