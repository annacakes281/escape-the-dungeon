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
if playing.lower() == "no":
    quit()

player_hp = 150
player_stamnia = 50

weapon_options = ["sword", "bow and arrow"]
master_weapon_option = ["master sword", "master bow and arrow"]
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
print(f"You start with {player_hp}hp and {player_stamnia}sp.")
print("You also find a flimsy bow and 1 arrow, with a durablity for one use.")
