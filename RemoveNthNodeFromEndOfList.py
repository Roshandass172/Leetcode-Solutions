class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # Create a dummy node to simplify edge cases (like removing the first node)
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        
        # Move the first pointer n+1 steps ahead so that the gap between first and second is n
        for _ in range(n + 1):
            first = first.next
        
        # Move both pointers until the first pointer reaches the end
        while first:
            first = first.next
            second = second.next
        
        # Skip the nth node
        second.next = second.next.next
        
        # Return the head of the modified list
        return dummy.next

# Example usage:
def print_list(node):
    output = []
    while node:
        output.append(node.val)
        node = node.next
    return output

# Create the linked list [1,2,3,4,5]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()
new_head = sol.removeNthFromEnd(head, 2)
print(print_list(new_head))  # Output: [1, 2, 3, 5]
