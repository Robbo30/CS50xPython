from validator_collection import checkers

email = input("Email: ")
validEmail = checkers.is_email(email)
if validEmail:
    print("Valid")
else:
    print("Invalid")