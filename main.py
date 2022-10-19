from typing import List, Any
from enum import Enum
from dataclasses import dataclass

from soupsieve import select

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