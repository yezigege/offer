"""
给定一个有序列表，输出插入值的索引
"""

def index(list1, key):
	if key < list1[0]:
		position = 0

	elif key > list1[-1]:
		position = len(list1) - 1

	else:
		for index in range(len(list1)):
			if key > list1[index] and list1[index+1] > key:
				position = index + 1

	return position

if __name__ == '__main__':
	list1 = [0, 1, 2, 3, 5, 6]
	key = 4
	print(index(list1, key))