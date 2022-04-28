class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        
        def backtrack(start, comb):
            print('backtrack start:', start, comb)
            if len(comb) == k:
                print('fin', comb)
                res.append(comb.copy())
                return
            
            for i in range(start, n+1):
                comb.append(i)
                print('-', i, comb)
                backtrack(i+1, comb) 
                print('- pop',comb.pop())
                print('- comb2', comb)
                print('------------------------')
        
        backtrack(1,[])

        return res
                
        
        
# output log    
backtrack start: 1 []
- 1 [1]
backtrack start: 2 [1]
- 2 [1, 2]
backtrack start: 3 [1, 2]
- 3 [1, 2, 3]
backtrack start: 4 [1, 2, 3]
- 4 [1, 2, 3, 4]
backtrack start: 5 [1, 2, 3, 4]
fin [1, 2, 3, 4]
- pop 4
- comb2 [1, 2, 3]
------------------------
- 5 [1, 2, 3, 5]
backtrack start: 6 [1, 2, 3, 5]
fin [1, 2, 3, 5]
- pop 5
- comb2 [1, 2, 3]
------------------------
- 6 [1, 2, 3, 6]
backtrack start: 7 [1, 2, 3, 6]
fin [1, 2, 3, 6]
- pop 6
- comb2 [1, 2, 3]
------------------------
- pop 3
- comb2 [1, 2]
------------------------
- 4 [1, 2, 4]
backtrack start: 5 [1, 2, 4]
- 5 [1, 2, 4, 5]
backtrack start: 6 [1, 2, 4, 5]
fin [1, 2, 4, 5]
- pop 5
- comb2 [1, 2, 4]
------------------------
- 6 [1, 2, 4, 6]
backtrack start: 7 [1, 2, 4, 6]
fin [1, 2, 4, 6]
- pop 6
- comb2 [1, 2, 4]
------------------------
- pop 4
- comb2 [1, 2]
------------------------
- 5 [1, 2, 5]
backtrack start: 6 [1, 2, 5]
- 6 [1, 2, 5, 6]
backtrack start: 7 [1, 2, 5, 6]
fin [1, 2, 5, 6]
- pop 6
- comb2 [1, 2, 5]
------------------------
- pop 5
- comb2 [1, 2]
------------------------
- 6 [1, 2, 6]
backtrack start: 7 [1, 2, 6]
- pop 6
- comb2 [1, 2]
------------------------
- pop 2
- comb2 [1]
------------------------
- 3 [1, 3]
backtrack start: 4 [1, 3]
- 4 [1, 3, 4]
backtrack start: 5 [1, 3, 4]
- 5 [1, 3, 4, 5]
backtrack start: 6 [1, 3, 4, 5]
fin [1, 3, 4, 5]
- pop 5
- comb2 [1, 3, 4]
------------------------
- 6 [1, 3, 4, 6]
backtrack start: 7 [1, 3, 4, 6]
fin [1, 3, 4, 6]
- pop 6
- comb2 [1, 3, 4]
------------------------
- pop 4
- comb2 [1, 3]
------------------------
- 5 [1, 3, 5]
backtrack start: 6 [1, 3, 5]
- 6 [1, 3, 5, 6]
backtrack start: 7 [1, 3, 5, 6]
fin [1, 3, 5, 6]
- pop 6
- comb2 [1, 3, 5]
------------------------
- pop 5
- comb2 [1, 3]
------------------------
- 6 [1, 3, 6]
backtrack start: 7 [1, 3, 6]
- pop 6
- comb2 [1, 3]
------------------------
- pop 3
- comb2 [1]
------------------------
- 4 [1, 4]
backtrack start: 5 [1, 4]
- 5 [1, 4, 5]
backtrack start: 6 [1, 4, 5]
- 6 [1, 4, 5, 6]
backtrack start: 7 [1, 4, 5, 6]
fin [1, 4, 5, 6]
- pop 6
- comb2 [1, 4, 5]
------------------------
- pop 5
- comb2 [1, 4]
------------------------
- 6 [1, 4, 6]
backtrack start: 7 [1, 4, 6]
- pop 6
- comb2 [1, 4]
------------------------
- pop 4
- comb2 [1]
------------------------
- 5 [1, 5]
backtrack start: 6 [1, 5]
- 6 [1, 5, 6]
backtrack start: 7 [1, 5, 6]
- pop 6
- comb2 [1, 5]
------------------------
- pop 5
- comb2 [1]
------------------------
- 6 [1, 6]
backtrack start: 7 [1, 6]
- pop 6
- comb2 [1]
------------------------
- pop 1
- comb2 []
------------------------
- 2 [2]
backtrack start: 3 [2]
- 3 [2, 3]
backtrack start: 4 [2, 3]
- 4 [2, 3, 4]
backtrack start: 5 [2, 3, 4]
- 5 [2, 3, 4, 5]
backtrack start: 6 [2, 3, 4, 5]
fin [2, 3, 4, 5]
- pop 5
- comb2 [2, 3, 4]
------------------------
- 6 [2, 3, 4, 6]
backtrack start: 7 [2, 3, 4, 6]
fin [2, 3, 4, 6]
- pop 6
- comb2 [2, 3, 4]
------------------------
- pop 4
- comb2 [2, 3]
------------------------
- 5 [2, 3, 5]
backtrack start: 6 [2, 3, 5]
- 6 [2, 3, 5, 6]
backtrack start: 7 [2, 3, 5, 6]
fin [2, 3, 5, 6]
- pop 6
- comb2 [2, 3, 5]
------------------------
- pop 5
- comb2 [2, 3]
------------------------
- 6 [2, 3, 6]
backtrack start: 7 [2, 3, 6]
- pop 6
- comb2 [2, 3]
------------------------
- pop 3
- comb2 [2]
------------------------
- 4 [2, 4]
backtrack start: 5 [2, 4]
- 5 [2, 4, 5]
backtrack start: 6 [2, 4, 5]
- 6 [2, 4, 5, 6]
backtrack start: 7 [2, 4, 5, 6]
fin [2, 4, 5, 6]
- pop 6
- comb2 [2, 4, 5]
------------------------
- pop 5
- comb2 [2, 4]
------------------------
- 6 [2, 4, 6]
backtrack start: 7 [2, 4, 6]
- pop 6
- comb2 [2, 4]
------------------------
- pop 4
- comb2 [2]
------------------------
- 5 [2, 5]
backtrack start: 6 [2, 5]
- 6 [2, 5, 6]
backtrack start: 7 [2, 5, 6]
- pop 6
- comb2 [2, 5]
------------------------
- pop 5
- comb2 [2]
------------------------
- 6 [2, 6]
backtrack start: 7 [2, 6]
- pop 6
- comb2 [2]
------------------------
- pop 2
- comb2 []
------------------------
- 3 [3]
backtrack start: 4 [3]
- 4 [3, 4]
backtrack start: 5 [3, 4]
- 5 [3, 4, 5]
backtrack start: 6 [3, 4, 5]
- 6 [3, 4, 5, 6]
backtrack start: 7 [3, 4, 5, 6]
fin [3, 4, 5, 6]
- pop 6
- comb2 [3, 4, 5]
------------------------
- pop 5
- comb2 [3, 4]
------------------------
- 6 [3, 4, 6]
backtrack start: 7 [3, 4, 6]
- pop 6
- comb2 [3, 4]
------------------------
- pop 4
- comb2 [3]
------------------------
- 5 [3, 5]
backtrack start: 6 [3, 5]
- 6 [3, 5, 6]
backtrack start: 7 [3, 5, 6]
- pop 6
- comb2 [3, 5]
------------------------
- pop 5
- comb2 [3]
------------------------
- 6 [3, 6]
backtrack start: 7 [3, 6]
- pop 6
- comb2 [3]
------------------------
- pop 3
- comb2 []
------------------------
- 4 [4]
backtrack start: 5 [4]
- 5 [4, 5]
backtrack start: 6 [4, 5]
- 6 [4, 5, 6]
backtrack start: 7 [4, 5, 6]
- pop 6
- comb2 [4, 5]
------------------------
- pop 5
- comb2 [4]
------------------------
- 6 [4, 6]
backtrack start: 7 [4, 6]
- pop 6
- comb2 [4]
------------------------
- pop 4
- comb2 []
------------------------
- 5 [5]
backtrack start: 6 [5]
- 6 [5, 6]
backtrack start: 7 [5, 6]
- pop 6
- comb2 [5]
------------------------
- pop 5
- comb2 []
------------------------
- 6 [6]
backtrack start: 7 [6]
- pop 6
- comb2 []
------------------------
