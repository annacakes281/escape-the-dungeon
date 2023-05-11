import random


def rules():
    """
    Rules for the game that will appear at the start so players know the goal
    """
    print("This is a text-based game, type your answers into the terminal\n\n")
    print("The goal is to defeat the Master boss in the boss room.")
    print("Collect all 6 items and all 4 keys to get to the Master Boss!\n")

    return rules


intro = rules()


playing = input("Would you like to try to Escape the dungeon (yes/no)\n")
if playing.lower() != "yes":
    quit()

player_hp = 150
player_stamnia = 50

# weapon_options = ["sword", "bow and arrow"]
# master_weapon_option = ["master sword", "master bow and arrow"]
master_armour = 100

hp_potion_one = 0.25
hp_potion_two = 0.50
hp_potion_three = 0.75

mini_boss_one_hp = 50
mini_boss_one_sp = 15

mini_boss_two_hp = 100
mini_boss_two_sp = 25

master_boss_hp = 250
master_boss_sp = 100

name = input("Type your name:\n")

print(f"Welcome {name} to the Escape the Dungeon Game. Good luck!\n")
print("You have found yourself in a dungeon and must find the way out")
print(f"You start with {player_hp}hp and {player_stamnia}sp.\n")

starting_room = input(
    "You are an empty room with nothing but dim lighting to show the way.\n"
    "You can either go North, South or East.\n"
    "Which way do you go? (north/south/east) \n").lower()

if starting_room == "north":
    room_one = input(
        "You enter the room to the North and see two weapons on the ground.\n"
        "You must decide which weapon you would like to go with.\n"
        "There is a sword on one pedestal.\n"
        "On the other pedestal there is a bow and a quiver full of arrows.\n"
        "Which do you choose? (sword/bow) \n").lower()

if starting_room == "south":
    room_two = input(
        "You enter the room to the South and come across a small lake.\n"
        "You can see some unstable looking pedestals across the lake.\n"
        "You can either swim throuhg the lake or jump across.\n"
        "Which do you choose? (swim/jump) \n").lower()

if starting_room == "east":
    room_five = input(
        "You go to the room to the East.\n"
        "You can either go back to the previous room or go North.\n"
        "Which way do you go? (north/west) \n").lower()
    
    