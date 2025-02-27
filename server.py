import socket
import threading
from gacha import GachaGame

# Function to send large messages in chunks of 1024 bytes
def send_large_message(client_socket, message):
    for i in range(0, len(message), 1024):
        client_socket.send(message[i:i+1024].encode('utf-8'))

# Function to handle client connections
def handle_client(client_socket):
    try:
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

        # Send welcome message
        try:
            intro_message = GachaGame.display_intro()
            print(f"Intro message: {intro_message}")
            send_large_message(client_socket, intro_message)
        except Exception as e:
            print(f"Error displaying intro message: {e}")
            client_socket.send(b"Welcome to the Gacha Game!\n")

        # Main game loop
        while True:
            client_socket.send(b"Enter the number of draws you want (or type 'exit' to quit): ")
            gacha_num = client_socket.recv(1024).decode('utf-8').strip()

            if not gacha_num:
                print("Client disconnected.")
                break  # Exit loop if client disconnects

            if gacha_num.lower() == 'exit':
                print("Client requested to exit.")
                client_socket.send(b"Goodbye!\n")
                break

            if not gacha_num.isdigit():
                client_socket.send(b"Invalid input. Please enter a valid number.\n")
                continue

            gacha_num = int(gacha_num)
            print(f"Client wants {gacha_num} draws.")

            while gacha_num > 0:
                messages = [
                    "Choose what you want to see:\n",
                    "1. Character Banner\n",
                    "2. Weapon Banner\n",
                    "3. Banner Details\n",
                    "4. Game Guide\n",
                    "5. Battle\n",
                    "6. Exit\n"
                    ]

                for message in messages:
                    client_socket.send(message.encode('utf-8'))

                option = client_socket.recv(1024).decode('utf-8').strip()

                if not option:
                    print("Client disconnected.")
                    break  # Exit loop if client disconnects

                if not option.isdigit():
                    client_socket.send(b"Invalid option. Please enter a number between 1 and 6.\n")
                    continue

                option = int(option)

                if option == 1:
                    client_socket.send(b"Character Banner selected.\n")
                    client_socket.send(b"Choose a banner (1 for Fantasy, 2 for Ocean): ")
                    banner_option = client_socket.recv(1024).decode('utf-8').strip()

                    if not banner_option.isdigit():
                        client_socket.send(b"Invalid option. Please enter 1 or 2.\n")
                        continue

                    banner_option = int(banner_option)

                    if banner_option == 1:
                        client_socket.send(b"Fantasy Banner selected.\n")
                        client_socket.send(b"Do you want to do 1 or 10 draws? ")
                        draw_option = client_socket.recv(1024).decode('utf-8').strip()

                        if not draw_option.isdigit():
                            client_socket.send(b"Invalid option. Please enter 1 or 10.\n")
                            continue

                        draw_option = int(draw_option)

                        if draw_option == 1:
                            if gacha_num > 0:
                                rarity = GachaGame.char_gacha()
                                if rarity == 5:
                                    character = GachaGame.get_5_star_fantasy_character()
                                elif rarity == 4:
                                    character = GachaGame.get_4_star_character()
                                elif rarity == 3:
                                    character = GachaGame.get_3_star_character()
                                player_characters[rarity].append(character)
                                gacha_num -= 1
                                client_socket.send(f"You got {character[0]}! ({rarity} Star)\n".encode('utf-8'))
                            else:
                                client_socket.send(b"You don't have anymore draws. Please play the game.\n")

                        elif draw_option == 10:
                            if gacha_num >= 10:
                                for i in range(10):
                                    rarity = GachaGame.char_gacha()
                                    if rarity == 5:
                                        character = GachaGame.get_5_star_fantasy_character()
                                    elif rarity == 4:
                                        character = GachaGame.get_4_star_character()
                                    elif rarity == 3:
                                        character = GachaGame.get_3_star_character()
                                    player_characters[rarity].append(character)
                                    client_socket.send(f"You got {character[0]}! ({rarity} Star)\n".encode('utf-8'))
                                gacha_num -= 10
                            else:
                                client_socket.send(b"You don't have enough draws. Please do single draws.\n")

                    elif banner_option == 2:
                        client_socket.send(b"Ocean Banner selected.\n")
                        client_socket.send(b"Do you want to do 1 or 10 draws? ")
                        draw_option = client_socket.recv(1024).decode('utf-8').strip()

                        if not draw_option.isdigit():
                            client_socket.send(b"Invalid option. Please enter 1 or 10.\n")
                            continue

                        draw_option = int(draw_option)

                        if draw_option == 1:
                            if gacha_num > 0:
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
                    client_socket.send(b"Weapon Banner selected.\n")
                    client_socket.send(b"Do you want to do 1 or 10 draws? ")
                    draw_option = client_socket.recv(1024).decode('utf-8').strip()

                    if not draw_option.isdigit():
                        client_socket.send(b"Invalid option. Please enter 1 or 10.\n")
                        continue

                    draw_option = int(draw_option)

                    if draw_option == 1:
                        if gacha_num > 0:
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
                    battle_option = client_socket.recv(1024).decode('utf-8').strip()

                    if not battle_option.isdigit():
                        client_socket.send(b"Invalid option. Please enter a number between 1 and 4.\n")
                        continue

                    battle_option = int(battle_option)

                    if battle_option == 1:
                        client_socket.send(b"Luck Battle\n")
                        client_socket.send(f"Number of 5 star characters: {len(player_characters[5])}\n".encode('utf-8'))
                        client_socket.send(f"Number of 4 star characters: {len(player_characters[4])}\n".encode('utf-8'))
                        client_socket.send(f"Number of 3 star characters: {len(player_characters[3])}\n".encode('utf-8'))
                        client_socket.send(f"Number of 5 star weapons: {len(player_weapons[5])}\n".encode('utf-8'))
                        client_socket.send(f"Number of 4 star weapons: {len(player_weapons[4])}\n".encode('utf-8'))
                        client_socket.send(f"Number of 3 star weapons: {len(player_weapons[3])}\n".encode('utf-8'))
                        points = (len(player_characters[5]) * 10) + (len(player_characters[4]) * 6) + (len(player_characters[3]) * 2) + (len(player_weapons[5]) * 10) + (len(player_weapons[4]) * 6) + (len(player_weapons[3]) * 2)
                        client_socket.send(f"Your total points: {points}\n".encode('utf-8'))

                    elif battle_option == 2:
                        client_socket.send(b"Under Construction\n")

                    elif battle_option == 3:
                        client_socket.send(b"Battle Guide:\n1. Luck Battle: In this battle, you win depending on how many rare characters/weapons you have.\n2. Strategy Battle: In this battle, you will need to use your characters and weapons to defeat your opponent with actual stats.\n3. You can exit the battle at any time by selecting the exit option.\n4. Have fun and enjoy the battle!\n")
                        client_socket.send(b"Press Enter to continue...\n")
                        client_socket.recv(1024)  # Wait for the client to press Enter

                    elif battle_option == 4:
                        continue

                elif option == 6:
                    client_socket.send(b"Exit\n")
                    break

                gacha_num -= 1  # Decrement the number of draws

    except socket.timeout:
        print("Client connection timed out.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Connection closed.")

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
            gacha_num = input("Enter the number of draws you want: ").strip()
            if not gacha_num.isdigit():
                print("Invalid input. Please enter a valid number.")
                continue
            gacha_num = int(gacha_num)
            print(f"You chose {gacha_num} draws.")

            while gacha_num > 0:
                print("Choose what you want to see:\n1. Character Banner\n2. Weapon Banner\n3. Banner Details\n4. Game Guide\n5. Battle\n6. Exit")
                option = input().strip()
                if not option.isdigit():
                    print("Invalid option. Please enter a number between 1 and 6.")
                    continue
                option = int(option)

                if option == 1:
                    print("Character Banner selected.")
                elif option == 2:
                    print("Weapon Banner selected.")
                elif option == 3:
                    print("Banner Details selected.")
                elif option == 4:
                    print("Game Guide selected.")
                elif option == 5:
                    print("Battle selected.")
                elif option == 6:
                    print("Exit")
                    return
                else:
                    print("Invalid option. Please enter a number between 1 and 6.")
    except Exception as e:
        print(f"Error: {e}")

# Main server function
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allows immediate reuse of the port

    port = input("Enter the port number you want to use: ")
    port = int(port) if port.isdigit() else 5000

    server.bind(('', port))
    server.listen(1)  # Only allow one client at a time
    print(f"Server listening on port {port}...")

    try:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")

        # Handle the client in the main thread
        handle_client(client_socket)

    except KeyboardInterrupt:
        print("\nServer shutting down.")
    finally:
        server.close()

if __name__ == "__main__":
    main()