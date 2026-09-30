# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next: # if fast is not none, we can do fast.next and if fast.next is not none then we can do fast.next.next
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False