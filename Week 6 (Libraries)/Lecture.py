import random #Random library
import statistics #Statistics library
import sys #Sys library - allows us to use the user inputs on the command line
#import requests

coin = random.choice(["Heads", "Tails"]) #randomly chooses one of the arguements inputted
print("Coinflip:",coin)


randomNum = random.randint(1,10) #randomly chooses a number between 1-10
print("1-10:",randomNum)


cards = ["Ace", "Jack", "Hearts", "Queen"] #shuffles the list randomly
random.shuffle(cards)
for i in cards[1:]: #Slices to only print the 2-4th item in the list
    print(i)


print("Average:",statistics.mean([100,90]))#finds the average of 100 and 90


#print("Hello, my name is", sys.argv[1]) #prints the first thing typed into the command line 


#artist = input("Artist Name: ")

#response = requests.get("https://itunes.apple.come/search?entity=song&limit=1%term=" + artist)
#x = response.json()
#for result in x["results"]:
#    print(result["trackname"]())










