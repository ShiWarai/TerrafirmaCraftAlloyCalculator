from os import system
from menu import Menu

if __name__ == '__main__':
    while True:
        result: list[int] = list()

        result.append(int(input('''1) Посчитать для нового сплава\n'''
                                '''2) Посчитать для встроенного сплава\n'''
                                '''0) Выйти\n> ''')))
        if result[0] == 0:
            break

        result.append(int(input('''1) Для фиксированных кусков металла\n'''
                                '''2) Подобрать с эффективным набором кусков металла\n'''
                                '''0) Выйти\n> ''')))
        if result[1] == 0:
            break

        # Запуск селектора режимов
        Menu.menu_selector(result)

        input("\n" + 50 * "-" + "\n")
        system('cls')
