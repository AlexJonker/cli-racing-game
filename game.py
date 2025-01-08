import json
import os

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
