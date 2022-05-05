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
