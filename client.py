import socket
import sys
from gacha import GachaGame

def main():
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Variables for the server's IP address and port number
    ip_address = input("Enter the server's IP address: ")
    port = int(input("Enter the server's port number: "))

    try:
        # Connects to the server
        client.connect((ip_address, port))
        print("Connected to the server")

        # Receive and print intro message
        GachaGame.display_intro()

        # Main game loop
        while True:

            # Get the number of gacha draws from the user. + 1 to keep the game running as everything is in a while loop
            gacha_num = GachaGame.get_gacha_option() + 1

            # Initialize player inventories
            player_characters = {
                5: [],
                4: [],
                3: []
            }

            # Main game loop
            while gacha_num > 0:

                # Display the game menu
                print("Choose where you want to go: ")
                print("1. Character Banner")
                print("2. Banner Details")
                print("3. Game Guide")
                print("4. Battle")
                print("5. Inventory")
                print("6. Exit\n")

                # Get the user's choice
                choice = int(input("Enter your choice: "))

                # Process the user's choice
                if choice == 1:

                    # Display the banners
                    banners = f"{GachaGame.character_banner_art}"
                    print(banners)

                    # Get the user's choice of banner
                    banner_option = int(input("Choose a banner (1 for Fantasy, 2 for Ocean): "))

                    # Process the user's choice of banner
                    if banner_option == 1:
                        print(f"{GachaGame.fantasy_banner}")

                        # Get the user's choice of draw option
                        draw_option = int(input("Do you want to do 1 or 10 draws? "))

                        # Process the user's choice of draw option for a 1 draw
                        if draw_option == 1:

                            # Check if the user has enough draws
                            if gacha_num > 1:

                                # Get the rarity of the character
                                rarity = GachaGame.rarity()

                                # Get the character based on the rarity
                                if rarity == 5:
                                    character = GachaGame.get_5_star_fantasy_character()
                                elif rarity == 4:
                                    character = GachaGame.get_4_star_character()
                                elif rarity == 3:
                                    character = GachaGame.get_3_star_character()
                                
                                # Add the character to the player's inventory
                                player_characters[rarity].append(character)

                                # Decrement the number of draws
                                gacha_num -= 1

                            # If the user doesn't have enough draws displays a message
                            else:
                                print("You don't have anymore draws. Please play the game.")
                                
                        # Process the user's choice of draw option for a 10 draw
                        elif draw_option == 10:

                            # Check if the user has enough draws
                            if gacha_num >= 10:

                                # Loop through 10 times to get 10 characters
                                for i in range(10):

                                    # Get the rarity of the character
                                    rarity = GachaGame.rarity()
                                    if rarity == 5:
                                        character = GachaGame.get_5_star_fantasy_character()
                                    elif rarity == 4:
                                        character = GachaGame.get_4_star_character()
                                    elif rarity == 3:
                                        character = GachaGame.get_3_star_character()

                                    # Add the character to the player's inventory
                                    player_characters[rarity].append(character)

                                # Decrement the number of draws
                                gacha_num -= 10

                            # If the user doesn't have enough draws displays a message
                            else:
                                print("You don't have enough draws. Please do single draws.")

                    # Process the user's choice of banner details
                    elif banner_option == 2:
                        print(f"{GachaGame.ocean_banner}")

                        # Get the user's choice of draw option
                        draw_option = int(input("Do you want to do 1 or 10 draws? "))

                        # Process the user's choice of draw option for a 1 draw
                        if draw_option == 1:

                            # Check if the user has enough draws
                            if gacha_num > 1:

                                # Get the rarity of the character
                                rarity = GachaGame.rarity()

                                # Get the character based on the rarity
                                if rarity == 5:
                                    character = GachaGame.get_5_star_ocean_character()
                                elif rarity == 4:
                                    character = GachaGame.get_4_star_character()
                                elif rarity == 3:
                                    character = GachaGame.get_3_star_character()

                                # Add the character to the player's inventory
                                player_characters[rarity].append(character)

                                # Decrement the number of draws
                                gacha_num -= 1

                            # If the user doesn't have enough draws displays a message
                            else:
                                print("You don't have any more draws. Please play the game.")   
                        
                        # Process the user's choice of draw option for a 10 draw
                        elif draw_option == 10:

                            # Check if the user has enough draws
                            if gacha_num >= 10:

                                # Loop through 10 times to get 10 characters
                                for i in range(10):

                                    # Get the rarity of the character
                                    rarity = GachaGame.rarity()
                                    if rarity == 5:
                                        character = GachaGame.get_5_star_ocean_character()
                                    elif rarity == 4:
                                        character = GachaGame.get_4_star_character()
                                    elif rarity == 3:
                                        character = GachaGame.get_3_star_character()

                                    # Add the character to the player's inventory
                                    player_characters[rarity].append(character)

                                # Decrement the number of draws
                                gacha_num -= 10

                            # If the user doesn't have enough draws displays a message
                            else:
                                print("You don't have enough draws. Please do single draws.")

                # Process the user's choice of banner details
                elif choice == 2:
                    print("Banner Details:")
                    print("1. Fantasy Banner")
                    print("2. Ocean Banner")

                    # Gets the user's choice of banner details
                    banner_option = int(input())

                    # Displays the Fantasy Banner details
                    if banner_option == 1:
                        print("""There are 3 exclusive 5 star characters in the Fantasy Banner (Dragon Deez, Ninja, and Cave Diver).\nThe 3 and 4 star characters are shared between the character banners. The 4 star characters are Florida Man, Big Chungus, and Among Us.\nThe 3 star characters are Stick Dude, Stick Woman, Mr. Beest. The rates for this banner are 0.5% for 5 star, 9.5% for 4 star, and 90% for 3 star.\n""")
                    
                    # Displays the Ocean Banner details
                    elif banner_option == 2:
                        print("""There are 3 exclusive 5 star characters in the Ocean Banner (Jeff the Shark, Eye of Rah, and Property in Egypt).\nThe 3 and 4 star characters are shared between the character banners. The 4 star characters are Florida Man, Big Chungus, and Among Us.\nThe 3 star characters are Stick Dude, Stick Woman, Mr. Beest. The rates for this banner are 0.5% for 5 star, 9.5% for 4 star, and 90% for 3 star.\n""")

                # Process the user's choice of game guide
                elif choice == 3:
                    print("Game Guide:")
                    print("1. The game is a gacha game where you can summon characters.")
                    print("2. There are two character banners (Fantasy and Ocean).")
                    print("3. The rates for 5 star characters are 0.5%, 4 star characters are 9.5%, and 3 star characters are 90%.")
                    print("4. You can do single draws or 10 draws at a time.")
                    print("5. You can exit the game at any time by selecting the exit option.")
                    print("6. Have fun and enjoy the game!\n")
                    input("Press Enter to continue...")

                # Process the user's choice of battle
                elif choice == 4:

                    # Display the battle options
                    print("Choose Your Battle:")
                    print("1. Luck Battle")
                    print("2. Strategy Battle")
                    print("3. Battle Guide")

                    # Get the user's choice of battle
                    Battle_option = int(input())

                    # Starts a Luck Battle if the user chooses 1
                    if Battle_option == 1:

                        # Display the Luck Battle UI
                        print("Luck Battle")
                        print(f"Number of 5 star characters: {len(player_characters[5])}")
                        print(f"Number of 4 star characters: {len(player_characters[4])}")   
                        print(f"Number of 3 star characters: {len(player_characters[3])}\n")
                        points = (len(player_characters[5]) * 100) + (len(player_characters[4]) * 6) + (len(player_characters[3]) * 2)
                        print(f"Your total points: {points}\n")
                        print("Waiting for Server...\n")

                        # Send points to server
                        client.sendall(str(points).encode())

                        # Receive and print the server's total points
                        server_points = client.recv(1024).decode()
                        print(f"Server's total points: {server_points}\n")

                        # Receive and print the result from the server
                        result = client.recv(1024).decode()
                        print(result)

                    # Displays a message that Strategy Battle is under construction
                    elif Battle_option == 2:
                        print("Under Construction (This will probably never get finished)")

                    # Displays the Battle Guide
                    elif Battle_option == 3:
                        print("Battle Guide:")
                        print("1. Luck Battle: In this battle, you win depending on how many rare characters/weapons you have. Points are awarded as follow: 5 star = 100 points, 4 star = 6 points, 3 star = 2 points.")
                        print("2. Strategy Battle: In this battle, you will need to use your characters and weapons to defeat your opponent with actual stats.")
                        print("3. You can exit the battle at any time by selecting the exit option.")
                        print("4. Have fun and enjoy the battle!")
                        input("Press Enter to continue...")

                # Process the user's choice of inventory
                elif choice == 5:

                    # Display the player's inventory
                    print("Inventory:")
                    print("Characters:")
                    print(f"5 Star Characters: {len(player_characters[5])}")
                    print(f"4 Star Characters: {len(player_characters[4])}")
                    print(f"3 Star Characters: {len(player_characters[3])}")
                    input("Press Enter to continue...")

                # Quits the game
                elif choice == 6:
                    print("Exiting the game...")

                    # Close the connection to the server
                    client.close()

                    # Exit the game
                    sys.exit()
                
    except ConnectionResetError:
        print("Connection lost. Server may have crashed or closed.")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client.close()
        print("Connection closed")

if __name__ == "__main__":
    main()