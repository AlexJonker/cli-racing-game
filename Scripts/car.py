from time import *
import json

import Scripts.data as data
import Scripts.display as display

def race():
    playerdata = data.load()
    cars = json.load(open("./cars.json", "r"))
    selected_car = playerdata["selected_car"]
    car_name = cars[selected_car]['name']
    damage = playerdata["cars"][car_name]["damage"]
    tune = playerdata["cars"][car_name]["tune"]
    money = playerdata["money"]
    level = playerdata["level"]
    xp = playerdata["xp"]

    choice = display.ask([
        f"damage: {damage}, tune: {tune}, money: ${money}, level: {level}, xp: {xp}",
        "What do you want to do?"],
        [
            "Optie 1",
            "Optie 2"
        ])


    return


def garage():
    choice = display.ask(["Welcome to the garage!", "What do you want to do?"], ["Tune car", "Repair", "Buy new car", "Back"])

    if choice == 0:
        tune = data.current_car("tune")
        price = 100 + (tune * 50)
        choice = display.ask([f"Current tune level is: {tune}", f"Do you want to upgrade for ${price}?"], ["Yes", "No"])

        if choice == 0:
            money = data.load()["money"]

            if money >= price:
                data.add("money", money -price)
                data.modify("tune", tune + 1)

            else:
                display.clear()
                display.output("Broke boi")

        sleep(1)

    elif choice == 1:
        damage = data.current_car("damage")
        price = damage * 15

        if damage == 0:
            display.clear()
            display.output("No damage to repair!")
            sleep(2)

        else:
            choice = display.ask([f"Current damage level is: {damage}/100", f"Do you want to repair for ${price}?"], ["Yes", "No"])

            if choice == 0:
                money = data.load()["money"]

                if money >= price:
                    data.add("money", money -price)
                    data.modify("damage", 0)

                else:
                    display.clear()
                    display.output("Broke boi")
                    sleep(1)

    elif choice == 2:
        display.clear()
        display.output("W.I.P.")
        sleep(1)

    return
