import random

done = False

deck = ["Pirates", "Trickster", "Robots", "Dinosaurs",
 "Ninjas", "Aliens", "Wizards", "Zombies"]

round_one_decks = []
round_two_decks = []
player_names = []

def get_num_players():
    get_player = input("How many Players? ")
    return int(get_player)

players = get_num_players()

print(players)

