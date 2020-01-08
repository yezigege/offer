"""
用两个栈实现队列
要求：用两个栈实现队列，分别实现入队和出队操作 思路：一个栈负责入队，另一个负责出队，出栈为空则从入栈中导入到出栈中
"""


class MyQueue(object):
    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack:
            self.stack2.append(self.stack.pop())
        return self.stack2.pop() if self.stack2 else u'队列为空'


if __name__ == '__main__':
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.stack2)
    print(q.pop())
    print(q.stack2)
    q.push(3)
    print(q.pop())
    print(q.stack2)
    print(q.stack)
    print(q.pop())

    # q.push(4)
    # print(q.pop())
    # print(q.pop())
    # print(q.pop())

"""
一个栈实心队列
class Queue(object):
    # 队列
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        # 进队列
        self.items.insert(0, item)

    def dequeue(self):
        # 出队列
        return self.items.pop()

    def size(self):
        # 返回大小
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue("hello")
    q.enqueue("world")
    q.enqueue("itcast")
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
"""
