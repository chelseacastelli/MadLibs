import random
from colorama import Fore, Back, Style
import textwrap

adjectives = list()
nouns = list()
verbs = list()
verb_ing = list()
integers = list()
# Article of clothing
article_of_clothing = ""
story = ""

#
# FUNCTIONS TO DRAW RANDOM WORDS FROM EACH LIST
#
def random_adj():
    item = random.choice(adjectives)
    adjectives.remove(item)
    item = color_text(item)
    return item

def random_noun():
    item = random.choice(nouns)
    nouns.remove(item)
    item = color_text(item)
    return item

def random_verb():
    item = random.choice(verbs)
    verbs.remove(item)
    item = color_text(item)
    return item

def random_verb_ing():
    # This word starts a sentence so I'm capitalizing the first letter
    item = random.choice(verb_ing).capitalize()
    item = color_text(item)
    return item

def random_int():
    item = random.choice(integers)
    integers.remove(item)
    item = color_text(item)
    return item

# GET WORDS FROM USER
def user_input(prompt):
    user_input = input(prompt)
    return user_input

def list_all_items(list):
    print('\n')
    # Output for empty list
    index = 0
    for item in list:
        print("{} {}".format(index, item))
        index += 1

def color_text(word):
    return Fore.MAGENTA + word + Style.RESET_ALL

# GET INPUT AND STORE IN EACH LIST
def store_words():
    for i in range(1, 5):
        adj = user_input("Input adjective: ")
        adjectives.append(adj)

    for i in range(1, 7):
        verb = user_input("Input verb: ")
        verbs.append(verb)

    for i in range(1, 3):
        noun = user_input("Input noun: ")
        nouns.append(noun)

    for i in range(1, 3):
        int = user_input("Input integer: ")
        integers.append(int)

    for i in range(1, 3):
        verb = user_input("Input a verb ending with 'ing': ")
        verb_ing.append(verb)

    article_of_clothing = user_input("Input article of clothing: ")

    return "Mondays are always " + random_adj() + ". I " + random_verb() + " my alarm " + random_int() + " times until I am officially late. I " + random_verb() + " out of bed, " + random_verb() + " on clothes, " + random_verb() + " my teeth, and was out of the dorm building in " + random_int() + " minutes. " + random_verb_ing() + " down the hills of San Francisco, I found myself completely out of breath. I run inside Make School and take off my " + color_text(article_of_clothing) + ", exposing mismatched socks. I curse the Gods for a second and focus my attention on getting to my huddle before it ends. I " + random_verb() + " up the steps, not forgetting to trip a couple times, and dart for the Great Hall. Before getting there, though, I realize the " + random_noun() + " is pretty empty. & now that I think about it, I didn’t see any other shoes down in the " + random_noun() + ". I get into the Great Hall and no one is there. I " + random_verb() + " at my calendar and face-palm myself. It’s Labor Day."

def print_story():
    print('\n')
    print(textwrap.fill(story, 53))
    print('\n')

# TEST
def test():
    list_all_items(adjectives)
    list_all_items(nouns)
    list_all_items(verbs)
    list_all_items(integers)
    print(article_of_clothing)

    print('\n')
    print_story()

#test()
story = store_words()
print_story()
