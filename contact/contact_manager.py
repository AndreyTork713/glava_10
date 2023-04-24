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

def get_menu_choice():
    pass

def load_contacts():
    pass

def look_up():
    pass

def add():
    pass

def change():
    pass

def delete():
    pass

def save_contacts(save_list):
    pass


if __name__ == '__main__':
    main()

