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

Kartičky do hry jsou generované dynamicky. Pokaždé, když hráč vezme kartu uprostřed, vygeneruje se nová karta. Od každého hráče se vybere jeden obrázek, který není sdílený s jiným hráčem, a ostatní obrázky se doplní ze seznamu nepoužitých obrázků.

## Credits:

Obrázky byly převzaty ze stránky Flaticon.com (https://www.flaticon.com). 