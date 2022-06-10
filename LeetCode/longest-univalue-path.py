
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal max_path
            
            if not node :
                return 0
            
            left_depth = dfs(node.left)
            if node.left and node.left.val == node.val :
                left_depth+=1
            else :
                left_depth=0
                
            right_depth = dfs(node.right)
            if node.right and node.right.val == node.val :
                right_depth +=1
            else :
                right_depth = 0
                
            max_path = max(max_path, left_depth+right_depth)
            
            return max(left_depth, right_depth)
    
        max_path=0
        
        dfs(root)
        
        return max_path
