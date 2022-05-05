class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        subset = [] 
        def dfs(i):
            if i >= len(nums):
                print('저장', subset)
                result.append(subset.copy())
                print(i, 'end')
                return
        
            # decision to include nums[i]
            print('-', i, subset)
            subset.append(nums[i])
            print('--', i, subset)
            dfs(i+1)

            # decision NOT to include nums[i]
            subset.pop()
            print('---', subset)
            print(i)
            dfs(i+1)
            print('')
            
        dfs(0)
        
        return result

    
0 []
0 [1]
1 [1]
1 [1, 2]
2 [1, 2]
2 [1, 2, 3]
저장 [1, 2, 3]
3 end
--pop [1, 2]
2
저장 [1, 2]
3 end
왜 여기에서 pop으로 다시?
--pop [1]
1 그리고 왜 index가 1로?
2 [1]
2 [1, 3]
저장 [1, 3]
3 end
--pop [1]
2
저장 [1]
3 end


--pop []
0 
1 []
1 [2]
2 [2]
2 [2, 3]
저장 [2, 3]
3 end
--pop [2]
2
저장 [2]
3 end

--pop []
1
2 []
2 [3]
저장 [3]
3 end
--pop []
2
저장 []
3 end
