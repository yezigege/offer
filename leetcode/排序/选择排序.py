def findsmallest(arr):
    min = arr[0]
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_index = i
    return min_index


def choice(array):
    newArr = []
    for i in range(len(array)):
        smallest = findsmallest(array)
        print(smallest)
        newArr.append(array.pop(smallest))
    return newArr


if __name__ == '__main__':
    list1 = [7, 3, 23, 6, 9, 10]
    res = choice(list1)
    print(res)