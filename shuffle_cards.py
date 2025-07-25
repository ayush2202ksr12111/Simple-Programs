#We will try to write a program that will help us shuffle deck of cards
# there are 4 group of cards and each group has 13 pair
# for this we are going to use random function this will help us pick the card from random number of list
import random

def shuffle_cards():
    # we have defined two simple that will use the randint function to print the value and check whether it will be able to print it or not
    card_g = random.randint(1,4)
    card_v= random.randint(1,13)
    if card_g == 1:
        return f"Spade of {card_v}"
    elif card_g == 2:
        return f"Heart of {card_v}"
    elif card_g == 3:
        return f"Club of {card_v}"
    elif card_g==4:
        return f"Diamond of {card_v}"
    return f"Something broke"
    
        

print(shuffle_cards())
