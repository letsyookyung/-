# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# 혼자 해본 방법
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
            

        # left/right 구간 값 저장하기
        prev_start = ListNode(0)
        root_start = prev_start

        for_reverse =[]

        prev_last = ListNode(0)
        root_last = prev_last

        i=1
        while head :        
            if i < left :
                prev_start.next = ListNode(head.val)
                prev_start = prev_start.next # root_start.next
            elif i>=left and i<=right:
                for_reverse.append(head.val) 
            elif i > right :
                prev_last.next = head
                prev_last = prev_last.next # root_last.next
            i+=1
            head = head.next
        
        
        # middle 부분 뒤집기
        root_middle = toListNode(for_reverse) # root_middle 

        
        # root_start - root_middle - root_last 이어붙이기        
        # root_final_temp = root_start -> root_middle
        root_final_temp = root_start
        i =1
        while root_start :
            
            if i ==left :
                root_start.next = root_middle
            root_start = root_start.next
            i+=1
        
        # root_final = root_final_temp -> root_last
        root_final = root_final_temp
        i=1
        while root_final_temp :
            if i == right+1 :
                root_final_temp.next = root_last.next
            root_final_temp = root_final_temp.next
            i+=1
        
        
        return root_final.next
    

    
def toListNode(for_reverse):
    prev = None
    for v in for_reverse:
        node = ListNode(v)
        node.next = prev
        prev = node
    return node
            
