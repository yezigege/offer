# 同时带不定长、关键字参数的装饰器

def new_func(func):
	def wrapped(*args, **kwargs):
		if args:
			counts = len(args)

			print('本系统包含: ', end='')
			for arg in args:
				print(arg, end=' ')

			print('等', counts, '部分')

			if kwargs:
				for k in kwargs:
					v = kwargs[k]
					print(k, '为: ', v)

			return func()
		else:
			if kwargs:
				for k in kwargs:
					v = kwargs[k]
					print(k, '为: ', v)
			return func()


	return wrapped


@new_func
def origin():
	print('开始执行函数...')


if __name__ == '__main__':
	# origin('硬件','软件','用户数据',总用户数=5,系统版本='CentOS 7.4')
	origin(总用户数=5, 系统版本='CentOS 7.4')