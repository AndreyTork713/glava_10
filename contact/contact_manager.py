# Эта программа управляет контактами
import pickle
import contact

    # Глобальные переменные для работы меню
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'contacts.dat'

def main():

    # ЗАГРУЗИТЬ СУЩЕСТВУЮЩИЙ СЛОВАРЬ И ПРИСВОИТЬ ЕГО ПЕРЕМЕННОЙ MYCONTACTS
    mycontacts = load_contacts()

    # нициализировать переменную для выбора пользователя
    choice = 0

    # Обрабатывать варианты выбора пунктов меню до тех пор,
    # пока пользователь не пожелает выйти из программы.
    while choice != QUIT:
        # Получить выбранный пользователем пункт меню.
        choice = get_menu_choice()
        # Обработать выбор
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)

    # Сохранить словарь mycontacts в файле.
    save_contacts(mycontacts)




# Рабочие методы

# Выводит меню и получает проверенный на
# допустимость выбранный пользователем пункт
def get_menu_choice():
    print()
    print('МЕНЮ')
    print('________________________________________')
    print('1. Найти контактное лицо')
    print('2. Добавить новое контактное лицо')
    print('3. Изменить существующее контактное лицо')
    print('4. Удалить контактное лицо')
    print('5. Выйти из программы')
    print()

    # Получить выбранный пользователем пункт меню
    choice = int(input('Введите выбранный пункт: '))

    # Проверить выбранный пункт
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Введите выбранный пункт: '))
    return choice


def load_contacts():
    try:
        # Открыть файл contacts.dat
        input_file = open('contacts.dat', 'rb')

        # Расконсервировать словарь
        contact_dct = pickle.load(input_file)

        # Закрыть файл phone_inventory.dat
        input_file.close()

    except IOError:
        # При неудаче создать пустой словарь
        contact_dct = {}

    return contact_dct


def look_up(mycontacts):
    # Получить искомое имя
    name = input('Введите имя: ')
    # Отыскать его в словаре
    print(mycontacts.get(name, 'Это имя не найдено.'))

# Функция add() добавляет новую запись в указанный словарь
def add(mycontacts):
    # Получить контактную информацию
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    email = input('Электронный адрес: ')

    # Создать именованную запись с объектом Contact
    entry = contact.Contact(name, phone, email)

    # Если такого имени в словаре нет создать новую запись в словаре
    if name not in mycontacts:
        mycontacts[name] = entry
        print('Запись добавлена.')
    else:
        print('Такая запись уже существует.')

# Функуия изменяет существующую запись в заданном словаре
def change(mycontacts):
    # Получить искомое имя
    name = input('Введите имя: ')

    if name in mycontacts:
        phone = input('Введите новый номер телефона: ')
        email = input('Введите новый электронный адрес: ')

        # Создать именованную запись с объектом Contact
        entry = contact.Contact(name, phone, email)

        # Обновить запись
        mycontacts[name] = entry
        print('Информация обновлена.')
    else:
        print('Это имя не найдено.')

def delete(mycontacts):
    # Получить искомое имя
    name = input('Введите имя: ')

    if name in mycontacts:
        del mycontacts[name]
        print('Запись удалена.')
    else:
        print('Имя не найдено.')

 # Функция save contacts консервирует указанный
 # объект и сохраняет его в файле контактов.
def save_contacts(mycontacts):
    # Открыть файл для записи
    output_file = open(FILENAME, 'wb')

    # Законсервировать файл и сохранить его
    pickle.dump(mycontacts, output_file)

    # Закрыть файл
    output_file.close()


if __name__ == '__main__':
    main()

