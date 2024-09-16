class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        # Function to reverse a portion of the list
        def reverseLinkedList(start, end):
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        # Function to check if there are at least k nodes left
        def hasKNodes(node, k):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k
        
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while hasKNodes(group_prev.next, k):
            group_start = group_prev.next
            group_end = group_start
            for _ in range(k - 1):
                group_end = group_end.next
            next_group_start = group_end.next
            
            # Reverse the group
            new_head = reverseLinkedList(group_start, next_group_start)
            
            # Connect the previous part to the newly reversed group
            group_prev.next = new_head
            group_start.next = next_group_start
            
            # Move the pointer for the next group
            group_prev = group_start
        
        return dummy.next

# Helper function to print the linked list
def print_list(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print(" -> ".join(values))

# Helper function to convert list to linked list nodes
def build_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Example usage
if __name__ == "__main__":
    input_list = [1,2,3,4,5]
    k = 2
    head = build_linked_list(input_list)
    solution = Solution()
    new_head = solution.reverseKGroup(head, k)
    print_list(new_head)
