from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, product):
        self.current = 0
        self.product = product

    def __next__(self):
        product = self.product[self.current]
        return product
