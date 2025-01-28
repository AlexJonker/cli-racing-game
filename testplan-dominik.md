Testplan Adventure Game



### 1. TypeWriter-functie
#### Test of de TypeWriter-functie elke letter van een string één voor één print met een vertraging.✅

* Stappen:
    * Roep de functie aan met een teststring, bijvoorbeeld "Hello, World!".
    * Controleer of de letters één voor één worden geprint met een vertraging.
    * Verwachte Uitkomst: De tekst wordt letter voor letter geprint met een vertraging van 10 milliseconden per letter.


### 2. clearScreen-functie
#### Test of de clearScreen-functie het scherm correct wist op verschillende besturingssystemen.✅

* Stappen:
    * Voer de game uit op Windows en controleer of het scherm wordt gewist met het cls-commando.
    * Verwachte Uitkomst: Het scherm wordt correct gewist op alle besturingssystemen.


### 3. Navigatie tussen Scenes
#### Test of de speler correct tussen scenes kan navigeren op basis van keuzes.✅

* Stappen:
    * Start het spel en kies een pad (bijvoorbeeld "Open de kist").
    * Controleer of de juiste volgende scene wordt geladen.
    * Herhaal dit voor meerdere keuzes en paden.
    * Verwachte Uitkomst: De speler wordt naar de juiste scene geleid op basis van de gemaakte keuzes.


### 4. Endings en Herstarten
#### Test of endings correct worden afgehandeld en of het spel correct herstart.✅

* Stappen:
    * Speel het spel tot een einde (bijvoorbeeld "Gevangen").
    * Controleer of de eindtekst wordt weergegeven.
    * Kies "j" om het spel opnieuw te starten en controleer of het spel teruggaat naar de "Start"-scene.
    * Kies "n" om het spel te beëindigen en controleer of het programma correct stopt.


### 5. Ongeldige Keuzes
#### Test hoe het spel omgaat met ongeldige keuzes.❌- quit de game ipv opnieuw vragen

* Stappen:
    * Voer het spel uit en voer een ongeldige keuze in (bijvoorbeeld een keuze die niet in de lijst staat).
    * Verwachte Uitkomst: Het spel geeft een foutmelding zoals "Invalid choice. Try again." en blijft in dezelfde scene.


### 6. Performance en Responsiviteit
#### Test of het spel soepel en responsief werkt. ✅

* Stappen:
    * Speel het spel en controleer of er geen vertragingen of vastlopers zijn.
    * Test met meerdere snel opeenvolgende keuzes.
    * Verwachte Uitkomst: Het spel reageert snel en zonder vertragingen op gebruikersinvoer.


### 7. Compleet Spelpad
#### Test een compleet pad van begin tot eind om te controleren of alle scenes en keuzes correct werken.✅

* Stappen:
    * Speel het spel en maak keuzes om een compleet pad te doorlopen (bijvoorbeeld: Start → Open de kist → Onderzoek de sleutel → Open de deur → Ga naar rechts → Negeer het zwaard → Verlaat de tempel).
    * Controleer of het spel correct eindigt en of alle tussenliggende scenes correct werken.
    * Verwachte Uitkomst: Het spel doorloopt het pad zonder fouten en eindigt correct.
