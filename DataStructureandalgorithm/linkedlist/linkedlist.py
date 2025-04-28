# here we will see how the linked list are created in the python and some basic operation of linked listt
class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
        
        


class LinkedList():
    def __init__(self):
        self.head = None
        self.length = 0 #we have given length just to keep track of the numbers of item in linked list
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def print_list(self):
            current_node = self.head
            while current_node:
                print(current_node.value, end=" ")
                current_node = current_node.next
            print()    
            
linked_list1 = LinkedList()
linked_list1.append(4)
linked_list1.append(3)
linked_list1.append(2)
print(linked_list1.print_list())
