### 带定长参数的装饰器


def new_func(func):
	def wrapped(username, password):
		if username == 'root' and password == '123456':
			print('验证通过!')
			print('开始执行附加功能')
			return func()
		else:
			print('用户名或密码错误')
			return 

	return wrapped


@new_func
def origin():
	print('开始执行函数...')


if __name__ == '__main__':
	origin('root', '123456')