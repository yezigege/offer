"""
从尾到头打印单链表
方法1：使用栈,可以使用列表模拟
方法2：直接递归
"""


# 创建节点
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 创建链表类
class Link(object):
    def __init__(self):
        self.__head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        cur = self.__head  # cur 初始状态下指向头结点
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.item, end='\n')
            cur = cur.next

    def add(self, item):
        """头部添加元素"""
        node = Node(item)  # 先创建一个保存 item 的节点
        node.next = self.__head  # 将新节点的 next 指向头结点
        self.__head = node  # 将链表的头 __head 指向新节点

    def append(self, item):
        """尾部添加元素"""
        node = Node(item)
        # 先判断链表当前是否为空，若空，则 __head 指向新节点
        if self.is_empty():
            self.__head = node
        # 若非空，则找到尾部，将尾结点的 next 指向新节点
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置插入元素"""
        # 若指定的位置位于第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定的位置 pos 超过链表尾部，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(item)
        # 查询指定位置
        else:
            node = Node(item)
            count = 0
            # pre 用来指代指定位置 pos 的前一个位置 pos-1， 初始从头结点开始移动到指定位置
            pre = self.__head
            while count < (pos-1):
                count += 1
                pre = pre.next
            # 将新节点的 next 指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur is not None:
            # 先找到指定元素
            if cur.item == item:
                # 如果第一个节点就是要删除的节点
                if not pre:
                    # 将头指针指向头结点的下一个节点
                    self.__head = cur.next
                # 如果第一个节点不是要删除的节点
                else:
                    # 将删除位置前的一个节点的next指向删除位置后的一个节点
                    pre.next = cur.next
                break
            else:
                # 继续遍历链表后移节点
                pre = cur
                cur = cur.next

    def search(self, item):
        """链表查找节点是否存在，并返回 True 或者 False"""
        cur = self.__head
        while cur is not None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


    @staticmethod
    def link(values):  # 遍历给定的列表，转换为链表
        head = Node(0)
        move = head
        try:
            for val in values:
                tmp = Node(val)
                move.next = tmp
                move = move.next
        except Exception as e:
            print(e)
        return head.next


# 法一
def print_links(links):
    """
    遍历链表，去除链表中每个节点的值，放入到一个列表中，再遍历这个列表，每次抛出一个值
    """
    stack = []
    while links:
        stack.append(links.val)
        links = links.next
    while stack:
        print(stack.pop())


# 法二
def print_link_recursion(links):
    """
    递归链表，递归到最后，抛出此节点的值
    """
    if links:
        print_link_recursion(links.next)
        print(links.val)


if __name__ == '__main__':
    head = Link.link([1, 2, 3, 4, 5, 6])
    print(head, end=' ')
    print_links(head)
    print_link_recursion(head)

