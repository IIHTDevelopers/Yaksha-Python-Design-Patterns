import numpy as np

class Bill:

    def __init__(self, price):
        self._price = price

    def generate_bill(self):
        return self._price

class AddGST:
    """
        Inherit Bill class and implement generate_bill which returns bill by adding 2.5% GST
    """
    pass

class AddDeliveryCharge:
    """
        Inherit Bill and implement generate_bill which returns bill by adding 5% of total bill(bill+ 2.5% of bill) after adding GST
    """
    pass


if __name__== "__main__":
    pass
