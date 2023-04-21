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

if __name__ == '__main__':
    main()

