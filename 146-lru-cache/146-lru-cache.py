class Node:
    
    def __init__(self, key = -1, val = -1):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.left, self.right = Node(), Node()
        self.left.next, self.right.prev = self.right, self.left
        
        self.capacity = capacity
        
        # { key : key node }
        self.cache = {}
    
    # inserts node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt
        
    # deletes node
    def delete(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev 
    
    # check if key is in cache
    """
    if key is in cache
        delete node and reinsert so key is LRU
    Else
        return -1
    
    """
    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
    
    """
    """
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.delete(self.cache[key])
            self.insert(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
            if len(self.cache) > self.capacity:
                lru = self.left.next
                self.delete(self.cache[lru.key])
                del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)