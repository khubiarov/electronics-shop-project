from src.item import Item

item1 = Item('acer', 100, 5)


item1.pay_rate = 1.0
print(item1.calculate_total_price())
print(item1.apply_discount())