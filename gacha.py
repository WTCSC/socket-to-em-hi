import random

def display_intro():
    print("Welcome to generic gacha game!\n")
    print("If you're lucky you will have a nice time, if not give up.\n")

def char_gacha():
    number = random.randint(1, 1000)
    if number <= 5:
        print("You got a 5 star character!")
        return 5
    elif number <= 100:
        print("You got a 4 star character!")
        return 4
    elif number > 100:
        print("You got a 3 star character!")
        return 3

def weapon_gacha():
    number = random.randint(1, 1000)
    if number <= 5:
        print("You got a 5 star weapon!")
        return 5
    elif number <= 100:
        print("You got a 4 star weapon!")
        return 4
    elif number > 100:
        print("You got a 3 star weapon!")
        return 3


def get_character_stats():
    if char_gacha() == 5:
        random_character = random.choice([
            (),
            (),
            (),
            (),
            (),
            (),
            ()
        ])


def main():
    display_intro()
    show_character_options()
    player_choice = get_character_choice()
    player_name, player_strength, player_health, special_move, special_cooldown, player_agility = get_character_attributes(player_choice)

    display_character_info(player_name, player_strength, player_health, special_move, special_cooldown, player_agility)

    opponents = [
        ("Sol Badguy", 18, 120, 8),
        ("Ky Kiske", 14, 100, 7),
        ("May", 16, 80, 10),
        ("Chip Zanuff", 12, 70, 12),
        ("I-No", 14, 90, 6),
        ("Jack-O", 14, 100, 5),
        ("Happy Chaos", 12, 90, 9)
    ]
    opponent_name, opponent_strength, opponent_health, opponent_agility = random.choice(opponents)

    print(f"\nYour opponent is {opponent_name}!\n")


if __name__ == "__main__":
    main()