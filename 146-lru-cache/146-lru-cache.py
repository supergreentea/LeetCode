class Node:
    
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        
        # left.next would next LRU, right.prev would be MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
        self.cache = {} # key is key, value is node
    
    def remove_node(self, node):
        prev, nxt = node.prev, node.next
        node.prev.next, node.next.prev = nxt, prev
    
    def add_node(self, node):
        mru = self.right.prev
        
        mru.next = node
        node.prev = mru
        
        self.right.prev = node
        node.next = self.right
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove_node(self.cache[key])
            self.add_node(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove_node(self.cache[key])
        self.cache[key] = Node(key, value)
        self.add_node(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove_node(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)