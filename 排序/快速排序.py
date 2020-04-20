def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        p = arr[0]
        less = [i for i in arr[1:] if i < p]
        big = [i for i in arr[1:] if i > p]
        return quicksort(less) + [p] + quicksort(big)


if __name__ == '__main__':
    list1 = [7, 3, 23, 6, 9, 10]
    res = quicksort(list1)
    print(res)

