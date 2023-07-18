class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n: int):
        if (self.size + n) > self.capacity:
            raise ValueError(
                "Depositing this amount of cookies will exceed the maximum capacity of the jar"
            )
        else:
            self.size += n

    def withdraw(self, n: int):
        if n > self.size:
            raise ValueError(
                "This amount of cookies is greater than that available in the jar"
            )
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not capacity or type(capacity) != int or capacity <= 0:
            raise ValueError("Invalid jar capacity")
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n: int):
        self._size = n
