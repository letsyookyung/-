    class Node :
        def __init__(self, value, right_node=None, left_node=None):
            self.value = value
            self.left = right_node
            self.right = left_node
            
        
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque, return true if the operation is successful.
        """
        if not self.isFull():
            new_node = Node(value) # 삽입할 노드 생성
            head_next = self.head.right # head 다음의 노드를 따로 저장 (본래 head <->head_next)
            # 빨간색
            self.head.right, head_next.left = new_node, new_node # head->new_node & new_node <- head_next
            # 파란색
            new_node.left, new_node.right = self.head, head_next # head <-new_node & new_node -> head_next
            self.cur_size +=1
            return True
        return False
    

    def deleteFront(self) -> bool:
        """
        Delete an item from the front of Deque. return true if the operation is successful.
        """
        if not self.isEmpty():
            head_right = self.head.right.right # head <-> head.right <-> head.right.right
            head_right.left, self.head.right = self.head, head_right # head <-> head.right.right
            self.cur_size -=1
            return True
        return False



### 본래 node
![내가 이해를 위해 그린 그림](/풀이/참고이미지/original_node.PNG)

### insertFront
![내가 이해를 위해 그린 그림](/풀이/참고이미지/insert_front.PNG)




