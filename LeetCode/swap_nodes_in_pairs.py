# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        root = prev = ListNode(0)
        prev.next = head

        while head and head.next:
            # step.1
            temp = head.next
            # step.2
            head.next = temp.next
            # step.3
            temp.next = head
            # step.4
            prev.next = temp
            # step.5
            head = head.next
            prev = prev.next.next
                        
        return root.next
