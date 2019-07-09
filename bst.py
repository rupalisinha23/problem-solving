class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None


    def insert(self, val):
        newNode = Node(val)
        if(self.root == None):
            self.root= newNode
            return self
        else:
            current = self.root
            while(True):
                if(val < current.val):
                    if current.left == None:
                        current.left = newNode
                        return self
                    else:
                        current = current.left
                elif val > current.val:
                    if current.right == None:
                        current.right = newNode
                        return self
                    else:
                        current = current.right


    def find(self, val):
        if self.root is None:
            return False

        current = self.root
        found = False

        while current and !False:
            if val < current.val:
                current = current.left
            elif val > current.val:
                current = current.right
            else:
                found = True

        if (!found):
            return False
        return current




