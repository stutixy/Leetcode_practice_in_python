class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.LRU = Node(0,0)
        self.MRU = Node(0,0)
        self.LRU.next, self.MRU.prev = self.MRU, self.LRU

    def remove(self, node):
        nxt, prev = node.next, node.prev
        nxt.prev = prev
        prev.next = nxt

    def insert(self, node):
        prev = self.MRU.prev
        self.MRU.prev = node
        node.next = self.MRU
        node.prev = prev
        prev.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        newNode = Node(key, value)
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) == self.cap:
            tobeDeleted = self.LRU.next
            del self.cache[tobeDeleted.key]
            self.remove(tobeDeleted)
        self.cache[key] = newNode
        self.insert(newNode)


            
        


        
