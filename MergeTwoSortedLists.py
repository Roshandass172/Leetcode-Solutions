class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a dummy node to act as the head of the new merged list
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If there are remaining nodes in either list1 or list2, append them
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # Return the head of the merged list (next of dummy node)
        return dummy.next

# Example usage:
def print_list(node):
    output = []
    while node:
        output.append(node.val)
        node = node.next
    return output

# Create the linked lists: list1 = [1,2,4] and list2 = [1,3,4]
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

sol = Solution()
merged_head = sol.mergeTwoLists(list1, list2)
print(print_list(merged_head))  # Output: [1, 1, 2, 3, 4, 4]

