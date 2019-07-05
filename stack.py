class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, val):
        newNode = Node(val)
        if (not self.first):
            self.first = newNode
            self.last = newNode
            self.size +=1
        else:
            temp = self.first
            self.first = newNode
            self.first.next = temp
            self.size +=1

        return self.size

    def pop(self):
        if (not self.first):
            return None

        temp = self.first

        if(self.first == self.last):
            self.last = None

        self.first = self.first.next
        self.size -=1
        return temp.value



stack = Stack()
stack.push(11)

