import curses


def init_curs():
    scr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, 1, 233) # selectie en achtergrondkleuren
    scr.bkgd(curses.color_pair(1))
    curses.curs_set(0) # hide the little type indicator

    return scr

stdscr = init_curs()


def clear():
    stdscr.clear()
    stdscr.refresh()

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