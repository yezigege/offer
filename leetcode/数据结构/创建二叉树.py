# coding=utf-8

"""
要求：用前序和中序遍历结果构建二叉树，遍历结果中不包含重复值

思路：前序的第一个元素是根结点的值，在中序中找到该值，中序中该值的左边的元素是根结点的左子树，右边是右子树，然后递归的处理左边和右边

"""
from collections import deque


class TreeNode(object):
    """
    二叉树结点定义
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    """
    二叉树
    """
    def __init__(self):
        self.root = None

    def bfs(self):
        """宽度优先搜索"""
        ret = []
        queue = deque([self.root])
        while queue:
            # print(f"queue___len__>>{queue.__len__()}")
            node = queue.popleft()
            # print(f"====>{node.val if node else ''}, ####>{queue.__len__()}")
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ret

    def pre_traversal(self):
        """前序遍历"""
        ret = []

        def traversal(root):
            if not root:
                return
            ret.append(root.val)
            traversal(root.left)
            traversal(root.right)

        traversal(self.root)
        return ret

    def in_traversal(self):
        """中序遍历"""
        ret = []

        def traversal(root):
            if not root:
                return
            traversal(root.left)
            ret.append(root.val)
            traversal(root.right)

        traversal(self.root)
        return ret

    def post_traversal(self):
        """后序遍历"""
        ret = []

        def traversal(root):
            # 判断是否已经到达叶子节点
            if not root:  # 递归过程中，每一个节点都是root，而初始化节点时，左右子树初始为None。
                return
            traversal(root.left)
            traversal(root.right)
            ret.append(root.val)

        traversal(self.root)
        return ret


def construct_tree(preorder=None, inorder=None):
    """
    构建二叉树
    """
    if not preorder or not inorder:
        return None
    index = inorder.index(preorder[0])  # 获取前序遍历中第一个元素在中序遍历中的索引位置，即根节点
    left = inorder[0:index]             # 根据根节点在中序遍历列表中的索引，获取左子树
    right = inorder[index+1:]           # 根据根节点在中序遍历列表中的索引，获取右子树
    root = TreeNode(preorder[0])        # 根据根节点在中序遍历列表中的索引，获取并创建根节点
    root.left = construct_tree(preorder[1:1+len(left)], left)       # 递归。左子树的前序遍历，左子树的中序遍历
    root.right = construct_tree(preorder[-len(right):], right)      # 递归。右子树的前序遍历，右子树的中序遍历
    return root


if __name__ == '__main__':
    t = Tree()
    root = construct_tree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
    t.root = root
    print(t.bfs())
    print(t.pre_traversal())
    print(t.in_traversal())
    print(t.post_traversal())
"""
ret方式运行结果
[1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 4, 7, 3, 5, 6, 8]
[4, 7, 2, 1, 5, 3, 8, 6]
[7, 4, 2, 5, 8, 6, 3, 1]
"""