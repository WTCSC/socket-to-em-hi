import random
import time
import os

class GachaGame:
    def display_intro():
        intro_message = (
            "Welcome to Generic Gacha Game!\n"
            "If you're lucky you will have a nice time, if not give up.\n"
        )
        return intro_message

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
    weapon_banner = """
                ☆ ✦ ✧ ✦ ☆ ✦ ✧ ✦ ☆ ✦ ✧ ✦ ☆  
            ✧           𝑾𝒆𝒂𝒑𝒐𝒏 𝑩𝒂𝒏𝒏𝒆𝒓           ✧   
                ☆ ✦ ✧ ✦ ☆ ✦ ✧ ✦ ☆ ✦ ✧ ✦ ☆  

                                                    ______,....----,  
                /VVVVVVVVVVVVVV|===================""""""""""""       ___,..-'  
                `^^^^^^^^^^^^^^|======================----------""""""  
                        

                (                                   _  
                    )                               /=>
                (  +____________________/\/\___ / /|  
                    .''._____________'._____      / /|/\  
                : () :              :\ ----\|    \ )  
                    '..'______________.'0|----|      \  
                                    0_0/____/        \  
                                        |----    /----\  
                                    || -\\ --|      \  
                                    ||   || ||\      \  
                                        \\____// '|      \  
                                                .'/       |  
                                            .:/        |  
                                            :/_________|  

                    ┌──────────────────┐  
                    │  🎟️ [1 Draw]      │  
                    │  ✨ [10 Draw]    │  
                    └──────────────────┘  

            ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦  

    """


    # Animations

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_animation():
        frames = [
            """
            ☆ ✦ ✧ ✦ ☆
            .
            """,
            """
            ☆ ✦ ✧ ✦ ☆
            .* *.
            """,
            """
            ☆ ✦ ✧ ✦ ☆
        * ✧   ✦ *
            """,
            """
            ☆ ✦ ✧ ✦ ☆
        ✦   ✦ 🌙 ✦   ✦
            """,
            """
            ☆ ✦ ✧ ✦ ☆
        * ✧   ✦ *
            .* *.
            """,
            """
            ☆ ✦ ✧ ✦ ☆
            ✦
            """,
            """
            ┌───────────────┐
            │  🎟️ Summoning... │
            └───────────────┘
            """,
            """
            ┌───────────────┐
            │  ✨ 3-Star Item  │
            └───────────────┘
            """,
            """
            ┌───────────────┐
            │  🌟 4-Star Item  │
            └───────────────┘
            """,
            """
            ┌───────────────┐
            │  🌟🌟🌟 5-Star!  │
            └───────────────┘
            """,
        ]
        
        for frame in frames:
            GachaGame.clear_screen()
            print(frame)
            time.sleep(0.5)
        
        print("✨ Summon Complete! ✨")


    # Functions

    def get_gacha_option():
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

    def get_5_star_weapon():
        # Attributes: (Name, Damage Bonus, Signature Character)
        random_weapon = random.randint(1, 6)
        if random_weapon == 1:
            print("You got America! (5 Star)")
            return "America", 20, "Jeff the Shark"
        elif random_weapon == 2:
            print("You got Shoes! (5 Star)")
            return "Shoes", 18, "Cave Diver"
        elif random_weapon == 3:
            print("You got Low Taper Fade! (5 Star)")
            return "Low Taper Fade", 16, "Ninja"
        elif random_weapon == 4:
            print("You got Property! (5 Star)")
            return "Property", 18, "Property in Egypt"
        elif random_weapon == 5:
            print("You got Eye of Ra! (5 Star)")
            return "Eye of Ra", 16, "Eye of Rah"
        elif random_weapon == 6:
            print("You got Nuts! (5 Star)")
            return "Nuts", 20, "Dragon Deez"

    def get_4_star_weapon():
        # Attributes: (Name, Damage Bonus, Signature Character)
        random_weapon = random.randint(1, 3)
        if random_weapon == 1:
            print("You got Scissors! (4 Star)")
            return "Scissors", 15, "Florida Man"
        elif random_weapon == 2:
            print("You got Knife! (4 Star)")
            return "Knife", 14, "Big Chungus"
        elif random_weapon == 3:
            print("You got Red 40! (4 Star)")
            return "Red 40", 13, "Among Us"

    def get_3_star_weapon():
        # Attributes: (Name, Damage Bonus, Signature Character)
        random_weapon = random.randint(1, 3)
        if random_weapon == 1:
            print("You got Stick! (3 Star)")
            return "Stick", 10, "Stick Dude"
        elif random_weapon == 2:
            print("You got Branch! (3 Star)")
            return "Branch", 9, "Stick Woman"
        elif random_weapon == 3:
            print("You got Lunchly! (3 Star)")
            return "Lunchly", 8, "Mr Beest"