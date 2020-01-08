"""
斐波那契数列
"""
from utils.clock import clock


@clock
def fib(num):
    a, b = 0, 1
    for i in range(num):
        yield b
        a, b = b, a + b


if __name__ == '__main__':
    print([n for n in fib(10)])
