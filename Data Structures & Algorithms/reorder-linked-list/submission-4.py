# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = []
        dummy = ListNode()
        dummy = node =  head

        while dummy:
            l.append(dummy.val)
            dummy = dummy.next

        left = 0
        right = len(l)-1

        while(left<right):
            node.val =l[left]
            node = node.next

            node.val = l[right]
            node = node.next
            left +=1
            right -=1
            if(left == right):
                node.val = l[left]
                break



