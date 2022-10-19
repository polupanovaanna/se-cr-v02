from typing import List, Any
from enum import Enum
from dataclasses import dataclass
import random

cnt_cells = 37
cells = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22,18, 29, 7, 28, 12, 35, 3, 26]
num_pos = [0] * cnt_cells
for i in range(cnt_cells):
    num_pos[cells[i]] = i


class RateType(Enum):
    VoisinsDeZero = 0
    Orphelins = 1
    Tier = 3
    Parity = 4
    Color = 6

@dataclass
class Rate:
    rtype: RateType
    value: Any

    def is_matching_number(self, round_result: int) -> bool:
        if self.rtype == RateType.VoisinsDeZero:
            return num_pos[round_result] >= num_pos[22] or num_pos[round_result] <= num_pos[25]
        if self.rtype == RateType.Orphelins:
            return (num_pos[round_result] >= num_pos[1] and num_pos[round_result] <= num_pos[9]) or \
                   (num_pos[round_result] >= num_pos[17] and num_pos[round_result] <= num_pos[6])
        if self.rtype == RateType.Tier:
            return num_pos[round_result] >= num_pos[27] and num_pos[round_result] <= num_pos[33]
        if self.rtype == RateType.Parity:
            return round_result % 2 == self.value
        if self.rtype == RateType.Color:
            if self.value == 'R':
                return num_pos[round_result] % 2 == 1
            if self.value == 'B':
                return num_pos[round_result] % 2 == 0 and round_result != 0
            if self.value == 'G':
                return round_result == 0 

@dataclass
class RoundResult:
    is_winner: List[bool]
    result_number: int

@dataclass
class DetermenisticRandomizer:
    number_to_return: int

    def get_number(self):
        return self.number_to_return



@dataclass
class GameRound:
    players: List[Rate]
    randomizer: Any

    def get_round_result(self):
        number = self.randomizer.get_number()
        assert number >= 0 and number <= 36
        results = [x.is_matching_number(number) for x in self.players]
        return RoundResult(results, number)


def get_random_game_result(players: List[Rate]) -> RoundResult:
    class Randomizer:
        lst: List[int]
        def __init__(self) -> None:
            self.lst = [i for i in range(37)]
        def get_number(self) -> int:
            return random.choice(self.lst)
    return GameRound(players, Randomizer()).get_round_result()

def convert_string_to_rate(str_rate: str) -> Rate:
    tokens = str_rate.split()
    if tokens[0] == "VoisinsDeZero":
        return Rate(RateType.VoisinsDeZero, None)
    if tokens[0] == "Orphelins":
        return Rate(RateType.Orphelins, None)
    if tokens[0] == "Tier":
        return Rate(RateType.Tier, None)
    if tokens[0] == "Parity":
        return Rate(RateType.Parity, int(tokens[1]))
    if tokens[0] == "Color":
        return Rate(RateType.Color, tokens[1])
    
        

