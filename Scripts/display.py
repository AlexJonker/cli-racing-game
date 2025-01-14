import curses
stdscr = curses.initscr()
stdscr.clear()
stdscr.refresh()


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
                return current_selection

    return curses.wrapper(main)