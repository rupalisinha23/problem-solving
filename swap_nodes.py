class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def swap_nodes(self, head):
        if not head:
            return
        if not head.next:
            return

        temp1 = head
        temp2 = head.next
        temp3 = head.next.next
        head = temp2
        head.next = temp1
        temp1.next = self.swap_nodes(temp3)
        return head

