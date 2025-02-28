import socket
from gacha import GachaGame

def main():
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    ip_address = input("Enter the server's IP address: ")
    port = int(input("Enter the server's port number: "))

    try:
        client.connect((ip_address, port))
        print("Connected to server")

        # Receive and print intro message
        GachaGame.display_intro()

        while True:
            gacha_num = GachaGame.get_gacha_option() + 1

            # Initialize player inventories
            player_characters = {
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
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    banners = f"{GachaGame.character_banner_art}"
                    print(banners)
                    banner_option = int(input("Choose a banner (1 for Fantasy, 2 for Ocean): "))

                    if banner_option == 1:
                        print(f"{GachaGame.fantasy_banner}")
                        draw_option = int(input("Do you want to do 1 or 10 draws? "))

                        if draw_option == 1:
                            if gacha_num > 1:
                                rarity = GachaGame.rarity()
                                if rarity == 5:
                                    character = GachaGame.get_5_star_fantasy_character()
                                elif rarity == 4:
                                    character = GachaGame.get_4_star_character()
                                elif rarity == 3:
                                    character = GachaGame.get_3_star_character()
                                player_characters[rarity].append(character)
                                gacha_num -= 1
                            else:
                                print("You don't have anymore draws. Please play the game.")
                                
                                
                        elif draw_option == 10:
                            if gacha_num >= 10:
                                for i in range(10):
                                    rarity = GachaGame.rarity()
                                    if rarity == 5:
                                        character = GachaGame.get_5_star_fantasy_character()
                                    elif rarity == 4:
                                        character = GachaGame.get_4_star_character()
                                    elif rarity == 3:
                                        character = GachaGame.get_3_star_character()
                                    player_characters[rarity].append(character)
                                gacha_num -= 10
                            else:
                                print("You don't have enough draws. Please do single draws.")

                    elif banner_option == 2:
                        print(f"{GachaGame.ocean_banner}")
                        draw_option = int(input("Do you want to do 1 or 10 draws? "))

                        if draw_option == 1:
                            if gacha_num > 1:
                                rarity = GachaGame.rarity()
                                if rarity == 5:
                                    character = GachaGame.get_5_star_ocean_character()
                                elif rarity == 4:
                                    character = GachaGame.get_4_star_character()
                                elif rarity == 3:
                                    character = GachaGame.get_3_star_character()
                                player_characters[rarity].append(character)
                                gacha_num -= 1
                            else:
                                print("You don't have any more draws. Please play the game.")
                                
                        elif draw_option == 10:
                            if gacha_num >= 10:
                                for i in range(10):
                                    rarity = GachaGame.rarity()
                                    if rarity == 5:
                                        character = GachaGame.get_5_star_ocean_character()
                                    elif rarity == 4:
                                        character = GachaGame.get_4_star_character()
                                    elif rarity == 3:
                                        character = GachaGame.get_3_star_character()
                                    player_characters[rarity].append(character)
                                gacha_num -= 10
                            else:
                                print("You don't have enough draws. Please do single draws.")
                elif choice == 2:
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

                elif choice == 3:
                    print("Game Guide:")
                    print("1. The game is a gacha game where you can summon characters and weapons.")
                    print("2. There are two character banners (Fantasy and Ocean) and one weapon banner.")
                    print("3. The rates for 5 star characters and weapons are 0.5%, 4 star characters and weapons are 9.5%, and 3 star characters and weapons are 90%.")
                    print("4. You can do single draws or 10 draws at a time.")
                    print("5. You can exit the game at any time by selecting the exit option.")
                    print("6. Have fun and enjoy the game!")
                    input("Press Enter to continue...")

                elif choice == 4:
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
                        points = (len(player_characters[5]) * 10) + (len(player_characters[4]) * 6) + (len(player_characters[3]) * 2)
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

                elif choice == 5:
                    break
                
    except ConnectionResetError:
        print("Connection lost. Server may have crashed or closed.")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client.close()
        print("Connection closed")

if __name__ == "__main__":
    main()