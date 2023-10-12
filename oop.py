class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Цена {price} не должна быть меньше нуля!"
        assert quantity >= 0, f"Количество {quantity} не должна быть меньше нуля!"


        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, 5)

item2 = Item("Laptop", 1000, 3)

item2.has_numpad = False

print(item1.calculate_total_price())
print(item2.calculate_total_price())
