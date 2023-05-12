import random
import os

# Player health and stamina
player_hp = 150
player_stamina = 50

# Map dictionary
rooms = {
    "Starting Room": {"North": "Room 1", "South": "Room 2", "East": "Room 5"},
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


# Quits game if user doesn't want to play
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
    current_room = "Starting Room"
    print(f"Welcome {name} to the Escape the Dungeon Game. Good luck!\n")
    print("You have found yourself in a dungeon and must find the way out.\n")
    print(f"Current room: {current_room}")
    print(f"Current stats: {player_hp}hp and {player_stamina}sp.")
    print(f"Current inventory: {inventory}\n")


def starting_room():
    """
    Starting room
    """
    print(
        "You are in an empty room with nothing but dim lighting around you.\n"
        "You can't see much but you see 3 possible paths.\n"
        "You can either go North, South or East.\n")

    direction = input("Which way do you go?:\n").lower().strip()
    while direction != "north" and direction != "south" and direction != "east":
        print("You can only go North, South, or East.")
        direction = input("Which way do you go?:\n").lower().strip()

    if direction == "north":
        room_one()
    elif direction == "south":
        room_two()
    else:
        room_five()


def room_one():
    """
    Room one - weapon, key and trap
    """
    current_room = "Room One"
    print(f"Current room: {current_room}\n")
    print("You can only go South.\n")

    direction = input("Which way do you go?:\n").lower().strip()
    while direction != "south":
        print("You can only go south.")
        direction = input("Which way do you go?:\n").lower().strip()

    if direction == "south":
        starting_room()


def room_two():
    """
    Room two - puzzle, item
    """
    current_room = "Room Two"
    print(f"Current room: {current_room}")
    print("You can only go North or East.")

    direction = input("Which way do you go?:\n").lower().strip()
    while direction != "north" and direction != "east":
        print("You can only go North or East.")
        direction = input("Which way do you go?:\n").lower().strip()

    if direction == "north":
        starting_room()
    else:
        room_three()


def room_three():
    """
    Room three - mini boss 1, requires key 1 and weapon
    """
    current_room = "Room Three"
    print(f"Current room: {current_room}")
    print("You can only go North, East or West.")

    direction = input("Which way do you go?:\n").lower().strip()
    while direction != "north" and direction != "east" and direction != "west":
        print("You can only go North, East or West.")
        direction = input("Which way do you go?:\n").lower().strip()

    if direction == "north":
        room_four()
    elif direction == "east":
        secret_room()
    else:
        room_two()


def room_three_completed():
    """
    Room three - when boss has been defeated
    """
    current_room = "Room Three"
    print(f"Current room: {current_room}")
    print("The mini boss of this room has already been defeated...Yay!")
    print("You can only go North, East or West.")

    direction = input("Which way do you go?:\n").lower()
    while direction != "north" and direction != "east" and direction != "west":
        print("You can only go North, East or West.")
        direction = input("Which way do you go?:\n").lower()

    if direction == "north":
        room_four()
    elif direction == "east":
        secret_room()
    else:
        room_two()


def room_four():
    """
    Room four - key
    """
    current_room = "Room four"
    print(f"Current room: {current_room}")
    print("You can only go South.")

    direction = input("Which way do you go?:\n").lower().strip()
    while direction != "south":
        print("You can only go South.")
        direction = input("Which way do you go?:\n").lower().strip()

    if direction == "south":
        room_three_completed()


def room_five():
    """
    Room five
    """
    current_room = "Room Five"
    print(f"Current room: {current_room}")
    print("You can only go North or West.")

    direction = input("Which way do you go?:\n").lower().strip()
    while direction != "north" and direction != "west":
        print("You can only go North or West.")
        direction = input("Which way do you go?:\n").lower().strip()

    if direction == "north":
        room_six()
    else:
        starting_room()


def room_six():
    """
    Room six - puzzle, item
    """
    current_room = "Room Six"
    print(f"Current room: {current_room}")
    print("You can only go East or South.")

    direction = input("Which way do you go?:\n").lower().strip()
    while direction != "east" and direction != "south":
        print("You can only go East or South.")
        direction = input("Which way do you go?:\n").lower().strip()

    if direction == "east":
        room_seven()
    else:
        room_five()


def room_seven():
    """
    Room seven - mini boss 2, requires key 2 and weapon
    """
    current_room = "Room Seven"
    print(f"Current room: {current_room}")
    print("You can only go East, South or West.")

    direction = input("Which way do you go?:\n").lower().strip()
    while direction != "east" and direction != "south" and direction != "west":
        print("You can only go East, South or West.")
        direction = input("Which way do you go?:\n").lower().strip()

    if direction == "east":
        room_nine()
    elif direction == "south":
        room_eight()
    else:
        room_six()


def room_eight():
    """
    Room eight - key
    """
    current_room = "Room Eight"
    print(f"Current room: {current_room}")
    print("You can only go North.")

    direction = input("Which way do you go?:\n").lower().strip()
    while direction != "north":
        print("You can only go North.")
        direction = input("Which way do you go?:\n").lower().strip()

    if direction == "north":
        room_seven()


def room_nine():
    """
    Room nine - key and item
    """
    current_room = "Room Nine"
    print(f"Current room: {current_room}")
    print("You can only go West or South.")

    direction = input("Which way do you go?:\n").lower().strip()
    while direction != "west" and direction != "south":
        print("You can only go West or South.")
        direction = input("Which way do you go?:\n").lower().strip()

    if direction == "west":
        room_seven()
    else:
        boss_room()


def secret_room():
    """
    Secret room - requires stone and secret room key, master weapon and armour
    """
    current_room = "Secret Room"
    print(f"Current room: {current_room}")
    print("You can only go West.")

    direction = input("Which way do you go?:\n").lower().strip()
    while direction != "west":
        print("You can only West.")
        direction = input("Which way do you go?:\n").lower().strip()

    if direction == "west":
        room_three_completed()


def boss_room():
    """
    Boss room - Master boss, requires key, armour and master weapon
    """
    current_room = "Boss Room"
    print(f"Current room: {current_room}")
    print("Time to fight the boss.")


# Player welcome screen
name = input("Type your name:\n").capitalize().strip()
clear()
start_game()
starting_room()


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