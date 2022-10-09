# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next: #we have to make sure the fast has a next pointer to it to return a cycle else it returns False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False