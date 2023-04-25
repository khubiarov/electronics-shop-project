import csv
import math
import os
#from src.phone import Phone
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate
        return self.price
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 11:
            self.__name = value
        else:
            print(f"'{value}' Длина наименования товара превышает 10 символов.")
    @classmethod
    def instantiate_from_csv(cls):

        #"C:\\Users\\nrchu\\electronics-shop-project\\src\\items.csv"
        #os.path.join("..", "cat", "data.txt")
        with open(os.path.join("..", 'src', 'items.csv'), 'rt',
                  encoding="windows-1251") as file:

            reader = csv.reader(file)

            for row in reader:

                name = row[0]
                price = row[1]
                quantity = row[2]

                if price[0].isalpha():
                    continue
                else:
                    cls.all.append(cls(name, price, quantity))
    @staticmethod
    def string_to_number(value):
        return int(math.floor(float(value)))

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if isinstance(other, Item):

            return self.quantity + other.quantity
        else:
            raise TypeError('Класс не настледован от Item')