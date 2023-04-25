import pytest
from src.phone import Phone
from src.item import Item



class Not_from_item_phone:
    """"Это заготовка для того, что бы проверять raise когда складываешь с не наследованным от Item классом"""
    def __init__(self, name, price, quantity, sim):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.sim = sim


@pytest.fixture
def phone_copy():
    return Phone


def test_add(phone_copy):
    some_device = Not_from_item_phone('GoldStar', 12000, 20, 2)
    phone1 = Phone('sony', 10000, 20, 1)
    phone2 = Phone('sumsung', 15000, 30, 2)

    assert phone1 + phone2 == 50
    # assert phone1 + some_device == TypeError
    # можно ли сделать такую проверку?
    # Я нашел про raise в pytest, но пока не разобрался
    phone1 = Phone('sony', 10000, 20, 1)
    assert phone1.__repr__() == "Phone('sony', 10000, 20, 1)"


def test_item_add(phone_copy):
    device1 = Phone('sony', 10000, 20, 1)
    device2 = Item('Белаз', 10000000, 1, )
    assert device1 + device2 == 21


def test_stter_sim(phone_copy):
    device1 = Phone('sony', 10000, 20, 1)
    assert device1.number_of_sim == 1
    device1.number_of_sim = 2
    assert device1.number_of_sim == 2
