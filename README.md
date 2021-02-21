# Dobble
zápočtový program do předmětu Programování I v zimním semestru 2020/2021

## Návod ke spuštění

Hru spustíte otevřením souboru main.py. Je potřeba mít nainstalovanou knihovnu Pygame.

## Soubory

Hra je rozdělena do několika souborů:

- v souboru main.py se inicializují hráči, obrázky a hudba, spouští se zde hra
- v souboru menu.py jsou funkce týkající se hlavního menu, návodu ke hře a nastavení
- v souboru tests.py jsou unit-testy používané na testování funkčnosti herní logiky
- v souboru game_loop.py je hlavní herní smyčka a výherní obrazovka
- v souboru game_logic.py jsou třídy pro hráče, herní kartu a tlačítko, také funkce generate_new_cards a check_input zajišťující funkčnost hry

## Herní logika

### Generování nových karet

Herní karty jednotlivých hráčů jsou generované dynamicky. Na začátku hry si každý hráč vezme 6 karet, jejichž obrázky jsou následně smazány ze seznamu unused_images.

Pokaždé, když hráč vezme kartu uprostřed, vygeneruje se nová prostřední karta. Od každého hráče se vybere jeden obrázek, který není sdílený s jiným hráčem (parametr shared_with), a ostatní obrázky se doplní ze seznamu nepoužitých obrázků.

### Braní karet

Funkce check_input má za úkol zjistit, jestli právě stisknutá klávesa patří nějakému hráči. Pomocí for cyklu prochází všechny karty všech hráčů a zjišťuje, jestli jsou spojené s právě stisknutou klávesou. Pokud ano, podívá se, zda je tato karta sdílená s prostředkem. Pokud ano, hráč získává bod, v opačném případě bod ztrácí.

Pokud hráč stiskl správnou klávesu, přichází na řadu metoda take_cards. Ta má kromě předání karty z prostředka za úkol updatovat odkazy shared_with (pomocí for cyklu přes všechny hráče) a vrátit již nepoužívané obrázky zpět do seznamu unused_images (ty, u jejichž karet je shared_with == None).

### Ostatní

Ostatní herní funkce jsou poměrně přímočaré, a snad není třeba je zde popisovat. Za zmínku možná ještě stojí pohyblivé obrázky v hlavním menu a na výherní obrazovce. Na obrazovku se vykresluje 15 náhodných obrázků na náhodné souřadnice (u kterých je ošetřeno, aby se nepřekrývaly s textem na obrazovce). Pokud by se ale vykreslovaly v každé iteraci while cyklu, měnily by se moc rychle a bylo by pro hráče nepříjemné je pozorovat. Řešením by mohlo být delší čekání na konci každé iterace, pak by ale zase nastal problém s ošetřováním vstupů, protože by program na uživatelský vstup reagoval moc pomalu. Proto je využita proměnná slower_movement_counter, díky které se stav obrazovky překresluje jen každou čtvrtou iteraci.

## Credits

Obrázky byly převzaty ze stránky Flaticon.com (https://www.flaticon.com). 