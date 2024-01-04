import emoji

emojiInp = str(input("Input: "))

emojiOut = emoji.emojize(emojiInp , language="alias")

print("Ouput:",emojiOut)