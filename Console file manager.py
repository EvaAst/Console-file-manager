import os
import shutil

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. выход')
    # создать папку передаем путь
    choice = input('Выберите пункт меню')
    if choice == '1':
        for i in range(10):
            # проверка на существование
            if not os.path.exists(f'new{i}'):
                os.mkdir(f'new{i}')
    # удалить папку
    elif choice == '2':
        for i in range(6):
            os.rmdir(f'new{i}')
    # Копировать папку   shutil
    elif choice == '3':
        # проверка на существование
        if not os.path.exists(f'new{i}'):
            shutil.copy('new0.py', 'new0_copy.py')
    # список файлов и папок
    elif choice == '4':
        print(os.listdir())
    # посмотреть только папки
    elif choice == '5':
        list = [f for f in os.listdir() if os.path.isdir(f)]
        print(list)
    # посмотреть только файлы
    elif choice == '6':
        import os.path
        listOfFiles = [f for f in os.listdir() if os.path.isfile(f)]
        print(listOfFiles)
    # просмотр информации об операционной системе
    elif choice == '7':
        print(os.name)
    # 8. создатель программы
    elif choice == '8':
        print('Астапцова Евгения')
    elif choice == '9':
        import viktorina

        viktorina
    elif choice == '10':
        import use_functions

        use_functions
    elif choice == '11':
        break
    else:
        print('Неверный пункт меню')