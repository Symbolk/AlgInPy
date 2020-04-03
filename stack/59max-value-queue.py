import queue
# from collections import deque

# use a deque to cache descending max values
class MaxQueue:
    """double deques is fastest"""
    def __init__(self):
        self.deque = deque()
        # self.deque = []
        self.queue = deque()
        # self.queue = queue.Queue()

    # O(1)
    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    # O(1)
    def push_back(self, value: int) -> None:
        # keep the deque[0] is the max value
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.append(value)

    # O(1)
    def pop_front(self) -> int:
        if not self.queue:
            return -1
        ans = self.queue.popleft()
        if ans == self.deque[0]:
            self.deque.popleft()
            # self.deque.pop(0)
        return ans

class MaxQueue:
    """2 arrays"""
    def __init__(self):
        self.queue = []
        self.max_stack = []

    def max_value(self) -> int:
        return self.max_stack[0] if self.max_stack else -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.max_stack and self.max_stack[-1] < value:
            self.max_stack.pop()
        self.max_stack.append(value)

    def pop_front(self) -> int:
        if not self.queue: return -1
        ans = self.queue.pop(0)
        if ans == self.max_stack[0]:
            self.max_stack.pop(0)
        return ans


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
