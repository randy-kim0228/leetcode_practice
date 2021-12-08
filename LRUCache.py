class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.dict = dict()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.remove(node)
        self.add(node)
        return node.val
    
    def put(self, key, val):
        if key in self.dict:
            self.remove(self.dict[key])
        node = Node(key, val)
        self.dict[key] = node
        self.add(node)
        if len(self.dict) > self.capacity:
            head = self.head.next
            self.remove(head)
            del self.dict[head.key]
    
    def add(self, node):
        tail = self.tail.prev
        tail.next = node
        node.prev = tail
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node):
        next, prev = node.next, node.prev
        next.prev = prev
        prev.next = next
    
