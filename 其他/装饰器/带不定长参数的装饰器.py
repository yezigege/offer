### 带不定长参数的装饰器


def new_func(func):
	def wrapped(*args):
		# print(*args, type(args), args)  # 硬件 软件 用户数据 <class 'tuple'> ('硬件', '软件', '用户数据')
		if args:
			counts = len(args)
			print('本系统包含: ', end='')
			for arg in args:
				print(arg, '', end='')
			print('等', counts, '部分')
			return func()
		else:
			print('用户名或密码错误')
			return func()

	return wrapped


@new_func
def origin():
	print('开始执行函数...')


if __name__ == '__main__':
 	 origin('硬件', '软件', '用户数据')