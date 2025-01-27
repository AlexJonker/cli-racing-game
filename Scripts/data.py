from time import *
import os
import json

import Scripts.scherm as scherm

autos = json.load(open("./autos.json", "r"))


def laad():
    if not os.path.exists("./data.json"):
        json.dump({}, open("./data.json", "w"))

    data = json.load(open("./data.json", "r"))

    return data


def toevoegen(naam, value):
    table = laad()
    table[naam] = value
    json.dump(table, open("./data.json", "w"), indent=2)


def geselecteerde_auto(item):
    data = laad()
    geselecteerd = data['geselecteerde_auto']
    auto_naam = autos[geselecteerd]['naam']

    return data["autos"][auto_naam][item]


def pas_aan(ding, nieuw_level):
    data = laad()  # Load the current data
    geselecteerd = data['geselecteerde_auto']
    auto_naam = autos[geselecteerd]['naam']
    data["autos"][auto_naam][ding] = nieuw_level
    json.dump(data, open("./data.json", "w"), indent=2)


def toevoegen_auto(naam):
    data = laad()
    data["autos"][naam] = {"tune": 0, "schade": 0}
    json.dump(data, open("./data.json", "w"), indent=2)


def nieuwe_speler():
    stdscr = scherm.init_curs()
    scherm.clear()
    scherm.tekst("Welkom! Dit is je eerste keer hier.")
    scherm.curses.curs_set(1)
    scherm.curses.echo()
    hoogte, breedte = stdscr.getmaxyx()
    prompt = "Wat is jouw naam? "

    speler_naam = ""
    y, _ = stdscr.getyx()
    x = (breedte // 2) - (len(prompt) // 2)
    while speler_naam == "":
        stdscr.addstr(y, x, prompt)
        input_x = x + len(prompt)
        stdscr.move(y, input_x)
        stdscr.refresh()
        speler_naam = stdscr.getstr().decode('utf-8')

    scherm.curses.noecho()
    scherm.curses.curs_set(0)

    scherm.clear()
    scherm.tekst(f"Leuk je te ontmoeten, {speler_naam}!")
    sleep(1)
    starter_autos = [auto for auto in autos if auto.get('starter')]

    auto_choice = scherm.vraag(
        ["Kies je eerste auto.:"],
        [f"{auto['jaar']} {auto['merk']} {auto['naam']} ({auto['pk']} PK)" for auto in starter_autos]
    )

    scherm.clear()
    scherm.tekst(f"Je hebt de {autos[auto_choice]["jaar"]} {autos[auto_choice]["merk"]} {autos[auto_choice]["naam"]} gekozen, Goede keuze!")
    sleep(1)
    scherm.tekst("Hier is €200 om te starten!")
    scherm.tekst("Veel plezier!")
    # add the data to data.json

    toevoegen("naam", speler_naam)
    toevoegen("autos", {autos[auto_choice]["naam"]: {"tune": 0, "schade": 0}})
    toevoegen("geselecteerde_auto", auto_choice)
    toevoegen("geld", 200)
    toevoegen("level", 1)
    toevoegen("xp", 0)
    sleep(2)
