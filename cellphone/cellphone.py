class Cellphone:
    def __init__(self, manufact, model, price):

        # Атрибуты класса
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

        #  Методы класса
        # Методы с префиксом set позволяют ПЕРЕОПРЕДЕЛЯТЬ атрибуты экземпляра класса
    def set_manufact(self, manufact):
        self.__manufact = manufact

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        self.__retail_price = price

        # Методы с префиксом get позволяют ОТОБРАЖАТЬ атрибуты экземпляра класса
    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price






