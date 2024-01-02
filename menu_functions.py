import math

from alloy import Alloy, Dict


def calculate_materials_quantity(alloy: Alloy, materials_unit: list[int], alloy_quantity: int) -> list[Dict[str, int]]:
    proportion = alloy.generate_proportion(materials_unit, alloy_quantity)

    material_names = list(alloy.composition.keys())
    material_proportions: Dict[str, int] = dict()
    for i in range(len(proportion)):
        material_proportions[material_names[i]] = proportion[i]

    return [material_proportions]


