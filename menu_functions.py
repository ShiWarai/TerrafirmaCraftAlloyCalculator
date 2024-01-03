from alloy import Alloy, Dict


def calculate_materials_quantity(alloy: Alloy, materials_unit: list[int], alloy_quantity: int) -> Dict[str, int]:
    minimal_proportion = alloy.get_minimal_proportion(materials_unit, alloy_quantity)

    material_names = list(alloy.composition.keys())
    material_proportion: Dict[str, int] = dict()
    for i in range(len(minimal_proportion)):
        material_proportion[material_names[i]] = materials_unit[i] * minimal_proportion[i]

    return material_proportion


