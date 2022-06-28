class RandomizedSet:

    def __init__(self):
        self.list = []
        self.map = {}
        

    def insert(self, val: int) -> bool:
        not_present = not val in self.map
        if not_present:
            self.map[val] = len(self.list)
            self.list.append(val)
        return not_present

    def remove(self, val: int) -> bool:
        present = val in self.map
        if present:
            val_index = self.map[val]
            last_val = self.list[-1]
            self.list[val_index] = last_val
            self.list.pop()
            self.map[last_val] = val_index
            del self.map[val]
        return present

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()