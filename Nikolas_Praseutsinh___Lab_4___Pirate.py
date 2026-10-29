
"""
Nikolas Praseutsinh
Python Programming 2026
Due: October 29, 2026
Lab 4: Translate sentences to pirate
"""
def toPirate(sentence):
    # Dictionary for english words and pirate words
    words = {
        "Hello": "Avast",
        "Excuse": "Arrr",
        "sir": "matey",
        "boy": "matey",
        "man": "matey",
        "madam": "proud beauty",
        "woman": "proud beauty",
        "officer": "foul blaggart",
        "the": "th'",
        "my": "me",
        "your": "yer",
        "is": "be",
        "are": "be",
        "kitchen": "galley",
        "hotel": "fleabag inn"
    }

    # Empty strings to store the words
    newsentence = ""
    word = ""

    # Goes through each character in the sentence
    for char in sentence:
        # Checks if there is a space
        if char == " ":
            # Checks if the word is in the dictionary
            if word in words:
                word = words[word]

            # Adds the word to the new sentence
            newsentence += word + " "
            word = ""
        else:
            # Adds the character together
            word += char

    # Checks the last word
    if word in words:
        word = words[word]

    newsentence += word

    return newsentence


sentence = "Hello excuse me sir"
print(toPirate(sentence))