import random

adjectives = list()
nouns = list()
verbs = list()
verb_ing = list()
integers = list()
# Article of clothing
article_of_clothing = ""

#
# FUNCTIONS TO DRAW RANDOM WORDS FROM EACH LIST
#
def random_adj():
    item = random.choice(adjectives)
    adjectives.remove(item)
    return item

def random_noun():
    item = random.choice(nouns)
    nouns.remove(item)
    return item

def random_verb():
    item = random.choice(verbs)
    verbs.remove(item)
    return item

def random_verb_ing():
    return random.choice(verb_ing).capitalize()

def random_int():
    item = random.choice(integers)
    integers.remove(item)
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
# TEST
def test():
    list_all_items(adjectives)
    list_all_items(nouns)
    list_all_items(verbs)
    list_all_items(integers)
    print(article_of_clothing)

    list_all_items(adjectives)
    list_all_items(verbs)

    print('\n')

    print_story()

    print('\n')

    list_all_items(adjectives)
    print('\n')
    list_all_items(verbs)

def print_story():
    print("Mondays are always {}. I {} my alarm {} times until I am officially late. I {} out of bed, {} on clothes, {} my teeth, and was out of the dorm building in {} minutes. {} down the hills of San Francisco, I found myself completely out of breath. I run inside Make School and take off my {}, exposing mismatched socks. I curse the Gods for a second and focus my attention on getting to my Huddle before it ends. I {} up the steps, not forgetting to trip a couple times, and dart for the Great Hall. Before getting there, though, I realize the {} is pretty empty. & now that I think about it, I didn’t see any other shoes down in the {}. I get into the Great Hall and no one is there. I look at my calendar and {} myself. It’s Labor Day.".format(random_adj(), random_verb(), random_int(), random_verb(), random_verb(), random_verb(), random_int(), random_verb_ing(), article_of_clothing, random_verb(), random_noun(), random_noun(), random_verb()))

#
# GET INPUT AND STORE IN EACH LIST
#
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

#test()
print_story()
