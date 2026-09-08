# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def getHeight(root):
            if not root:
                return 0
            
            return 1 + max(getHeight(root.left), getHeight(root.right))

        if not root:
            return True

        curr= root
        stack =[]
        while curr or stack:
            while curr:
                stack.append(curr)
                curr= curr.left
            curr = stack.pop()
            if abs(getHeight(curr.left) - getHeight(curr.right))>1:
                return False

            curr = curr.right

        return True

        
        