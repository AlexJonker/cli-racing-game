from time import *
import Scripts.display as display
import os
import json

def load():
    if not os.path.exists("./data.json"):
        json.dump({}, open("./data.json", "w"))
    data = json.load(open("./data.json", "r"))
    return data


def add(name, value):
    table = load()
    table[name] = value
    json.dump(table, open("./data.json", "w"), indent=2)



def new_player(stdscr):
    cars = json.load(open("./cars.json", "r"))
    display.clear()
    display.output("Welcome! Looks like this is your first time playing.")

    display.curses.curs_set(1)
    display.curses.echo()
    height, width = stdscr.getmaxyx()
    prompt = "What's your name? "
    y, _ = stdscr.getyx()
    x = (width // 2) - (len(prompt) // 2)

    stdscr.addstr(y, x, prompt)
    input_x = x + len(prompt)
    stdscr.move(y, input_x)
    stdscr.refresh()

    player_name = stdscr.getstr().decode('utf-8')
    display.curses.noecho()
    display.curses.curs_set(0)

    display.output(f"Nice to meet you, {player_name}!")
    sleep(1)
    starter_cars = [car for car in cars if car.get('starter')]
    car = display.ask(
        ["Please choose your starter car:"],
        [f"{car['year']} {car['brand']} {car['name']} ({car['hp']} HP)" for car in starter_cars]
    )

    display.clear()
    display.output(f"You chose the {cars[car]["year"]} {cars[car]["brand"]} {cars[car]["name"]}, Good choice!")
    sleep(1)
    display.output("Here's $200 to get started!")
    display.output("Have fun playing!")
    # add the data to data.json

    add("name", player_name)
    add("cars", {cars[car]["name"]: {"tune": 0}})
    add("selected_car", car)
    add("money", 200)
    add("level", 1)
    add("xp", 0)
    sleep(2)
