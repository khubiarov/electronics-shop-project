"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def test_shop():
    return Item('acer', 100, 5)


def test_calculate_total_price(test_shop):
    assert test_shop.calculate_total_price() == 500



def test_apply_discount(test_shop):

    assert test_shop.apply_discount() == 100
    test_shop.pay_rate = 0.5
    assert test_shop.apply_discount() == 50

