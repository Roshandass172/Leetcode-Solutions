import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists):
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, l)

        dummy = ListNode()
        current = dummy
        while heap:
            node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, node.next)
        
        return dummy.next

def print_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "")
        node = node.next
    print()

# Helper to convert lists to linked lists
def build_linked_lists(lists):
    linked_lists = []
    for lst in lists:
        dummy = ListNode()
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        linked_lists.append(dummy.next)
    return linked_lists

# Example usage
if __name__ == "__main__":
    input_lists = [[1,4,5],[1,3,4],[2,6]]
    linked_lists = build_linked_lists(input_lists)
    solution = Solution()
    merged_head = solution.mergeKLists(linked_lists)
    print_list(merged_head)
