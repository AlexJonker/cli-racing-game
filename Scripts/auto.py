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
        f"damage: {schade}, tune: {tune}, money: ${geld}, level: {level}, xp: {xp}",
        "What do you want to do?"],
        [
            "Optie 1",
            "Optie 2"
        ])


    return


def garage():
    keuze = scherm.vraag(["Welcome to the garage!", "What do you want to do?"], ["Tune auto", "Repair", "Buy new auto", "Back"])

    if keuze == 0:
        tune = data.geselecteerde_auto("tune")
        prijs = 100 + (tune * 50)
        keuze = scherm.vraag([f"Current tune level is: {tune}", f"Do you want to upgrade for ${prijs}?"], ["Yes", "No"])

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
            scherm.tekst("No damage to repair!")
            sleep(2)

        else:
            keuze = scherm.vraag([f"Current damage level is: {schade}/100", f"Do you want to repair for ${prijs}?"], ["Yes", "No"])

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
            ["Please choose the auto you want to buy:"],
            [f"{auto['jaar']} {auto['merk']} {auto['naam']} ({auto['pk']} HP)" for auto in autos]
        )

        data.toevoegen_auto(autos[auto_keuze]["naam"])
    sleep(1)

    return
