import random
import os

# Player health and stamina
player_hp = 150
player_stamina = 50

# List to keep track on invetory items
inventory = []
required_items = []


def clear():
    """
    Clears terminal before the text adventure starts to clean up space
    """
    os.system("cls" if os.name == "nt" else "clear")


def rules():
    """
    Rules for the game that will appear at the start so players know the goal
    """
    print("This is a text-based game, type your answers into the terminal.\n")
    print("Type the first letter of the word to continue.")
    print("e.g 'n' for 'north' or 'y' for 'yes'.\n\n")

    print("The goal is to defeat the Master boss in Boss room.\n")

    print("There are required items to gain access to the Boss Room.")
    print("You must have a Master Weapon and a Master Key to defeat the Boss!")
    print("...but the armour won't be a bad chocie to have either.\n\n")

    return rules


intro = rules()


# Quits game if user doesn't want to play
print("Type 'y' or 'yes' to play.")
playing = input("Would you like to Escape the dungeon?\n> ").lower().strip()
if playing != "yes" and playing != "y":
    print("Oh well, I guess you're not up for the challenge.")
    print("Exiting the game...")
    quit()


def start_game():
    """
    Game start intro message
    """
    print(f"Welcome {name} to the Escape the Dungeon Game. Good luck!\n")
    print(f"Your current stats:")
    print(f"{player_hp}hp")
    print(f"{player_stamina}sp")
    print("You currently have nothing in your inventory.\n\n")


def starting_room():
    """
    The main room where the player starts
    """
    current_room = "Starting Room"
    print(f"Current room: {current_room}\n")
    print(
        "You fell down a trap door and end up in an empty room.\n"
        "You look around in the dimmly lit room and see 3 possible paths.\n"
        "You can either go North, South or East.\n")
    
    print("Remember you can type just the first letter of the word.")
    direction = input("Which way do you want to go?:\n> ").lower().strip()
    while direction != "n" and direction != "s" and direction != "e":
        print("Invalid move, please enter a valid move.")
        print("'n' for 'north, 's' for 'south' or 'e' for 'east'.")
        direction = input("Which way do you want to go?:\n> ").lower().strip()

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

    current_room = "Room One"
    print(f"Current room: {current_room}\n")
    
    if "Key 1" not in required_items:
        take_item = input("You see a key, do you take it? (yes/no)").lower().strip()
        while take_item != "yes" and take_item != "no":
            take_item = input("You see a key, do you take it? (yes/no)").lower().strip()

        if take_item == "yes":
            required_items.append("Key 1")
            print(f"Current inventory:{required_items}")
        else:
            print("You left the key")
    else:
        print("you have the key")
        print(f"Current inventory:{required_items}")

    if "Sword" not in required_items and "Bow" not in required_items:
        print("You see 2 weapons.")
        print("A sword and a bow and arrow")
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
    else:
        print("You already have a weapon.")
        print(f"Current inventory:{required_items}")
    
    print("You choose your weapon and this set off a trap.")

    trap = input("disarm trap or jump through it?").lower().strip()
    while trap != "disarm" and trap != "jump":
        print("You must choose to do something.")
        trap = input("disarm trap or jump through it?").lower().strip()

    if trap == "disarm":
        disarm(player_stamina)
    else:
        jump(player_hp, player_stamina)

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
        swim(player_hp, player_stamina)
    else:
        hop(player_hp, player_stamina)

    if "Potion 1" not in inventory:
        take_item = input("You see a potion, do you take it? (yes/no)").lower().strip()
        while take_item != "yes" and take_item != "no":
            take_item = input("You see a potion, do you take it? (yes/no)").lower().strip()

        if take_item == "yes":
            inventory.append("Potion 1")
            print(f"Current inventory:{inventory}")
        else:
            print("You left the potion")
    else:
        print("you have the potion")
        print(f"Current inventory:{inventory}")

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
        required_items.remove("Key 1")
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
    
    if "Key 2" not in required_items:
        take_item = input("You see a key, do you take it? (yes/no)").lower().strip()
        while take_item != "yes" and take_item != "no":
            take_item = input("You see a key, do you take it? (yes/no)").lower().strip()

        if take_item == "yes":
            required_items.append("Key 2")
            print(f"Current inventory:{required_items}")
        else:
            print("You left the key")
    else:
        print("you have the key")
        print(f"Current inventory:{required_items}")
    
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
# clearing screen
# formatting 
# using item
# boss attacks with random hits
# player attack random hits
# stamina regen