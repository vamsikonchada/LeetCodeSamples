# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderHelper(self, root, ans):
        if root == None:
            return ans
        ans.append(root.val)
        self.preorderHelper(root.left, ans)
        self.preorderHelper(root.right, ans)

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        self.preorderHelper(root, ans)
        return ans
    
