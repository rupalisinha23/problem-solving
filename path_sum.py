class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def hasPathSum(self, root, s):
        if not root:
            return False
        else:
            if root.val == s:
                if root.left == None and root.right == None:
                    return True
                else:
                    return self.hasPathSum(root.left,0) or self.hasPathSum(root.right, 0)
            else:
                leftover = s-root.val
                return self.hasPathSum(root.left, leftover) or self.hasPathSum(root.right, leftover)




s = 21
root = Node(1)
root.left = Node(8)
root.right = Node(2)
root.left.right = Node(5)
root.left.left = Node(3)
root.right.left = Node(2)

sol = Tree()
print(sol.hasPathSum(root, 0))