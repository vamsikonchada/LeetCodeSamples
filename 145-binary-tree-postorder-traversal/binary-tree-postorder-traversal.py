# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderHelper(self, root, ans):
        if root == None:
            return ans
        self.postorderHelper(root.left, ans)
        self.postorderHelper(root.right, ans)
        ans.append(root.val)

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        #self.postorderHelper(root, ans)
        if root == None:
            return ans
        mystack = [root]

        while mystack:
            node = mystack.pop()
            ans.insert(0, node.val)
            if (node.left):
                mystack.append(node.left)
            if (node.right):
                mystack.append(node.right)
        
        return ans
