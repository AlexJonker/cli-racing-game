import json
import os
from time import *

cars = {
    1: {
        "name": "Miata",
        "brand": "Mazda",
        "year": 1990,
        "hp": 116
    },
    2: {
        "name": "AE86",
        "brand": "Toyota",
        "year": 1983,
        "hp": 112
    },
    3: {
        "name": "Swift GTi",
        "brand": "Suzuki",
        "year": 1987,
        "hp": 100
    }
}

def load():
    if not os.path.exists('./data.json'):
        json.dump({}, open('./data.json', 'w'))
    data = json.load(open('./data.json', 'r'))
    return data

def add(name, value):
    table = load()
    table[name] = value
    json.dump(table, open('./data.json', 'w'))


def new_player():
    print("Welcome! Looks like this is your first time playing.")
    print("What's your name?")
    add("name", input("Name: "))
    sleep(1)
    print(f"Nice to meet you, {load()['name']}!")
    sleep(1)
    print("Please choose your starter car:")
    print("1. 1990 Mazda Miata (116 HP)")
    print("2. 1983 Toyota AE86 (112 HP)")
    print("3. 1987 Suzuki Swift GTi (100 HP)")
    add("car", input("1, 2 or 3: "))
    add("hp", cars[int(load()['car'])]['hp'])
    print(f"You chose the {cars[int(load()['car'])]['year']} {cars[int(load()['car'])]['brand']} {cars[int(load()['car'])]['name']}, Good choice!")
    sleep(1)
    print("Have fun playing!")

if load() == {}:
    new_player()
else:
    print(f"Welcome back! Your current car is the {cars[int(load()['car'])]['year']} {cars[int(load()['car'])]['brand']} {cars[int(load()['car'])]['name']} and you are pushing {cars[int(load()['car'])]['hp']} HP.")

#################################

def race():
    print("You chose racing!")
def upgrade():
    print("You chose upgrading/reparing your car!")


def start():
    print("What do you want to do?")
    print("1. Race")
    print("2. Upgrade/repair your car")
    choice = input("1 or 2: ")
    if choice == "1":
        race()
    elif choice == "2":
        upgrade()

start()