"""快速排序"""


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        p = arr[0]
        less = [x for x in arr[1:] if x < p]
        big = [x for x in arr[1:] if x > p]
        return quicksort(less) + [p] + quicksort(big)


if __name__ == '__main__':
    list1 = [4, 2, 9, 7, 8, 3, 1, 0, 2, 5]
    res = quicksort(list1)
    print(res)