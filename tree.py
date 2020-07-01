class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.sz = 0

l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
l4 = TreeNode(4)
l5 = TreeNode(5)
l6 = TreeNode(6)
l7 = TreeNode(7)
l8 = TreeNode(8)
l9 = TreeNode(9)
l1.left = l2
l1.right = l3
l2.left = l4
l2.right = l5
l4.right = l9
l4.left = l8
l3.left = l6
l3.right = l7


ans = 0

def dfs(node,depth):
	global ans
	ans += depth
	if  node.left:
		dfs(node.left,depth+1)
	if node.right:
		dfs(node.right,depth+1)


def sumofdepth(root):
	global ans
	dfs(root,0)
	print('sum of depth in tree',ans)

sumofdepth(l1)
ans = 0

# # p = (1,0) 
# p[0] no of node in sub tree
# p[1] sum of depth of sub tree
def sub_node_dfs(node):
	global ans
	p = [1,0]
	if  node.left:
		l = sub_node_dfs(node.left)
		p[0] += l[0]
		p[1] += l[0] + l[1]
	if node.right:
		r =sub_node_dfs(node.right)
		p[0] += r[0]
		p[1] += r[0] + r[1]
	ans += p[1]
	node.sz = p[0]
	return p
	
def sum_of_depth_of_sub_node(root):
	global ans, n
	sub_node_dfs(root)
	print('sum of depth of sub tree',ans)

sum_of_depth_of_sub_node(l1)


ans = 0

def distance(root,dis,target):
	global n,ans
	if root.val == target:
		ans = dis

	if root.left:
		newdis = dis-root.left.sz+(n-root.left.sz)
		distance(root.left,newdis,target)
	if root.right:
		newdis = dis-root.right.sz+(n-root.right.sz)
		distance(root.right,newdis,target)


def sum_distance(root,target):
	global ans,n

	p = sub_node_dfs(root)
	n = p[0]
	distance(root,p[1],target)
	print(ans)

sum_distance(l1,4)





