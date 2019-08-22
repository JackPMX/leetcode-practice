class MinStack:

    def __init__(self):
        self.minItem = None
        self.stack = list()

    def push(self, x: int) -> None:
        item = Node(x)
        self.stack.append(x)
        p = self.minItem
        while(x > p.val):
            p = p.next

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


class Node:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.next = nextNode

