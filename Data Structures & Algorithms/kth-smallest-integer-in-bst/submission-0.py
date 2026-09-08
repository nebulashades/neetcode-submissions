# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = 0
        value = 0

        def inOrder(root):
            if root == None:
                return
            
            inOrder(root.left)
            nonlocal count
            count+= 1
            if count == k:
                nonlocal value 
                value = root.val
            inOrder(root.right)

        inOrder(root)
        return value


                
            
            

        