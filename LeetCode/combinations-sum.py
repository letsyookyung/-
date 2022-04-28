class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, current, total):
            if total == target :
                print('----------------------target', current)
                res.append(current.copy())
                
                return
            
            if i >= len(candidates) or total>target:
                print('-over fin', '/index', i, total)
                return
            
            current.append(candidates[i])
            print('-current',current)
            # 1)
            dfs(i, current, total+candidates[i])
            current.pop()
            # 2) 
            print('use next value')
            dfs(i+1, current, total)    
            
        dfs(0,[],0)
        
        return res
                
                
        
