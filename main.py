import os
import json
from time import sleep

import Scripts.data as data
import Scripts.scherm as scherm
import Scripts.auto as auto

autos = json.load(open("./autos.json", "r"))


def main():
    try:
        if data.laad() == {}:
            data.nieuwe_speler()

        if data.laad()["geld"] == 0:
            keuze = scherm.vraag(["Helaas, je hebt verloren.", "Wil je opnieuw beginnen?"], ["Ja", "Nee"])
            if keuze == 0:
                os.remove("data.json")
                scherm.clear()
                scherm.tekst("Alle data is verwijderd!")
                sleep(2)
                main()
            else:
                scherm.clear()
                scherm.tekst("Sure, Dan niet")
                sleep(2)

        else:
            keuze = scherm.vraag(
                [ # tekst
                    "Welkom!",
                    "Wat wil je doen?"
                ],
                [ # opties
                    "Race",
                    "garage",
                    "Danger zone",
                    "Selecteer auto",
                    "Exit"
                ]
            )

            if keuze == 0:
                auto.race()
                scherm.tekst("Woosh!")

            elif keuze == 1:
                auto.garage()

            elif keuze == 2:
                keuze = scherm.vraag(["Welkom in de danger zone! Wat wil je doen?"], ["Clear je data", "Terug"])

                if keuze == 0:
                    keuze = scherm.vraag(["Weet je zeker dat je al je data wil verwijderen?"], ["Ja", "Nee"])

                    if keuze == 0:
                        os.remove("data.json")
                        scherm.clear()
                        scherm.tekst("Alle data is verwijderd!")
                        sleep(2)
                        main()

            elif keuze == 3:
                auto_namen = [f"{selectie}" for selectie in data.laad()["autos"]]
                keuze = scherm.vraag(["Welkom in de auto selectie!"], auto_namen)
                geselecteerde_auto_naam = auto_namen[keuze]

                for auto_num, vrumvrum in enumerate(autos):
                    if vrumvrum["naam"] == geselecteerde_auto_naam:
                        data.toevoegen("geselecteerde_auto", auto_num)


            elif keuze == 4:
                scherm.curses.curs_set(1)
                exit()

            main() # run main opnieuw wanneer je klaar bent

    except KeyboardInterrupt:
        scherm.curses.curs_set(1)
        exit()



if __name__ == "__main__":
    main()