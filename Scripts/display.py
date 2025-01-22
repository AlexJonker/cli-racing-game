import curses
import Scripts.data as data
import json

cars = json.load(open("./cars.json", "r"))


def init_curs():
    scr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, 1, 233) # selectie en achtergrondkleuren
    scr.bkgd(curses.color_pair(1))
    curses.curs_set(0) # hide the little type indicator

    return scr

stdscr = init_curs()


def data_menu():
    if data.load() != {}:
        selected_car_name = f"{cars[data.load()['selected_car']]['year']} {cars[data.load()['selected_car']]['brand']} {cars[data.load()['selected_car']]['name']}"

        car_names = []
        for car in data.load()["cars"]:
            car_names.append(f"- {car}")

        menu_width = 35
        menu_data = [
            f"Name : {data.load()['name']}",
            f"Money: ${data.load()["money"]}",
            f"Level: {data.load()["level"]}",
            f"XP: {data.load()["xp"]}",
            "",
            "-" * menu_width ,
            "",
            f"Selected car: {selected_car_name}",
            f"Tune: {data.current_car("tune")}",
            f"Damage: {data.current_car("damage")}/100",
            "",
            "-" * menu_width ,
            "",
            f"Owned cars:\n {"\n ".join(car_names)}",
        ]
        menu_height = len(menu_data) + len(car_names) + 2
        menu_win = curses.newwin(menu_height, menu_width, 0, 0)
        num = 0
        for item in menu_data:
            menu_win.addstr(num + 1, 1, f"{item}")
            num += 1
        menu_win.bkgd(curses.color_pair(1))
        menu_win.border()
        menu_win.refresh()


def clear():
    stdscr.erase()
    stdscr.refresh()
    data_menu() # het menu met speler data

def output(text):
    height, width = stdscr.getmaxyx()
    y, _ = stdscr.getyx()
    x = (width // 2) - (len(text) // 2)
    stdscr.addstr(y, x, f"{text} \n")
    stdscr.refresh()


def ask(text_array, options):
    def main(curs):
        current_selection = 0
        count = len(options)

        while True:
            clear()
            height, width = curs.getmaxyx()

            for text in text_array:
                output(text)
            output("--------------------")

            for num, option in enumerate(options):
                y = num + len(text_array) + 1
                x = (width // 2) - (len(option) // 2)

                if num == current_selection:
                    x = x - 2
                    curs.addstr(y, x, f"> {option} <", curses.A_REVERSE)

                else:
                    curs.addstr(y, x, f"{option}")

            curs.refresh()

            key = curs.getch()

            if key == curses.KEY_UP:
                current_selection = (current_selection - 1) % count

            elif key == curses.KEY_DOWN:
                current_selection = (current_selection + 1) % count

            elif key in [curses.KEY_ENTER, ord("\n")]:
                return current_selection

    return curses.wrapper(main)