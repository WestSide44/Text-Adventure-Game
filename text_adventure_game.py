import time

def intro():
    print("\033[1;34m--�    --� ------� --�     --�---�   --�--�-------�-------�\033[0m")
    print("\033[1;34m--�    --�--�===--�--�     --�----�  --�--�--�====---�====-\033[0m")
    print("\033[1;34m--� -� --�--�   --�--�     --�--�--� --�--�-------�-----�  \033[0m")
    print("\033[1;34m--�---�--�--�   --�--�     --�--�L--�--�--�L====--�--�==-  \033[0m")
    print("\033[1;34mL---�---�-L------�--------�--�--� L----�--�-------�-------�\033[0m")
    print("\033[1;34m L==-L==-  L=====- L======-L=-L=-  L===-L=-L======-L======-\033[0m")
    time.sleep(1)
    print("\nWelcome to the Text-Based Adventure Game!")
    time.sleep(1)
    print("You find yourself standing at a crossroads...")
    time.sleep(1)
    print("Each path leads to a different adventure...")
    time.sleep(1)

def choose_path():
    print("\nWhich path will you choose?")
    print("\033[1;32m1. The Dark Forest\033[0m")
    print("\033[1;33m2. The Rocky Mountains\033[0m")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        dark_forest()
    elif choice == "2":
        rocky_mountains()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        choose_path()

def dark_forest():
    print("\nYou enter the \033[1;32mdark forest\033[0m...")
    time.sleep(1)
    print("You hear strange noises all around you...")
    time.sleep(1)
    print("You see a faint light in the distance. Do you:")
    print("1. Follow the light")
    print("2. Stay put")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\nYou follow the light and find a treasure chest!")
        time.sleep(1)
        print("Congratulations, you win!")
    elif choice == "2":
        print("\nYou stay put and nothing happens.")
        time.sleep(1)
        print("You eventually find your way out of the forest.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        dark_forest()

def rocky_mountains():
    print("\nYou climb the \033[1;33mrocky mountains\033[0m...")
    time.sleep(1)
    print("It's a challenging journey, but you press on...")
    time.sleep(1)
    print("You reach a fork in the path. Do you:")
    print("1. Take the steep path")
    print("2. Take the winding path")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\nYou take the steep path and reach the summit!")
        time.sleep(1)
        print("You enjoy the breathtaking view from the top.")
    elif choice == "2":
        print("\nYou take the winding path and get lost.")
        time.sleep(1)
        print("After wandering for hours, you find your way back down.")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        rocky_mountains()

def main():
    intro()
    choose_path()

if __name__ == "__main__":
    main()
