from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque() 
#Deque is a doubly linked list while List is just an array. Randomly accessing an object at index i is O(n) for Deque but O(1) for List . Fast insertions and deletions at the beginning is the biggest advantage of Deque . Fast random reads is the advantage of List .

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
            return

        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min)))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()