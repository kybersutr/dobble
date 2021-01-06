from game_logic import *
# Unit tests for game_logic

def test1_generate():
    Player1 = Player(None)
    Player2 = Player(None)

    unused_images = ["Evžen","Oněgin","Je","Placeholder","Který","Z","Nějakého","Důvodu","Používám"]

    cards1 = [Card("1.0", 0, None), Card("1.1", 1, None), Card("1.2", 2, None), Card("1.3", 3, None), Card("1.4", 4, None), Card("1.5", 5, None)]
    cards2 = [Card("2.0", 0, None), Card("2.1", 1, None), Card("2.2", 2, None), Card("2.3", 3, None), Card("2.4", 4, None), Card("2.5", 5, None)]

    Player1.cards = cards1
    Player2.cards = cards2

    players = [Player1, Player2]

    generate_new_cards(players, unused_images)

    for card in mid.cards:
        print(card.image, card.position, card.shared_with)

    for card in Player1.cards:
        print(card.image, card.position, card.shared_with)

    for card in Player2.cards:
        print(card.image, card.position, card.shared_with)

def test2_check_input():
    Player1 = Player(['q','w','e','a','s','d'])
    Player2 = Player(['t','y','u','g','h','j'])
    players = [Player1, Player2]
    cards1 = [Card("1.0", 0, mid), Card("1.1", 1, None), Card("1.2", 2, mid), Card("1.3", 3, None),
              Card("1.4", 4, None), Card("1.5", 5, mid)]
    cards2 = [Card("2.0", 0, None), Card("2.1", 1, mid), Card("2.2", 2, mid), Card("2.3", 3, None),
              Card("2.4", 4, None), Card("2.5", 5, None)]

    Player1.cards = cards1
    Player2.cards = cards2

    keys = ['q','w','e','a','s','d','t','y','u','g','h','j']
    for key in keys:
        check_input(players, key)
        print(Player1.points, Player2.points)