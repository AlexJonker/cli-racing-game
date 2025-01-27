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
            scherm.tekst("Geen schade!")
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
        spelerdata = data.laad()
        bezitte_auto_namen = spelerdata["autos"].keys()
        beschikbare_autos = [auto for auto in autos if auto["naam"] not in bezitte_auto_namen]
        auto_opties = [f"{auto['jaar']} {auto['merk']} {auto['naam']} ({auto['pk']} HP)" for auto in beschikbare_autos]
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