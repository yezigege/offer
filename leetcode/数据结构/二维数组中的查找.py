"""
题目：二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中

思路：从左下角或者右上角开始比较
    先获取数组的 行长， 和列长
    再 根据行长， 列长遍历所有值，
    判断 最后一行第一列 是否是所需的值，
    是=》直接返回
    大于=》就减少行值
    小于=》就减少列值
"""


def find_integer(matrix, num):
    """
    :param matrix: [[], []...]
    :param num: int
    :return: bool
    """
    if not matrix:
        return False
    rows, cols = len(matrix), len(matrix[0])  # 3 行， 4 列
    row, col = rows - 1, 0  # 2, 0
    while row >= 0 and col <= cols - 1:
        if matrix[row][col] == num:
            return True, row, col
        elif matrix[row][col] > num:
            row -= 1
        else:
            col += 1
    return False


if __name__ == "__main__":
    data = [[0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11]]
    res, row, col = find_integer(data, 9)
    print(res, row, col)
