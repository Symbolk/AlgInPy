class Node:
    def __init__(self, key, value, cnt=0):
        self.val = [key, value, cnt]
        self.prev = None
        self.next = None


# least frequently use
# cache by descending cnt (access num)
class LFUCache:

    def __init__(self, capacity: int):
        # key:node
        self.cache = {}
        self.capacity = capacity
        # dummy head and tail
        self.head = Node(1, 1, float('inf'))
        self.tail = Node(-1, -1, float('-inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def refresh(self, node, cnt):
        pn, nn = node.prev, node.next
        if cnt < pn.val[2]:
            return
        # remove node between pn and nn
        pn.next, nn.prev = nn, pn
        # find forward for the first one that > cnt
        while cnt >= pn.val[2]:
            pn = pn.prev
        nn = pn.next
        # insert node between new pn and nn
        pn.next = nn.prev = node
        node.prev = pn
        node.next = nn

    def get(self, key: int) -> int:
        if self.capacity <= 0 or key not in self.cache:
            return -1
        node = self.cache[key]
        k, v, cnt = node.val
        node.val[2] = cnt + 1
        self.refresh(node, cnt + 1)
        return v

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.cache:
            node = self.cache[key]
            _, _, cnt = node.val
            node.val = [key, value, cnt + 1]
            self.refresh(node, cnt + 1)
        else:
            if len(self.cache) >= self.capacity:
                # full so remove the last (tp)
                tp, tpp = self.tail.prev, self.tail.prev.prev
                self.cache.pop(tp.val[0])
                tpp.next = self.tail
                self.tail.prev = tpp
            new = Node(key, value)  # cnt = 0
            # append
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new
            self.cache[key] = new
            self.refresh(new, 0)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


cache = LFUCache(2)

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)

cache.get(2)
cache.get(3)

cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)
