from html.parser import HTMLParser
import os

class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        self.text.append(data)

    def get_text(self):
        return ''.join(self.text)

def remove_html_tags(html):
    stripper = HTMLStripper()
    stripper.feed(html)
    return stripper.get_text()

os.system('cls')

print("Paste text with HTML tags (press Enter twice to finish):")

lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

input_text = "\n".join(lines)

print("\nCleaned text:\n")
print(remove_html_tags(input_text))
