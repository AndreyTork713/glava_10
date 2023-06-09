

class Contact:
        # Инициализация атрибутов класса
    def __init__(self, name, phone, email):
        self.__name = name
        self.__phone = phone
        self.__email = email

        # Модификаторы
    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
        self.__email = email

        # Получатели
    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

        # Метод __str__ возвращает текущее состояние объекта
    def __str__(self):
        return f'Имя: {self.__name}\n'\
               f'телефон: {self.__phone}\n' \
               f'электронная почта: {self.__email}'
