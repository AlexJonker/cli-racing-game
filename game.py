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
    print("Please choose your starter car:")
    print("1. 1990 Mazda Miata (116 HP)")
    print("2. 1983 Toyota AE86 (112 HP)")
    print("3. 1987 Suzuki Swift GTi (100 HP)")
    add("car", input("1, 2 or 3: "))

if load() == {}:
    new_player()
else:
    print(f"Welcome back! Your current car is the {cars[int(load()['car'])]['year']} {cars[int(load()['car'])]['brand']} {cars[int(load()['car'])]['name']} and you are pushing {cars[int(load()['car'])]['hp']} HP.")
