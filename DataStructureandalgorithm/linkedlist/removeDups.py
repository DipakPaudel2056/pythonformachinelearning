# linked list remove duplicate solution
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def removedups(self):
        if not self.head:
            return
        seen = set()
        current = self.head
        seen.add(current.data)
        
        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
            else:
                seen.add(current.next.data)
                current = current.next
    def kth_last(self,k):
        left = self.head
        right = self.head
        if self.head == None:
            return 0
        for i in range(k):
            if (left.next == None):
                return None
            left = left.next
        while (left.next != None):
            left = left.next
            right = right.next
        return right
   
              
        