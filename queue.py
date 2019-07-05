class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0


    def enqueue(self, val):
        """
        Add an element at the end of this linked list

        """
        newNode = Node(val)
        if (not self.first):
            self.first = newNode
            self.last = newNode
            self.size +=1
        else:
            self.last.next = newNode
            self.last = newNode
            self.size += 1

        return self.size


    def dequeue(self):
        if (not self.first):
            return None

        temp = self.first
        if(self.first == self.last):
            self.last = None
        self.first = self.first.next
        self.size -=1

        return temp.value

queue = Queue()
queue.enqueue(11)