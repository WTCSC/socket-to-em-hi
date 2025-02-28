import random
import time
import os

def display_intro():
    print("Welcome to Generic Gacha Game!\nIf you're lucky you will have a nice time, if not give up.\n")

character_banner_art = """
      ☆ ✦ ✧ ✦ ☆ ✦ ✧ ✦ ☆ ✦                                       🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊    
  ✧      𝑭𝒂𝒏𝒕𝒂𝒔𝒚 𝑩𝒂𝒏𝒏𝒆𝒓      ✧                                ✧          𝑶𝒄𝒆𝒂𝒏 𝑩𝒂𝒏𝒏𝒆𝒓         ✧   
      ☆ ✦ ✧ ✦ ☆ ✦ ✧ ✦ ☆ ✦                                       🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊 

        .      ✦ ✧ ✦      .                                          .      🌊 ~ ~ ~ 🌊      .  
      .* *.   * ✦  *    .* *.                                      .* *.   ~ ~ 🌊 ~ ~   .* *.  
    * ✧   ✦    ✧    ✦   ✧ *                                      * ✧   🌊    ✧    🌊   ✧ *  
   ✦   ✦      🌙      ✦   ✦                                     ✦   ✦      🦈      ✦   ✦  
    * ✧   ✦    ✧    ✦   ✧ *                                      * ✧   🌊    ✧    🌊   ✧ *  
      * *.   * ✦  *    .* *.                                        .* *.   ~ ~ 🌊 ~ ~   .* *.  
        '      ✦ ✧ ✦      '                                          '      🌊 ~ ~ ~ 🌊      '  

      ┌───────────────┐                                               ┌───────────────┐
      │  🎟️  [1 Draw]  │                                               │  🎟️  [1 Draw]  │
      │  ✨ [10 Draw] │                                               │  🌊 [10 Draw] │
      └───────────────┘                                               └───────────────┘

  ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦                                     🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊
  """

fantasy_banner = """
      ☆ ✦ ✧ ✦ ☆ ✦ ✧ ✦ ☆ ✦                        
  ✧      𝑭𝒂𝒏𝒕𝒂𝒔𝒚 𝑩𝒂𝒏𝒏𝒆𝒓      ✧                      
      ☆ ✦ ✧ ✦ ☆ ✦ ✧ ✦ ☆ ✦                          

        .      ✦ ✧ ✦      .                                 
      .* *.   * ✦  *    .* *.                                    
    * ✧   ✦    ✧    ✦   ✧ *                                   
   ✦   ✦      🌙      ✦   ✦                                  
    * ✧   ✦    ✧    ✦   ✧ *                         
      * *.   * ✦  *    .* *.                                       
        '      ✦ ✧ ✦      '                                        

      ┌───────────────┐                                              
      │  🎟️  [1 Draw]  │                                                   
      │  ✨ [10 Draw] │                                                    
      └───────────────┘                                                    

  ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦  
"""

ocean_banner = """
        🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊    
     ✧          𝑶𝒄𝒆𝒂𝒏 𝑩𝒂𝒏𝒏𝒆𝒓         ✧   
        🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊 

            .      🌊 ~ ~ ~ 🌊      .  
          .* *.   ~ ~ 🌊 ~ ~   .* *.  
         * ✧   🌊    ✧    🌊   ✧ *  
        ✦   ✦      🦈      ✦   ✦  
         * ✧   🌊    ✧    🌊   ✧ *  
          .* *.   ~ ~ 🌊 ~ ~   .* *.  
            '      🌊 ~ ~ ~ 🌊      '  

        ┌───────────────┐
        │  🎟️  [1 Draw]  │
        │  🌊 [10 Draw] │
        └───────────────┘

    🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊
"""

# Functions

def get_gacha_option():
    while True:
        try:
            gacha_num = int(input("Enter the number of draws you want (this will be for both you and your opponent): "))
            return gacha_num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def char_gacha():
    number = random.randint(1, 1000)
    if number <= 5:
        return 5
    elif number <= 100:
        return 4
    elif number > 100:
        return 3

def weapon_gacha():
    number = random.randint(1, 1000)
    if number <= 5:
        return 5
    elif number <= 100:
        return 4
    elif number > 100:
        return 3

def get_5_star_fantasy_character():
    # Attributes: (Name, Strength, Health, Special Move, Special Cooldown)
    random_character = random.randint(1, 3)
    if random_character == 1:
        print("You got Dragon Deez! (5 Star)")
        return "Dragon Deez", 20, 150, "Draggin Deez Nuts", 2
    elif random_character == 2:
        print("You got Ninja! (5 Star)")
        return "Ninja", 18, 140, "LOWWWWW", 3
    elif random_character == 3:
        print("You got Cave Diver! (5 Star)")
        return "Cave Diver", 16, 130, "Cave Divers When They:", 4

def get_5_star_ocean_character():
    random_character = random.randint(1, 3)
    if random_character == 1:
        print("You got Jeff the Shark! (5 Star)")
        return "Jeff the Shark", 20, 150, "It's Jeff!", 2
    elif random_character == 2:
        print("You got Eye of Rah! (5 Star)")
        return "Eye of Rah", 18, 140, "RAHHH", 3
    elif random_character == 3:
        print("You got Property in Egypt! (5 Star)")
        return "Property in Egypt", 16, 130, "They gave me the property", 4

def get_4_star_character():
    random_character = random.randint(1, 3)
    if random_character == 1:
        print("You got Florida Man! (4 Star)")
        return "Florida Man", 15, 120, "Alligator", 2
    elif random_character == 2:
        print("You got Big Chungus! (4 Star)")
        return "Big Chungus", 14, 110, "Chunk", 3
    elif random_character == 3:
        print("You got Among Us! (4 Star)")
        return "Among Us", 13, 100, "Imposter", 4
    
def get_3_star_character():
    random_character = random.randint(1, 3)
    if random_character == 1:
        print("You got Stick Dude! (3 Star)")
        return "Stick Dude", 10, 80, "Stick Punch", 2
    elif random_character == 2:
        print("You got Stick Woman! (3 Star)")
        return "Stick Woman", 9, 70, "Cook", 3
    elif random_character == 3:
        print("You got Mr Beest! (3 Star)")
        return "Mr Beest", 8, 60, "10,000 Zimbabwean dollars", 4

def main():
    display_intro()
    gacha_num = get_gacha_option() + 1
    
    # Initialize player inventories
    player_characters = {
        5: [],
        4: [],
        3: []
    }
    player_weapons = {
        5: [],
        4: [],
        3: []
    }

    while gacha_num > 0:
        print("Choose what you want to see:")
        print("1. Character Banner")
        print("2. Banner Details")
        print("3. Game Guide")
        print("4. Battle")
        print("5. Exit")
        option = int(input())

        if option == 1:
            banners = f"{character_banner_art}"
            print(banners)
            banner_option = int(input("Choose a banner (1 for Fantasy, 2 for Ocean): "))

            if banner_option == 1:
                print(f"{fantasy_banner}")
                draw_option = int(input("Do you want to do 1 or 10 draws? "))

                if draw_option == 1:
                    if gacha_num > 1:
                        rarity = char_gacha()
                        if rarity == 5:
                            character = get_5_star_fantasy_character()
                        elif rarity == 4:
                            character = get_4_star_character()
                        elif rarity == 3:
                            character = get_3_star_character()
                        player_characters[rarity].append(character)
                        gacha_num -= 1
                    else:
                        print("You don't have anymore draws. Please play the game.")
                        
                        
                elif draw_option == 10:
                    if gacha_num >= 10:
                        for i in range(10):
                            rarity = char_gacha()
                            if rarity == 5:
                                character = get_5_star_fantasy_character()
                            elif rarity == 4:
                                character = get_4_star_character()
                            elif rarity == 3:
                                character = get_3_star_character()
                            player_characters[rarity].append(character)
                        gacha_num -= 10
                    else:
                        print("You don't have enough draws. Please do single draws.")

            if banner_option == 2:
                print(f"{ocean_banner}")
                draw_option = int(input("Do you want to do 1 or 10 draws? "))

                if draw_option == 1:
                    if gacha_num > 1:
                        rarity = char_gacha()
                        if rarity == 5:
                            character = get_5_star_ocean_character()
                        elif rarity == 4:
                            character = get_4_star_character()
                        elif rarity == 3:
                            character = get_3_star_character()
                        player_characters[rarity].append(character)
                        gacha_num -= 1
                    else:
                        print("You don't have any more draws. Please play the game.")
                        
                elif draw_option == 10:
                    if gacha_num >= 10:
                        for i in range(10):
                            rarity = char_gacha()
                            if rarity == 5:
                                character = get_5_star_ocean_character()
                            elif rarity == 4:
                                character = get_4_star_character()
                            elif rarity == 3:
                                character = get_3_star_character()
                            player_characters[rarity].append(character)
                        gacha_num -= 10
                    else:
                        print("You don't have enough draws. Please do single draws.")

        elif option == 2:
            print("Banner Details:")
            print("1. Fantasy Banner")
            print("2. Ocean Banner")
            print("3. Weapon Banner")
            print("4. Exit")
            banner_option = int(input())
            if banner_option == 1:
                print("""There are 3 exclusive 5 star characters in the Fantasy Banner (Dragon Deez, Ninja, and Cave Diver). 
                      The 3 and 4 star characters are shared between the character banners. The 4 star characters are Florida Man, Big Chungus, and Among Us.
                      The 3 star characters are Stick Dude, Stick Woman, Mr. Beest. The rates for this banner are 0.5% for 5 star, 9.5% for 4 star, and 90% for 3 star.""")
            elif banner_option == 2:
                print("""There are 3 exclusive 5 star characters in the Ocean Banner (Jeff the Shark, Eye of Rah, and Property in Egypt). 
                      The 3 and 4 star characters are shared between the character banners. The 4 star characters are Florida Man, Big Chungus, and Among Us.
                      The 3 star characters are Stick Dude, Stick Woman, Mr. Beest. The rates for this banner are 0.5% for 5 star, 9.5% for 4 star, and 90% for 3 star.""")
            elif banner_option == 3:
                print("""There are six 5 star weapons in the Weapon Banner (America, Shoes, Low Taper Fade, Nuts, Property, and Eye of Ra). 
                      The 4 star weapons are Scissors, Knife, and Red 40.
                      The 3 star weapons are Stick, Branch, and Lunchly. 
                      The rates for this banner are 0.5% for 5 star, 9.5% for 4 star, and 90% for 3 star.""")
            elif banner_option == 4:
                break

        elif option == 3:
            print("Game Guide:")
            print("1. The game is a gacha game where you can summon characters and weapons.")
            print("2. There are two character banners (Fantasy and Ocean) and one weapon banner.")
            print("3. The rates for 5 star characters and weapons are 0.5%, 4 star characters and weapons are 9.5%, and 3 star characters and weapons are 90%.")
            print("4. You can do single draws or 10 draws at a time.")
            print("5. You can exit the game at any time by selecting the exit option.")
            print("6. Have fun and enjoy the game!")
            input("Press Enter to continue...")

        elif option == 4:
            print("Choose Your Battle:")
            print("1. Luck Battle")
            print("2. Strategy Battle")
            print("3. Battle Guide")
            print("4. Exit")
            Battle_option = int(input())

            if Battle_option == 1:
                print("Luck Battle")
                print(f"Number of 5 star characters: {len(player_characters[5])}")
                print(f"Number of 4 star characters: {len(player_characters[4])}")   
                print(f"Number of 3 star characters: {len(player_characters[3])}")
                print(f"Number of 5 star weapons: {len(player_weapons[5])}")
                print(f"Number of 4 star weapons: {len(player_weapons[4])}")
                print(f"Number of 3 star weapons: {len(player_weapons[3])}")
                points = (len(player_characters[5]) * 10) + (len(player_characters[4]) * 6) + (len(player_characters[3]) * 2) + (len(player_weapons[5]) * 10) + (len(player_weapons[4]) * 6) + (len(player_weapons[3]) * 2)
                print(f"Your total points: {points}")

            elif Battle_option == 2:
                print("Under Construction")

            elif Battle_option == 3:
                print("Battle Guide:")
                print("1. Luck Battle: In this battle, you win depending on how many rare characters/weapons you have.")
                print("2. Strategy Battle: In this battle, you will need to use your characters and weapons to defeat your opponent with actual stats.")
                print("3. You can exit the battle at any time by selecting the exit option.")
                print("4. Have fun and enjoy the battle!")
                input("Press Enter to continue...")

            elif Battle_option == 4:
                break


    print("HI!")


if __name__ == "__main__":
    main()