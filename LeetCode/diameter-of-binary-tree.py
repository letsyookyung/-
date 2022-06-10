class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root : 
            return None
        
        def dfs(node):
            nonlocal max_diameter
            
            left_depth = 0
            right_depth = 0
            
            if node.left :
                left_depth = dfs(node.left)
            if node.right :
                right_depth = dfs(node.right)
                
            node_diameter = left_depth + right_depth    
            max_diameter = max(max_diameter, node_diameter)
            
            node_depth = max(left_depth, right_depth)
            
            return 1 + node_depth
        
        max_diameter = 0
        dfs(root)
        
        return max_diameter


    
