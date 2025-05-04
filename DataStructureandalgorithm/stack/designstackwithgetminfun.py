# in this challenge we need to implement the stack with the get min and getmax function where the push and pop must have O(1) time complexity

class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.max_stack = [] 
    
    def push(self,item):
        self.stack.append(item)
        # check if the minstack is empty or the last element of the min stack is less than the element
        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)
        if not self.max_stack or item >= self.max_stack[-1]:
            self.max_stack.append(item)
    def pop(self):
        if not self.stack :
            return None
        item = self.stack.pop()
        # pop from the individual min and max stack as well
        if item == self.min_stack[-1]:
            self.min_stack.pop()
        if item == self.max_stack[-1]:
            self.max_stack.pop()
        return item
    
    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None
    def getMax(self):
        return self.max_stack[-1] if self.max_stack else None
    def sortStack(self):
        # sort from small at the top and large at end
        return