"""
interval 周期触发任务
"""

from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

def job_function():
    print("Hello World")

sched = BlockingScheduler()


"""
hours=2 每两小时触发
"""

# 每2秒触发
# sched.add_job(job_function, 'interval', seconds=2)

# 周期触发的时间范围在2010-10-10 9:30 至 2014-06-15 11:00
# sched.add_job(job_function, 'interval', seconds=2, start_date='2019-12-05 16:22:00', end_date='2019-12-15 11:00:00')



# jitter振动参数，给每次触发添加一个随机浮动秒数，一般适用于多服务器，避免同时运行造成服务拥堵。
# 每小时（上下浮动3秒区间内）运行`job_function`
sched.add_job(job_function, 'interval', seconds=1, jitter=3)


sched.start()

# 通过装饰器实现  ==> 20191205 162400 测试不成功
# @sched.scheduled_job('interval', id='my_job_id', seconds=2)
# def job_function():
#     print("Hello World")


