from models import GroupModel


if __name__ == '__main__':
    gr_manager = GroupModel()

    while True:
        try:
            choise = int(input("""
---------------------------------------------------
Выберите действие:
1. Вывод списка всех групп.
2. Добавление новой группы в указанный факультет. 
3. Удаление группы.
4. Завершение работы.
 ---------------------------------------------------
 Ваш выбор: """))
        except ValueError:
            print('Вводите только числа!')
            continue
        if choise == 1:
            print("Список всех груп: \n", gr_manager.get_all_groups())
        elif choise == 2:
            gr_manager.add_group(input('Введите название групы: '), input("Введите название факультета: "))
        elif choise == 3:
            gr_manager.dell_group(input('Введите название группы: '))
        elif choise == 4:
            break
        else:
            print("Неправильный вариант действия!")
