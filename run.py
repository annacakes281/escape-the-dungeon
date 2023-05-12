import random
import os

# Player health and stamina
player_hp = 150
player_stamina = 50

# Map dictionary
rooms = {
    "Starting Room": {"North": "Room 1", "South": "Room 2", "East": "Room 3"},
    "Room 1": {"South": "Starting Room", "Key": "Key 1", "Weapon Choice 1": "Sword", "Weapon Choice 2": "Bow", "Trap": "Fire"},
    "Room 2": {"North": "Starting Room", "East": "Room 3", "Item": "Potion", "Trap": "Lake"},
    "Room 3": {"West": "Room 2", "North": "Room 4", "East": "Secret Room", "Mini Boss": "Imp"},
    "Room 4": {"South": "Room 3", "Key": "Key 2", "NPC": "Fairy"},
    "Secret Room": {"West": "Room 3", "Item": "Armour", "Master Weapon 1": "Sword", "Master Weapon 2": "Bow"},
    "Room 5": {"West": "Starting Room", "North": "Room 6"},
    "Room 6": {"South": "Room 5", "East": "Room 7", "Item": "Potion", "Trap": "Jungle"},
    "Room 7": {"West": "Room 6", "East": "Room 9", "South": "Room 8", "Mini Boss": "Orc", "Item": "Stone"},
    "Room 8": {"North": "Room 7", "Item": "Secret Room Key"},
    "Room 9": {"West": "Room 7", "South": "Boss Room", "Item": "Potion", "Key": "Master Key"},
    "Boss Room": {"Boss": "Dragon"}
}

# List to keep track on invetory items
inventory = []
required_items = []

# Tracks the current room
current_room = "Starting Room"


def rules():
    """
    Rules for the game that will appear at the start so players know the goal
    """
    print("This is a text-based game, type your answers into the terminal\n\n")
    print("The goal is to defeat the Master boss in final room.\n")
    print("There are required items to gain access to the Boss Room.")
    print("You must have all 3 required items to defeat the Boss and win!\n")

    return rules


intro = rules()


playing = input("Would you like to try to Escape the dungeon (yes/no)\n")
if playing.lower().strip() != "yes":
    print("Exiting the game...")
    quit()


def clear():
    """
    Clears terminal before the text adventure starts to clean up space
    """
    os.system("cls" if os.name == "nt" else "clear")


clear()


def start_game():
    """
    Game start intro message
    """
    print(f"Welcome {name} to the Escape the Dungeon Game. Good luck!\n")
    print("You have found yourself in a dungeon and must find the way out.\n")
    print(f"Current room: {current_room}")
    print(f"Current stats: {player_hp}hp and {player_stamina}sp.")
    print(f"Current inventory: {inventory}\n")


# def mini_boss_imp():
#     """
#     Mini boss fight for attack and damage stats
#     """

# def mini_boss_orc():
#     """
#     Mini boss fight for attack and damage stats
#     """

# def master_boss():
#     """
#     Master boss fight for attack and damage stats
#     """

# def stamina_regen():
#     """
#     Regeneration of stamina per turn
#     """

# def player_health():
#     """
#     Players health damage
#     """

# def use_item():
#     """
#     Using an item
#     """

# def player_attack():
#     """
#     Random damage for player attack
#     """

# def fire_trap():
#     """
#     Fire trap in room 1
#     """

# def river_puzzle():
#     """
#     River puzzle in room 2
#     """

# def jungle_puzzle():
#     """
#     Jungle puzzle in room 6
#     """

# def tunnel_puzzle():
#     """
#     Tunnel puzzle, linked to jungle puzzle in room 6
#     """

def starting_room():
    print(
        "You are an empty room with nothing but dim lighting to show the way.\n"
        "You can either go North, South or East.\n")

def choose_direction():
    direction = ""
    while direction != "north" and direction != "east" and direction != "south" and direction != "west":
        direction = input("Which way do you go?:\n").lower()
    
    return direction

# Player welcome screen
name = input("Type your name:\n").strip()
clear()
start_game()
starting_room()
choose_direction()