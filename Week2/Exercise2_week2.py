# Counting a letter apparance frequency in a word
import math
word = ' '
character_dict = {}


def count_char(word):
    # Add each character of word into character_dict and if it (the key) appears more than 1, value + 1
    for character in word: 
        if (character in character_dict):
            character_dict[character] = character_dict[character] + 1
        else:
            character_dict[character] = 1
    return character_dict
    

if __name__ == "__main__":
    word_ex = "Happiness"
    print(count_char(word_ex))
