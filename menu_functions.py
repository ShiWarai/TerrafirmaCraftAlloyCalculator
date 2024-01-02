import math

from alloy import Alloy, Dict


def calculate_materials_quantity(alloy: Alloy, materials_unit: list[int], alloy_quantity: int) -> list[Dict[str, int]]:
    material_proportions = list()

    while True:
        try:
            proportion = alloy.generate_proportion(materials_unit, alloy_quantity)
        except StopIteration:
            break

        material_names = list(alloy.composition.keys())
        material_proportion: Dict[str, int] = dict()
        for i in range(len(proportion)):
            material_proportion[material_names[i]] = proportion[i]

        material_proportions.append(material_proportion)

    return material_proportions


