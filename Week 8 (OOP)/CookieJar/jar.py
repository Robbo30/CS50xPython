class Jar:
    def __init__(self, capacity = 12, size = 0):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity

        if size < 0:
            raise ValueError
        else:
            self._size = size

    def __str__(self):
        return self._size * "🍪"
    
    def deposit(self, num):
        self._size = self._size + num
        if self._size > self._capacity:
            raise ValueError
    
    def withdraw(self, num):
        self._size = self._size - num
        if self._size < 0:
            raise ValueError
        
    @property
    def returnCapacity(self):
        return self._capacity
    
    @property
    def retrunSize(self):
        return self._size