import re
import sys

def main():
    HTML = input("HTML: ")
    print(parse(HTML))

def parse(s):
    matches = re.search(r'"https:??(www\.)?youtube\.com/embed(\w+)"')
    if not matches:
        return None
    
    return "https://youtu.be/" + matches.group(2)

main()