"""
Singly Linked List
"""

class Node:
   def __init__(self,value):
       self.val = value
       self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def push(self, value):
        newNode = Node(value)
        if (not self.head):
            self.head = newNode
            self.tail = self.head
            self.length +=1

        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length +=1
        return self

    def pop(self):
        if (not self.head):
            return None

        current = self.head
        newTail = current
        while(current.next):
            newTail = current;
            current = current.next
        self.tail = newTail
        self.tail.next = None
        self.length -=1
        return current

    def shift(self):
        """
        Removes the first element.
        """
        if (not self.head):
            return None
        currentHead = self.head
        self.head = currentHead.next
        self.length -=1
        return currentHead

    def unshift(self, value):
        """
        Add an element at the begining.
        """
        newNode = Node(value)
        if (not self.head):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length +=1
        return self

    def get(self,pos):
        """
        Retrieving a node by its position in the linked list.
        """
        if (pos < 0 or pos >= self.length):
            return None
        counter = 0
        current = self.head
        while counter != pos:
            current = current.next
            counter +=1
        return current

    def set(self, idx, value):
        """
        Changing the value at the provided index
        """
        foundNode = self.get(idx)
        if (foundNode):
            foundNode.val = value
            return True
        return False

    def insert(self, index, val):
        if (index < 0 or index > self.length):
            return False
        if(index == self.length):
            return self.push(val)
        if (index == 0):
            return self.unshift(val)
        newNode = Node(val)
        prev = self.get(index-1)
        temp = prev.next
        prev.next = newNode
        newNode.next = temp
        self.length +=1
        return True

    def remove(self, idx):
        if(idx < 0 or idx >= self.length):
            return None
        if(idx == 0):
            return self.shift()
        if(idx == self.length-1):
            return self.pop()
        prevNode = self.get(idx-1)
        removed = prevNode.next
        prevNode.next = removed.next
        self.length -=1
        return removed

    def reverse(self):
        node = self.head
        self.head = self.tail
        self.tail = node
        prev = None
        for i n range(self.length):
            next = node.next
            node.next = prev
            prev = node
            node = next

        return self




list = SinglyLinkedList()
list.push(11)
list.push(12)
list.push(13)
list.push(14)
list.shift()
print(list.length)







