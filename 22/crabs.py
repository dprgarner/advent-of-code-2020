def parse_input():
    player1 = []
    player2 = []
    try:
        for player in [player1, player2]:
            input()  # Player 1/2
            line = input()
            while line:
                player.append(int(line))
                line = input()
    except EOFError:
        pass

    return player1, player2


def play_simple_round(player1, player2):
    player1 = player1.copy()
    player2 = player2.copy()
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if card1 > card2:
        player1.extend([card1, card2])
    else:
        player2.extend([card2, card1])
    return player1, player2


def play_simple_game(player1, player2):
    while player1 and player2:
        player1, player2 = play_simple_round(player1, player2)
    return player1, player2


def play_full_round(player1, player2):
    player1 = player1.copy()
    player2 = player2.copy()
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    if len(player1) >= card1 and len(player2) >= card2:
        # print('Playing subgame:')
        player1_wins, _ = play_full_game(player1[:card1], player2[:card2])
    else:
        # print('Playing high-card:', card1, card2)
        player1_wins = card1 > card2

    # print('Player {} won'.format('one' if player1_wins else 'two'))

    if player1_wins:
        player1.extend([card1, card2])
    else:
        player2.extend([card2, card1])
    return player1, player2


def play_full_game(*players):
    """
    Returns a bool stating if player 1 won.
    """
    cache = set()
    while all(players):
        cache_str = '--'.join(
            ','.join(str(i) for i in player)
            for player in players
        )
        if cache_str in cache:
            return True, players[0]
        cache.add(cache_str)

        players = play_full_round(*players)
    return bool(players[0]), players[0] or players[1]


def get_score(player):
    score = 0
    for i, card in enumerate(player):
        score += card * (len(player) - i)
    return score


def main():
    """
    A little slow and inefficient, but it still runs in a few seconds.
    """
    player1, player2 = parse_input()
    cards = play_simple_game(player1, player2)
    score = get_score(cards[0] or cards[1])
    print('Simple game: Player {} won'.format('one' if cards[0] else 'two'))
    print('Final cards:', cards)
    print('Final score: ', score)

    player1_wins, cards = play_full_game(player1, player2)
    score = get_score(cards)
    print('Full game: Player {} won'.format('one' if player1_wins else 'two'))
    print('Final cards:', cards)
    print('Final score: ', score)


main()
