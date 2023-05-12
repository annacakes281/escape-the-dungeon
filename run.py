import random
import os


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
if playing.lower().strip() != "yes":
    quit()


def clear():
    """
    Clears terminal before the text adventure starts to clean up space
    """
    os.system("cls" if os.name == "nt" else "clear")


clear()

# Player health and stamina
player_hp = 150
player_stamnia = 50

name = input("Type your name:\n").strip()

print(f"Welcome {name} to the Escape the Dungeon Game. Good luck!\n")
print("You have found yourself in a dungeon and must find the way out.")
print(f"You start with {player_hp}hp and {player_stamnia}sp.\n")