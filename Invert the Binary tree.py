# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        root.left, root.right= root.right,root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
        
        
##I liked this one, pretty cute , just where I got stuck was not knowing that we have to use self. to use a function from the same recursion 
