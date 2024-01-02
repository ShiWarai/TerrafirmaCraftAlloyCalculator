import itertools
import math
from typing import Dict


class Alloy:
    def __init__(self, name: str = None, composition: Dict[str, tuple[int, int]] = {}):
        self.name = name
        self.composition = composition
        self.__priority = itertools.permutations(range(len(self.composition.keys())))

    def generate_proportion(self, materials_unit: list[int], req_quantity: int) -> list[int]:
        current_priority = list(next(self.__priority))

        proportion: list[list[int, int]] = list()
        for material_index in current_priority:
            key = list(self.composition.keys())[material_index]
            proportion.append([material_index, math.ceil((self.composition[key][0] / 100 * req_quantity) / materials_unit[material_index])])

        while True:
            current_sum = sum_priority(materials_unit, proportion)
            print(current_sum)

            if current_sum >= req_quantity:
                break
            else:
                last_priority_key = proportion[-1][0]
                print(last_priority_key)
                proportion[-1][1] += 1

        return current_priority

    def __str__(self):
        if self.name is None:
            return "<неизвестный>"
        else:
            return self.name


def sum_priority(materials_unit: list[int], proportion: list[list[int, int]]):
    current_sum = 0
    for material in proportion:
        current_sum += material[1] * materials_unit[material[0]]

    return current_sum

BUILTIN_ALLOYS: list[Alloy] \
    = [Alloy("бронза", {"медь": (88, 92), "олово": (8, 12)}),
       Alloy("висмутовая бронза", {"медь": (50, 65), "цинк": (20, 30), "висмут": (10, 20)})]
