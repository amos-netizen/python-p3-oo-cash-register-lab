#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.items.append((title, price, quantity))
        self.total += price*quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            title, price, quantity = self.items.pop()
            self.total -= price * quantity
            print(f"Voided last transaction: {quantity} {title}(s) at ${price} each.")
        else:
            print("No transactions to void.")
    
     
