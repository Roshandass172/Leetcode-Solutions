class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        # Dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Iterate through the list in pairs
        while head and head.next:
            first = head
            second = head.next

            # Swap the nodes
            prev.next = second
            first.next = second.next
            second.next = first

            # Move the pointers forward
            prev = first
            head = first.next

        return dummy.next
