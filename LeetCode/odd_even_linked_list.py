# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        odd_result = ListNode()
        odd = odd_result
        
        even_result = ListNode()
        even = even_result
        
        i=1
        while head:
            if i%2!=0:
                odd.next = ListNode(head.val)
                odd = odd.next
            else:
                even.next = ListNode(head.val)
                even = even.next
            head = head.next
            i+=1
            
        odd_result = odd_result.next
        odd.next = even_result.next
        
        return odd_result
