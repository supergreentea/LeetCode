class RandomizedSet:

    def __init__(self):
        self.item_to_index = {}
        self.items_list = []

    def insert(self, val: int) -> bool:
        if val not in self.item_to_index:
            self.item_to_index[val] = len(self.items_list)
            self.items_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.item_to_index:
            val_index = self.item_to_index[val]
            last_val = self.items_list[-1]
            self.items_list[val_index] = last_val
            self.items_list.pop()
            self.item_to_index[last_val] = val_index
            del self.item_to_index[val]
            return True
        
        return False
            

    def getRandom(self) -> int:
        return random.choice(self.items_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()