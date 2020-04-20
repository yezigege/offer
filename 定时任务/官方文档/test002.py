from datetime import date
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

def my_job(text):
    print(text)


"""
date 在指定时间点触发任务

"""

# 在2019年12月5日执行
# sched.add_job(my_job, 'date', run_date=date(2009, 12, 5), args=['text'])

# datetime类型（用于精确时间） 在2019年11月6日 16:30:05执行
# sched.add_job(my_job, 'date', run_date=datetime(2019, 11, 6, 16, 30, 5), args=['text'])

# 文本类型
# sched.add_job(my_job, 'date', run_date='2019-12-05 16:15:00', args=['text'])


# 未显式指定，那么则立即执行
sched.add_job(my_job, args=['text'])


sched.start()