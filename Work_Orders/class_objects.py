class Order:
    pass

class Work_Order(Order):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id}: {self.name}"