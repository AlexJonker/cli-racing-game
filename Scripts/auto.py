from time import *
import json

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
    xp = spelerdata["xp"]

    keuze = scherm.vraag([
        f"Schade: {schade}, tune: {tune}, geld: ${geld}, level: {level}, xp: {xp}",
        "Wat wil je doen??"],
        [
            "Optie 1",
            "Optie 2"
        ])


    return


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
            scherm.tekst("Geen scahde!")
            sleep(2)

        else:
            keuze = scherm.vraag([f"Je schade level is: {schade}/100", f"Wil je repareren voor ${prijs}?"], ["Ja", "Nee"])

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
        auto_keuze = scherm.vraag(
            ["Welke auto wil je kopen?:"],
            [f"{auto['jaar']} {auto['merk']} {auto['naam']} ({auto['pk']} HP)" for auto in autos]
        )

        data.toevoegen_auto(autos[auto_keuze]["naam"])
    sleep(1)

    return
