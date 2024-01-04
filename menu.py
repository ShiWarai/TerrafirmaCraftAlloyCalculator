import math
from morph import decline_noun_by_number
from itertools import product
from alloy import Alloy, BUILTIN_ALLOYS
from typing import Dict


class Menu:
    @classmethod
    def menu_selector(cls, mode: list[int]):
        match mode[1]:
            case 1:
                introduced_alloy = cls.input_alloy(mode[0])
                materials_units = cls.input_materials_units(introduced_alloy)
                alloy_quantity = cls.input_alloy_quantity()

                material_proportions = cls.calculate_materials_quantity(introduced_alloy, materials_units, alloy_quantity)

                # Вывод данных
                print("\n" + 50 * "-")
                cls.print_proportion(introduced_alloy, materials_units, material_proportions)
            case 2:
                introduced_alloy = cls.input_alloy(mode[0])
                alloy_quantity = cls.input_alloy_quantity()

                best_proportion: tuple[Dict[str, int], list[int], int] = (None, None, math.inf)
                unit_types = [1, 2, 3, 4]
                for permutation in list(product(unit_types, repeat=len(unit_types))):
                    materials_units: list[int] = list(map(cls.get_material_unit_by_type, permutation))

                    material_proportions = cls.calculate_materials_quantity(introduced_alloy, materials_units, alloy_quantity)
                    materials_sum = sum(list(material_proportions.values()))
                    if best_proportion[2] > materials_sum:
                        best_proportion = (material_proportions, materials_units, materials_sum)

                print("\n" + 50 * "-")
                print("\nЛучший вариант с размерами кусков:", end='')
                for material in list(introduced_alloy.composition.keys()):
                    print(" '%s': %d %s" % (material, best_proportion[1][list(introduced_alloy.composition.keys()).index(material)], "мВ"), end=';')
                print('')

                cls.print_proportion(introduced_alloy, best_proportion[1], best_proportion[0])
            case _:
                return

    @classmethod
    def input_alloy(cls, input_type: int) -> Alloy:
        match input_type:
            case 1:
                alloy_name = input("\nВведите имя сплава: ")

                alloy_composition = dict()
                material_index = 0
                while True:
                    material_index += 1
                    material_name = input(
                        f"\n%d) Введите имя материала (или ничего, если состав введён до конца): " % material_index)
                    if material_name == "" or not material_name:
                        break

                    min_percentage, max_percentage = map(float, input(
                        "Диапазон % содержания в сплаве (через пробел): ").split())
                    alloy_composition[material_name] = (min_percentage, max_percentage)

                return Alloy(alloy_name, alloy_composition)
            case 2:
                # Выбор сплава из заранее созданных
                print("\nВстроенные сплавы:")
                for i in range(len(BUILTIN_ALLOYS)):
                    print(f"%d) %s" % (i + 1, BUILTIN_ALLOYS[i].name))

                return BUILTIN_ALLOYS[int(input("> ")) - 1]
            case _:
                return None

    @classmethod
    def input_materials_units(cls, alloy: Alloy):
        materials_units: list[int] = list()

        # Размер кусков металлов, которые будут использоваться в плавке
        print("Размер кусков материала (1 - богатый, 2 - обычный, 3 - бедный, 4 - кусочек, остальные согласно введённому кол-ву с клавиатуры):")
        for material_name in list(alloy.composition.keys()):
            unit = cls.get_material_unit_by_type(int(input(f"%s: " % material_name)))
            materials_units.append(unit)

        return materials_units

    @classmethod
    def get_material_unit_by_type(cls, unit_type: int) -> int:
        unit = 0
        match unit_type:
            case 1:
                unit = 35
            case 2:
                unit = 25
            case 3:
                unit = 15
            case 4:
                unit = 10

        return unit

    @classmethod
    def input_alloy_quantity(cls):
        alloy_quantity: int = int(input("Требуемый минимальный объём сплава (в мВ): "))
        assert alloy_quantity > 0

        return alloy_quantity

    @classmethod
    def print_proportion(cls, alloy: Alloy, materials_unit: list[int], material_proportions: Dict[str, int]):
        materials_names = list(material_proportions.keys())

        print(f"\nВариант пропорции для получения сплава %s в объёме %d %s:" % (
            alloy, sum(list(material_proportions.values())), 'мВ'))
        for material in materials_names:
            print(f"Металл \"%s\": %d %s" % (material, material_proportions[material], "мВ"), end='')
            material_unit = materials_unit[list(alloy.composition.keys()).index(material)]
            print(" или %s" % decline_noun_by_number(int(material_proportions[material] / material_unit), "кусок"))

    @classmethod
    def calculate_materials_quantity(cls, alloy: Alloy, materials_unit: list[int], alloy_quantity: int) -> Dict[str, int]:
        minimal_proportion = alloy.get_minimal_proportion(materials_unit, alloy_quantity)

        material_names = list(alloy.composition.keys())
        material_proportion: Dict[str, int] = dict()
        for i in range(len(minimal_proportion)):
            material_proportion[material_names[i]] = materials_unit[i] * minimal_proportion[i]

        return material_proportion


