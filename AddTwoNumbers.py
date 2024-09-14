class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        p, q, current = l1, l2, dummy
        carry = 0
        
        while p is not None or q is not None:
            x = p.val if p is not None else 0
            y = q.val if q is not None else 0
            total = carry + x + y
            
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        
        if carry > 0:
            current.next = ListNode(carry)
        
        return dummy.next

# Helper function to convert a list to a linked list
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linkedlist_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

# Example usage
sol = Solution()
l1 = list_to_linkedlist([2, 4, 3])
l2 = list_to_linkedlist([5, 6, 4])
result = sol.addTwoNumbers(l1, l2)
print(linkedlist_to_list(result))  # Output: [7, 0, 8]
