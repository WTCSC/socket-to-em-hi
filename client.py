import socket
from gacha import GachaGame

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to 0.0.0.0:5000
server.bind(('0.0.0.0', 5000))

# Listen for connections
server.listen(1)
print("Waiting for connection...")

# Accept client connection
client, addr = server.accept()
print(f"Connected to {addr}")


def main():
    GachaGame.display_intro()
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

    
client.close()
server.close()