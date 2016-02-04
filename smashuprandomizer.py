#######################################################################
# This is still under devolopment and will change often as I learn    #
# more about Python.                                                  #
#                                                                     #
# Smash Up Game Random Deck Selector.                                 #
#######################################################################

import random

done = False #variable to control loop future feature.

#List of available decks to pulled from and they are removed from list in draft function.
deck = ["Pirates", "Tricksters", "Robots", "Dinosaurs",
 "Ninjas", "Aliens", "Wizards", "Zombies"]

class Player(): #adding this later as I learn more.
    def __init__(self):
        self.name = ""
        self.round_one_deck = ""
        self.round_two_deck = ""
        self.deck_messege = ""
        self.wins = 0
        

#list where decks can be stored after being drafted. A loop to check if deck
#has been drafted might be a better approach to this.

round_one_decks = []
round_two_decks = []

# list of stored player names.
player_names = []

#Get user input of how many players in game.
def num_players():
    get_num_player = input("How many Players? ")
    return int(get_num_player)

#Get user input of player names.
def get_names():
    for i in range(0 , players):
        player_num = i + 1
        messege = "Name of Player %s? " % player_num
        get_name = input(messege)
        player_names.append(get_name)
        
#Draft decks and place them in list according to round drafted
def draft():
    for i in range(0, players):
        pulled_deck = random.choice(deck)
        round_one_decks.append(pulled_deck)
        deck.remove(pulled_deck)
    for j in range(0, players):
        pulled_deck = random.choice(deck)
        round_two_decks.append(pulled_deck)
        deck.remove(pulled_deck)

def return_decks(): #function to return decks pulled by rounds to the main deck.
    for i in range(0, players):
        pulled_deck = round_one_decks[0]
        deck.append(pulled_deck)
        round_one_decks.remove(pulled_deck)
    for i in range(0, players):
        pulled_deck = round_two_decks[0]
        deck.append(pulled_deck)
        round_two_decks.remove(pulled_deck)

def display_draft(): #funstion to diplay the draft results this will be cleaned up when I get player class working.
    if players == 4:
        print()
        print(player_names[0], " Drafts : ",round_one_decks[0], " & ", round_two_decks[3])
        print(player_names[1], " Drafts : ",round_one_decks[1], " & ", round_two_decks[2])
        print(player_names[2], " Drafts : ",round_one_decks[2], " & ", round_two_decks[1])
        print(player_names[3], " Drafts : ",round_one_decks[3], " & ", round_two_decks[0])
        print()
    elif players == 3:
        print()
        print(player_names[0], " Drafts : ",round_one_decks[0], " & ", round_two_decks[2])
        print(player_names[1], " Drafts : ",round_one_decks[1], " & ", round_two_decks[1])
        print(player_names[2], " Drafts : ",round_one_decks[2], " & ", round_two_decks[0])
        print()
    elif players == 2:
        print()
        print(player_names[0], " Drafts : ",round_one_decks[0], " & ", round_two_decks[1])
        print(player_names[1], " Drafts : ",round_one_decks[1], " & ", round_two_decks[0])
        print()
    else:
        print()
        print("You didn't select two, three or four players.")
        print()
        
players = num_players()
get_names()
draft()
display_draft()

################################################################
#this is just for checking working code and will be deleted.   #
################################################################
print("Print statments to check code will be deleted later.")
player_1 = Player()
player_1.name = player_names[0]
print(player_1.name)
print(players)
print(player_names)
print(round_one_decks)
print(round_two_decks)
return_decks()
print(deck)


