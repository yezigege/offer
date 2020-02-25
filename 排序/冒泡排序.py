"""冒泡排序"""
def bubble_sort(alist):
	for j in range(len(alist)-1, 0, -1):
		for i in range(j):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]


if __name__ == '__main__':
	data = [4, 2, 9, 7, 8, 3, 1, 0, 2, 5]
	bubble_sort(data)
	print(data)