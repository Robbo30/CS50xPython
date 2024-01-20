camel = input("camelCase: ")

for i in range(len(camel)):
    if camel[i].isupper():
        camel = camel[:i] + "_"+camel[i].lower() + camel[i+1:]

print(f"snake_case: {camel}")




