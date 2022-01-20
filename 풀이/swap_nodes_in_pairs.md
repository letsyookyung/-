
        prev = ListNode(0) 
        root = prev 
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
                        
       => root.next


### 1번째 
![내가 이해를 위해 그린 그림](/풀이/참고이미지/swarp_nodes_in_pairs_1.jpg)

### 2번째 . . . 마지막
![내가 이해를 위해 그린 그림](/풀이/참고이미지/swarp_nodes_in_pairs_2.jpg)
