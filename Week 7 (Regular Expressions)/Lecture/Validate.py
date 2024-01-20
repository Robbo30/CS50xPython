import re
# . = any character except a newline
# * = 0 or more repetitions
# + = 1 or more repetitions
# ? = 0 or 1 repetition
# {m} m repetitions
# {m, n} m-n repetitions
# ^ = matches the start of the string
# $ = mathces the end of the string or just before the newline at the end of the string
# [] = set of characters
# [^] = complementing the set
# \w = any word character
# \W = not a word character
# \s = blank space or space input

email = input("Email: ").strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
    










