class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


class Solution:
    def remove_nth_node(self, head,n):
        dummy = Node(0)
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(n):
            first = first.next

        while(first.next) is not None:
            first = first.next
            second = second.next
        else:
            second.next = second.nex.next

        return dummy.next

sol = Solution()
