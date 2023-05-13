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
    print(f"Welcome {name} to the Escape the Dungeon Game. Good luck!\n")
    print("You have found yourself in a dungeon and must find the way out.\n")
    print(f"Current stats: {player_hp}hp and {player_stamina}sp.")
    print(f"Current inventory: {inventory}\n")

# need to add correct dialogue to game, currently placeholder dialogue
def starting_room():
    """
    Starting room
    """
    current_room = "Starting Room"
    print(f"Current room: {current_room}")
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
    clear()

    current_room = "Room One"
    print(f"Current room: {current_room}\n")
    
    take_item = input("You see a key, do you take it? (yes/no)").lower().strip()
    while take_item != "yes" and take_item != "no":
        take_item = input("You see a key, do you take it? (yes/no)").lower().strip()

    # need to fix code so that player cant take item again
    try:
        if take_item == "yes":
            required_items.append("Key 1")
            print(f"Current inventory:{required_items}")

            if "Key 1" not in required_items:
                print("You do not have the item")

            else:
                print("you have the item")
        else:
            print("You left the key")

    except:
        print("you have the item")
   
    print("You see 2 weapons.\n")
    print("Sword or Bow/Arrow?\n")
   
    # need to fix code so that player cant take item again
    choose_weapon = input("which weapon?").lower().strip()
    while choose_weapon != "sword" and choose_weapon != "bow":
        print("choose a weapon")
        choose_weapon = input("which weapon?").lower().strip()

    if choose_weapon == "sword":
        required_items.append("Sword")
        print(f"Current inventory:{required_items}")
    else:
        required_items.append("Bow")
        print(f"Current inventory:{required_items}")

    print("You choose your weapon and this set off a trap.")

    trap = input("disarm trap or jump through it?").lower().strip()
    while trap != "disarm" and trap != "jump":
        print("You must choose to do something.")
        trap = input("disarm trap or jump through it?").lower().strip()

    if trap == "disarm":
        disarm()
    else:
        jump()

    print("South is the only way you can go.\n")
    print("So you head south back to the room you started in.\n")
    starting_room()


def room_two():
    """
    Room two - puzzle, item
    """
    
    current_room = "Room Two"
    print(f"Current room: {current_room}")
    print("River puzzle")
    
    trap = input("swim through or hop across?").lower().strip()
    while trap != "swim" and trap != "hop":
        print("You must choose to do something.")
        trap = input("swim through or hop across?").lower().strip()

    if trap == "swim":
        swim()
    else:
        hop()

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
    clear()

    if "Key 1" not in required_items:
        print("You need the key and a weapon to pass")
        room_two()
    else:
        required_items.pop(0)
        print("you use the key to enter the room")
        print(f"{required_items}")

        current_room = "Room Three"
        print(f"Current room: {current_room}")

        print("Mini boss 1")
        fight = input("do you fight the boss?:\n").lower().strip()
        while fight != "yes" and fight != "no":
            print("you must choose.")
            fight = input("do you fight the boss?:\n").lower().strip()

        if fight == "yes":
            mini_boss_imp()
        else:
            print("You fleed the mini boss fight and lost")
            quit()

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
    print("you see another key")

    take_item = input("You see a key, do you take it? (yes/no)").lower().strip()
    while take_item != "yes" and take_item != "no":
        take_item = input("You see a key, do you take it? (yes/no)").lower().strip()

    # need to fix code so that player cant take item again
    try:
        if take_item == "yes":
            required_items.append("Key 2")
            print(f"Current inventory:{required_items}")

            if "Key 2" not in required_items:
                print("You do not have the item")

            else:
                print("you have the item")
        else:
            print("You left the key")

    except:
        print("you have the item")
    
    print("NPC fairy")

    talk = input("Do you speak to the fairy?:\n").lower()
    while talk != "yes" and talk != "no":
        print("The fairy is waiting for a response.")
        talk = input("Do you speak to the fairy?:\n").lower()

    if talk == "yes":
        print("You speak to the fairy")
    else:
        print("You decide not to speak to the fairy")

    print("You can only go South.")
    print("You head south back to the room you camr from")
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
    print("Jungle puzzle")
    
    trap = input("go through or way around?").lower().strip()
    while trap != "through" and trap != "around":
        print("You must choose to do something.")
        trap = input("go through or way around?").lower().strip()

    if trap == "through":
        jungle_puzzle()
    else:
        tunnel_puzzle()

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
    if "Key 2" not in required_items:
        print("You need the key and a weapon to pass")
        room_five()
    else:
        required_items.pop(1)
        print("you use the key to enter the room")
        print(f"{required_items}")

    current_room = "Room Seven"
    print(f"Current room: {current_room}")

    print("Mini boss 1")
        fight = input("do you fight the boss?:\n").lower().strip()
        while fight != "yes" and fight != "no":
            print("you must choose.")
            fight = input("do you fight the boss?:\n").lower().strip()

        if fight == "yes":
            mini_boss_orc()
        else:
            print("You fleed the mini boss fight and lost")
            quit()

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


def disarm():
    """
    Disarm fire trap with stone
    """
    # add random function for using stone whether they hit or miss trap
    # possibly add a function if they have bow to use that?
    print("You disarmed the fire trap")


def jump():
    """
    Jump through fire trap
    """
    # add function to take damage and show the hp and sp
    print("You successfully jumped through the fire trap.")
    print("You did however take significant damage")
    print(f"{player_hp}hp")
    print(f"{player_stamina}sp")


def swim():
    """
    Swim through river
    """
    print("You succssfully swam through the river.")
    print("You did however take some damage")
    print(f"{player_hp}hp")
    print(f"{player_stamina}sp")


def hop():
    """
    Hop across pedestals in river
    """
    print("You succssfully hopped across the river.")
    print("You did however take minimal damage")
    print(f"{player_hp}hp")
    print(f"{player_stamina}sp")


def mini_boss_imp():
    """
    Mini boss fight for attack and damage stats
    """
    print("mini boss fight")


def jungle_puzzle():
    """
    Jungle puzzle in room 6
    """
    # add not in statement for sword item and auto send to tunnel
    print("jungle")


def tunnel_puzzle():
    """
    Tunnel puzzle, linked to jungle puzzle in room 6
    """
    # add jump and duck statements
    print("jump and duck")


def mini_boss_orc():
    """
    Mini boss fight for attack and damage stats
    """
    print("mini boss fight")
    
   
# Player welcome screen
name = input("Type your name:\n").capitalize().strip()
clear()
start_game()
starting_room()


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
