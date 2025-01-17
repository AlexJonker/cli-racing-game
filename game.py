from time import *
import Scripts.data as data
import Scripts.display as display
import os
import json
stdscr = display.curses.initscr()

display.curses.start_color()
display.curses.init_pair(1, 1, 233) # selectie en achtergrondkleuren
stdscr.bkgd(display.curses.color_pair(1))
display.curses.curs_set(0) # hide the little type indicator


cars = json.load(open("./cars.json", "r"))


try:

    def race():
        display.clear()
        display.output("W.I.P.")
        sleep(1)

        return

    def garage():
        choice = display.ask(["Welcome to the garage!", "What do you want to do?"], ["Tune car", "Buy new car", "Repair", "Back"])
        if choice == 0:
            display.clear()
            display.output("W.I.P.")
            sleep(1)
        elif choice == 1:
            display.clear()
            display.output("W.I.P.")
            sleep(1)
        elif choice == 2:
            display.clear()
            display.output("W.I.P.")
            sleep(1)
        return


    def start():
        if data.load() == {}:
            data.new_player(stdscr)
        choice = display.ask(
            [ # text
                f"Welcome back! Your current selected car is the {cars[data.load()['selected_car']]['year']} {cars[data.load()['selected_car']]['brand']} {cars[data.load()['selected_car']]['name']}.",
                f"You are currently at level {data.load()['level']} with {data.load()['xp']} XP.",
                "What do you want to do?"
            ],
            [ # options
                "Race",
                "garage",
                "Danger zone",
                "Exit"
            ]
        )
        if choice == 0:
            race()
        elif choice == 1:
            garage()
        elif choice == 2:
            choice = display.ask(["Welcome to the danger zone! What do you want to do?"], ["Clear all data", "Back"])
            if choice == 0:
                choice = display.ask(["Are you sure you want to remove all data?"], ["Yes", "No"])
                if choice == 0:
                    os.remove("data.json")
                    display.clear()
                    display.output("All data has been removed!")
                    sleep(2)
                    start()
        elif choice == 3:
            display.curses.curs_set(1)
            exit()

        start()


    start()
except KeyboardInterrupt:
    display.curses.curs_set(1)
    exit()
