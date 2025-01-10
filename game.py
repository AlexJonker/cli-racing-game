import json
import os
from time import *
import curses
stdscr = curses.initscr()
stdscr.clear()
stdscr.refresh()

curses.start_color()
curses.init_pair(1, 1, 233) # selectie en achtergrond kleuren
stdscr.bkgd(curses.color_pair(1))
curses.curs_set(0) # balkje wanneer je typt weg

cars = {
    1: {"name": "Miata", "brand": "Mazda", "year": 1990, "hp": 116},
    2: {"name": "AE86", "brand": "Toyota", "year": 1983, "hp": 112},
    3: {"name": "Swift GTi", "brand": "Suzuki", "year": 1987, "hp": 100},
}


try:
    def clear():
        stdscr.clear()
        stdscr.refresh()

    def display(text):
        height, width = stdscr.getmaxyx()
        y, _ = stdscr.getyx()
        x = (width // 2) - (len(text) // 2)
        stdscr.addstr(y, x, f"{text} \n")
        stdscr.refresh()
    def load():
        if not os.path.exists("./data.json"):
            json.dump({}, open("./data.json", "w"))
        data = json.load(open("./data.json", "r"))
        return data


    def add(name, value):
        table = load()
        table[name] = value
        json.dump(table, open("./data.json", "w"))


    def ask(options):
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        answer = input("Please enter the number of your choice: ")
        if (answer.isnumeric()) and (int(answer) in range(1, len(options) + 1)):
            return int(answer)
        else:
            print("Invalid choice, please try again.")
            return ask(options)


    def new_player():
        print("Welcome! Looks like this is your first time playing.")
        print("What's your name?")
        add("name", input("Name: "))
        print(f"Nice to meet you, {load()['name']}!")
        sleep(1)
        print("Please choose your starter car:")
        add("car", ask(["1990 Mazda Miata (116 HP)", "1983 Toyota AE86 (112 HP", "1987 Suzuki Swift GTi (100 HP)",]))
        add("hp", cars[int(load()["car"])]["hp"])
        print(f"You chose the {cars[int(load()['car'])]['year']} {cars[int(load()['car'])]['brand']} {cars[int(load()['car'])]['name']}, Good choice!")
        sleep(1)
        print("Here's $3K to get started!")
        add("money", 3000)
        print("Have fun playing!")
        # adding some default values to the data.json file
        add("level", 1)
        add("xp", 0)
        sleep(2)


    #################################


    def race():
        print("You chose racing!")
        return

    def upgrade():
        print("You chose upgrading/repairing your car!")
        return


    def start():
        if load() == {}:
            new_player()
        else:
            print(f"Welcome back! Your current car is the {cars[int(load()['car'])]['year']} {cars[int(load()['car'])]['brand']} {cars[int(load()['car'])]['name']} and you are pushing {load()["hp"]} HP.")

        print("---------------------------------------")
        print("What do you want to do?")
        choice = ask(["Race", "Upgrade/repair your car", "Exit"])
        if choice == 1:
            race()
        elif choice == 2:
            upgrade()
        elif choice == 3:
            print("Goodbye!")
            exit()

        start()


    start()
except KeyboardInterrupt:
    print("")
    print("Goodbye!")
    exit()