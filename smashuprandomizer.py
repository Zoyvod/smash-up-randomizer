import random

done = False #variable to control loop future feature.

#List of available decks to pulled from and they are removed from list in draft function.
deck = ["Pirates", "Tricksters", "Robots", "Dinosaurs",
 "Ninjas", "Aliens", "Wizards", "Zombies"]

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



players = num_players()
get_names()
draft()

#this is just for checking working code and will be deleted.
print("Code check print statments")
print(players)
print(player_names)
print(round_one_decks)
print(round_two_decks)


