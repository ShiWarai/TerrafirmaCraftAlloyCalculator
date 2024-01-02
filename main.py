from menu_functions import calculate_materials_quantity, Alloy
from alloy import BUILTIN_ALLOYS
from os import system


def menu_selector(mode: int):
    match mode:
        case 1:
            introduced_alloy: Alloy = Alloy()
            material_proportions = calculate_materials_quantity(introduced_alloy, [10, 15])
        case 2:
            # Выбор сплава из заранее созданных
            print("Встроенные сплавы:")
            for i in range(len(BUILTIN_ALLOYS)):
                print(f"%d) %s" % (i+1, BUILTIN_ALLOYS[i].name))

            introduced_alloy: Alloy = BUILTIN_ALLOYS[int(input("> ")) - 1]

            # Размер кусков металлов, которые будут использоваться в плавке
            print("Размер кусков материала (1 - богатый, 2 - обычный, 3 - бедный, 4 - кусочек, остальные согласно введённому кол-ву с клавиатуры):")
            materials_unit: list[int] = list()
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

            material_proportions = calculate_materials_quantity(introduced_alloy, materials_unit, alloy_quantity)
        case _:
            return

    print(f"\nВарианты пропорций для получения сплава %s:" % introduced_alloy)
    for i in range(len(material_proportions)):
        print(f"\n%d)" % (i+1))
        for material in material_proportions[i].keys():
            print(f"Металл \"%s\": %d %s" % (material, material_proportions[i][material], "мВ"))


if __name__ == '__main__':
    while True:
        result: int = int(input('1) Посчитать для нового сплава\n2) Посчитать для встроенного сплава\n0) Выйти\n> '))

        if result == 0:
            break
        else:
            menu_selector(result)

            input("\n" + 50 * "-" + "\n")
            system('cls')
