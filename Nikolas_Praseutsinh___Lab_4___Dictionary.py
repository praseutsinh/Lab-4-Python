"""
Nikolas Praseutsinh
Python Programming 2026
Due: October 29, 2026
Lab 4: Dictionary
"""

names = ["Joe", "Tom", "Barb", "Sue", "Sally"]
scores = [10, 23, 13, 18, 12]

#Create a dictionary from two lists
def makeDictionary(names, scores):
    dictionary = {}

    for i in range(len(names)):
        dictionary[names[i]] = scores[i]

    return dictionary

#Function to calculate the average for dictionary
def averageScore(scoreDict):
    total = 0

    for name in scoreDict:
        total += scoreDict[name]

    return total / len(scoreDict)


#Assign the dictionary to scoreDict
dictionary = makeDictionary(names, scores)

#Print the dictionary
print(dictionary)

#Print Barb's score
print(dictionary["Barb"])

#Add John with a score of 19
dictionary["John"] = 19
print(dictionary)

#Create a sorted list of scores
sortedScores = sorted(dictionary.values())
print(sortedScores)

#Calculate and print the average
print(averageScore(dictionary))

#Update Sally's score to 13
dictionary["Sally"] = 13
print(dictionary)

#Delete Tom from the dictionary
del dictionary["Tom"]
print(dictionary)
