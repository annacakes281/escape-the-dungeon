import random
import os

# Player health and stamina - fix so that it changes with damage and potion
player_hp = 150
player_stamina = 50

# List to keep track on invetory items
inventory = []
weapons = []
keys = []


def clear():
    """
    Clears terminal
    """
    os.system("cls" if os.name == "nt" else "clear")


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
    clear()

    print("Remember you just need to type the first letter of the word.\n")

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
            print("\nYou decided to leave the key on the pedestal.\n")
    else:
        print("You see an empty pedestal.\n")
    
    # Prompts user to choose their weapon, if not in inventory
    if "Sword" not in weapons and "Bow" not in weapons:
        print(
            "You notice a table in the middle of the room.\n"
            "There are 2 weapons lying on the table.\n"
            "One is a broadsword with a gem encrusted handle and a belt.\n"
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
                disarm(player_stamina)  # format text
            else:
                jump(player_hp, player_stamina)  # format text
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
                disarm(player_stamina)  # format text
            else:
                jump(player_hp, player_stamina)  # format text
            
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
    clear()

    print("Remember you just need to type the first letter of the word.\n")

    current_room = "Room Two"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    print(
        "You enter the room to the South and come to a river.\n"
        "You can either swim through the river, it looks safe...enough.\n"
        "Or you can jump across the pillars sticking out the river,\n"
        "although they look a bit unsafe.\n")

    print(
        "Do you swim across the river, or"
        "take your chances and jump across the pillars?\n")

    # Players must choose to swim or jump for this puzzle
    trap = input("Swim or jump? (s/j)\n> ").lower().strip()
    while trap != "s" and trap != "j":
        print("\nInvalid choice, please select a valid option:")
        print("'s' for 'swim' or 'j' for 'jump'.\n")
        trap = input("Swim or jump? (s/j)\n> ").lower().strip()

    if trap == "s":
        swim(player_hp, player_stamina)  # need to format
    else:
        hop(player_hp, player_stamina)  # need to format

    # Prompts player to take potion of not in inventory
    if "Potion 1" not in inventory:
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
            inventory.append("Potion 1")
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
        "You can either follow the path East or go back North.\n"
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
            swim(player_hp, player_stamina)  # need to format
            starting_room()
        else:
            hop(player_hp, player_stamina)  # need to format
            starting_room()
    else:
        room_three()


def room_two_west():
    """
    Room two:\n
    Only avaliable if player enters room 2 from room 3
    Player choices to either swim across lake or jump across pedestals\n
    Player can choose to pick up health potion\n
    """
    clear()

    print("Remember you just need to type the first letter of the word.\n")

    current_room = "Room Two"
    print(f"Current room: {current_room}\n")

    view_stats()
    view_items()

    print(
        "You head back West.\n"
        "Looks like you have to cross the river...again.\n"
        "Will you jump or swim across?\n")

    # Players must choose to swim or jump for this puzzle
    trap = input("Swim or jump? (s/j)\n> ").lower().strip()
    while trap != "s" and trap != "j":
        print("\nInvalid choice, please select a valid option:")
        print("'s' for 'swim' or 'j' for 'jump'.\n")
        trap = input("Swim or jump? (s/j)\n> ").lower().strip()

    if trap == "s":
        swim(player_hp, player_stamina)  # need to format
    else:
        hop(player_hp, player_stamina)  # need to format

    # Player can choose to take potion if not in inventory
    if "Potion 1" not in inventory:
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
            inventory.append("Potion 1")
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
    clear()

    print("Remember you just need to type the first letter of the word.\n")

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

    print("Remember you just need to type the first letter of the word.\n")

    current_room = "Room Three"
    print(f"Current room: {current_room}")

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
    clear()

    print("Remember you just need to type the first letter of the word.\n")
  
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
            print("\nYou decided to leave the key on the pedestal.\n")
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
            "\nYou decide not to speak to the fairy"
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

    clear()

    print("Remember you just need to type the first letter of the word.\n")

    current_room = "Room Five"
    print(f"Current room: {current_room}")

    view_stats()
    view_items()

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


def room_six():
    """
    Room six:\n
    Player choices to either to ho through jungle but this requires sword
    or player can go through the tunnel\n
    Player has option to pick up a potion if not in inventory
    """
    clear()

    print("Remember you just need to type the first letter of the word.\n")

    current_room = "Room Six"
    print(f"Current room: {current_room}")
    
    print("Jungle puzzle")
    
    trap = input("go through or way around?").lower().strip()
    while trap != "through" and trap != "around":
        print("You must choose to do something.")
        trap = input("go through or way around?").lower().strip()

    if trap == "through":
        jungle_puzzle(player_stamina)
    else:
        tunnel_puzzle(player_hp, player_stamina)

    if "Potion 2" not in inventory:
        take_item = input("You see a potion, do you take it? (yes/no)").lower().strip()
        while take_item != "yes" and take_item != "no":
            take_item = input("You see a potion, do you take it? (yes/no)").lower().strip()

        if take_item == "yes":
            inventory.append("Potion 2")
            print(f"Current inventory:{inventory}")
        else:
            print("You left the potion")
    else:
        print("you have the potion")
        print(f"Current inventory:{inventory}")

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

    print("Remember you just need to type the first letter of the word.\n")
    if "Key 2" not in required_items:
        print("You need the key and a weapon to pass")
        room_five()
    else:
        required_items.remove("Key 2")
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

        if "Secret Stone" not in required_items:
            take_item = input("You see a stone, do you take it? (yes/no)").lower().strip()
            while take_item != "yes" and take_item != "no":
                take_item = input("You see a stone, do you take it? (yes/no)").lower().strip()

            if take_item == "yes":
                required_items.append("Stone")
                print(f"Current inventory:{required_items}")
            else:
                print("You left the stone")
        else:
            print("you have the stone")
            print(f"Current inventory:{required_items}")

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


def room_seven_completed():

    print("Remember you just need to type the first letter of the word.\n")
    current_room = "Room Seven"
    print("The mini boss of this room has already been defeated...Yay!")
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

    print("Remember you just need to type the first letter of the word.\n")
    current_room = "Room Eight"
    print(f"Current room: {current_room}")

    if "Secret Key" not in required_items:
        take_item = input("You see a key, do you take it? (yes/no)").lower().strip()
        while take_item != "yes" and take_item != "no":
            take_item = input("You see a key, do you take it? (yes/no)").lower().strip()

        if take_item == "yes":
            required_items.append("Secret Key")
            print(f"Current inventory:{required_items}")
        else:
            print("You left the key")
    else:
        print("you have the key")
        print(f"Current inventory:{required_items}")

    print("You can only go North.")
    direction = input("Which way do you go?:\n").lower().strip()
    while direction != "north":
        print("You can only go North.")
        direction = input("Which way do you go?:\n").lower().strip()

    if direction == "north":
        room_seven_completed()


def room_nine():
    """
    Room nine - key and item
    """
    print("Remember you just need to type the first letter of the word.\n")
    current_room = "Room Nine"
    print(f"Current room: {current_room}")

    if "Master Key" not in required_items:
        take_item = input("You see a key, do you take it? (yes/no)").lower().strip()
        while take_item != "yes" and take_item != "no":
            take_item = input("You see a key, do you take it? (yes/no)").lower().strip()

        if take_item == "yes":
            required_items.append("Master Key")
            print(f"Current inventory:{required_items}")
        else:
            print("You left the key")
    else:
        print("you have the key")
        print(f"Current inventory:{required_items}")

    if "Potion 3" not in inventory:
        take_item = input("You see a potion, do you take it? (yes/no)").lower().strip()
        while take_item != "yes" and take_item != "no":
            take_item = input("You see a potion, do you take it? (yes/no)").lower().strip()

        if take_item == "yes":
            inventory.append("Potion 3")
            print(f"Current inventory:{inventory}")
        else:
            print("You left the potion")
    else:
        print("you have the potion")
        print(f"Current inventory:{inventory}")

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
    print("Remember you just need to type the first letter of the word.\n")
    if "Secret Key" not in required_items:
        print("You need the key enter.")
        room_three_completed()
    else:
    # possbile secret tunnel to boss room?
        required_items.remove("Secret Key")
        print("You secret key")
        current_room = "Secret Room"
        print(f"Current room: {current_room}")

        if "Master Sword" not in required_items and "Master Bow" not in required_items:
            print("You see 2 weapons.")
            print("A sword and a bow and arrow")
            choose_weapon = input("which weapon?").lower().strip()
            while choose_weapon != "sword" and choose_weapon != "bow":
                print("choose a weapon")
                choose_weapon = input("which weapon?").lower().strip()

            if choose_weapon == "sword":
                required_items.append("Master Sword")
                required_items.remove("Sword")
                print(f"Current inventory:{required_items}")
            else:
                required_items.append("Master Bow")
                required_items.remove("Bow")
                print(f"Current inventory:{required_items}")
        else:
            print("You already have a weapon.")
            print(f"Current inventory:{required_items}")

        print("Armour")
        if "Stone" in required_items:
            if "Armour" not in required_items:
                take_item = input("You see some armour? (yes/no)").lower().strip()
                while take_item != "yes" and take_item != "no":
                    take_item = input("You some armour, do you take it? (yes/no)").lower().strip()

                if take_item == "yes":
                    required_items.append("Armour")
                    print("You take and put on the armour.")
                    print("You feel stronger.")
                    print(f"Current inventory:{required_items}")
                else:
                    print("You left the armour")
            else:
                print("you have the armour")
                print(f"Current inventory:{required_items}")
        else:
            print("You need the secret stone for the armour")

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
    print("Remember you just need to type the first letter of the word.\n")
    if "Master Key" not in required_items:
        print("You need the key and a weapon to pass")
        room_nine()
    else:
        current_room = "Boss Room"
        print(f"Current room: {current_room}")
        print("Time to fight the boss.")
        master_boss()


def disarm_sp_loss(player_stamina):
    player_stamina = player_stamina - 5
    return player_stamina


def disarm(player_stamina):
    """
    Disarm fire trap with stone
    """
    # add random function for using stone whether they hit or miss trap
    # possibly add a function if they have bow to use that?
    player_stamina = disarm_sp_loss(player_stamina)
    print("You disarmed the fire trap")
    print(f"{player_hp}hp")
    print(f"{player_stamina}sp")


def jump_hp_loss(player_hp):
    player_hp = player_hp - 100
    return player_hp


def jump_sp_loss(player_stamina):
    player_stamina = player_stamina - 50
    return player_stamina


def jump(player_hp, player_stamina):
    """
    Jump through fire trap
    """
    # add function to take damage and show the hp and sp
    player_hp = jump_hp_loss(player_hp)
    player_stamina = jump_sp_loss(player_stamina)
    print("You successfully jumped through the fire trap.")
    print("You did however take significant damage")
    print(f"{player_hp}hp")
    print(f"{player_stamina}sp")


def swim_hp_loss(player_hp):
    player_hp = player_hp - 50
    return player_hp


def swim_sp_loss(player_stamina):
    player_stamina = player_stamina - 30
    return player_stamina


def swim(player_hp, player_stamina):
    """
    Swim through river
    """
    player_hp = swim_hp_loss(player_hp)
    player_stamina = swim_sp_loss(player_stamina)
    print("You succssfully swam through the river.")
    print("You did however take some damage")
    print(f"{player_hp}hp")
    print(f"{player_stamina}sp")


def hop_hp_loss(player_hp):
    player_hp = player_hp - 5
    return player_hp


def hop_sp_loss(player_stamina):
    player_stamina = player_stamina - 10
    return player_stamina


def hop(player_hp, player_stamina):
    """
    Hop across pedestals in river
    """
    player_hp = hop_hp_loss(player_hp)
    player_stamina = hop_sp_loss(player_stamina)
    print("You succssfully hopped across the river.")
    print("You did however take minimal damage")
    print(f"{player_hp}hp")
    print(f"{player_stamina}sp")


def mini_boss_imp():
    """
    Mini boss fight for attack and damage stats
    """
    print("mini boss fight")


def jungle_sp_loss(player_stamina):
    player_stamina = player_stamina - 25
    return player_stamina


def jungle_puzzle(player_stamina):
    """
    Jungle puzzle in room 6
    """
    if "Sword" not in required_items:
        print("You need the sword to get through the jungle.")
        print("So you have to go through the tunnel.")
        tunnel_puzzle(player_hp, player_stamina)
    else:
        player_stamina = jungle_sp_loss(player_stamina)
        print("jungle")
        print(f"{player_hp}hp")
        print(f"{player_stamina}sp")


def tunnel_hp_loss(player_hp):
    player_hp = player_hp - 10
    return player_hp


def tunnel_sp_loss(player_stamina):
    player_stamina = player_stamina - 5
    return player_stamina


def tunnel_puzzle(player_hp, player_stamina):
    """
    Tunnel puzzle, linked to jungle puzzle in room 6
    """
    # add jump and duck statements
    print("jump and duck")
    trap = input("jump or duck?").lower().strip()
    while trap != "jump" and trap != "duck":
        print("You must choose to do something.")
        trap = input("jump or duck?").lower().strip()

    if trap == "jump":
        player_stamina = tunnel_sp_loss(player_stamina)
        print("you took some damage")
        print(f"{player_hp}hp")
        print(f"{player_stamina}sp")
    else:
        player_hp = tunnel_hp_loss(player_hp)
        print("you took some damage")
        print(f"{player_hp}hp")
        print(f"{player_stamina}sp")


def mini_boss_orc():
    """
    Mini boss fight for attack and damage stats
    """
    print("mini boss fight")


def master_boss():
    """
    Master boss fight for attack and damage stats
    """


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
        print(f"{player_hp}hp")
        print(f"{player_stamina}sp\n")
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
#     if statement? 

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


# Things to fix:
# Heading back to prev locked rooms to be opened
# flow of commands 
# clearing screen - auto do it or ask player?
# formatting 
# using item
# boss attacks with random hits
# player attack random hits
# stamina regen
# function for different ways when entering room
# should i make seprate functions inside functions if it is too long?