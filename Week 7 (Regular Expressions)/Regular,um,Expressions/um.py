import re
import sys

def main():
    text = input("Text: ")
    print(count(text))

def count(s):
    phrases = re.findall(r"\b(um)\b", s, re.IGNORECASE)
    return len(phrases)

main()