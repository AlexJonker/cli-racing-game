import curses
import Scripts.data as data
import json

autos = json.load(open("./autos.json", "r"))


def init_curs():
    scr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, 1, 233) # selectie en achtergrondkleuren
    scr.bkgd(curses.color_pair(1))
    curses.curs_set(0) # hide the little type indicator

    return scr

stdscr = init_curs()


def data_menu():
    if data.laad() != {}:
        geselecteerde_auto_naam = f"{autos[data.laad()['geselecteerde_auto']]['jaar']} {autos[data.laad()['geselecteerde_auto']]['merk']} {autos[data.laad()['geselecteerde_auto']]['naam']}"

        auto_naam = []
        for auto in data.laad()["autos"]:
            auto_naam.append(f"- {auto}")

        menu_breedte = 35
        menu_data = [
            f"Naam : {data.laad()['naam']}",
            f"geld: ${data.laad()["geld"]}",
            f"Level: {data.laad()["level"]}",
            f"XP: {data.laad()["xp"]}",
            "",
            "-" * menu_breedte ,
            "",
            f"geselecteerde auto: {geselecteerde_auto_naam}",
            f"Tune: {data.geselecteerde_auto("tune")}",
            f"Schade: {data.geselecteerde_auto("schade")}/100",
            "",
            "-" * menu_breedte ,
            "",
            f"Auto's:\n {"\n ".join(auto_naam)}",
        ]
        menu_hoogte = len(menu_data) + len(auto_naam) + 2
        menu_win = curses.newwin(menu_hoogte, menu_breedte, 0, 0)
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

def tekst(text):
    hoogte, breedte = stdscr.getmaxyx()
    y, _ = stdscr.getyx()
    x = (breedte // 2) - (len(text) // 2)
    stdscr.addstr(y, x, f"{text} \n")
    stdscr.refresh()


def vraag(text_array, options):
    def main(curs):
        selectie = 0
        count = len(options)

        while True:
            clear()
            hoogte, breedte = curs.getmaxyx()

            for text in text_array:
                tekst(text)
            tekst("--------------------")

            for num, optie in enumerate(options):
                y = num + len(text_array) + 1
                x = (breedte // 2) - (len(optie) // 2)

                if num == selectie:
                    x = x - 2
                    curs.addstr(y, x, f"> {optie} <", curses.A_REVERSE)

                else:
                    curs.addstr(y, x, f"{optie}")

            curs.refresh()

            key = curs.getch()

            if key == curses.KEY_UP:
                selectie = (selectie - 1) % count

            elif key == curses.KEY_DOWN:
                selectie = (selectie + 1) % count

            elif key in [curses.KEY_ENTER, ord("\n")]:
                return selectie

    return curses.wrapper(main)