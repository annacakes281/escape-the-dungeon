import random
import os

# Player health and stamina - need potion to restore health
MAX_HP = 150
PLAYER_HP = 145
PLAYER_STAMINA = 50  # this restores on its own

# Armour hp - this can decrease with damage
armour_hp = 100

# List to keep track on inventory items
inventory = ["Potion"]
weapons = []
keys = []


def clear():
    """
    Clears terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


def clear_terminal():
    """
    Prompts players whether they want to cleat terminal
    """
    print("\nType 'y' to clear the terminal:")
    clear_term = input("Clear the terminal?\n> ").lower().strip()
    if clear_term == "y":
        clear()
    # add an else


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
    current_room = "Starting Room"
    print(f"Current room: {current_room}\n")

    use_potion(PLAYER_HP)

    view_stats()
    view_items()

    print(
        "You look around in the dimmly lit room and see 3 possible paths.\n"
        "You can either go north, south or east.\n")

    print("Remember you can type just the first letter of the word.\n")

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
    # global PLAYER_HP
    clear_terminal()
    # global hp global stamina

    print("\nRemember you just need to type the first letter of the word.\n")

    current_room = "Room One"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    print("You enter the room to the north.\n")


    # Prompts user to collect key, if not in inventory
    if "Key 1" not in keys:
        print("You see a key on a pedestal... it could be important.")
        take_item = input("Do you take it? (y/n)\n> ").lower().strip()
        while take_item != "y" and take_item != "n":
            print("\nInvalid choice, please select a valid option:")
            print("'y' for 'yes' or 'n' for 'no'.\n")
            print("You see a key on a pedestal... it could be important.")
            take_item = input("Do you take it?\n> ").lower().strip()

        if take_item == "y":
            keys.append("Key 1")
            print("\nYou picked up the key and added it to your bag.")
            print(f"Current key inventory:{keys}\n")
        else:
            print(
                "\nYou decided to leave the key on the pedestal..."
                "I hope it wasn't important...\n")
    else:
        print("You see an empty pedestal.\n")

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
                disarm(PLAYER_STAMINA)  # format text
            else:
                jump(PLAYER_HP, PLAYER_STAMINA)  # format text
        else:
            print("\nYou choose the bow and attached it to your back.\n")
            weapons.append("Bow")
            print(f"Current required items:{weapons}\n")

            # Choosing weapon will trigger a trap
            print(
                "Picking up your weapon sets off a trap.\n"
                "A wall of fire is blocking the way out.\n")

            # possibly use bow and arrow and remove one arrow from invt.
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
                disarm(PLAYER_STAMINA)  # format text
            else:
                jump(PLAYER_HP, PLAYER_STAMINA)  # format text

    else:
        print("You see an empty table.\n")

    print("There is nothing left to do in this room.\n")
    print("So you head south back to the room you started in.\n")
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
        "Do you swim across the river, or"
        "take your chances and jump across the pillars?\n")
    trap = input("Swim or jump? (s/j)\n> ").lower().strip()
    while trap != "s" and trap != "j":
        print("\nInvalid choice, please select a valid option:")
        print("'s' for 'swim' or 'j' for 'jump'.\n")
        trap = input("Swim or jump? (s/j)\n> ").lower().strip()

    if trap == "s":
        swim(PLAYER_HP, PLAYER_STAMINA)  # need to format
    else:
        hop(PLAYER_HP, PLAYER_STAMINA)  # need to format

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
            swim(PLAYER_HP, PLAYER_STAMINA)  # need to format
            starting_room()
        else:
            hop(PLAYER_HP, PLAYER_STAMINA)  # need to format
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

    print(
        "You head back west.\n"
        "Looks like you have to cross the river...again.\n"
        "Will you jump or swim across?\n")

    # Players must choose to swim or jump for this puzzle
    trap = input("Swim or jump? (s/j)\n> ").lower().strip()
    while trap != "s" and trap != "j":
        print("\nInvalid choice, please select a valid option:")
        print("'s' for 'swim' or 'j' for 'jump'.\n")
        trap = input("Swim or jump? (s/j)\n> ").lower().strip()

    if trap == "s":
        swim(PLAYER_HP, PLAYER_STAMINA)  # need to format
    else:
        hop(PLAYER_HP, PLAYER_STAMINA)  # need to format

    # Player can choose to take potion if not in inventory
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
        print(
            "You cross the river and look around...\n"
            "you see nothing on the ground.\n"
            )

    print("After crossing the river you head back north.\n")
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
    if "Key 1" not in keys:
        print("The door is locked and you need a key to open it.\n")
        room_two_west()
    else:
        keys.remove("Key 1")
        print("You use the key and open the door to the room\n")

        current_room = "Room Three"
        print(f"Current room: {current_room}\n")

        view_stats()
        view_items()

        print(
            "You enter the room and the door shuts behind you.\n"
            "You notice an imp looking at you... it is ready to fight you!\n"
            )
        # Prompts players whether they fight the mini boss
        print("What do you do?")
        fight = input("Do you fight? (y/n):\n> ").lower().strip()
        while fight != "y" and fight != "n":
            print("\nInvalid choice, please select a valid option:")
            print("'y' for 'yes' or 'n' for 'no'.\n")
            fight = input("Do you fight?:\n> ").lower().strip()

        if fight == "y":
            mini_boss_imp()  # code and format
        else:
            print(
                "You decided to try and flee the imp\n"
                "...but as soon as you turned to open the door,\n"
                "it kept attacking you and you died...")
            quit()

        # Promps players to choose a direction
        print("You look around and can go north, east or west.\n")
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
    print("You look around and can go north, east, or west.\n")
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

    current_room = "Room four"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    # Prompsts player to take key if not in inventory
    if "Key 2" not in keys:
        print("You see a key on a pedestal... it could be important.")
        take_item = input("Do you take it? (y/n)\n> ").lower().strip()
        while take_item != "y" and take_item != "n":
            print("\nInvalid choice, please select a valid option:")
            print("'y' for 'yes' or 'n' for 'no'.\n")
            print("You see a key on a pedestal... it could be important.\n")
            take_item = input("Do you take it?\n> ").lower().strip()

        if take_item == "y":
            keys.append("Key 2")
            print("\nYou picked up the key and added it to your bag.")
            print(f"Current key inventory:{keys}\n")
        else:
            print(
                "\nYou decided to leave the key on the pedestal..."
                "I hope it wasn't important...\n")
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
            "Hopefully she had nothing important to say.\n"
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
        "There are only 2 ways to go, north or west.\n")

    # Prompts user to choose a direction to go
    direction = input("Which way do you go? (n/w)\n> ").lower().strip()
    while direction != "n" and direction != "w":
        print("\nInvalid move, please enter a valid move:")
        print("'n' for 'north' or 'w' for 'west'.\n")
        direction = input("Which way do you go?:\n> ").lower().strip()

    if direction == "n":
        room_six()
    else:
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

    view_stats()
    view_items()

    print(
        "You head south and enter an empty room that smells musty.\n"
        "There are only 2 ways to go, north or west.\n")

    # Prompts user to choose a direction to go
    direction = input("Which way do you go? (n/w)\n> ").lower().strip()
    while direction != "n" and direction != "w":
        print("\nInvalid move, please enter a valid move:")
        print("'n' for 'north' or 'w' for 'west'.\n")
        direction = input("Which way do you go?:\n> ").lower().strip()

    if direction == "n":
        room_six()
    else:
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
        jungle_puzzle(PLAYER_STAMINA)  # need to format
    else:
        tunnel_puzzle(PLAYER_HP, PLAYER_STAMINA)  # need to format

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
            jungle_puzzle(PLAYER_STAMINA)  # need to format
        else:
            tunnel_puzzle(PLAYER_HP, PLAYER_STAMINA)  # need to format
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
        jungle_puzzle(PLAYER_STAMINA)  # need to format
    else:
        tunnel_puzzle(PLAYER_HP, PLAYER_STAMINA)  # need to format

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
            jungle_puzzle(PLAYER_STAMINA)  # need to format
        else:
            tunnel_puzzle(PLAYER_HP, PLAYER_STAMINA)  # need to format
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

    # Player must have key to enter
    if "Key 2" not in keys:
        print("The door is locked and you need a key to open it.\n")
        room_six_west()
    else:
        keys.remove("Key 2")
        print("You use the key and open the door to the room\n")

        current_room = "Room Seven"
        print(f"Current room: {current_room}\n")

        view_stats()
        view_items()

        print(
            "You enter the room and the door shuts behind you.\n"
            "You notice an orc looking at you... it is ready to fight you!\n"
            )
        # Prompts players whether they fight the mini boss
        print("What do you do?")
        fight = input("Do you fight? (y/n):\n> ").lower().strip()
        while fight != "y" and fight != "n":
            print("\nInvalid choice, please select a valid option:")
            print("'y' for 'yes' or 'n' for 'no'.\n")
            fight = input("Do you fight?:\n> ").lower().strip()

        if fight == "y":
            mini_boss_orc()  # code and format
        else:
            print(
                "You decided to try and flee the orc\n"
                "...but as soon as you turned to open the door,\n"
                "it kept attacking you and you died...")
            quit()

        # Prompts players to choose whether to take the stone
        if "Secret Stone" not in inventory:

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

    # Prompts players to choose whether to take the stone
    if "Secret Stone" not in inventory:

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
        "You look around and see 3 paths."
        "You can go back west, go east or try going south.")

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
            print("You took the key off the pedestal.")
            print(f"Current inventory:{keys}\n")
            print("Since there is nothing left to do here, you head back.\n")
            room_seven_completed()
        else:
            print(
                "\nYou decided to leave the key on the pedestal..."
                "I hope it wasn't important...\n")
            print("Since there is nothing left to do here, you head back.\n")
            room_seven_completed()
    else:
        print("You see an empty pedestal.\n")
        print("Since there is nothing left to do here, you head back.\n")
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
    Tunnel to room 8 - revealled when armour is taken
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

    if "Secret Key" not in keys:
        print("The door is locked and you need a key to open it.\n")
        room_three_completed()
    else:
        keys.remove("Secret Key")
        print("You use the key and open the door to the room\n")

        current_room = "Secret Room"
        print(f"Current room: {current_room}\n")

        view_stats()
        view_items()

        # Prompts players to choose a new weapon
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

            if weapon == "sword":
                weapons.append("Master Sword")
                weapons.remove("Sword")  # If player switched weapons
                weapons.remove("Bow")  # If player switched weapons
                print(f"Current inventory:{weapons}")
            else:
                weapons.append("Master Bow")
                weapons.remove("Bow")  # If player switched weapons
                weapons.remove("Sword")  # If player switched weapons
                print(f"Current inventory:{weapons}")
        else:
            print("You see an empty table.\n")

        print(
            "You see some armour leaning against the wall in a case.\n"
            "There is some of slot in the wall next to it.\n"
            "It seems like you need to place an item into the slot.\n")

        # Prompt whether players take the armour - requires stone
        if "Stone" in inventory:
            print("You don't have the stone to unlock the armour.\n")

            if "Armour" not in inventory:
                print(
                    "You place the stone into the wall.\n"
                    "The case around the armour decends into the ground.\n")
                inventory.remove("Stone")
                take_item = input("Do you take it? (y/n)\n> ").lower().strip()
                while take_item != "y" and take_item != "n":
                    print("\nInvalid choice, please select a valid option:")
                    print("'y' for 'yes' or 'n' for 'no'.\n")
                    print("The armour can be taken.")
                    take_item = input("Take item? (y/n)\n> ").lower().strip()

                if take_item == "y":
                    inventory.append("Armour")
                    print(
                        "You take the armour off the stand,\n"
                        "and put it on... You feel stronger")
                    print(f"Current inventory:{inventory}\n")

                    print(
                        "The wall then suddenly sides open...\n"
                        "This reveals a passageway.\n")

                    direction = input("Enter? (y/n)\n> ").lower().strip()
                    while direction != "y" and direction != "n":
                        print("\nInvalid choice, select a valid option:")
                        print("'y' for 'yes' or 'n' for 'no'.\n")
                        print("You look at the passageway.")
                        direction = input("Enter? (y/n)\n> ").lower().strip()

                    if direction == "y":
                        room_eight_secret()
                    else:
                        print(
                            "You decide to not enter the passageway.\n"
                            "The only way left to go is west.")
                        room_three_completed()

                else:
                    print(
                        "You decided to leave the armour...\n"
                        "let's hope it wasn't useful.\n")
            else:
                print(
                    "You see an empty armour stand.\n"
                    "You also see a passageway revealed.\n")

                direction = input("Do you enter? (y/n)\n> ").lower().strip()
                while direction != "y" and direction != "n":
                    print("\nInvalid choice, please select a valid option:")
                    print("'y' for 'yes' or 'n' for 'no'.\n")
                    print("You look at the passageway.")
                    direction = input("Enter? (y/n)\n> ").lower().strip()

                if direction == "y":
                    room_eight_secret()
                else:
                    print(
                        "You decide to not enter the passageway.\n"
                        "The only way left to go is west.")
                    room_three_completed()
        else:
            print("You need a small item to insert into the wall.\n")
            print("West is the only way you can go.")
            room_three_completed()


def boss_room():
    """
    Master boss room:\n
    Requires master key to enter\n
    PLayer must defeat the boss to win and escape\n
    """
    clear_terminal()

    print("\nRemember you just need to type the first letter of the word.\n")

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
                    print("If you're sure then...\n")
                    master_boss()  # code and format
                else:
                    print(
                        "Good choice...\n"
                        "However it's too late now...\n"
                        "Should have picked it up when you had the chance.\n"
                        "The dragon eats you...\n"
                        "No one is surviving that...\n")
                    quit()
        else:
            print(
                "You decided to try and flee the dragon\n"
                "...but as soon as you turned to open the door,\n"
                "The dragon eats you...\n"
                "No one is surviving that...\n")
            quit()


def disarm_sp_loss(PLAYER_STAMINA):
    """
    Reduces players stamina when disarming the trap
    """
    PLAYER_STAMINA = PLAYER_STAMINA - 5
    return PLAYER_STAMINA


def disarm(PLAYER_STAMINA):
    """
    Disarm fire trap with stone
    """
    PLAYER_STAMINA = disarm_sp_loss(PLAYER_STAMINA)
    print(
        "You see some stones on the ground and pick one up.\n"
        "You throw the stone at the target above the door.\n"
        "This action did take some of your stamnia.\n")
    # if not doing random do a statement saying successful
    print(f"{PLAYER_STAMINA}sp\n")


def jump_hp_loss():
    """
    Reduces players health when jumping through the trap
    """
    global PLAYER_HP
    PLAYER_HP = PLAYER_HP - 100
    return PLAYER_HP


def jump_sp_loss(PLAYER_STAMINA):
    """
    Reduces players stamina when jumping through the trap
    """
    PLAYER_STAMINA = PLAYER_STAMINA - 50
    return PLAYER_STAMINA


def jump(PLAYER_HP, PLAYER_STAMINA):
    """
    Jump through fire trap
    """
    PLAYER_HP = jump_hp_loss()
    PLAYER_STAMINA = jump_sp_loss(PLAYER_STAMINA)
    print(
        "You successfully jumped through the fire trap.\n"
        "However you did take significant damage.\n")
    print(f"{PLAYER_HP}hp")
    print(f"{PLAYER_STAMINA}sp\n")


def swim_hp_loss():
    """
    Reduces players health when swimming through river
    """
    global PLAYER_HP
    PLAYER_HP = PLAYER_HP - 25
    return PLAYER_HP


def swim_sp_loss(PLAYER_STAMINA):
    """
    Reduces players stamina when disarming the trap
    """
    PLAYER_STAMINA = PLAYER_STAMINA - 30
    return PLAYER_STAMINA


def swim(PLAYER_HP, PLAYER_STAMINA):
    """
    Swim through river
    """
    PLAYER_HP = swim_hp_loss()
    PLAYER_STAMINA = swim_sp_loss(PLAYER_STAMINA)
    print(
        "You succssfully swam through the river.\n"
        "You did feel something biting at you the whole time.\n"
        "You also took some damage.\n"
        )
    print(f"{PLAYER_HP}hp")
    print(f"{PLAYER_STAMINA}sp\n")


def hop_hp_loss():
    """
    Reduces players health when jumping on pillars
    """
    global PLAYER_HP
    PLAYER_HP = PLAYER_HP - 5
    return PLAYER_HP


def hop_sp_loss(PLAYER_STAMINA):
    """
    Reduces players stamina when jumping on pillars
    """
    PLAYER_STAMINA = PLAYER_STAMINA - 10
    return PLAYER_STAMINA


def hop(PLAYER_HP, PLAYER_STAMINA):
    """
    Hop across pillars in river
    """
    PLAYER_HP = hop_hp_loss()
    PLAYER_STAMINA = hop_sp_loss(PLAYER_STAMINA)
    print(
        "You succssfully hopped across the river.\n"
        "You however took minimal damage.\n"
        )
    print(f"{PLAYER_HP}hp")
    print(f"{PLAYER_STAMINA}sp\n")


def mini_boss_imp():
    """
    Mini boss fight for attack and damage stats
    """
    # combat function - hit each time
    # damage stats for weapons
    # while loop until hp loss
    # choice to attack/def, attack/run
    # break loop if boss/player hp low, or player flee
    # use randrange for dmg - all within while true loop
    # seperate function for weapon dmg
    print("mini boss fight")


def jungle_sp_loss(PLAYER_STAMINA):
    """
    Reduces players stamnia when going through jungle
    """
    PLAYER_STAMINA = PLAYER_STAMINA - 25
    return PLAYER_STAMINA


def jungle_puzzle(PLAYER_STAMINA):
    """
    Jungle puzzle in room 6
    """
    if "Sword" not in weapons:
        print(
            "The vines are too thick to get through...\n"
            "It looks like you have to use the tunnel.\n")
        tunnel_puzzle(PLAYER_HP, PLAYER_STAMINA)
    else:
        PLAYER_STAMINA = jungle_sp_loss(PLAYER_STAMINA)
        print(
            "You successfully made your way through the vines.\n"
            "Chopping them as you make your way through...\n"
            "but they grow back as you pass.\n")
        print(f"{PLAYER_STAMINA}sp\n")


def tunnel_hp_loss():
    """
    Reduces players health when going through tunnel
    """
    global PLAYER_HP
    PLAYER_HP = PLAYER_HP - 30
    return PLAYER_HP


def tunnel_sp_loss(PLAYER_STAMINA):
    """
    Reduces players stamina when going through tunnel
    """
    PLAYER_STAMINA = PLAYER_STAMINA - 15
    return PLAYER_STAMINA


def tunnel_puzzle(PLAYER_HP, PLAYER_STAMINA):
    """
    Tunnel puzzle, linked to jungle puzzle in room 6
    """
    print(
        "You see a huge branch coming towards you.\n"
        "What do you do?")

    trap = input("Jump or duck? (j/d)\n> ").lower().strip()
    while trap != "j" and trap != "d":
        print("\nInvalid choice, please select a valid option:")
        print("'j' for 'jump' or 'd' for 'duck'.\n")
        print(
            "You see a huge branch coming towards you.\n"
            "What do you do?")
        trap = input("Jump or duck? (j/d)\n> ").lower().strip()

    if trap == "j":
        PLAYER_STAMINA = tunnel_sp_loss(PLAYER_STAMINA)
        print("You jumped over the low swinging branch")
        print(f"{PLAYER_STAMINA}sp")
    else:
        PLAYER_HP = tunnel_hp_loss()
        PLAYER_STAMINA = tunnel_sp_loss(PLAYER_STAMINA)
        print(
            "You tried to duck...\n"
            "But it was a low swinging branch...\n"
            "You took some damage from getting hit.\n")
        print(f"{PLAYER_HP}hp")
        print(f"{PLAYER_STAMINA}sp")


def mini_boss_orc():
    """
    Mini boss fight for attack and damage stats
    """
    print("mini boss fight")


def master_boss():
    """
    Master boss fight for attack and damage stats
    """
    print("master boss fight")


def view_stats():
    """
    Asks player if they want to view their stats
    """
    stats = input("View your current stats? (y/n)\n> ").lower().strip()
    while stats != "y" and stats != "n":
        print("\nInvalid choice, please enter a valid choice:")
        print("'y' for 'yes or 'n' for 'no'.")
        stats = input("\nView your current stats? (y/n)\n> ").lower().strip()

    if stats == "y":
        print(f"\nYour current stats:")
        print(f"{PLAYER_HP}hp")
        print(f"{PLAYER_STAMINA}sp\n")
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
    print("You smile back at the fairy and say 'hello'")
    print("She says:")
    print(f"'Hello {name}'")
    print(
        "'The only escape is to defeat the evil dragon'\n"
        "'Only you can defeat him!'\n"
        "'I can tell you more about the dungeon...'\n")

    talk = input("Would you like to learn more? (y/n)\n> ").lower().strip()
    while talk != "y" and talk != "n":
        print("\nInvalid choice, please select a valid option:")
        print("'y' for 'yes' or 'n' for 'no'.\n")
        print("The fairy looks at you.\n")
        talk = input("Would you like to learn more? (y/n)\n> ").lower().strip()

    if talk == "y":
        print(
            "'There is a secret room in this dungeon'\n"
            "'To access that room you need a special key'\n"
            "'In that room you can find some strong weapons'\n"
            "'There is also a special piece of armour'\n"
            "'This will be needed to kill the dragon'\n"
            "'But you need a special stone to access it\n"
            "'The stone will also open a secret path'\n"
            "'That is all I can tell you.'\n")
        print(f"'Good luck {name}")
        print(
            "The fairy then disappears.\n"
            "The only path you can take is south.\n"
            "You head back south to the room you just came from.\n")
        room_three_completed()
    else:
        print("\n'That is okay...maybe next time\n")
        print("The fairy then disappears.\n")
        print(
            "Hopefully what she wanted to say wasn't important.\n"
            "The only path you can take is south.\n"
            "You head back south to the room you just came from.\n")
        room_three_completed()



def use_potion(PLAYER_HP):
    """
    Using potion to restore health
    """
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
                "You drink the health potion and your "
                "health is restored to the max.\n")
            if PLAYER_HP != MAX_HP:
                PLAYER_HP += 100
                print(f"{PLAYER_HP}")
        else:
            print("You decide not to drink a health potion.\n")


# Player welcome screen
clear()
name = input("Type your name:\n> ").capitalize().strip()
clear()
start_game()
starting_room()


# def stamina_regen():
#     """
#     Regeneration of stamina per turn
#     """
#     if statement? - simialr to hp restore


# def player_attack():
#     """
#     Random damage for player attack
#     """


# Left to add:
# boss attack random hits
# player attack random hits
# stamina regen per turn IF not at max
# use potion before boss room IF not at max
# story for boss attacks
# rather than quit when die, play again statement that takes to game start
# refactor hp/sp loss once everything working

# Questions to ask:
# should i make sperate functions if function too long?
# if statement for boss defeated rather than different rooms?
# randomise whether stone hits tatget?
# is there a way to randomise jump/duck option?
# how to keep health/stamina bar the changed values
