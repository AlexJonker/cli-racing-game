import os
import json
from time import sleep

import Scripts.data as data
import Scripts.display as display
import Scripts.car as car

cars = json.load(open("./cars.json", "r"))


def main():
    try:
        if data.load() == {}:
            data.new_player()
        choice = display.ask(
            [ # text
                f"Welcome back! Your current selected car is the {cars[data.load()['selected_car']]['year']} {cars[data.load()['selected_car']]['brand']} {cars[data.load()['selected_car']]['name']}.",
                f"You are currently at level {data.load()['level']} with {data.load()['xp']} XP and you have ${data.load()["money"]}",
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
            car.race()
            display.output("Woosh!")

        elif choice == 1:
            car.garage()

        elif choice == 2:
            choice = display.ask(["Welcome to the danger zone! What do you want to do?"], ["Clear all data", "Back"])

            if choice == 0:
                choice = display.ask(["Are you sure you want to remove all data?"], ["Yes", "No"])

                if choice == 0:
                    os.remove("data.json")
                    display.clear()
                    display.output("All data has been removed!")
                    sleep(2)
                    main()

        elif choice == 3:
            display.curses.curs_set(1)
            exit()

        main() # run main opnieuw wanneer je klaar bent

    except KeyboardInterrupt:
        display.curses.curs_set(1)
        exit()



if __name__ == "__main__":
    main()