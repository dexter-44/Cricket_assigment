def batting_points(player):
    points = player['runs'] // 2

    if player['runs'] >= 50:
        points += 5

    if player['runs'] >= 100:
        points += 10

    strike_rate = (player['runs'] / player['balls']) * 100

    if 80 <= strike_rate <= 100:
        points += 2
    elif strike_rate > 100:
        points += 4

    points += player['4'] * 1
    points += player['6'] * 2

    points += player['field'] * 10

    return points


def bowling_points(player):
    points = player['wkts'] * 10

    if player['wkts'] >= 3:
        points += 5

    if player['wkts'] >= 5:
        points += 10

    economy = player['runs'] / player['overs']

    if 3.5 <= economy <= 4.5:
        points += 4
    elif 2 <= economy < 3.5:
        points += 7
    elif economy < 2:
        points += 10

    points += player['field'] * 10

    return points