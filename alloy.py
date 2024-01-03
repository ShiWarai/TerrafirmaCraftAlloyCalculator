import itertools
import math
from typing import Dict


class Alloy:
    def __init__(self, name: str = None, composition: Dict[str, tuple[int, int]] = {}):
        self.name = name
        self.composition = composition
        self.__material_quantity = len(list(self.composition.keys()))

    def get_minimal_proportion(self, materials_unit: list[int], req_quantity: int) -> list[int]:
        # Получение первичной пропорции (по минимальной границе)
        composition_values = list(self.composition.values())
        proportion: list[int] = [math.ceil((composition_values[i][0] / 100 * req_quantity) / materials_unit[i]) for i in range(self.__material_quantity)]

        while True:
            current_sum, potentially_incr_index = self.get_potentially_increasing_material(proportion, materials_unit)

            if current_sum >= req_quantity and self.validate_proportion(proportion, materials_unit):
                break
            else:
                proportion[potentially_incr_index] += 1

        return proportion

    def get_potentially_increasing_material(self, current_proportion: list[int], materials_unit: list[int]) -> tuple[int, int]:
        current_materials_quantities = [current_proportion[i] * materials_unit[i] for i in range(self.__material_quantity)]
        current_sum = sum(current_materials_quantities)
        composition_values = list(self.composition.values())

        calculated_coefficients: list[float] = list()
        for i in range(self.__material_quantity):
            calculated_coefficients.append((composition_values[i][1] - 100 * current_materials_quantities[i] / current_sum) / materials_unit[i])

        return current_sum, calculated_coefficients.index(max(calculated_coefficients))

    def validate_proportion(self, current_proportion: list[int], materials_unit: list[int]) -> bool:
        current_materials_quantities = [current_proportion[i] * materials_unit[i] for i in range(self.__material_quantity)]
        current_sum = sum(current_materials_quantities)
        composition_values = list(self.composition.values())

        for i in range(self.__material_quantity):
            if (composition_values[i][0] > (100 * current_materials_quantities[i] / current_sum)
                    or composition_values[i][1] < (100 * current_materials_quantities[i] / current_sum)):
                return False

        return True

    def __str__(self):
        if self.name is None:
            return "<неизвестный>"
        else:
            return self.name


BUILTIN_ALLOYS: list[Alloy] \
    = [Alloy("бронза", {"медь": (88, 92), "олово": (8, 12)}),
       Alloy("висмутовая бронза", {"медь": (50, 65), "цинк": (20, 30), "висмут": (10, 20)})]
