"""
问题：二叉树如何求两个叶节点的最近公共祖先？

解析：
    二叉树是搜索二叉树。
    原理：二叉搜索树是排序过的，位于左子树的结点都比父结点小，位
    于右子树的结点都比父结点大，我们只需从根节点开始和两个输入的结点进行
    比较，如果当前节点的值比两个结点的值都大，那么最低的公共祖先结点一定
    在该结点的左子树中，下一步开遍历当前结点的左子树。如果当前节点的值比
    两个结点的值都小，那么最低的公共祖先结点一定在该结点的右子树中，下一
    步开遍历当前结点的右子树。这样从上到下找到第一个在两个输入结点的值之
    间的结点
"""
class TreeNode(object):

    def __init__(self, left=None, right=None, data=None):
        self.data = data
        self.left = left
        self.right = right

    def getCommonAncestor(root, node1, node2):
        while root:
            if root.data > node1.data and root.data > node2.data:
                root = root.left
            elif root.data < node1.data and root.data < node2.data:
                root = root.right
            else:
                return root

    return None


