import os
import json
from time import sleep

import Scripts.data as data
import Scripts.scherm as scherm
import Scripts.auto as auto
## import scripts en modules


autos = json.load(open("./autos.json", "r")) #laad de autos.json

def game_over():
    keuze = scherm.vraag(["Helaas, je hebt verloren.", "Wil je opnieuw beginnen?"], ["Ja", "Nee"])
    if keuze == 0:
        os.remove("data.json")
        scherm.clear()
        scherm.tekst("Alle data is verwijderd!")
        sleep(2)
        main() # terug naar main
    else:
        scherm.clear()
        scherm.tekst("Sure, Dan niet")
        sleep(2)
        scherm.curses.curs_set(1) # zet het type ding weer aan
        exit()


def main():
    try:
        if data.laad() == {}:
            data.nieuwe_speler() # start nieuwe speler

        if data.laad()["geld"] == 0:
            game_over() # game over

        else:

            for naam, vrum in data.laad()["autos"].items(): # loopt door al je auto's
                if vrum["schade"] >= 100: # als schade 100 of meer is ben je je auto kwijt
                    scherm.clear()
                    scherm.tekst(f"Je {naam} is total loss! Deze ben je nu kwijt.")
                    if data.laad()["autos"].length() == 1:
                        scherm.tekst("Je hebt geen auto's meer!")
                        sleep(2)
                        game_over()

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
                auto.race() # gaa naar de race functie

            elif keuze == 1:
                auto.garage() # ga naar de garage functie

            elif keuze == 2:
                keuze = scherm.vraag(["Welkom in de danger zone! Wat wil je doen?"], ["Clear je data", "Terug"])

                if keuze == 0:
                    keuze = scherm.vraag(["Weet je zeker dat je al je data wil verwijderen?"], ["Ja", "Nee"])

                    if keuze == 0:
                        os.remove("data.json") # verwijder het data.json bestand
                        scherm.clear()
                        scherm.tekst("Alle data is verwijderd!")
                        sleep(2)
                        main()

            elif keuze == 3:
                auto_namen = [f"{selectie}" for selectie in data.laad()["autos"]]
                keuze = scherm.vraag(["Welkom in de auto selectie!"], auto_namen)
                geselecteerde_auto_naam = auto_namen[keuze]

                for auto_num, vrumvrum in enumerate(autos): # loop door je autos
                    if vrumvrum["naam"] == geselecteerde_auto_naam:
                        data.toevoegen("geselecteerde_auto", auto_num) # selecteer de auto


            elif keuze == 4:
                scherm.curses.curs_set(1) # type ding weer aan
                exit()

            main() # run main opnieuw wanneer je klaar bent

    except KeyboardInterrupt: # ^c geeft geen error
        scherm.curses.curs_set(1)# type ding weer aan
        exit()



if __name__ == "__main__":
    main() # run het de main functie