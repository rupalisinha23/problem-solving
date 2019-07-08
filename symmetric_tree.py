class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# recurvive solution
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is none or right is None:
            return False

        if left.val == right.val:
            outPair = isMirror(left.left, right.right)
            inPair = isMirror(left.right, right.left)
            return outPair and inPair

# iterative solution
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        stack = [[root.left, root.right]]

        while len(stack) > 0:
            pair = stack.pop()
            left = pair[0]
            right = pair[1]

            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append([left.left, right.right])
                stack.append([left.right, right.left])
            else:
                return False
        return True
