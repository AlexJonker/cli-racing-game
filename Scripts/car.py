from time import *

import Scripts.data as data
import Scripts.display as display

def race():
    display.clear()
    display.output("W.I.P.")
    sleep(1)

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
