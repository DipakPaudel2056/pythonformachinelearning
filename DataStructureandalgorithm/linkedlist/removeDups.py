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
    
    def delete_node(node):
        if node == None or node.next == None:
            return False
        next = node.next
        node.data = next.data
        node.next = next.next
        return True
    
   
              
# implement the 2 sum problem using linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1, l2):
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    while l1 or l2 or carry: #the loop continues as long as there is any of value in l1 or l2 or carry
        val1 = l1.val if l1 else 0 #if the l1 doesnot have any value it is 0
        val2 = l2.val if l2 else 0 #if tthe l2 doesnot have any value it is 0

        total_sum = val1 + val2 + carry
        carry = total_sum // 10
        digit = total_sum % 10

        current.next = ListNode(digit)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy_head.next

def loop_detection(head):
    # create two pointer fast and slow
    fast = head
    slow = head
    # move fast at 2 steps at time and slow at 1 step at time
    while fast != None or fast.next != None:
        slow = slow.next
        fast = fast.next
        # whenever they collide break the loop
        if slow == fast :
            break
    # move slow to head and fast at the same place
    slow = head
    # error check if they donot collide return
    if (fast == None or fast.next == None):
        return None
    #find another collision point
    while (slow != fast):
        slow = slow.next
        fast = fast.next
    return fast

        