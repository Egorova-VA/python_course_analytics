from logger import input_data, print_data, delete_data, update_data


def interface():
    print("Добрый день! Вы попали на специальный бот справочник от GeekBrains! \n 1 - запись данных \n 2 - вывод данных \n 3 - изменение данных \n 4 - удаление данных")
    command = int(input('Введите данные'))

    while command not in range(1,5):
        print("неправильный ввод")
        command = int(input('введите число '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        update_data()
    elif command == 4:
        delete_data()
