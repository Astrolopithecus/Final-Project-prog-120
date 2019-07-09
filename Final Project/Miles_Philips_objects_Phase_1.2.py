# Miles Philips
# Prog 120
# Final ProjectProject Phase 1.2
# objects
# 5-31-19

#!/usr/bin/env python3
import random
CARDS_CHARACTERS = {"Spades": "♠", "Hearts": "♥", "Diamonds": "♦", "Clubs": "♣"}

##########################################################################
## Definitions for the classes: Card, Deck and Hand
##########################################################################

#create Card class
class Card:

    # initialize
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit =suit

    # define value property
    @property
    def value(self):
        if self.__rank == "Ace":
            v = 11
        elif self.__rank in ("Jack", "Queen", "King"):
            v = 10
        else:
            v = int(self.__rank)
        return v

    # define displayCard module 
    def displayCard(self):
        card = str(self.__rank) + " of " + str(self.__suit) + CARDS_CHARACTERS[self.__suit]
        return card
        
#create Deck class
class Deck:
    
    # initialize a deck of 52 cards
    def __init__(self):
        self.__deck = []
        suits = ["Hearts", "Spades", "Diamonds", "Clubs"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for s in suits:
            for r in ranks:
                c = Card(r,s)
                self.__deck.append(c) 

    # define count property   
    @property
    def count(self):    
        self.__count = len(self.__deck)
        return self.__count

    # define shuffle property
    def shuffle(self):
        random.shuffle(self.__deck)

    # define dealCard property
    def dealCard(self):
        return self.__deck.pop()
    
# create Hand class
class Hand:
    
    # initialize 
    def __init__(self):
        self.__cards = []

    # define count property
    @property
    def count(self):    
        count = len(self.__cards)
        return count

    # define points property
    @property
    def points(self):
        points = 0
        for c in self.__cards:
            points += c.value
        return points
    
    # define addCard method
    def addCard(self,card):
        self.__cards.append(card)
        return self.__cards
        
    # define displayHand method
    def displayHand(self):
        for h in self.__cards:
            h.displayCard()

# define main function        
def main():
    print("Cards - Tester")
    print()

    # test deck
    print("DECK")
    deck = Deck()
    print("Deck created.")
    deck.shuffle()    
    print("Deck shuffled.")
    print("Deck count:", deck.count)
    print()

    # test hand
    print("HAND")
    hand = Hand()
    for i in range(4):
        hand.addCard(deck.dealCard())
    hand.displayHand()
    print()

    print("Hand points:", hand.points)
    print("Hand count:", hand.count)
    print("Deck count:", deck.count)

if __name__ == "__main__":
    main()
