# LRU: FIFO
# checkExist, get, put: O(1)
from collections import OrderedDict


# 1. hash table + linkedlist = OrderedDict() in py or LinkedHashMap in Java
# get/in/set/move_to_end/popitem（get/containsKey/put/remove) : O(1)
class LRUCache:

    def __init__(self, capacity: int):
        self.dic = OrderedDict()
        self.remain = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        # remove
        v = self.dic.pop(key)
        # append
        self.dic[key] = v
        return v

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        else:
            if self.remain > 0:
                self.remain -= 1
            else:
                self.dic.popitem(last=False)
        self.dic[key] = value


# 2. extend OrderedDict
class LRUCache1(OrderedDict):

    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        # move_to_end(key, last): move to the front(last=False) or tail(last=True or default)
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            # last=True(default): remove the last item; last=False: remove the first item (FIFO)
            self.popitem(last=False)


# 3. hash + implement a +double linked list
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache2:
    def __init__(self, capacity):
        self.capacity = capacity
        # key:node
        self.hashmap = {}
        # init the double-end linked list
        self.head = ListNode()  # dummy node to represent the head
        self.tail = ListNode()
        # !must be updated bidirectionally
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_tail(self, key):
        node = self.hashmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key):
        if key in self.hashmap:
            self.move_to_tail(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return -1
        else:
            return res.value

    def put(self, key, value):
        if key in self.hashmap:
            # update and move
            self.hashmap[key].value = value
            self.move_to_tail(key)
        else:
            # add
            if len(self.hashmap) == self.capacity:
                # full so remove the least recently use
                self.hashmap.pop(self.head.next.key)
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            new = ListNode(key, value)
            self.hashmap[key] = new
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)
