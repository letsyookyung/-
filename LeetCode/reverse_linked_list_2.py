# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
            
        m = left
        n = right
        
        prev_start = ListNode(0)
        root_start = prev_start

        for_reverse =[]

        prev_last = ListNode(0)
        root_last = prev_last

        i=1
        while head :        

            if i < m :
                print('-1')
                prev_start.next = ListNode(head.val)
                prev_start = prev_start.next # root_start.next
                
            elif i>=m and i<=n:
                print('-2')
                for_reverse.append(head.val) 
            elif i > n :
                print('-3')
                prev_last.next = head
                prev_last = prev_last.next # root_last.next

            i+=1
            head = head.next
        
        def toListNode(for_reverse):
            prev = None
            for v in for_reverse:
                node = ListNode(v)
                node.next = prev
                prev = node
            return node
            
        root_middle = toListNode(for_reverse) # root_middle 

        
        root_start.
