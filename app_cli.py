from main import *


possible_rates = ["VoisinsDeZero", "Tier", "Orphelins", "Parity 1", "Parity 0", "Color R", "Color G", "Color B"]

rate_list = []
dilet_rate = None

while True:
    s = input("Print new player rate:").strip()
    if s == "No new players":
        break
    if s == "Diler":
        if dilet_rate is not None:
            print("Diler is already in the game")
            continue
        diler_rate_str = random.choice(possible_rates)
        print("Diler rate is " + diler_rate_str)
        dilet_rate = convert_string_to_rate(diler_rate_str)
        continue
    rate_list.append(convert_string_to_rate(s))

if dilet_rate is not None:
    rate_list.append(dilet_rate)
results = get_random_game_result(rate_list)
print(f"\n\n\nThe number on the roulette wheel is {results.result_number}")

for i, res in enumerate(results.is_winner):
    if i + 1 == len(rate_list) and dilet_rate is not None:
        print("Diler", end='')
    else:
        print(f"{i}th player", end='')
    if results.is_winner[i]:
        print(" won the bet")
    else:
        print(" lost a bet")