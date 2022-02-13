        root = start = ListNode()
        root.next = head
        
        # 시작start 지정
        for _ in range(left-1):
            start = start.next
        # 결국 시작start 다음이 가장 마지막end이 됨
        end = start.next
        
        # tmp/start/end 순서 바꾸는 과정 밑에 그림으로 하나하나..
        for _ in range(right-left):
            tmp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = tmp

![내가 이해를 위해 그린 그림](/풀이/참고이미지/reversed_list2_1.jpg)

![내가 이해를 위해 그린 그림](/풀이/참고이미지/reversed_list2_2.jpg)

         .  
         .  
         .  
         (right-left) 횟수 만큼 loop  

        root = start니깐, 
        return root.next 
