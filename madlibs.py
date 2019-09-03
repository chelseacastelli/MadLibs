import random

#4
adjectives = list()
#2
nouns = list()
#4
verbs = list()
#2
integers = list()
#1
other = list()

def random_adj():
    random.choice(adjectives)

def random

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

def test():
    list_all_items(adjectives)
    list_all_items(nouns)
    list_all_items(verbs)
    list_all_items(integers)
    list_all_items(other)

def print_story():
    print("Mondays are always {}. I {} my alarm (integer) times until I was officially late. I (adjective) out of bed, (adjective) on clothes, (adjective) my teeth, and was out of the dorm building in (integer) minutes. (Verb(ing)) down the hills of San Francisco, I found myself completely out of breath. I run inside Make School and take off my (article of clothing), exposing mismatched socks. I curse the Gods for a second and focus my attention back to getting to my Huddle before it ends. I (verb) up the steps, not forgetting to trip a couple times, and dart for the Great Hall. Before getting there, though, I realize the (noun) is pretty empty. & now that I think about it, I didn’t see any other shoes down in the (noun). I get into the Great Hall and no one is there. I look at my calendar and (verb) myself. It’s Labor Day.".format(random_adj(adjectives), random_verb(verb)))

for i in range(1, 5):
    adj = user_input("Input adjective: ")
    adjectives.append(adj)

for i in range(1, 5):
    verb = user_input("Input verb: ")
    verbs.append(verb)

for i in range(1, 3):
    noun = user_input("Input noun: ")
    nouns.append(noun)

for i in range(1, 3):
    int = user_input("Input integer: ")
    integers.append(int)

clothing = user_input("Input article of clothing: ")
other.append(clothing)

test()
