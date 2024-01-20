import re

#replace - replaces the first string in the brackets with the second
#removeprefix - removes the entered string 

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))



