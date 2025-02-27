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
