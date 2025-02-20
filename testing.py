import random
import time
import os

def display_intro():
    print("Welcome to Generic Gacha Game!\n")
    print("If you're lucky you will have a nice time, if not give up.\n")

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
        clear_screen()
        print(frame)
        time.sleep(0.5)
    
    print("✨ Summon Complete! ✨")


# Functions

def get_gacha_option():
    try:
        gacha_num = int(input("Enter the number of draws you want: "))
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
        print("You got a 5 star weapon!")
        return 5
    elif number <= 100:
        print("You got a 4 star weapon!")
        return 4
    elif number > 100:
        print("You got a 3 star weapon!")
        return 3

def get_5_star_fantasy_character():
    random_character = random.randint(1, 3)
    if random_character == 1:
        print("You got Dragon Deez! (5 Star)")
        return "Dragon Deez", 18, 120, "Draggin Deez Nuts", 2, 8
    elif random_character == 2:
        print("You got Ninja! (5 Star)")
        return "Ninja", 14, 100, "LOWWWWW", 3, 7
    elif random_character == 3:
        print("You got Cave Diver! (5 Star)")
        return "Cave Diver", 12, 80, "Cave Divers When They:", 4, 6

def get_5_star_ocean_character():
    random_character = random.randint(1, 3)
    if random_character == 1:
        print("You got Jeff the Shark! (5 Star)")
        return "Jeff the Shark", 18, 120, "It's Jeff!", 2, 8
    elif random_character == 2:
        print("You got Eye of Rah! (5 Star)")
        return "Eye of Rah", 14, 100, "RAHHH", 3, 7
    elif random_character == 3:
        print("You got Property in Egypt! (5 Star)")
        return "Property in Egypt", 12, 80, "They gave me the property", 4, 6

def get_4_star_character():
    random_character = random.randint(1, 3)
    if random_character == 1:
        print("You got Florida Man! (4 Star)")
        return "Florida Man", 18, 120, "Alligator", 2, 8
    elif random_character == 2:
        print("You got Big Chungus! (4 Star)")
        return "Big Chungus", 14, 100, "Chunk", 3, 7
    elif random_character == 3:
        print("You got Among Us! (4 Star)")
        return "Among Us", 12, 80, "Imposter", 4, 6
    
def get_3_star_character():
    random_character = random.randint(1, 3)
    if random_character == 1:
        print("You got Stick Dude! (3 Star)")
        return "Stick Dude", 18, 120, "Stick Punch", 2, 8
    elif random_character == 2:
        print("You got Stick Woman! (3 Star)")
        return "Stick Woman", 14, 100, "Cook", 3, 7
    elif random_character == 3:
        print("You got Mr Beest! (3 Star)")
        return "Mr Beest", 12, 80, "10,000 Zimbabwean dollars", 4, 6

def get_5_star_weapon():
    random_weapon = random.choice([
        ("America", "Gun"),
        ("Goofy", "Sword"),
        ("Low Taper", "Scissors"),
        (""),
        (),
        (),
        ()
    ])

def get_4_star_weapon():
    random_weapon = random.choice([
        (),
        (),
        (),
        (),
        (),
        (),
        ()
    ])

def get_3_star_weapon():
    random_weapon = random.choice([
        ("Stick"),
        (),
        (),
        (),
        (),
        (),
        ()
    ])

def main():
    display_intro()
    gacha_num = get_gacha_option()
    while gacha_num > 0:
        print("Choose what you want to draw:")
        print("1. Character")
        print("2. Weapon")
        print("3. Exit")
        option = int(input())

        if option == 1:
            banners = f"{character_banner_art}"
            print(banners)
            banner_option = int(input("Choose a banner (1 for Fantasy, 2 for Ocean): "))

            if banner_option == 1:
                print(f"{fantasy_banner}")
                draw_option = int(input("Do you want to do 1 or 10 draws? "))

                if draw_option == 1:
                    draw_animation()
                    gacha_num -= 1
                    if gacha_num > 0:
                        rarity = char_gacha()
                        if rarity == 5:
                            get_5_star_fantasy_character()
                        elif rarity == 4:
                            get_4_star_character()
                        elif rarity == 3:
                            get_3_star_character()
                        
                elif draw_option == 10:
                    if gacha_num >= 10:
                        gacha_num -= 10
                        for i in range(10):
                            rarity = char_gacha()
                            if rarity == 5:
                                get_5_star_fantasy_character()
                            elif rarity == 4:
                                get_4_star_character()
                            elif rarity == 3:
                                get_3_star_character()
                    else:
                        print("You don't have enough draws. Please do single draws.")

            if banner_option == 2:
                print(f"{ocean_banner}")
                draw_option = int(input("Do you want to do 1 or 10 draws? "))

                if draw_option == 1:
                    gacha_num -= 1
                    draw_animation()
                    if gacha_num > 0:
                        rarity = char_gacha()
                        if rarity == 5:
                            get_5_star_ocean_character()
                        elif rarity == 4:
                            get_4_star_character()
                        elif rarity == 3:
                            get_3_star_character()
                        
                elif draw_option == 10:
                    if gacha_num >= 10:
                        gacha_num -= 10
                        for i in range(10):
                            rarity = char_gacha()
                            if rarity == 5:
                                get_5_star_ocean_character()
                            elif rarity == 4:
                                get_4_star_character()
                            elif rarity == 3:
                                get_3_star_character()
                    else:
                        print("You don't have enough draws. Please do single draws.")

        elif option == 2:
            print(f"{weapon_banner}")
            draw_option = int(input("Do you want to do 1 or 10 draws? "))
            if draw_option == 1:
                gacha_num -= 1
                draw_animation()
                if gacha_num > 0:
                    rarity = weapon_gacha()
                    if rarity == 5:
                        get_5_star_weapon()
                    elif rarity == 4:
                        get_4_star_weapon()
                    elif rarity == 3:
                        get_3_star_weapon()
                        
            elif draw_option == 10:
                if gacha_num >= 10:
                    gacha_num -= 10
                    for i in range(10):
                        rarity = weapon_gacha()
                        if rarity == 5:
                            get_5_star_weapon()
                        elif rarity == 4:
                            get_4_star_weapon()
                        elif rarity == 3:
                            get_3_star_weapon()
                else:
                    print("You don't have enough draws. Please do single draws.")

        elif option == 3:
            break


    print(f"HI!")


if __name__ == "__main__":
    main()