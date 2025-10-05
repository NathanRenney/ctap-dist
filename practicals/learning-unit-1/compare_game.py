import random
from nathans_characters import nathans_character_list
#todo: you can use imports to import a list from another file
# use the form: from name_of_file import name_of_list

# Handle nested stats
def get_stat(character, stat):
    if stat in character:
        return character[stat]
    elif "abilities" in character and stat in character["abilities"]:
        return character["abilities"][stat]
    else:
        return None

#  todo: modify this function for the behaviour of your game.
def compare_stats(stat_name, val1, val2):
    # Custom logic based on stat name
    if stat_name == "is legendary":
        # Legendary status wins if only one is True
        if val1 and not val2:
            return "Player 1 wins!"
        elif val2 and not val1:
            return "Player 2 wins!"
        else:
            return "It's a tie!"

    elif stat_name == "inventory":
        # Compare inventory size
        return "Player 1 wins!" if len(val1) > len(val2) else "Player 2 wins!" if len(val2) > len(val1) else "It's a tie!"

    elif stat_name in ["name", "class"]:
        # Compare string length
        return "Player 1 wins!" if len(val1) > len(val2) else "Player 2 wins!" if len(val2) > len(val1) else "It's a tie!"

    elif isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
        # Default numeric comparison
        return "Player 1 wins!" if val1 > val2 else "Player 2 wins!" if val2 > val1 else "It's a tie!"

    else:
        return "Cannot compare these values."

# The code below actually runs the functions above and 
# handles things like user inputs and the program flow

characters = nathans_character_list # todo: modify this line to use a different list!

player_1 = random.choice(characters)
player_2 = random.choice(characters)
while player_2 == player_1:
    player_2 = random.choice(characters)

print("Player 1:", player_1["name"])
print("Player 2:", player_2["name"])

# Get user to give stat to compare
print("\nAvailable stats:")
print("- Top-level keys:", list(player_1.keys()))
print("- Nested 'abilities':", list(player_1.get("abilities", {}).keys()))
chosen_stat = input("Enter the stat to compare: ").strip().lower()

stat_1 = get_stat(player_1, chosen_stat)
stat_2 = get_stat(player_2, chosen_stat)

print(f"\n{player_1['name']} has {chosen_stat}: {stat_1}")
print(f"{player_2['name']} has {chosen_stat}: {stat_2}")
print(compare_stats(chosen_stat, stat_1, stat_2))