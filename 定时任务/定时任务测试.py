import time

num = 0
def timer(n):
	"""每n秒执行一次"""
	while True:
		print(time.strftime('%Y-%m-%d %X', time.localtime()))
		global num
		num += 1
		print(f"执行次数==》{num}")  # 此处为要执行的任务
		time.sleep(n)

timer(2)