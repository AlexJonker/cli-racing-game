from time import *
import json
import random

import Scripts.data as data
import Scripts.scherm as scherm

autos = json.load(open("./autos.json", "r"))


def race():
    spelerdata = data.laad()
    geselecteerde_auto = spelerdata["geselecteerde_auto"]
    auto_naam = autos[geselecteerde_auto]['naam']
    schade = spelerdata["autos"][auto_naam]["schade"]
    tune = spelerdata["autos"][auto_naam]["tune"]
    geld = spelerdata["geld"]
    level = spelerdata["level"]


    stdscr = scherm.init_curs()
    scherm.curses.curs_set(1)
    scherm.curses.echo()
    hoogte, breedte = stdscr.getmaxyx()
    scherm.clear()
    prompt = f"Hoeveel geld wil je inzetten? Je hebt €{geld}. "

    inzet_geld = ""
    y, _ = stdscr.getyx()
    x = (breedte // 2) - (len(prompt) // 2)
    while inzet_geld == "":
        scherm.clear()
        stdscr.addstr(y, x, prompt)
        input_x = x + len(prompt)
        stdscr.move(y, input_x)
        stdscr.refresh()

        try:
            inzet_geld = int(stdscr.getstr().decode('utf-8'))
            if inzet_geld > geld:
                scherm.clear()
                scherm.tekst("Je hebt niet genoeg geld.")
                inzet_geld = ""
                sleep(1)

        except ValueError:
            scherm.clear()
            scherm.tekst("Voer een geldig getal in.")
            inzet_geld = ""
            sleep(1)

    scherm.curses.noecho()
    scherm.curses.curs_set(0)
    scherm.clear()
    scherm.tekst(f"Je hebt €{inzet_geld} ingezet.")

    sleep(2)

    snelheid = scherm.vraag(["Hoe snel wil je gaan?", "Hoe sneller je gaat hoe meer kans om te winnen maar ook meer schade."], ["Snel", "Normaal", "Traag"])

    winkans = (100 - schade) * ((1 + tune) * 2) * (3 - snelheid) / (level * 10)
    schade = (4 - snelheid) * 3
    data.pas_aan("schade", data.geselecteerde_auto("schade") + schade)

    scherm.clear()

    winst = random.random() * 100

    if winst < winkans:
        gewonnen_geld = inzet_geld * 2
        data.toevoegen("geld", data.laad()["geld"] + gewonnen_geld)
        data.toevoegen("level", level + 1)
        scherm.tekst(f"Gewonnen! Je hebt nu €{data.laad()["geld"]}.")

    else:
        data.toevoegen("geld", data.laad()["geld"] - inzet_geld)
        scherm.tekst(f"Oei, je hebt verloren! Je hebt nu €{data.laad()["geld"]}.")

    sleep(2)






def garage():
    keuze = scherm.vraag(["Welkom in de garage!", "Wat wil je doen?"], ["Auto tunen", "Auto repareren", "Nieuwe auto kopen", "Terug"])

    if keuze == 0:
        tune = data.geselecteerde_auto("tune")
        prijs = 100 + (tune * 50)
        keuze = scherm.vraag([f"Tune level is: {tune}", f"Wil je upgraden voor €{prijs}?"], ["Ja", "Nee"])

        if keuze == 0:
            geld = data.laad()["geld"]

            if geld >= prijs:
                data.toevoegen("geld", geld -prijs)
                data.pas_aan("tune", tune + 1)

            else:
                scherm.clear()
                scherm.tekst("Broke boi")

        sleep(1)

    elif keuze == 1:
        schade = data.geselecteerde_auto("schade")
        prijs = schade * 15

        if schade == 0:
            scherm.clear()
            scherm.tekst("Geen schade!")
            sleep(2)

        else:
            keuze = scherm.vraag([f"Je schade level is: {schade}/100", f"Wil je repareren voor €{prijs}?"], ["Ja", "Nee"])

            if keuze == 0:
                geld = data.laad()["geld"]

                if geld >= prijs:
                    data.toevoegen("geld", geld -prijs)
                    data.pas_aan("schade", 0)

                else:
                    scherm.clear()
                    scherm.tekst("Broke boi")
                    sleep(1)

    elif keuze == 2:
        scherm.clear()
        spelerdata = data.laad()
        bezitte_auto_namen = spelerdata["autos"].keys()
        beschikbare_autos = [auto for auto in autos if auto["naam"] not in bezitte_auto_namen]
        auto_opties = [f"{auto['pk']} PK {auto['jaar']} {auto['merk']} {auto['naam']} (€{auto['prijs']})" for auto in beschikbare_autos]
        auto_opties.append("Exit")

        auto_keuze = scherm.vraag(
            ["Welke auto wil je kopen?:"],
            auto_opties
        )

        if auto_keuze != len(auto_opties) - 1:
            prijs = beschikbare_autos[auto_keuze]["prijs"]
            geld = data.laad()["geld"]
            if geld >= prijs:
                data.toevoegen_auto(beschikbare_autos[auto_keuze]["naam"])
                data.toevoegen("geld", geld - prijs)
            else:
                scherm.clear()
                scherm.tekst("Broke boi")
                sleep(1)