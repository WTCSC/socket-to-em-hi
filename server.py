import socket
import threading
from gacha import GachaGame

# Function to handle client connections
def handle_client(client_socket):
    try:
        # Send a welcome message to the client
        intro_message = GachaGame.display_intro()
        client_socket.send(intro_message.encode('utf-8'))

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
        
        # Main game loop
        while True:
            # Receive the client's choice
            client_socket.send(b"Enter the number of draws you want: ")
            gacha_num = client_socket.recv(1024).decode('utf-8').strip()

            if gacha_num.isdigit():
                gacha_num = int(gacha_num)

                while gacha_num > 0:
                    client_socket.send(b"Choose what you want to see:\n1. Character Banner\n2. Weapon Banner\n3. Banner Details\n4. Game Guide\n5. Battle\n6. Exit\n")
                    option = client_socket.recv(1024).decode('utf-8').strip()
                    if not option.isdigit():
                        client_socket.send(b"Invalid option. Please enter a number between 1 and 6.\n")
                        continue
                    option = int(option)

                    if option == 1:
                        banners = f"{GachaGame.character_banner_art}"
                        client_socket.send(banners.encode('utf-8'))
                        client_socket.send(b"Choose a banner (1 for Fantasy, 2 for Ocean): ")
                        banner_option = client_socket.recv(1024).decode('utf-8').strip()
                        if not banner_option.isdigit():
                            client_socket.send(b"Invalid option. Please enter 1 or 2.\n")
                            continue
                        banner_option = int(banner_option)

                        if banner_option == 1:
                            client_socket.send(f"{GachaGame.fantasy_banner}".encode('utf-8'))
                            client_socket.send(b"Do you want to do 1 or 10 draws? ")
                            draw_option = client_socket.recv(1024).decode('utf-8').strip()
                            if not draw_option.isdigit():
                                client_socket.send(b"Invalid option. Please enter 1 or 10.\n")
                                continue
                            draw_option = int(draw_option)

                            if draw_option == 1:
                                if gacha_num > 0:
                                    GachaGame.draw_animation()
                                    rarity = GachaGame.char_gacha()
                                    if rarity == 5:
                                        character = GachaGame.get_5_star_fantasy_character()
                                    elif rarity == 4:
                                        character = GachaGame.get_4_star_character()
                                    elif rarity == 3:
                                        character = GachaGame.get_3_star_character()
                                    player_characters[rarity].append(character)
                                    gacha_num -= 1
                                else:
                                    client_socket.send(b"You don't have anymore draws. Please play the game.\n")
                                    
                            elif draw_option == 10:
                                if gacha_num >= 10:
                                    for i in range(10):
                                        GachaGame.draw_animation()
                                        rarity = GachaGame.char_gacha()
                                        if rarity == 5:
                                            character = GachaGame.get_5_star_fantasy_character()
                                        elif rarity == 4:
                                            character = GachaGame.get_4_star_character()
                                        elif rarity == 3:
                                            character = GachaGame.get_3_star_character()
                                        player_characters[rarity].append(character)
                                    gacha_num -= 10
                                else:
                                    client_socket.send(b"You don't have enough draws. Please do single draws.\n")

                        elif banner_option == 2:
                            client_socket.send(f"{GachaGame.ocean_banner}".encode('utf-8'))
                            client_socket.send(b"Do you want to do 1 or 10 draws? ")
                            draw_option = client_socket.recv(1024).decode('utf-8').strip()
                            if not draw_option.isdigit():
                                client_socket.send(b"Invalid option. Please enter 1 or 10.\n")
                                continue
                            draw_option = int(draw_option)

                            if draw_option == 1:
                                if gacha_num > 0:
                                    GachaGame.draw_animation()
                                    rarity = GachaGame.char_gacha()
                                    if rarity == 5:
                                        character = GachaGame.get_5_star_ocean_character()
                                    elif rarity == 4:
                                        character = GachaGame.get_4_star_character()
                                    elif rarity == 3:
                                        character = GachaGame.get_3_star_character()
                                    player_characters[rarity].append(character)
                                    gacha_num -= 1
                                else:
                                    client_socket.send(b"You don't have any more draws. Please play the game.\n")
                                    
                            elif draw_option == 10:
                                if gacha_num >= 10:
                                    for i in range(10):
                                        GachaGame.draw_animation()
                                        rarity = GachaGame.char_gacha()
                                        if rarity == 5:
                                            character = GachaGame.get_5_star_ocean_character()
                                        elif rarity == 4:
                                            character = GachaGame.get_4_star_character()
                                        elif rarity == 3:
                                            character = GachaGame.get_3_star_character()
                                        player_characters[rarity].append(character)
                                    gacha_num -= 10
                                else:
                                    client_socket.send(b"You don't have enough draws. Please do single draws.\n")

                    elif option == 2:
                        client_socket.send(f"{GachaGame.weapon_banner}".encode('utf-8'))
                        client_socket.send(b"Do you want to do 1 or 10 draws? ")
                        draw_option = client_socket.recv(1024).decode('utf-8').strip()
                        if not draw_option.isdigit():
                            client_socket.send(b"Invalid option. Please enter 1 or 10.\n")
                            continue
                        draw_option = int(draw_option)

                        if draw_option == 1:
                            if gacha_num > 0:
                                GachaGame.draw_animation()
                                rarity = GachaGame.weapon_gacha()
                                if rarity == 5:
                                    weapon = GachaGame.get_5_star_weapon()
                                elif rarity == 4:
                                    weapon = GachaGame.get_4_star_weapon()
                                elif rarity == 3:
                                    weapon = GachaGame.get_3_star_weapon()
                                player_weapons[rarity].append(weapon)
                                gacha_num -= 1
                            else:
                                client_socket.send(b"You don't have any more draws. Please play the game.\n")
                                    
                        elif draw_option == 10:
                            if gacha_num >= 10:
                                for i in range(10):
                                    GachaGame.draw_animation()
                                    rarity = GachaGame.weapon_gacha()
                                    if rarity == 5:
                                        weapon = GachaGame.get_5_star_weapon()
                                    elif rarity == 4:
                                        weapon = GachaGame.get_4_star_weapon()
                                    elif rarity == 3:
                                        weapon = GachaGame.get_3_star_weapon()
                                    player_weapons[rarity].append(weapon)
                                gacha_num -= 10
                            else:
                                client_socket.send(b"You don't have enough draws. Please do single draws.\n")

                    elif option == 3:
                        client_socket.send(b"Banner Details:\n1. Fantasy Banner\n2. Ocean Banner\n3. Weapon Banner\n4. Exit\n")
                        banner_option = client_socket.recv(1024).decode('utf-8').strip()
                        if not banner_option.isdigit():
                            client_socket.send(b"Invalid option. Please enter a number between 1 and 4.\n")
                            continue
                        banner_option = int(banner_option)
                        if banner_option == 1:
                            client_socket.send(b"There are 3 exclusive 5 star characters in the Fantasy Banner (Dragon Deez, Ninja, and Cave Diver). The 3 and 4 star characters are shared between the character banners. The 4 star characters are Florida Man, Big Chungus, and Among Us. The 3 star characters are Stick Dude, Stick Woman, Mr. Beest. The rates for this banner are 0.5% for 5 star, 9.5% for 4 star, and 90% for 3 star.\n")
                        elif banner_option == 2:
                            client_socket.send(b"There are 3 exclusive 5 star characters in the Ocean Banner (Jeff the Shark, Eye of Rah, and Property in Egypt). The 3 and 4 star characters are shared between the character banners. The 4 star characters are Florida Man, Big Chungus, and Among Us. The 3 star characters are Stick Dude, Stick Woman, Mr. Beest. The rates for this banner are 0.5% for 5 star, 9.5% for 4 star, and 90% for 3 star.\n")
                        elif banner_option == 3:
                            client_socket.send(b"There are six 5 star weapons in the Weapon Banner (America, Shoes, Low Taper Fade, Nuts, Property, and Eye of Ra). The 4 star weapons are Scissors, Knife, and Red 40. The 3 star weapons are Stick, Branch, and Lunchly. The rates for this banner are 0.5% for 5 star, 9.5% for 4 star, and 90% for 3 star.\n")
                        elif banner_option == 4:
                            continue

                    elif option == 4:
                        client_socket.send(b"Game Guide:\n1. The game is a gacha game where you can summon characters and weapons.\n2. There are two character banners (Fantasy and Ocean) and one weapon banner.\n3. The rates for 5 star characters and weapons are 0.5%, 4 star characters and weapons are 9.5%, and 3 star characters and weapons are 90%.\n4. You can do single draws or 10 draws at a time.\n5. You can exit the game at any time by selecting the exit option.\n6. Have fun and enjoy the game!\n")
                        client_socket.send(b"Press Enter to continue...\n")
                        client_socket.recv(1024)  # Wait for the client to press Enter

                    elif option == 5:
                        client_socket.send(b"Choose Your Battle:\n1. Luck Battle\n2. Strategy Battle\n3. Battle Guide\n4. Exit\n")
                        Battle_option = client_socket.recv(1024).decode('utf-8').strip()
                        if not Battle_option.isdigit():
                            client_socket.send(b"Invalid option. Please enter a number between 1 and 4.\n")
                            continue
                        Battle_option = int(Battle_option)

                        if Battle_option == 1:
                            client_socket.send(b"Luck Battle\n")
                            client_socket.send(f"Number of 5 star characters: {len(player_characters[5])}\n".encode('utf-8'))
                            client_socket.send(f"Number of 4 star characters: {len(player_characters[4])}\n".encode('utf-8'))
                            client_socket.send(f"Number of 3 star characters: {len(player_characters[3])}\n".encode('utf-8'))
                            client_socket.send(f"Number of 5 star weapons: {len(player_weapons[5])}\n".encode('utf-8'))
                            client_socket.send(f"Number of 4 star weapons: {len(player_weapons[4])}\n".encode('utf-8'))
                            client_socket.send(f"Number of 3 star weapons: {len(player_weapons[3])}\n".encode('utf-8'))
                            points = (len(player_characters[5]) * 10) + (len(player_characters[4]) * 6) + (len(player_characters[3]) * 2) + (len(player_weapons[5]) * 10) + (len(player_weapons[4]) * 6) + (len(player_weapons[3]) * 2)
                            client_socket.send(f"Your total points: {points}\n".encode('utf-8'))

                        elif Battle_option == 2:
                            client_socket.send(b"Under Construction\n")

                        elif Battle_option == 3:
                            client_socket.send(b"Battle Guide:\n1. Luck Battle: In this battle, you win depending on how many rare characters/weapons you have.\n2. Strategy Battle: In this battle, you will need to use your characters and weapons to defeat your opponent with actual stats.\n3. You can exit the battle at any time by selecting the exit option.\n4. Have fun and enjoy the battle!\n")
                            client_socket.send(b"Press Enter to continue...\n")
                            client_socket.recv(1024)  # Wait for the client to press Enter

                        elif Battle_option == 4:
                            continue

                    elif option == 6:
                        client_socket.send(b"Exit\n")
                        break

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the client connection
        client_socket.close()

# Function to handle host interactions
def handle_host():
    try:
        intro_message = GachaGame.display_intro()
        print(intro_message)

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

        # Main game loop
        while True:
            # Receive the host's choice
            gacha_num = GachaGame.get_gacha_option()

            print(f"You chose {gacha_num} draws.")
            # Perform gacha draws and print results
            for _ in range(gacha_num):
                result = GachaGame.char_gacha()
                print(f"Gacha result: {result}-Star Item")
            print("✨ Summon Complete! ✨")
            break
    except Exception as e:
        print(f"Error: {e}")

# Main server function
def main():
    # Create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Port Selection
    port = input("Enter the port number you want to use: ")
    if port.isdigit():
        port = int(port)
    else:
        print("Invalid input. Using default port 5000.")
        port = 5000

    # Bind the socket to an IP address and port
    server.bind(('', port))

    # Listen for incoming connections
    server.listen(1)  # Only allow one connection at a time
    print(f"Server listening on port {port}")

    # Accept a new client connection
    client_socket, addr = server.accept()
    print(f"Accepted connection from {addr}")

    # Start a thread to handle the client connection
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

    # Handle the host interactions
    handle_host()

    # Wait for the client thread to finish
    client_thread.join()

if __name__ == "__main__":
    main()