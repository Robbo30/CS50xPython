def makingFaces():
    input1 = input("Enter a sentence with a sad face or happy face: ")
    print(input1.replace(":)", "🙂").replace(":(", "🙁"))

makingFaces()