import random

# Gacha Game Class to use in the main file
class GachaGame:

    # Intro fucntion
    def display_intro():
        print("Welcome to Generic Gacha Game!\nIf you're lucky you will have a nice time, if not give up.\n")

    # Banner art
    character_banner_art = """
        ☆ ✦ ✧ ✦ ☆ ✦ ✧ ✦ ☆ ✦                                       🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊    
    ✧      Fantasy Banner      ✧                                ✧          Ocean Banner         ✧   
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

    # Fantasy banner art
    fantasy_banner = """
        ☆ ✦ ✧ ✦ ☆ ✦ ✧ ✦ ☆ ✦                        
    ✧      Fantasy Banner      ✧                      
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
    # Ocean banner art
    ocean_banner = """
            🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊 ~ ~ ~ 🌊    
        ✧          Ocean Banner         ✧   
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

    # Get the number of draws
    def get_gacha_option():

        # Try and except for invalid input
        try:
            # Get the number of draws the player wants
            gacha_num = int(input("Enter the number of draws you want (it is recommended to use the same amount as your opponent): "))
            return gacha_num
        
        # Displays an error message if the input is invalid
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Gets the rarity
    def rarity():
        number = random.randint(1, 1000)
        if number <= 5:
            return 5
        elif number <= 100:
            return 4
        elif number > 100:
            return 3

    # Get the fantasy 5 star character
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
        
    # Get the ocean 5 star character
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

    # Get the 4 star character
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
        
    # Get the 3 star character
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