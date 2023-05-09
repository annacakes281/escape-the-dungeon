def rules():
    """
    Rules for the game that will appear at the start so players know the goal
    """
    print("This is a text-based game, type your answers into the terminal\n\n")
    print("The goal is to defeat the Master boss in the boss room.")
    print("Collect all 6 items and all 4 keys to get to the Master Boss!\n")

    return rules


intro = rules()

player_hp = 150
player_stamnia = 50

name = input("Type your name:\n")

print(f"Welcome {name} to the Escape the Dungeon Game. Good luck!\n")
print(f"You start with {player_hp}hp and {player_stamnia}sp.")
print("You also find a flimsy bow and 1 arrow, with a durablity for one use.")