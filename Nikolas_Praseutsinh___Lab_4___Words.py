"""
Nikolas Praseutsinh
Python Programming 2026
Due: October 29, 2026
Lab 4: output the number of words in the sentence.
"""

def numWords(text):
    count = 0

    for char in text:
        if char == " ":
            count += 1

    return count + 1

number = input("Enter a string: ")
print("Words:", numWords(number))