class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Pallindrome:
    def isPallindrome(self, head:ListNode) -> bool:
        if not head or not head.next:
            return True
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        length = len(stack)
        for i in range(length/2):
            if stack[i] != stack[len(stack)-i-1]:
                return False
        return True

