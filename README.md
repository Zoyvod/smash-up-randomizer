# smash-up-randomizer
import random

faction_decks = ["Wizards", "Pirates", "Zombies", "Aliens", "Tricksters", "Ninjas", "Dinosuars", "Robots"]
player_one_name = input("Enter name for Player 1: ")
player_two_name = input("Enter name for Player 2: ")


player_one_hand = []
player_two_hand = []

def random_draft():
    first_pick = random.choice(faction_decks)
    player_one_hand.append(first_pick)
    faction_decks.remove(first_pick)
    second_pick = random.choice(faction_decks)
    player_two_hand.append(second_pick)
    faction_decks.remove(second_pick)
    third_pick = random.choice(faction_decks)
    player_two_hand.append(third_pick)
    faction_decks.remove(third_pick)
    fourth_pick = random.choice(faction_decks)
    player_one_hand.append(fourth_pick)
    faction_decks.remove(fourth_pick)

random_draft()
print (" ")
print (player_one_name + " Drafts: " + player_one_hand[0] + " & " + player_one_hand[1])
print (" ")
print (player_two_name + " Drafts: " + player_two_hand[0] + " & " + player_two_hand[1])
print (" ")

who_won = input("Winner is ")
