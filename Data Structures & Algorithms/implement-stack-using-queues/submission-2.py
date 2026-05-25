class MyStack:

    def __init__(self):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1): 
            self.queue.append(self.queue.popleft())
        # # EXAMPLE TRACE:
        # Initial Queue: [1, 2] (Front is 1)
        # 1. push(3) -> Queue becomes [1, 2, 3]
        # 2. Rotate (Loop runs 2 times):
        #    - Pop 1, Append 1 -> [2, 3, 1]
        #    - Pop 2, Append 2 -> [3, 1, 2]
        # Result: [3, 1, 2] -> 3 is now at the front (Top of Stack)
        
    def pop(self) -> int:
        return self.queue.popleft()
        
    def top(self) -> int:
        return self.queue[0]

        
    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()