import json
import os
from time import *
import curses
stdscr = curses.initscr()
stdscr.clear()
stdscr.refresh()

curses.start_color()
curses.init_pair(1, 1, 233) # selectie en achtergrondkleuren
stdscr.bkgd(curses.color_pair(1))
curses.curs_set(0) # hide the little type indicator
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



    def ask(textarr, options):
        def main(curs):
            current_selection = 0
            count = len(options)

            while True:
                clear()
                height, width = curs.getmaxyx()

                for text in textarr:
                    display(text)
                display("--------------------")
                # display(text)

                for num, option in enumerate(options):
                    y = num + len(textarr) + 1
                    x = (width // 2) - (len(option) // 2)
                    if num == current_selection:
                        curs.addstr(y, x, f"> {option}", curses.A_REVERSE)
                    else:
                        curs.addstr(y, x, f"  {option}")

                curs.refresh()

                key = curs.getch()
                if key == curses.KEY_UP:
                    current_selection = (current_selection - 1) % count
                elif key == curses.KEY_DOWN:
                    current_selection = (current_selection + 1) % count
                elif key in [curses.KEY_ENTER, ord("\n")]:
                    return current_selection + 1

        return curses.wrapper(main)





    def new_player():
        clear()
        display("Welcome! Looks like this is your first time playing.")

        curses.curs_set(1)
        curses.echo()
        height, width = stdscr.getmaxyx()
        prompt = "What's your name? "
        y, _ = stdscr.getyx()
        x = (width // 2) - (len(prompt) // 2)

        stdscr.addstr(y, x, prompt)
        input_x = x + len(prompt)
        stdscr.move(y, input_x)
        stdscr.refresh()

        player_name = stdscr.getstr().decode('utf-8')
        curses.noecho()
        curses.curs_set(0)

        display(f"Nice to meet you, {player_name}!")
        sleep(1)
        car = ask(["Please choose your starter car:"], ["1990 Mazda Miata (116 HP)", "1983 Toyota AE86 (112 HP", "1987 Suzuki Swift GTi (100 HP)",])
        clear()
        display(f"You chose the {cars[car]["year"]} {cars[car]["brand"]} {cars[car]["name"]}, Good choice!")
        sleep(1)
        display("Here's $3K to get started!")
        display("Have fun playing!")
        # add the data to data.json

        add("name", player_name)
        add("car", car)
        add("hp", cars[int(load()["car"])]["hp"])
        add("money", 3000)
        add("level", 1)
        add("xp", 0)
        sleep(2)


    #################################


    def race():
        clear()
        display("You chose racing!")
        return

    def upgrade():
        clear()
        display("You chose upgrading/repairing your car!")
        return


    def start():
        if load() == {}:
            new_player()
        choice = ask(
            [ # text
                f"Welcome back! Your current car is the {cars[int(load()['car'])]['year']} {cars[int(load()['car'])]['brand']} {cars[int(load()['car'])]['name']} and you are pushing {load()["hp"]} HP.",
                f"You are currently at level {load()['level']} with {load()['xp']} XP.",
                "What do you want to do?"
            ],
            [ # options
                "Race",
                "Upgrade/repair your car",
                "Danger zone",
                "Exit"
            ]
        )
        if choice == 1:
            race()
        elif choice == 2:
            upgrade()
        elif choice == 3:
            choice = ask(["Welcome to the danger zone! What do you want to do?"], ["Clear all data", "Back"])
            if choice == 1:
                choice = ask(["Are you sure you want to remove all data?"], ["Yes", "No"])
                if choice == 1:
                    os.remove("./data.json")
                    clear()
                    display("All data has been removed!")
                    sleep(2)
                    start()
        elif choice == 4:
            curses.curs_set(1)
            exit()

        start()


    start()
except KeyboardInterrupt:
    curses.curs_set(1)
    exit()
