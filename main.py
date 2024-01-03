from menu_functions import calculate_materials_quantity, Alloy
from alloy import BUILTIN_ALLOYS
from os import system
from morph import decline_noun_by_number


def menu_selector(mode: int):
    materials_unit: list[int] = list()
    match mode:
        case 1:
            alloy_name = input("Введите имя сплава: ")

            alloy_composition = dict(); material_index = 0
            while True:
                material_index += 1
                material_name = input(f"\n%d) Введите имя материала (или ничего, если состав введён до конца): " % material_index)
                if material_name == "" or not material_name:
                    break

                min_percentage, max_percentage = map(float, input("Диапазон % содержания в сплаве (через пробел): ").split())
                alloy_composition[material_name] = (min_percentage, max_percentage)

            introduced_alloy: Alloy = Alloy(alloy_name, alloy_composition)
        case 2:
            # Выбор сплава из заранее созданных
            print("Встроенные сплавы:")
            for i in range(len(BUILTIN_ALLOYS)):
                print(f"%d) %s" % (i+1, BUILTIN_ALLOYS[i].name))

            introduced_alloy: Alloy = BUILTIN_ALLOYS[int(input("> ")) - 1]
        case _:
            return

    # Размер кусков металлов, которые будут использоваться в плавке
    print("Размер кусков материала (1 - богатый, 2 - обычный, 3 - бедный, 4 - кусочек, остальные согласно введённому кол-ву с клавиатуры):")
    for material_name in list(introduced_alloy.composition.keys()):
        unit = int(input(f"%s: " % material_name))
        match unit:
            case 1:
                unit = 35
            case 2:
                unit = 25
            case 3:
                unit = 15
            case 4:
                unit = 10
            case _:
                pass
        materials_unit.append(unit)

    # Кол-во сплава, для которого надо рассчитать пропорцию
    alloy_quantity: int = int(input("Требуемый минимальный объём сплава (в мВ): "))
    assert alloy_quantity > 0

    material_proportions = calculate_materials_quantity(introduced_alloy, materials_unit, alloy_quantity)

    # Вывод данных
    materials_names = list(material_proportions.keys())
    print(f"\nВариант пропорции для получения сплава %s в объёме %d %s:" % (introduced_alloy, sum(list(material_proportions.values())), 'мВ'))
    for material in materials_names:
        print(f"Металл \"%s\": %d %s" % (material, material_proportions[material], "мВ"), end='')
        material_unit = materials_unit[list(introduced_alloy.composition.keys()).index(material)]
        print(" или %s" % decline_noun_by_number(int(material_proportions[material]/material_unit), "кусок"))


if __name__ == '__main__':
    while True:
        result: int = int(input('1) Посчитать для нового сплава\n2) Посчитать для встроенного сплава\n0) Выйти\n> '))

        if result == 0:
            break
        else:
            menu_selector(result)

            input("\n" + 50 * "-" + "\n")
            system('cls')
