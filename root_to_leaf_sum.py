class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def doSumNumbers(self, root, val):
        if root.left is None and root.right is None:
            return val * 10 + root.val
        left = 0
        right = 0
        if root.left is not None:
            left = self.doSumNumbers(root.left, val*10+root.val)
        if root.right is not None:
            right = self.doSumNumbers(root.right, val*10 + root.val)
        return left+right

    def sumNumbers(self, root):
        if root == None:
            return 0

        return self.doSumNumbers(root, 0)