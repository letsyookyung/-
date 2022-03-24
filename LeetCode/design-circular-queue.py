class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value: int) -> bool:
        """
        Insert an elemnet into the circular queue. Return true if the operation is successful.
        """
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            # 다음자리로 p2포인터 이동해두고, 길이가 넘어가면 나머지 연산자를 이용하여 한바퀴 돌아서 자리찾기
            self.p2 = (self.p2+1) % self.maxlen 
            return True
        else :
            return False
        
    def deQueue(self) -> bool:
        """
        delete an element from the circular queue. Return true if the oper is successful.
        """
        if self.q[self.p1] is None :
            return False #이미 내보낼 것이 없는 상태
        else :
            self.q[self.p1] = None
            self.p1 = (self.p1+1) % self.maxlen
            return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        # p1이 가르키는 맨앞의 요소를 반환
        if self.q[self.p1] is None :
            return -1
        else :
            return self.q[self.p1]


    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        # p2이 가르키는 맨 뒤의 요소를 반환 
        # p2는 이미 뒤에 삽입될 자리를 가르키고 있기 때문에 p2-1이 맨 뒤의 요소를 가르키고 있음
        if self.q[self.p2-1] is None :
            return -1
        else :
            return self.q[self.p2-1]
        

    def isEmpty(self) -> bool:
        """
        check whether the circular queue is full or not.
        """
        # p1,p2가 가르키는 자리가 같고, 그 안의 요소가 존재하지 않는다면 큐는 empty
        if self.p1 == self.p2 and self.q[self.p1] == None :
            return "empty"
        

    def isFull(self) -> bool:
        """
        check whether the circular queue is full or not.
        """
        # p1, p2가 가르키는 자리가 같고, 그 안의 요소가 존재하면 공간이 다 찬것입니다.
        if self.p1 == self.p2 and self.q[self.p1] != None :
            return "full"
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
