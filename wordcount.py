"""Count words in file."""

"""
Problem Description
Write a program, wordcount.py, that opens a file and counts how many times each space-separated word occurs in that file. 
Your program should then output each word and the number of times it appears in the file.

For example, the file test.txt (which we’ve included in your starter code):

test.txt
As I was going to St. Ives
I met a man with seven wives
Every wife had seven sacks
Every sack had seven cats
Every cat had seven kits
Kits, cats, sacks, wives.
How many were going to St. Ives?
...should produce the output below:

"""

# loop through the file and sethe words using .split(' ') to target the spaces 
seperated_words_dictionary = {} # defined a dictionary
count = 0
def word_count(filename): # created a function that reads the word_count in filename
    for line in open(filename): # loops through filename
        seperate_words = line.rstrip().replace(",","").replace(".","").replace("?","").replace("-","").split(' ')#assigns split words into a variable
        for word in seperate_words:
            # seperated_words_dictionary.get(word, 0)
            # if(word in seperated_words_dictionary):
            #     count+=1
            word = word.lower()
            seperated_words_dictionary[word] = seperated_words_dictionary.get(word, 0) + 1

    for word, count in seperated_words_dictionary.items():
        print(word, count)
    
word_count('test.txt')
# put your code here.
