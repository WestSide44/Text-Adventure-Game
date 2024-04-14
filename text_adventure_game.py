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

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name] -= quantity
            if self.items[item_name] <= 0:
                del self.items[item_name]

    def show_inventory(self):
        print("Inventory:")
        for item, quantity in self.items.items():
            print(f"{item}: {quantity}")

# Example usage:
inventory = Inventory()
inventory.add_item("Key")
inventory.add_item("Potion", 3)
inventory.add_item("Map")
inventory.show_inventory()

inventory.remove_item("Potion", 2)
inventory.show_inventory()

import time
import random

class Player:
    def __init__(self, level=1, health=100, attack=10):
        self.level = level
        self.health = health
        self.attack = attack
        self.inventory = Inventory()

    def display_stats(self):
        print(f"Level: {self.level}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        self.inventory.show_inventory()

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def display_enemy(self):
        print(f"Enemy: {self.name}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")

def intro():
    # Your intro code here...

def choose_path(player):
    # Your path selection code here...

def combat(player, enemy):
    print(f"A wild {enemy.name} appears!")
    time.sleep(1)
    
    while player.health > 0 and enemy.health > 0:
        print("\nWhat will you do?")
        print("1. Fight")
        print("2. Run")
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            player_attack = random.randint(1, player.attack)
            enemy_attack = random.randint(1, enemy.attack)

            print(f"You attack the {enemy.name} for {player_attack} damage.")
            enemy.health -= player_attack

            if enemy.health > 0:
                print(f"The {enemy.name} attacks you for {enemy_attack} damage.")
                player.health -= enemy_attack
        elif choice == "2":
            print("You run away!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    if player.health <= 0:
        print("You were defeated.")
    elif enemy.health <= 0:
        print(f"You defeated the {enemy.name}!")

def main():
    intro()
    
    player = Player()
    
    # Example enemy
    enemy = Enemy("Goblin", 50, 8)
    
    choose_path(player)
    
    # Combat example
    combat(player, enemy)
    
    player.display_stats()

if __name__ == "__main__":
    main()

























