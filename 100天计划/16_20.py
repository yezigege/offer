def select_sort(origin_items, comp=lambda x, y: x < y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def bubble_sort(origin_items, comp=lambda x, y: x > y):
    """高质量冒泡排序(搅拌排序)"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items

def merge_sort(items, comp=lambda x, y: x <= y):
    """归并排序(分治法)"""
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    # print('*'*10)
    left = merge_sort(items[:mid], comp)
    # print('^'*10)
    right = merge_sort(items[mid:], comp)
    # print('#'*20)
    # print('left', left)
    # print('right', right)
    return merge(left, right, comp)


def merge(items1, items2, comp):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items

def seq_search(items, key):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1

prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}


if __name__ == '__main__':
    nums = [2, 3, 1, 8, 4, 9, 5, 6, 0, 7]
    # nums2 = select_sort(nums)
    # nums2 = bubble_sort(nums)
    nums2 = merge_sort(nums)
    # print(nums2)

    # num_index = seq_search(nums, 9)
    num_index = bin_search(nums2, 9)
    print(num_index)

    # 用股票价格大于100元的股票构造一个新的字典
    prices2 = {key: value for key, value in prices.items() if value > 100}
    print(prices2)

    # names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    # courses = ['语文', '数学', '英语']
    # # 录入五个学生三门课程的成绩
    # # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
    # # scores = [[None] * len(courses)] * len(names)
    # scores = [[None] * len(courses) for _ in range(len(names))]
    # for row, name in enumerate(names):
    #     for col, course in enumerate(courses):
    #         scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
    #         print(scores)




