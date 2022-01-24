
:bulb: odd_result/even_result 위치를 옮겨줄 odd/even 필요

        odd_result = ListNode()
        odd = odd_result 
        even_result = ListNode()
        even = even_result 
        
:bulb: head의 홀수/짝수 번의 value를 뽑아 잇는 listnode 생성

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


:bulb: even_result를 odd_result에 연결해주고 싶으니, 바로 next로 접근가능한 odd.next에 연결

        odd.next = even_result.next 
     
:bulb: odd_result = odd_result(odd).next

        odd_result = odd_result.next




