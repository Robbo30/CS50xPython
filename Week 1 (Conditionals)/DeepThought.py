list = ["42","fourty-two","fourty two"] 

answer = input("What is the answer to the Greate Question of Life, the Universe, and Everything? ")

if answer.lower() in list:
    print("Yes")
else:
    print("No")