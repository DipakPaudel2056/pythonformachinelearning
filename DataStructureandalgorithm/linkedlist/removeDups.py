# linked list remove duplicate solution
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def removeDups(linkedList):
        hashmap = {}
        pervious = None
        while