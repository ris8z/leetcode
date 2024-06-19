ex = 'https://leetcode.com/problems/lru-cache/description/'




class Node:
    def __init__(self, val:int=0, key:int=None, next_:'Node'=None, prev:'Node'=None) -> None:
        self.val = val
        self.key = key
        self.next = next_
        self.prev = prev

class LinkedList:
    def __init__(self) -> None:
        self.head, self.tail = Node(0), Node(0)
        self.head.next, self.tail.prev = self.tail, self.head

    def add(self, new:'Node') -> None:
        before, after = self.head, self.head.next
        new.prev, new.next = before, after
        before.next, after.prev = new, new

    def remove(self, target:'Node') -> 'Node':
        if target is self.head or target is self.tail or target is None:
            return None
        before, after = target.prev, target.next
        before.next, after.prev = after, before
        target.prev, target.next = None, None
        return target

    def moveToHead(self, node:'Node') -> None:
        self.add(self.remove(node))

    def getLastElement(self) -> 'Node':
        result = self.tail.prev
        if result is self.head:
            return None
        return result

    def removeLastElemnt(self) -> None:
        self.remove(self.getLastElement)


class LRUCache:

    def __init__(self, capacity: int):
        self.maxSize = capacity
        self.cache = {}
        self.lst = LinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            obj = self.cache[key]
            self.lst.moveToHead(obj)
            return obj.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            obj = self.cache[key]
            obj.val = value
            self.lst.moveToHead(obj)
            return

        if not (len(self.cache) < self.maxSize):
            #evict the least used node
            obj = self.lst.getLastElement()
            self.lst.remove(obj)
            del self.cache[obj.key]

        obj = Node(value, key)
        self.lst.add(obj)
        self.cache[key] = obj

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
