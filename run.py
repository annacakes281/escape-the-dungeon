import random
import os
from colorama import Fore, Style


# Player health and stamina - need potion to restore health
MAX_HP = 150
PLAYER_HP = 135  # Player has inital fall damage
MAX_ARMOUR = 275
PLAYER_HP_ARMOUR = 275
PLAYER_STAMINA = 50  # this restores on its own

# Boss health
IMP_HP = 50
ORC_HP = 100
DRAGON_HP = 250

# Universal minimum health
MIN_HP = 0

# List to keep track on inventory items
inventory = []
weapons = []
keys = []

# List for current boss - used to check for attacks
current_boss = []

# List for completed rooms/tasks
completed_tasks = []


def clear():
    """
    Clears terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def clear_terminal():
    """
    Prompts players whether they want to clear terminal
    """
    print("\nType 'y' to clear the terminal:")
    clear_term = input("Clear the terminal?\n> ").lower().strip()
    if clear_term == "y":
        clear()
    else:
        print("Terminal not cleared.\n\n")


def rules():
    """
    Rules for the game that will appear at the start so players know the goal
    """
    print("This is a text-based game, type your answers into the terminal.\n")

    print("Type the first letter of the word to continue.")
    print("e.g 'n' for 'north' or 'y' for 'yes'.\n\n")

    print("The goal is to defeat the Master Boss in Boss Room.\n")

    print("There are required items to gain access to the Boss Room.")
    print("You must have a Master Weapon and a Master Key to defeat the Boss!")
    print("...but the armour won't be a bad choice to have either.\n\n")

    return rules


intro = rules()


# Quits game if user doesn't want to play
print("Type 'y' or 'yes' to play.")
playing = input("Would you like to Escape the dungeon?\n> ").lower().strip()
# Strip used to clear empty space if players type by mistake
if playing != "yes" and playing != "y":
    print("\nOh well, I guess you're not up for the challenge.")
    print("Exiting the game...")
    quit()


def start_game():
    """
    Game start intro message
    """
    print(f"Welcome {name} to the Escape the Dungeon Game. Good luck!\n")

    print("You fell down a trap door and end up in an empty room.\n")


def starting_room():
    """
    The main room where the player starts
    """
    print("Remember you can type just the first letter of the word.\n")

    current_room = "Starting Room"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    print(
        "You look around in the dimmly lit room and see 3 possible paths.\n"
        "You can either go north, south or east.\n\n"
        "North seems quiet,\n"
        "east has an odd smell coming from it...\n"
        "and south sounds like there is water running.\n")

    # Players choose which direction they want to go
    direction = input("Which way do you go?:\n> ").lower().strip()
    while direction != "n" and direction != "s" and direction != "e":
        print("\nInvalid move, please enter a valid move:")
        print("'n' for 'north, 's' for 'south' or 'e' for 'east'.\n")
        direction = input("Which way do you go?:\n> ").lower().strip()

    if direction == "n":
        room_one()
    elif direction == "s":
        room_two()
    else:
        room_five()


def room_one():
    """
    Room one:\n
    Player can choose to pick up the key (if not in inventory)\n
    Player chooses weapon (if not in inventory)\n
    Player has 2 choices to escape trap
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    current_room = "Room One"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    print("You enter the room to the north.\n")

    if "Room One" not in completed_tasks:

        # Prompts user to collect key, if not in inventory
        if "Key 1" not in keys:
            print(
                "You look around..."
                "You see a key on a pedestal... it could be important.")
            take_item = input("Do you take it? (y/n)\n> ").lower().strip()
            while take_item != "y" and take_item != "n":
                print("\nInvalid choice, please select a valid option:")
                print("'y' for 'yes' or 'n' for 'no'.\n")
                print("You see a key on a pedestal... it could be important.")
                take_item = input("Do you take it?\n> ").lower().strip()

            if take_item == "y":
                keys.append("Key 1")
                completed_tasks.append("Room One")
                print("\nYou picked up the key and added it to your bag.")
                print(f"Current key inventory:{keys}\n")
            else:
                print(
                    "\nYou decided to leave the key on the pedestal..."
                    "I hope it wasn't important...\n")
    else:
        print("You see an empty pedestal.\n")

    if "Weapon Chosen" not in completed_tasks:
        # Prompts user to choose their weapon, if not in inventory
        if "Sword" not in weapons and "Bow" not in weapons:
            print(
                "You notice a table in the middle of the room.\n"
                "There are 2 weapons lying on the table.\n"
                "One is a broadsword and a belt.\n"
                "The other is a bow with a quiver full of arrows.\n\n"
                "There is an inscription on the table:\n"
                "Choose a weapon!\n")

            weapon = input("Which do you choose? (s/b)\n> ").lower().strip()
            while weapon != "s" and weapon != "b":
                print("\nInvalid choice, please select a valid option:")
                print("'s' for 'sword' or 'b' for 'bow'.\n")
                print("Choose a weapon!\n")
                weapon = input("Which do you choose?\n> ").lower().strip()

            if weapon == "s":
                weapons.append("Sword")
                completed_tasks.append("Weapon Chosen")
                print("\nYou choose the sword attached it to your side.\n")
                print(f"Current weapon:{weapons}\n")

                # Choosing weapon will trigger a trap
                print(
                    "Picking up your weapon sets off a trap.\n"
                    "A wall of fire is blocking the way out.\n")

                print(
                    "What will you do?\n"
                    "Disarm the trap with a stone you see on the ground,\n"
                    "or risk jumping through it?\n")

                trap = input("Disarm or jump? (d/j)\n> ").lower().strip()
                while trap != "d" and trap != "j":
                    print("\nInvalid choice, please select a valid option:")
                    print("'d' for 'disarm' or 'j' for 'jump'.\n")
                    trap = input("Disarm or jump? (d/j)\n> ").lower().strip()

                if trap == "d":
                    disarm(PLAYER_STAMINA)
                else:
                    jump(PLAYER_STAMINA)
            else:
                print("\nYou choose the bow and attached it to your back.\n")
                weapons.append("Bow")
                completed_tasks.append("Weapon Chosen")
                print(f"Current weapon:{weapons}\n")

                # Choosing weapon will trigger a trap
                print(
                    "Picking up your weapon sets off a trap.\n"
                    "A wall of fire is blocking the way out.\n")

                print(
                    "What will you do?\n"
                    "Disarm the trap with a stone you see on the ground,\n"
                    "or risk jumping through it?\n")

                trap = input("Disarm or jump? (d/j)\n> ").lower().strip()
                while trap != "d" and trap != "j":
                    print("\nInvalid choice, please select a valid option:")
                    print("'d' for 'disarm' or 'j' for 'jump'.\n")
                    trap = input("Disarm or jump? (d/j)\n> ").lower().strip()

                if trap == "d":
                    disarm(PLAYER_STAMINA)
                else:
                    jump(PLAYER_STAMINA)

        else:
            print("You see an empty table.\n")
    else:
        print("You see an empty table.\n")

    print("There is nothing left to do in this room.")
    print("So you head south back to the room you started in.\n")
    clear_terminal()
    starting_room()


def room_two():
    """
    Room two:\n
    Player choices to either swim across lake or jump across pedestals\n
    Player can choose to pick up health potion\n
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    current_room = "Room Two"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    print(
        "You enter the room to the south and come to a river.\n"
        "You can either swim through the river, it looks safe...enough.\n"
        "Or you can jump across the pillars sticking out the river,\n"
        "although they look a bit unsafe.\n")

    # Players must choose to swim or jump for this puzzle
    print(
        "Do you swim across the river, or "
        "take your chances and jump across the pillars?\n")
    trap = input("Swim or jump? (s/j)\n> ").lower().strip()
    while trap != "s" and trap != "j":
        print("\nInvalid choice, please select a valid option:")
        print("'s' for 'swim' or 'j' for 'jump'.\n")
        trap = input("Swim or jump? (s/j)\n> ").lower().strip()

    if trap == "s":
        swim(PLAYER_STAMINA)
    else:
        hop(PLAYER_STAMINA)

    if "Room Two" not in completed_tasks:

        # Prompts player to take potion of not in inventory
        if "Potion" not in inventory:
            print(
                "\nYou look around and see something on the ground.\n"
                "You take a closer look and see it is a potion...\n"
                "it could be useful.\n")

            take_item = input("Do you take it? (y/n)\n> ").lower().strip()
            while take_item != "y" and take_item != "n":
                print("\nInvalid choice, please select a valid option:")
                print("'y' for 'yes' or 'n' for 'no'.\n")
                print("You see a potion on the ground, it could be useful...")
                take_item = input("Do you take it? (y/n)\n> ").lower().strip()

            if take_item == "y":
                inventory.append("Potion")
                completed_tasks.append("Room Two")
                print(
                    "\nYou take the potion and read the label.\n"
                    "It reads: 'Health Potion'.\n"
                    "Lucky you!\n")
                print(f"Current inventory:{inventory}\n")
            else:
                print(
                    "You decided to leave the potion..."
                    "I hope it wasn't important.\n")
    else:
        print("\nYou look around see nothing on the ground.\n")

    print(
        "After crossing the river you can see a path ahead.\n"
        "You can either follow the path east or go back north.\n"
        )

    # Prompts player which direction they want to go
    direction = input("Which way do you go? (e/n):\n> ").lower().strip()
    while direction != "n" and direction != "e":
        print("\nInvalid choice, please select a valid option:")
        print("'e' for 'east' or 'n' for 'north'.\n")
        direction = input("Which way do you go?:\n> ").lower().strip()

    if direction == "n":
        print(
            "\nYou have to go back across the river...again\n"
            "Will you swim or jump this time?\n")
        trap = input("Swim or jump? (s/j)\n> ").lower().strip()

        while trap != "s" and trap != "j":
            print("\nInvalid choice, please select a valid option:")
            print("'s' for 'swim' or 'j' for 'jump'.\n")
            trap = input("Swim or jump? (s/j)\n> ").lower().strip()

        if trap == "s":
            swim(PLAYER_STAMINA)
            clear_terminal()
            starting_room()
        else:
            hop(PLAYER_STAMINA)
            clear_terminal()
            starting_room()
    else:
        room_three()


def room_two_west():
    """
    Room two:\n
    Only avaliable if player enters room 2 from room 3\n
    Player choices to either swim across lake or jump across pedestals\n
    Player can choose to pick up health potion\n
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    current_room = "Room Two"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    if "Room Two" not in completed_tasks:

        # Prompts player to take potion of not in inventory
        if "Potion" not in inventory:
            print(
                "\nYou head back west.\n"
                "You look around and see something on the ground.\n"
                "You take a closer look and see it is a potion...\n"
                "it could be useful.\n")

            take_item = input("Do you take it? (y/n)\n> ").lower().strip()
            while take_item != "y" and take_item != "n":
                print("\nInvalid choice, please select a valid option:")
                print("'y' for 'yes' or 'n' for 'no'.\n")
                print("You see a potion on the ground, it could be useful...")
                take_item = input("Do you take it? (y/n)\n> ").lower().strip()

            if take_item == "y":
                inventory.append("Potion")
                completed_tasks.append("Room Two")
                print(
                    "\nYou take the potion and read the label.\n"
                    "It reads: 'Health Potion'.\n"
                    "Lucky you!\n")
                print(f"Current inventory:{inventory}\n")
            else:
                print(
                    "You decided to leave the potion..."
                    "I hope it wasn't important.\n")
        else:
            print(
                "You head back west.\n"
                "You look around see nothing on the ground.\n")
    else:
        print(
            "You head back west.\n"
            "You see nothing on the ground.\n")

    print(
        "Looks like you have to cross the river...again.\n"
        "Will you jump or swim across?\n")

    # Players must choose to swim or jump for this puzzle
    trap = input("Swim or jump? (s/j)\n> ").lower().strip()
    while trap != "s" and trap != "j":
        print("\nInvalid choice, please select a valid option:")
        print("'s' for 'swim' or 'j' for 'jump'.\n")
        trap = input("Swim or jump? (s/j)\n> ").lower().strip()

    if trap == "s":
        swim(PLAYER_STAMINA)
    else:
        hop(PLAYER_STAMINA)

    print("After crossing the river you head back north.\n")
    clear_terminal()
    starting_room()


def room_three():
    """
    Room three:\n
    Player requires the key to enter this room\n
    Player can decide to fight the mini boss\n
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    # Player must have key to enter
    if "Room Three" not in completed_tasks:
        if "Key 1" not in keys:
            print("The door is locked and you need a key to open it.\n")
            room_two_west()
        else:
            keys.remove("Key 1")
            completed_tasks.append("Room Three")
            print("You use the key and open the door to the room\n")

            current_room = "Room Three"
            print(f"Current room: {current_room}\n")

            view_stats()
            view_items()

        print(
            "You enter the room and the door shuts behind you.\n"
            "You notice an imp looking at you... it is ready to fight you!\n")

        # Asks players if they want to use a potion
        use_potion()

        # Prompts players whether they fight the mini boss
        print("The imp steps towards you with its weapon.")
        fight = input("Do you fight? (y/n):\n> ").lower().strip()
        while fight != "y" and fight != "n":
            print("\nInvalid choice, please select a valid option:")
            print("'y' for 'yes' or 'n' for 'no'.\n")
            fight = input("Do you fight?:\n> ").lower().strip()

        if fight == "y":
            mini_boss_imp()
        else:
            print(
                "\nYou decided to try and flee the imp\n"
                "...but as soon as you turned to open the door,\n"
                "it kept attacking you and you died...")
            quit()
    else:
        current_room = "Room Three"
        print(f"Current room: {current_room}\n")

        view_stats()
        view_items()

        print(
            "You enter the room and see the imp you defeated on the ground.\n"
            "You take a moment to remember your triumph!\n")

        # Prompts players to choose a direction
        print(
            "You look around and can go north to the open room.\n"
            "East to mysterious door,\n"
            "or west towards the river.\n")

        direction = input("Which way do you go?:\n> ").lower().strip()
        while direction != "n" and direction != "e" and direction != "w":
            print("\nInvalid move, please enter a valid move:")
            print("'n' for 'n', 'e' for 'east' or 'w' for 'west'.\n")
            direction = input("Which way do you go?:\n> ").lower().strip()

        if direction == "n":
            room_four()
        elif direction == "e":
            secret_room()
        else:
            room_two_west()


def room_three_completed():
    """
    Room three:\n
    Player enters this room when boss has already been defeated
    """

    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    current_room = "Room Three"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    print(
        "You enter the room and see the imp you defeated on the ground.\n"
        "You take a moment to remember your triumph!\n")

    # Prompts players to choose a direction
    print(
            "You look around and can go north to the open room.\n"
            "East to mysterious door,\n"
            "or west towards the river.\n")

    direction = input("Which way do you go?:\n> ").lower().strip()
    while direction != "n" and direction != "e" and direction != "w":
        print("\nInvalid move, please enter a valid move:")
        print("'n' for 'n', 'e' for 'east' or 'w' for 'west'.\n")
        direction = input("Which way do you go?:\n> ").lower().strip()

    if direction == "n":
        room_four()
    elif direction == "e":
        secret_room()
    else:
        room_two_west()


def room_four():
    """
    Room four:\n
    Player can choose to collect key (if not in inventory)\n
    Player can choose to speak to NPC
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    current_room = "Room Four"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    if "Room Four" not in completed_tasks:

        # Prompts player to take key if not in inventory
        if "Key 2" not in keys:
            print("You see a key on a pedestal... it could be important.")
            take_item = input("Do you take it? (y/n)\n> ").lower().strip()
            while take_item != "y" and take_item != "n":
                print("\nInvalid choice, please select a valid option:")
                print("'y' for 'yes' or 'n' for 'no'.\n")
                print("You see a key on a pedestal...it could be important.\n")
                take_item = input("Do you take it?\n> ").lower().strip()

            if take_item == "y":
                keys.append("Key 2")
                completed_tasks.append("Room Four")
                print("\nYou picked up the key and added it to your bag.")
                print(f"Current key inventory:{keys}\n")
            else:
                print(
                    "\nYou decided to leave the key on the pedestal..."
                    "I hope it wasn't important...\n")
        else:
            print("You see an empty pedestal.\n")
    else:
        print("You see an empty pedestal.\n")

    # Prompts players if they want to speak to the NPC
    print("You see a fairy appear and she smiles at you.\n")
    talk = input("Do you speak to her? (y/n)\n> ").lower().strip()
    while talk != "y" and talk != "n":
        print("\nInvalid choice, please select a valid option:")
        print("'y' for 'yes' or 'n' for 'no'.\n")
        print("The fairy continues to smile at you...\n")
        talk = input("Do you speak to her? (y/n)\n> ").lower().strip()

    if talk == "y":
        fairy()
    else:
        print(
            "\nYou decide not to speak to the fairy.\n"
            "She then disappears...\n"
            "Hopefully she had nothing important to say.\n\n"
            "The only path you can take is south.\n"
            "You head back south to the room you just came from.\n")
        room_three_completed()


def room_five():
    """
    Room five:\n
    An empty room where the player just has to choose a direction to go
    """

    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    current_room = "Room Five"
    print(f"Current room: {current_room}\n")

    print(
        "You head east and enter an empty room that smells musty.\n"
        "There are only 2 ways to go...\n"
        "Either north towards to foresty smell...\n"
        "or west.\n")

    # Prompts user to choose a direction to go
    direction = input("Which way do you go? (n/w)\n> ").lower().strip()
    while direction != "n" and direction != "w":
        print("\nInvalid move, please enter a valid move:")
        print("'n' for 'north' or 'w' for 'west'.\n")
        direction = input("Which way do you go?:\n> ").lower().strip()

    if direction == "n":
        room_six()
    else:
        clear_terminal()
        starting_room()


def room_five_south():
    """
    Room five:\n
    Only avaliable if player enters room 5 from room 6\n
    An empty room where the player just has to choose a direction to go
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    current_room = "Room Five"
    print(f"Current room: {current_room}\n")

    print(
        "You head south and enter an empty room that smells musty.\n"
        "There are only 2 ways to go...\n"
        "Either north towards to foresty smell...\n"
        "or west.\n")

    # Prompts user to choose a direction to go
    direction = input("Which way do you go? (n/w)\n> ").lower().strip()
    while direction != "n" and direction != "w":
        print("\nInvalid move, please enter a valid move:")
        print("'n' for 'north' or 'w' for 'west'.\n")
        direction = input("Which way do you go?:\n> ").lower().strip()

    if direction == "n":
        room_six()
    else:
        clear_terminal()
        starting_room()


def room_six():
    """
    Room six:\n
    Player choices to either to go through jungle but this requires sword
    or player can go through the tunnel\n
    Player has option to pick up a potion if not in inventory
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    current_room = "Room Six"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    print(
        "You enter the room to the north.\n"
        "It has a very foresty smell...\n\n"
        "You see 2 possible paths ahead of you.\n"
        "Either through the thick vines \n"
        "or through a small tunnel.\n")

    # Player must choose which way to go, the vines require the sword
    print("Which route do you take?\n")
    trap = input("Vines or tunnel? (v/t)\n> ").lower().strip()
    while trap != "v" and trap != "t":
        print("\nInvalid choice, please select a valid option:")
        print("'v' for 'vines' or 't' for 'tunnel'.\n")
        trap = input("Vines or tunnel? (v/t)\n> ").lower().strip()

    if trap == "v":
        jungle_puzzle(PLAYER_STAMINA)
    else:
        tunnel_puzzle(PLAYER_STAMINA)

    if "Room Six" not in completed_tasks:

        # Prompts player to take potion of not in inventory
        if "Potion" not in inventory:
            print(
                "\nYou look around and see something on the ground.\n"
                "You take a closer look and see it is a potion...\n"
                "it could be useful.\n")

            take_item = input("Do you take it? (y/n)\n> ").lower().strip()
            while take_item != "y" and take_item != "n":
                print("\nInvalid choice, please select a valid option:")
                print("'y' for 'yes' or 'n' for 'no'.\n")
                print("You see a potion on the ground, it could be useful...")
                take_item = input("Do you take it? (y/n)\n> ").lower().strip()

            if take_item == "y":
                inventory.append("Potion")
                completed_tasks.append("Room Six")
                print(
                    "\nYou take the potion and read the label.\n"
                    "It reads: 'Health Potion'.\n"
                    "Lucky you!\n")
                print(f"Current inventory:{inventory}\n")
            else:
                print(
                    "You decided to leave the potion..."
                    "I hope it wasn't important.\n")
    else:
        print("\nYou look around see nothing on the ground.\n")

    print("You look around and see a path ahead, or you can turn back.\n")

    # Player has choice in direction
    direction = input("Which way do you go? (e/s)\n> ").lower().strip()
    while direction != "e" and direction != "s":
        print("\nInvalid move, please enter a valid move:")
        print("'e' for 'east' or 's' for 'south'.\n")
        direction = input("Which way do you go?:\n> ").lower().strip()

    if direction == "e":
        room_seven()
    else:
        print(
            "\nYou decide to turn back around...\n"
            "But will need to traverse through the vines...\n"
            "or go through the tunnel.\n")

        print("Which route do you take?\n")
        trap = input("Vines or tunnel? (v/t)\n> ").lower().strip()
        while trap != "v" and trap != "t":
            print("\nInvalid choice, please select a valid option:")
            print("'v' for 'vines' or 't' for 'tunnel'.\n")
            trap = input("Vines or tunnel? (v/t)\n> ").lower().strip()

        if trap == "v":
            jungle_puzzle(PLAYER_STAMINA)
        else:
            tunnel_puzzle(PLAYER_STAMINA)
            room_five_south()


def room_six_west():
    """
    Room six:\n
    Only avaliable if player enters room 6 from room 7\n
    Player choices to either to go through jungle but this requires sword
    or player can go through the tunnel\n
    Player has option to pick up a potion if not in inventory
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    current_room = "Room Six"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    print("You enter the room to the west.\n")

    if "Room Six" not in completed_tasks:

        # Prompts player to take potion of not in inventory
        if "Potion" not in inventory:
            print(
                "\nYou look around and see something on the ground.\n"
                "You take a closer look and see it is a potion...\n"
                "it could be useful.\n")

            take_item = input("Do you take it? (y/n)\n> ").lower().strip()
            while take_item != "y" and take_item != "n":
                print("\nInvalid choice, please select a valid option:")
                print("'y' for 'yes' or 'n' for 'no'.\n")
                print("You see a potion on the ground, it could be useful...")
                take_item = input("Do you take it? (y/n)\n> ").lower().strip()

            if take_item == "y":
                inventory.append("Potion")
                completed_tasks.append("Room Six")
                print(
                    "\nYou take the potion and read the label.\n"
                    "It reads: 'Health Potion'.\n"
                    "Lucky you!\n")
                print(f"Current inventory:{inventory}\n")
            else:
                print(
                    "You decided to leave the potion..."
                    "I hope it wasn't important.\n")
    else:
        print("\nYou look around see nothing on the ground.\n")

    print(
        "Looks like you have to go back again...\n"
        "Either through the thick vines \n"
        "or through a small tunnel.\n")

    # Player must choose which way to go, the vines require the sword
    print("Which route do you take?\n")
    trap = input("Vines or tunnel? (v/t)\n> ").lower().strip()
    while trap != "v" and trap != "t":
        print("\nInvalid choice, please select a valid option:")
        print("'v' for 'vines' or 't' for 'tunnel'.\n")
        trap = input("Vines or tunnel? (v/t)\n> ").lower().strip()

    if trap == "v":
        jungle_puzzle(PLAYER_STAMINA)
    else:
        tunnel_puzzle(PLAYER_STAMINA)

    print("You look around and see a path ahead, or you can turn back.\n")

    # Player has choice in direction
    direction = input("Which way do you go? (e/s)\n> ").lower().strip()
    while direction != "e" and direction != "s":
        print("\nInvalid move, please enter a valid move:")
        print("'e' for 'east' or 's' for 'south'.\n")
        direction = input("Which way do you go?:\n> ").lower().strip()

    if direction == "s":
        room_five_south()
    else:
        print(
            "You decide to turn back around...\n"
            "But will need to traverse through the vines...again"
            "or go through the tunnel.\n")

        print("Which route do you take?\n")
        trap = input("Vines or tunnel? (v/t)\n> ").lower().strip()
        while trap != "v" and trap != "t":
            print("\nInvalid choice, please select a valid option:")
            print("'v' for 'vines' or 't' for 'tunnel'.\n")
            trap = input("Vines or tunnel? (v/t)\n> ").lower().strip()

        if trap == "v":
            jungle_puzzle(PLAYER_STAMINA)
        else:
            tunnel_puzzle(PLAYER_STAMINA)
            room_seven()


def room_seven():
    """
    Room seven:\n
    Player requires the key to enter this room\n
    Player can decide to fight the mini boss\n
    Player can collect secret room item after mini boss defeated
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    if "Room Seven" not in completed_tasks:

        # Player must have key to enter
        if "Key 2" not in keys:
            print("The door is locked and you need a key to open it.\n")
            room_six_west()
        else:
            keys.remove("Key 2")
            completed_tasks.append("Room Seven")
            print("You use the key and open the door to the room\n")

            current_room = "Room Seven"
            print(f"Current room: {current_room}\n")

            view_stats()
            view_items()

            print(
                "You enter the room and the door shuts behind you.\n"
                "You notice an orc looking at you...it is ready to fight!\n")
            # Prompts players whether they fight the mini boss
            print("The orc steps towards you with its weapon.")
            fight = input("Do you fight? (y/n):\n> ").lower().strip()
            while fight != "y" and fight != "n":
                print("\nInvalid choice, please select a valid option:")
                print("'y' for 'yes' or 'n' for 'no'.\n")
                fight = input("Do you fight?:\n> ").lower().strip()

            if fight == "y":
                use_potion()
                mini_boss_orc()
            else:
                print(
                    "You decided to try and flee the orc\n"
                    "...but as soon as you turned to open the door,\n"
                    "it kept attacking you and you died...")
                quit()

        if "Secret Completed" not in completed_tasks:

            # Prompts players to choose whether to take the stone
            if "Stone" not in inventory:
                print(
                    "You see a shiny looking stone around the orcs neck.\n"
                    "It could be important...\n")

                take_item = input("Do you take it? (y/n)\n> ").lower().strip()
                while take_item != "y" and take_item != "n":
                    print("\nInvalid choice, please select a valid option:")
                    print("'y' for 'yes' or 'n' for 'no'.\n")
                    print("You see a shiny looking stone around the orcs neck.")
                    take_item = input("Do you take it? (y/n)\n> ").lower().strip()

                if take_item == "y":
                    inventory.append("Stone")
                    print("You take the shiny looking stone.\n")
                    print(f"Current inventory:{inventory}\n")
                else:
                    print(
                        "\nYou decided to leave the stone...\n"
                        "hopefully it wasn't important.\n")
            else:
                print("You see the orc you defeated, and smile.\n")
        else:
            print("You see the orc you defeated, and smile.\n")

        print(
            "You look around and see 3 paths.\n"
            "You can go back west, go east or try going south.\n")

        # Player choice of direction
        direction = input("Which way do you go? (w/e/s)\n> ").lower().strip()
        while direction != "e" and direction != "s" and direction != "w":
            print("\nInvalid move, please enter a valid move:")
            print("'e' for 'east', 's' for 'south' or 'w' for 'west'.\n")
            direction = input("Which way do you go?:\n> ").lower().strip()

        if direction == "e":
            room_nine()
        elif direction == "s":
            room_eight()
        else:
            room_six_west()
    else:
        current_room = "Room Seven"
        print(f"Current room: {current_room}\n")

        view_stats()
        view_items()

        print("You see the orc you defeated, and smile.\n")

        print(
            "You look around and see 3 paths.\n"
            "You can go back west, go east or try going south.\n")

        # Player choice of direction
        direction = input("Which way do you go? (w/e/s)\n> ").lower().strip()
        while direction != "e" and direction != "s" and direction != "w":
            print("\nInvalid move, please enter a valid move:")
            print("'e' for 'east', 's' for 'south' or 'w' for 'west'.\n")
            direction = input("Which way do you go?:\n> ").lower().strip()

        if direction == "e":
            room_nine()
        elif direction == "s":
            room_eight()
        else:
            room_six_west()


def room_seven_completed():
    """
    Room seven:\n
    Only avaliable if boss defeated\n
    Secret room stone can be collected if not in inventory
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    current_room = "Room Seven"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    print(
        "You enter the room and see the orc you defeated on the ground.\n"
        "You take a moment to remember your triumph!\n")

    if "Secret Completed" not in completed_tasks:

        # Prompts players to choose whether to take the stone
        if "Stone" not in inventory:

            print(
                "You see a shiny looking stone around the orcs neck.\n"
                "It could be important...\n")

            take_item = input("Do you take it? (y/n)\n> ").lower().strip()
            while take_item != "y" and take_item != "n":
                print("\nInvalid choice, please select a valid option:")
                print("'y' for 'yes' or 'n' for 'no'.\n")
                print("You see a shiny looking stone around the orcs neck.")
                take_item = input("Do you take it? (y/n)\n> ").lower().strip()

            if take_item == "y":
                inventory.append("Stone")
                print("You take the shiny looking stone.\n")
                print(f"Current inventory:{inventory}\n")
            else:
                print(
                    "You decided to leave the stone...\n"
                    "hopefully it wasn't important.\n")
    else:
        print("You see the orc you defeated, and smile.\n")

    print(
        "You look around and see 3 paths.\n"
        "You can go back west, go east or try going south.\n")

    # Player choice of direction
    direction = input("Which way do you go? (w/e/s)\n> ").lower().strip()
    while direction != "e" and direction != "s" and direction != "w":
        print("\nInvalid move, please enter a valid move:")
        print("'e' for 'east', 's' for 'south' or 'w' for 'west'.\n")
        direction = input("Which way do you go?:\n> ").lower().strip()

    if direction == "e":
        room_nine()
    elif direction == "s":
        room_eight()
    else:
        room_six_west()


def room_eight():
    """
    Room eight:\n
    Player has choice to pick up a secret key
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    current_room = "Room Eight"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    print("You enter the room to the south.\n")

    if "Room Eight" not in completed_tasks:

        # Prompts user to take secret room key if not in inventory
        if "Secret Key" not in keys:
            print(
                "You see a key on a pedestal in the middle of the room.\n"
                "If you've learned anything so far about keys...\n"
                "They seem to be very useful!\n")
            take_item = input("Do you take the key? (y/n)\n> ").lower().strip()
            while take_item != "y" and take_item != "n":
                print("\nInvalid choice, please select a valid option:")
                print("'y' for 'yes' or 'n' for 'no'.\n")
                print("You see a key.")
                take_item = input("Do you take it? (y/n)\n> ").lower().strip()

            if take_item == "y":
                keys.append("Secret Key")
                completed_tasks.append("Room Eight")
                print("You took the key off the pedestal.")
                print(f"Current inventory:{keys}\n")
                print("Since there is nothing left to do, you head back.\n")
                room_seven_completed()
            else:
                print(
                    "\nYou decided to leave the key on the pedestal..."
                    "I hope it wasn't important...\n")
                print("Since there is nothing left to do, you head back.\n")
                room_seven_completed()
    else:
        print("You see an empty pedestal.\n")
        print("Since there is nothing left to do, you head back.\n")
        room_seven_completed()


def room_eight_secret():
    """
    Room eight:\n
    Only accessible through secret room
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    current_room = "Room Eight"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    print(
        "You enter the passgeway into a familar looking room.\n"
        "As soon as you go through the passageway it shuts behind you\n"
        "...guess you can't go back that way now.\n"
        "Ahead is the only way you can go.\n")
    room_seven_completed()


def room_nine():
    """
    Room nine:\n
    Player can choose to pick up the key (if not in inventory)\n
    Player can pick up potion (if not in inventory)\n
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    current_room = "Room Nine"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    print("You enter the room to the east and get an eerie feeling.\n")

    # Player prompted to take master key if not in inventory
    if "Master Key" not in keys:
        print(
            "You see a large glowing skeleton key on a pedestal...\n"
            "It looks pretty ominous...but important.\n")

        take_item = input("Do you take the key? (y/n)\n> ").lower().strip()
        while take_item != "y" and take_item != "n":
            print("\nInvalid choice, please select a valid option:")
            print("'y' for 'yes' or 'n' for 'no'.\n")
            print("You see a key.")
            take_item = input("Do you take it? (y/n)\n> ").lower().strip()

        if take_item == "y":
            keys.append("Master Key")
            print("You take the flowing skeleton key off the pedestal.")
            print(f"Current inventory:{keys}\n")
        else:
            print(
                "\nYou decided to leave the key on the pedestal..."
                "I hope it wasn't important...\n")
    else:
        print("You see an empty pedestal.\n")

    # Player prompted to take potion if not in inventory
    if "Potion" not in inventory:
        print(
            "\nYou look around and see something on the ground.\n"
            "You take a closer look and see it is a potion...\n"
            "it could be useful.\n")

        take_item = input("Do you take it? (y/n)\n> ").lower().strip()
        while take_item != "y" and take_item != "n":
            print("\nInvalid choice, please select a valid option:")
            print("'y' for 'yes' or 'n' for 'no'.\n")
            print("You see a potion on the ground, it could be useful...")
            take_item = input("Do you take it? (y/n)\n> ").lower().strip()

        if take_item == "y":
            inventory.append("Potion")
            completed_tasks.append("Room Nine")
            print(
                "\nYou take the potion and read the label.\n"
                "It reads: 'Health Potion'.\n"
                "Lucky you!\n")
            print(f"Current inventory:{inventory}\n")
        else:
            print(
                "You decided to leave the potion...\n"
                "I hope it wasn't important.\n")
    else:
        print("\nYou look around see nothing on the ground.\n")

    print(
        "You see a locked door ahead of you,\n"
        "with a skeleton shaped keyhole.\n"
        "You also feel a heat coming off that door...\n"
        "You can either go through the door or turn back west.\n")

    # Prompts player for direction choice
    direction = input("Which way do you go? (s/w)\n> ").lower().strip()
    while direction != "s" and direction != "w":
        print("\nInvalid move, please enter a valid move:")
        print("'s' for 'south' or 'w' for 'west'.\n")
        direction = input("Which way do you go? (s/w)\n> ").lower().strip()

    if direction == "w":
        room_seven_completed()
    else:
        boss_room()


def secret_room():
    """
    Secret Room:\n
    Requires secret key to enter\n
    Player can choose a master weapon\n
    Player can take armour - requires stone\n
    Tunnel to room 8 - revealed when armour is taken
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    if "Secret Completed" not in completed_tasks:
        if "Secret Key" not in keys:
            print("The door is locked and you need a key to open it.\n")
            room_three_completed()
        else:
            keys.remove("Secret Key")
            completed_tasks.append("Secret Completed")
            print("You use the key and open the door to the room\n")

        current_room = "Secret Room"
        print(f"Current room: {current_room}\n")

        view_stats()
        view_items()

    # Prompts players to pick up the master weapon
    if "Master Sword" not in weapons and "Master Bow" not in weapons:
        print(
            "You notice a table in the middle of the room.\n"
            "There are 2 weapons lying on the table.\n"
            "One is a longsword with a gem encrusted handle and a belt.\n"
            "The other is a longbow with a quiver full of arrows.\n\n"
            "There is an inscription on the table:\n"
            "Choose a weapon!\n")

        weapon = input("Which do you choose? (s/b)\n> ").lower().strip()
        while weapon != "s" and weapon != "b":
            print("\nInvalid choice, please select a valid option:")
            print("'s' for 'sword' or 'b' for 'bow'.\n")
            print("Choose a weapon!\n")
            weapon = input("Which do you choose?\n> ").lower().strip()

        if weapon == "s":
            weapons.append("Master Sword")
            if "Sword" in weapons:
                weapons.remove("Sword")  # If player switched weapons
                print(f"Current weapon:{weapons}\n")
                collect_armour()
            else:
                weapons.remove("Bow")  # If player switched weapons
                print(f"Current weapon:{weapons}\n")
                collect_armour()
        else:
            weapons.append("Master Bow")
            if "Bow" in weapons:
                weapons.remove("Bow")  # If player switched weapons
                print(f"Current weapon:{weapons}\n")
                collect_armour()
            else:
                weapons.remove("Sword")  # If player switched weapons
                print(f"Current weapon:{weapons}\n")
                collect_armour()
    else:
        current_room = "Secret Room"
        print(f"Current room: {current_room}\n")

        print("You see an empty table.\n")
        collect_armour()


def collect_armour():
    """
    Player to collect armour if not in inventory
    """
    if "Armour" not in inventory:

        if "Armour Unlocked" not in completed_tasks:

            if "Stone" in inventory:
                print(
                    "You see some armour leaning against the wall in a case.\n"
                    "There is some of slot in the wall next to it.\n"
                    "It seems like you need to place an item into the slot.\n")
                print(
                    "You remember about the stone you picked up.\n"
                    "You place the stone into the wall.\n"
                    "The case around the armour decends into the ground.\n")
                inventory.remove("Stone")
                completed_tasks.append("Armour Unlocked")
                completed_tasks.append("Secret Completed")

                take_item = input("Do you take it? (y/n)\n> ").lower().strip()
                while take_item != "y" and take_item != "n":
                    print("\nInvalid choice, please select a valid option:")
                    print("'y' for 'yes' or 'n' for 'no'.\n")
                    print("The armour can be taken.")
                    take_item = input("Take item? (y/n)\n> ").lower().strip()

                if take_item == "y":
                    inventory.append("Armour")
                    print(
                        "\nYou take the armour off the stand,\n"
                        "and put it on... You feel stronger")
                    print(f"Current inventory:{inventory}\n")
                    secret_passage()
                else:
                    print(
                        "\nYou decided to leave the armour...\n"
                        "let's hope it wasn't useful.\n")
                    room_three_completed()
            else:
                print(
                    "\nYou don't have the stone...\n"
                    "So you go back the way you came.\n")
                room_three_completed()
        else:
            print(
                "You see the armour on the stand,\n"
                "the case remains open.\n")
            take_item = input("Do you take it? (y/n)\n> ").lower().strip()
            while take_item != "y" and take_item != "n":
                print("\nInvalid choice, please select a valid option:")
                print("'y' for 'yes' or 'n' for 'no'.\n")
                print("The armour  on the stand.\n")
                take_item = input("Take item? (y/n)\n> ").lower().strip()

            if take_item == "y":
                inventory.append("Armour")
                print(
                    "\nYou take the armour off the stand,\n"
                    "and put it on... You feel stronger")
                print(f"Current inventory:{inventory}\n")
                secret_passage()
            else:
                print(
                    "You decided to leave the armour...\n"
                    "let's hope it wasn't useful.\n")
                room_three_completed()
    else:
        print("You see an empty armour stand.\n")
        secret_passage()


def secret_passage():
    """
    Players can use secret passage once armour been removed
    """
    print(
        "The wall then suddenly sides open...\n"
        "This reveals a passageway.\n")

    choice = input("Enter? (y/n)\n> ").lower().strip()
    while choice != "y" and choice != "n":
        print("\nInvalid choice, select a valid option:")
        print("'y' for 'yes' or 'n' for 'no'.\n")
        print("You look at the passageway.")
        choice = input("Enter? (y/n)\n> ").lower().strip()

    if choice == "y":
        room_eight_secret()
    else:
        print(
            "\nYou decide to not enter the passageway.\n"
            "The only way left to go is west.")
        room_three_completed()


def boss_room():
    """
    Master boss room:\n
    Requires master key to enter\n
    PLayer must defeat the boss to win and escape\n
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    if "Master Sword" not in weapons and "Master Bow" not in weapons:
        print("You need a master weapon to defeat the boss.")
        room_nine()
    else:
        if "Master Key" not in keys:
            print("The door is locked...try using the skeleton shaped key...\n")
            room_nine()
        else:
            keys.remove("Master Key")
            print("You use the key and open the door to the room\n")

        current_room = "Boss Room"
        print(f"Current room: {current_room}\n")

        view_stats()
        view_items()

        print(
            "You enter the room and the door shuts behind you.\n"
            "You start feeling very hot...\n"
            "You notice a huge dragon looking at you...\n"
            "it is ready to fight you!\n")

        print("What do you do?")
        fight = input("Do you fight? (y/n):\n> ").lower().strip()
        while fight != "y" and fight != "n":
            print("\nInvalid choice, please select a valid option:")
            print("'y' for 'yes' or 'n' for 'no'.\n")
            fight = input("Do you fight?:\n> ").lower().strip()

        if fight == "y":
            if "Armour" not in inventory:
                print("You don't have the armour on...\n")
                chance = input("Will you fight? (y/n)\n> ").lower().strip()
                while chance != 'y' and chance != 'n':
                    print("\nInvalid choice, please select a valid option:")
                    print("'y' for 'yes' or 'n' for 'no'.\n")
                    input("Will you fight? (y/n)\n> ").lower().strip()

                if chance == "y":
                    print("\nIf you're sure then...\n")
                    use_potion()
                    master_boss()
                else:
                    print(
                        "Good choice...\n"
                        "However it's too late now...\n"
                        "Should have picked it up when you had the chance.\n"
                        "The dragon eats you...\n"
                        "No one is surviving that...\n")
                    quit()
            else:
                print("You have the armour on...and feel ready!\n")
                use_potion()
                master_boss()
        else:
            print(
                "You decided to try and flee the dragon\n"
                "...but as soon as you turned to open the door,\n"
                "The dragon eats you...\n"
                "No one is surviving that...\n")
            quit()


def disarm(PLAYER_STAMINA):
    """
    Fire trap in room 1 - disarm option\n
    Reduces players stamina when disarming the trap
    """
    PLAYER_STAMINA = PLAYER_STAMINA - 5

    print(
        "\nYou see some stones on the ground and pick one up.\n"
        "You throw the stone at the target above the door.\n\n"
        "This action did take some of your stamnia.\n"
        "You were successful though.\n")
    print(Fore.YELLOW + f"You have {PLAYER_STAMINA}sp remaining.")
    print(Style.RESET_ALL)

    return PLAYER_STAMINA


def jump(PLAYER_STAMINA):
    """
    Fire trap in room 1 - jump option
    Reduces players health and stamina when jumping through the trap
    """
    global PLAYER_HP

    PLAYER_HP = PLAYER_HP - 100
    PLAYER_STAMINA = PLAYER_STAMINA - 50

    if PLAYER_HP < MIN_HP:
        print(
            "\nYour HP hit 0...\n"
            "You lost...")
        quit()
    else:
        print(
            "\nYou successfully jumped through the fire trap.\n"
            "However you did take significant damage.\n"
            "It did cost you some stamina as well.\n")
        print(Fore.RED + f"You have {PLAYER_HP}hp remaining.")
        print(Fore.YELLOW + f"You have {PLAYER_STAMINA}sp remaining.")
        print(Style.RESET_ALL)

    return PLAYER_HP and PLAYER_STAMINA


def swim(PLAYER_STAMINA):
    """
    River puzzle in room 2 - swim option\n
    Reduces players health and stamina when swimming through river
    """
    global PLAYER_HP
    PLAYER_HP = PLAYER_HP - 25
    PLAYER_STAMINA = PLAYER_STAMINA - 30

    if PLAYER_HP < MIN_HP:
        print(
            "\nYour HP hit 0...\n"
            "You lost...")
        quit()
    else:
        print(
            "\nYou succssfully swam through the river.\n"
            "You did feel something biting at you the whole time.\n"
            "You also took some damage.\n"
            "It did cost you some stamina as well.\n")
        print(Fore.RED + f"You have {PLAYER_HP}hp remaining.")
        print(Fore.YELLOW + f"You have {PLAYER_STAMINA}sp remaining.")
        print(Style.RESET_ALL)

    return PLAYER_HP and PLAYER_STAMINA


def hop(PLAYER_STAMINA):
    """
    River puzzle in room 2 - hop/jump option\n
    Reduces players health and stamina when jumping across river
    """
    global PLAYER_HP
    PLAYER_HP = PLAYER_HP - 5
    PLAYER_STAMINA = PLAYER_STAMINA - 10

    if PLAYER_HP < MIN_HP:
        print(
            "\nYour HP hit 0...\n"
            "You lost...")
        quit()
    else:
        print(
            "\nYou successfully jumped across the river.\n"
            "You however took minimal damage.\n"
            "It did cost you some stamina as well.\n")
        print(Fore.RED + f"You have {PLAYER_HP}hp remaining.")
        print(Fore.YELLOW + f"You have {PLAYER_STAMINA}sp remaining.")
        print(Style.RESET_ALL)

    return PLAYER_HP and PLAYER_STAMINA


def sword_attack():
    """
    Random damage for sword attack
    """
    global IMP_HP
    global ORC_HP
    global DRAGON_HP
    if "Sword" in weapons:
        sword_dmg = random.randrange(10, 21)
        sword_att = sword_dmg
        IMP_HP = IMP_HP - sword_att
        ORC_HP = ORC_HP - sword_att

        if "Imp" in current_boss:
            print("You attack the imp:")
            print(Fore.BLUE + "The imp took", sword_att, "damage.")
            if IMP_HP > MIN_HP:
                print(Fore.RED + f"The imp has {IMP_HP}hp remaining.")
                print(Style.RESET_ALL)
            else:
                print(Fore.RED + "The imp has 0hp remaining.\n")
                print(Style.RESET_ALL)

        if "Orc" in current_boss:
            print("You attack the orc:")
            print(Fore.BLUE + "The orc took", sword_att, "damage.")
            if ORC_HP > MIN_HP:
                print(Fore.RED + f"The orc has {ORC_HP}hp remaining.")
                print(Style.RESET_ALL)
            else:
                print(Fore.RED + "The orc has 0hp remaining.\n")
                print(Style.RESET_ALL)
    else:
        if "Master Sword" in weapons:
            master_sword_dmg = random.randrange(40, 56)
            master_sword_att = master_sword_dmg
            DRAGON_HP = DRAGON_HP - master_sword_att
            print("You attack the dragon:")
            print(Fore.BLUE + "The dragon took", master_sword_att, "damage.")
            if DRAGON_HP > MIN_HP:
                print(Fore.RED + f"The dragon has {DRAGON_HP}hp remaining.")
                print(Style.RESET_ALL)
            else:
                print(Fore.RED + "The dragon has 0hp remaining.\n")
                print(Style.RESET_ALL)


def bow_attack():
    """
    Random damage for bow attack
    """
    global IMP_HP
    global ORC_HP
    global DRAGON_HP
    if "Bow" in weapons:
        bow_dmg = random.randrange(10, 16)
        bow_att = bow_dmg
        IMP_HP = IMP_HP - bow_att
        ORC_HP = ORC_HP - bow_att

        if "Imp" in current_boss:
            print("You attack the imp:")
            print(Fore.BLUE + "The imp took", bow_att, "damage.")
            if IMP_HP > MIN_HP:
                print(Fore.RED + f"The imp has {IMP_HP}hp remaining.")
                print(Style.RESET_ALL)
            else:
                print(Fore.RED + "The imp has 0hp remaining.\n")
                print(Style.RESET_ALL)

        if "Orc" in current_boss:
            print("You attack the orc:")
            print(Fore.BLUE + "The orc took", bow_att, "damage.")
            if ORC_HP > MIN_HP:
                print(Fore.RED + f"The orc has {ORC_HP}hp remaining.")
                print(Style.RESET_ALL)
            else:
                print(Fore.RED + "The orc has 0hp remaining.\n")
                print(Style.RESET_ALL)
    else:
        if "Master Bow" in weapons:
            master_bow_dmg = random.randrange(35, 51)
            master_bow_att = master_bow_dmg
            DRAGON_HP = DRAGON_HP - master_bow_att
            print("You attack the dragon:")
            print(Fore.BLUE + "The dragon took", master_bow_att, "damage.")
            if DRAGON_HP > MIN_HP:
                print(Fore.RED + f"The dragon has {DRAGON_HP}hp remaining.")
                print(Style.RESET_ALL)
            else:
                print(Fore.RED + "The dragon has 0hp remaining.\n")
                print(Style.RESET_ALL)


def imp_attack():
    """
    Imp attack function
    """
    global PLAYER_HP
    random_attack = random.randrange(5, 16)
    imp_att = random_attack
    PLAYER_HP = PLAYER_HP - imp_att
    print("\nThe imp attacks you:")
    print(Fore.BLUE + "You took", imp_att, "damage.")
    if PLAYER_HP > MIN_HP:
        print(Fore.RED + f"You have {PLAYER_HP}hp remaining.\n")
        print(Style.RESET_ALL)
    else:
        print(Style.RESET_ALL)
        print("You have 0hp remaining.\n")
        print("The little imp managed to kill you...")
        quit()


def mini_boss_imp():
    """
    Mini boss fight for attack and damage stats
    """
    current_boss.append("Imp")
    print(
        "\nThe imp steps even closer towards you..."
        "smiling with weapon in hand...\n"
        "What do you do?")
    attack = input("Attack or flee? (a/f)\n> ").lower().strip()
    while attack != "a" and attack != "f":
        print("\nInvalid move, please enter a valid move:")
        print("'a' for 'attack' or 'f' for 'flee'.\n")
        attack = input("Attack or flee?:\n> ").lower().strip()

    if attack == "a":
        while PLAYER_HP != MIN_HP and IMP_HP != MIN_HP:
            imp_attack()
            sword_attack()
            bow_attack()
            if PLAYER_HP < MIN_HP:
                print("The little imp managed to kill you...")
                quit()
            elif IMP_HP < MIN_HP or IMP_HP == MIN_HP:
                print("You defeated the imp...Well done!\n")
                current_boss.remove("Imp")
                room_three_completed()
    else:
        print(
            "\nYou decided to flee...\n"
            "but the imp managed to kill you while you\n"
            "struggle to get the door open.")
        quit()


def jungle_puzzle(PLAYER_STAMINA):
    """
    Jungle puzzle in room 6 - vine option\n
    Reduces players stamina when cutting the vines\n
    Requires sword
    """
    PLAYER_STAMINA = PLAYER_STAMINA - 25

    if "Sword" not in weapons and "Master Sword" not in weapons:
        print(
            "\nThe vines are too thick to get through...\n"
            "It looks like you have to use the tunnel.\n")
        tunnel_puzzle(PLAYER_STAMINA)
    else:
        print(
            "\nYou successfully made your way through the vines.\n"
            "Chopping them as you make your way through...\n"
            "but they grow back as you pass.\n"
            "It did cost you some stamina though.\n")
        print(Fore.YELLOW + f"You have {PLAYER_STAMINA}sp remaining.")
        print(Style.RESET_ALL)

    return PLAYER_STAMINA


def tunnel_puzzle(PLAYER_STAMINA):
    """
    Tunnel puzzle in room 6 - tunnel option\n
    Reduces players health and stamina depending on choice
    """
    global PLAYER_HP

    print(
        "You see a huge branch coming towards you.\n"
        "What do you do?\n")

    trap = input("Jump or duck? (j/d)\n> ").lower().strip()
    while trap != "j" and trap != "d":
        print("\nInvalid choice, please select a valid option:")
        print("'j' for 'jump' or 'd' for 'duck'.\n")
        print(
            "You see a huge branch coming towards you.\n"
            "What do you do?")
        trap = input("Jump or duck? (j/d)\n> ").lower().strip()

    if trap == "j":
        PLAYER_STAMINA = PLAYER_STAMINA - 15
        print(
            "\nYou jumped over the low swinging branch\n"
            "It did cost you some stamina though.\n")
        print(Fore.YELLOW + f"You have {PLAYER_STAMINA}sp remaining.")
        print(Style.RESET_ALL)
    else:
        PLAYER_HP = PLAYER_HP - 30
        PLAYER_STAMINA = PLAYER_STAMINA - 15
        if PLAYER_HP < MIN_HP:
            print(
                "\nYour HP hit 0...\n"
                "You lost...")
            quit()
        else:
            print(
                "\nYou tried to duck...\n"
                "But it was a low swinging branch...\n"
                "You took some damage from getting hit.\n")
            print(Fore.RED + f"You have {PLAYER_HP}hp remaining.")
            print(Fore.YELLOW + f"You have {PLAYER_STAMINA}sp remaining.")
            print(Style.RESET_ALL)

    return PLAYER_HP and PLAYER_STAMINA


def orc_attack():
    """
    Orc attack function
    """
    global PLAYER_HP
    random_attack = random.randrange(10, 26)
    orc_att = random_attack
    PLAYER_HP = PLAYER_HP - orc_att
    print("\nThe orc attacks you:")
    print(Fore.BLUE + "You took", orc_att, "damage.")
    if PLAYER_HP > MIN_HP:
        print(Fore.RED + f"You have {PLAYER_HP}hp remaining.\n")
        print(Style.RESET_ALL)
    else:
        print(Style.RESET_ALL)
        print("You have 0hp remaining.\n")
        print("The orc managed to kill you...")
        quit()


def mini_boss_orc():
    """
    Mini boss fight for attack and damage stats
    """
    current_boss.append("Orc")
    print(
        "\nThe orc steps even closer towards you..."
        "smiling with weapon in hand...\n"
        "What do you do?")
    attack = input("Attack or flee? (a/f)\n> ").lower().strip()
    while attack != "a" and attack != "f":
        print("\nInvalid move, please enter a valid move:")
        print("'a' for 'attack' or 'd' for 'defend'.\n")
        attack = input("Attack for defend?:\n> ").lower().strip()

    if attack == "a":
        while PLAYER_HP != MIN_HP and ORC_HP != MIN_HP:
            orc_attack()
            sword_attack()
            bow_attack()
            if PLAYER_HP < MIN_HP:
                print("\nThe orc managed to kill you...")
                quit()
            elif ORC_HP < MIN_HP or ORC_HP == MIN_HP:
                print("You defeated the orc...Well done!\n")
                current_boss.remove("Orc")
                break
    else:
        print(
            "You decided to flee...\n"
            "but the orc managed to kill you while you\n"
            "struggle to get the door open.")
        quit()


def dragon_attack():
    """
    Dragon attack function
    """
    global PLAYER_HP_ARMOUR
    global PLAYER_HP
    if "Armour" in inventory:
        random_attack = random.randrange(35, 51)
        dragon_att = random_attack
        PLAYER_HP_ARMOUR = PLAYER_HP_ARMOUR - dragon_att
        print("The dragon attacks you:")
        print(Fore.BLUE + "You took", dragon_att, "damage.")
        if PLAYER_HP_ARMOUR > MIN_HP:
            print(Fore.RED + f"You have {PLAYER_HP_ARMOUR}hp remaining.\n")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + "You have 0hp remaining.")
            print(Style.RESET_ALL)
            print("The dragon managed to kill you...\n")
            print("Unfortunetly you could not escape the dungeon...")
            quit()
    else:
        random_attack = random.randrange(35, 51)
        dragon_att = random_attack
        PLAYER_HP = PLAYER_HP - dragon_att
        print("The dragon attacks you:")
        print(Fore.BLUE + "You took", dragon_att, "damage.")
        if PLAYER_HP > MIN_HP:
            print(Fore.RED + f"You have {PLAYER_HP}hp remaining.\n")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + "\nYou have 0hp remaining.")
            print(Style.RESET_ALL)
            print("The dragon managed to kill you...")
            print("Unfortunetly you could not escape the dungeon...")
            quit()


def master_boss():
    """
    Master boss fight for attack and damage stats
    """
    if "Armour" in inventory:
        current_boss.append("Dragon")
        attack = input("Attack or flee? (a/f)\n> ").lower().strip()
        while attack != "a" and attack != "f":
            print("\nInvalid move, please enter a valid move:")
            print("'a' for 'attack' or 'd' for 'defend'.\n")
            attack = input("Attack for defend?:\n> ").lower().strip()

        if attack == "a":
            while PLAYER_HP_ARMOUR != MIN_HP and DRAGON_HP != MIN_HP:
                dragon_attack()
                sword_attack()
                bow_attack()
                if PLAYER_HP_ARMOUR < MIN_HP:
                    print("The dragon managed to kill you...")
                    quit()
                elif DRAGON_HP < MIN_HP or DRAGON_HP == MIN_HP:
                    print(
                        "You defeated the dragon...Well done!\n"
                        "You look up and see the way out...\n"
                        "You have escaped and won the game!\n")
                    current_boss.remove("Dragon")
                    quit()
        else:
            print(
                "\nYou decided to flee...\n"
                "but the orc managed to kill you while you\n"
                "struggle to get the door open.")
            quit()
    else:
        current_boss.append("Dragon")
        attack = input("Attack or flee? (a/f)\n> ").lower().strip()
        while attack != "a" and attack != "f":
            print("\nInvalid move, please enter a valid move:")
            print("'a' for 'attack' or 'd' for 'defend'.\n")
            attack = input("Attack for defend?:\n> ").lower().strip()

        if attack == "a":
            while PLAYER_HP != MIN_HP and DRAGON_HP != MIN_HP:
                dragon_attack()
                sword_attack()
                bow_attack()
                if PLAYER_HP < MIN_HP:
                    print("\nThe dragon managed to kill you...")
                    quit()
                elif DRAGON_HP < MIN_HP or DRAGON_HP == MIN_HP:
                    print(
                        "You defeated the dragon...Well done!\n"
                        "You look up and see the way out...\n"
                        "You have escaped and won the game!\n")
                    current_boss.remove("Dragon")
                    quit()
        else:
            print(
                "\nYou decided to flee...\n"
                "but the orc managed to kill you while you\n"
                "struggle to get the door open.")
            quit()


def view_stats():
    """
    Asks player if they want to view their stats
    """
    if "Armour" not in inventory:
        stats = input("View your current stats? (y/n)\n> ").lower().strip()
        while stats != "y" and stats != "n":
            print("\nInvalid choice, please enter a valid choice:")
            print("'y' for 'yes or 'n' for 'no'.")
            stats = input("\nView your current stats? (y/n)\n> ").lower().strip()

        if stats == "y":
            print(f"\nYour current stats:")
            print(Fore.GREEN + f"You have {PLAYER_HP}hp remaining.")
            print(Fore.CYAN + f"You have {PLAYER_STAMINA}sp remaining.")
            print(Style.RESET_ALL)
        else:
            print("\nYou decided not to view your current stats.\n")
    else:
        stats = input("View your current stats? (y/n)\n> ").lower().strip()
        while stats != "y" and stats != "n":
            print("\nInvalid choice, please enter a valid choice:")
            print("'y' for 'yes or 'n' for 'no'.\n")
            stats = input("View your current stats? (y/n)\n> ").lower().strip()

        if stats == "y":
            print(f"\nYour current stats:")
            print(Fore.GREEN + f"You have {PLAYER_HP_ARMOUR}hp remaining.")
            print(Fore.CYAN + f"You have {PLAYER_STAMINA}sp remaining.")
            print(Style.RESET_ALL)
        else:
            print("\nYou decided not to view your current stats.\n")


def view_items():
    """
    Asks player if they want to view their items
    """
    items = input("View your current items? (y/n)\n> ").lower().strip()
    while items != "y" and items != "n":
        print("\nInvalid choice, please enter a valid choice:")
        print("'y' for 'yes or 'n' for 'no'.")
        items = input("\nView your current items? (y/n)\n> ").lower().strip()

    if items == "y":
        print(f"\nYour current items:")
        print(f"Inventory:{inventory}")
        print(f"Key inventory:{keys}")
        print(f"Weapon:{weapons}\n")
    else:
        print("\nYou decided not to view your current items.\n")


def fairy():
    """
    Conversation with the NPC fairy
    """
    print("You smile back at the fairy.")
    print("She says:")
    print(Fore.MAGENTA + f"'Hello {name}'")
    print(
        Fore.MAGENTA + "'The only escape is to defeat the evil dragon'\n"
        "'Only you can defeat him!'\n"
        "'I can tell you more about the dungeon...'\n")
    print(Style.RESET_ALL)

    talk = input("Would you like to learn more? (y/n)\n> ").lower().strip()
    while talk != "y" and talk != "n":
        print("\nInvalid choice, please select a valid option:")
        print("'y' for 'yes' or 'n' for 'no'.\n")
        print("The fairy looks at you.\n")
        talk = input("Would you like to learn more? (y/n)\n> ").lower().strip()

    if talk == "y":
        print(
            Fore.MAGENTA + "'There is a secret room in this dungeon'\n"
            "'To access that room you need a special key'\n"
            "'In that room you can find some strong weapons'\n"
            "'There is also a special piece of armour'\n"
            "'This will be needed to kill the dragon'\n"
            "'But you need a special stone to access it\n"
            "'The stone will also open a secret path'\n"
            "'That is all I can tell you.'\n")
        print(f"'Good luck {name}'")
        print(Style.RESET_ALL)
        print(
            "The fairy then disappears.\n"
            "The only path you can take is south.\n"
            "You head back south to the room you just came from.\n")
        room_three_completed()
    else:
        print(Fore.MAGENTA + "\n'That is okay...maybe next time")
        print(Style.RESET_ALL)
        print("The fairy then disappears.\n")
        print(
            "Hopefully what she wanted to say wasn't important.\n"
            "The only path you can take is south.\n"
            "You head back south to the room you just came from.\n")
        room_three_completed()


def use_potion():
    """
    Using potion to restore health
    """
    global PLAYER_HP
    if "Potion" not in inventory:
        print("You don't have any health potions to use...\n")
    else:
        print("You have health potions in your inventory.\n")
        print(f"Inventory:{inventory}\n")
        use_potion = input("Use a potion? (y/n)\n> ").lower().strip()
        while use_potion != "y" and use_potion != "n":
            print("\nInvalid choice, please enter a valid choice:")
            print("'y' for 'yes or 'n' for 'no'.\n")
            input("Use a potion? (y/n)\n> ").lower().strip()

        if use_potion == "y":
            if PLAYER_HP == MAX_HP:
                print("Your health is full...\n")
            else:
                inventory.remove("Potion")
            print(
                "\nYou drink the health potion and your "
                "health is restored to the max.\n")
            if PLAYER_HP < MAX_HP:
                PLAYER_HP += 200
                if PLAYER_HP > MAX_HP:
                    PLAYER_HP = MAX_HP
        else:
            print("\nYou decide not to drink a health potion.\n")


# Player welcome screen
clear()
name = input("Type your name:\n> ").capitalize().strip()
clear()
start_game()
starting_room()
