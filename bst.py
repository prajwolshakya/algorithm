# Definition for a binary tree node.
import  sys
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():

    def bst(self,limit,preorder):
        if len(preorder) == self.i or preorder[self.i] > limit:
            return None
        root_node = preorder[self.i]
        print(self.i,root_node)


        node = TreeNode(root_node)
        self.i +=1
        node.left = self.bst(root_node,preorder)
        node.right = self.bst(limit,preorder)

        return node

    def bstFromPreorder(self, preorder):
        self.i = 0
        return  self.bst(sys.maxsize,preorder)



        # l = len(preorder)
        # if l == 0:
        #     return None
        # root_node = preorder[0]
        # node = TreeNode(root_node)
        # s,b = [] ,[]
        # for i in range(1,l):
        #     if root_node > preorder[i]:
        #         s.append(preorder[i])
        #     else:
        #         b.append(preorder[i])
        # node.left = self.bstFromPreorder(s)
        # node.right = self.bstFromPreorder(b)
        # return  node




x = Solution()
y = x.bstFromPreorder([8,5,1,7,10,12])
print(y)

