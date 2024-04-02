# we import two modules: json and difflib. The json module allows us to work with JSON data, which is a common format for storing and transmitting data. The difflib module provides functions for finding differences between sequences, which we'll use to suggest similar words for misspelled inputs.

import json
import difflib

# In this part, we're loading the word definitions from the datadictionary.json file into a Python dictionary called dictionary. A dictionary is a data structure that stores key-value pairs, which is perfect for our word definitions (where the word is the key, and the definition is the value).
# The with open('datadictionary.json') as f: line opens the JSON file, and json.load(f) reads the contents of the file and converts it into a Python dictionary.
with open('datadictionary.json') as f:
    dictionary = json.load(f)
    
# This is a function called get_closest_word. It takes a word as input and tries to find the closest matching word in the dictionary.

def get_closest_word(word):
    # creates a list of all the words (keys) in the dictionary.dictionary is the name of the dictionary variable we're working with. In this case, it holds the word definitions loaded from the JSON file. .keys() is a method that belongs to dictionary objects in Python. Using dictionary.keys() is a convenient way to get all the keys in a dictionary without having to manually access each key one by one. It's a common operation when working with dictionaries in Python.
    word_list = dictionary.keys()
    
    # difflib.get_close_matches(word, word_list, n=1, cutoff=0.6) uses the difflib module to find the closest matching word in word_list to the input word. The n=1 parameter means it will return at most one match, and cutoff=0.6 means it will only consider matches that are at least 60% similar to the input word.
    closest_match = difflib.get_close_matches(word, word_list, n=1, cutoff=0.6)   #The difflib module provides classes and functions for comparing sequences, and get_close_matches is one of those functions. It's designed to find close matches between sequences, which can be useful for tasks like spelling correction, finding similar strings, or detecting typos.
    
    # If a close match is found, the function returns that match. Otherwise, it returns an empty string.
    if closest_match:
        return closest_match[0]
    else:
        return ""
    

#This is the main function, get_definition. It takes a word as input and returns its definition from the dictionary, or a relevant message if the word is not found or misspelled.

def get_definition(word):
    # converts the input word to lowercase for case-insensitive search.
    word = word.lower()
    
    # checks if the word exists in the dictionary. If it does, it returns the definition (dictionary[word]).
    if word in dictionary:
        return dictionary[word]
    else:
        # If the word is not found, it calls the get_closest_word function to find the closest matching word.
        closest_word = get_closest_word(word)
        if closest_word:
            suggestion = f"Did you mean '{closest_word}'? Its definition is: {dictionary[closest_word]}"
            return suggestion
        else:
            return f"Sorry, the word '{word}' is not found in the dictionary, and no close matches were found."
        #The f before the string tells Python that this is an f-string, and any expressions within curly braces {} will be evaluated and their values will be inserted into the string.
        

# This is the main program loop. It runs indefinitely, prompting the user to enter a word (or 'q' to quit)
while True:
    user_input = input("Enter a word (or 'q' to quit): ")   #prompts the user to enter a word and stores their input in user_input.
    if user_input.lower() == 'q':
        break              #checks if the user entered 'q' (case-insensitive). If they did, it breaks out of the loop, effectively quitting the program.
    definition = get_definition(user_input)   #If the user didn't enter 'q', it calls the get_definition function with the user's input and stores the result in definition.
    print(definition)   #prints the definition or the relevant message returned by the get_definition function.After printing the definition or message, the loop repeats, prompting the user for another word.