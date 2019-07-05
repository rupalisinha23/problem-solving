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
        





list = SinglyLinkedList()
list.push(11)
list.push(12)
list.push(13)
list.push(14)
list.shift()
print(list.length)







