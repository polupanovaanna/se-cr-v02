from main import *
from dataclasses import dataclass
import traceback

possible_rates = ["VoisinsDeZero", "Tier", "Orphelins", "Parity 1", "Parity 0", "Color R", "Color G", "Color B"]


@dataclass
class Player:
    name: str
    rate: Rate


players: List[Player] = []


def add_player(name, rate):
    players.append(Player(name, convert_string_to_rate(rate)))


def get_results():
    response = ''
    results = get_random_game_result([p.rate for p in players])
    response += f"\n\n\nThe number on the roulette wheel is {results.result_number}\n"

    for i, res in enumerate(results.is_winner):
        response += players[i].name
        if results.is_winner[i]:
            response += " won the bet\n"
        else:
            response += " lost the bet\n"
    return response


def get_rate():
    str = input("Print new player rate:").strip()
    if str in possible_rates:
        return str
    while True:
        str = input("Print RIGHT new player rate:").strip()
        if str in possible_rates:
            return str


def get_player_list():
    playerlist = ''
    for player in players:
        playerlist += 'name: ' + player.name + ', rate: ' + player.rate.rtype.name + ' '
        try:
            playerlist += player.rate.value
        except Exception as e:
            playerlist += ''
        playerlist += '\n'
    return playerlist


if __name__ == "__main__":
    diler_rate_str = None
    while True:
        name = input("Print new player name:").strip()
        if name == "No new players":
            break
        if name == "Diler":
            if diler_rate_str is not None:
                print("Diler is already in the game")
                continue
            diler_rate_str = random.choice(possible_rates)
            print("Diler rate is " + diler_rate_str)
            continue
        add_player(name, get_rate())

    if diler_rate_str is not None:
        add_player("Diler", diler_rate_str)

    print(get_results())
