class Element:
    def __init__(self, data=None):
        self.data = data


class OpenHashTable:
    def __init__(self, size):
        assert size > 0
        self.table = [Element() for _ in range(size)]
        self.size = size

    def hashing(self, data):
        return data % self.size

    def step_hash(self, data):
        return 1 + data % self.size

    def expansion(self):
        new = OpenHashTable(2*self.size)
        for i in self.table:
            new.add_element(i.data)
        self.table = new.table
        self.size = new.size

    def add_element(self, data):
        index = self.hashing(data)
        step = self.step_hash(data)
        if self.table[index].data is None:
            self.table[index].data = data
        else:
            circle = index
            while self.table[index].data is not None:
                index += step
                index = index % self.size
                if index == circle:
                    self.expansion()
            self.table[index].data = data

    def print_table(self):
        for i in range(self.size):
            print(i, self.table[i].data)
        print("-----------------")