"""
注意参数顺序

class apscheduler.triggers.cron.CronTrigger(
year=None, 
month=None, 
day=None, 
week=None, 
day_of_week=None, 
hour=None, 
minute=None,
second=None, 
start_date=None, 
end_date=None, 
timezone=None, 
jitter=None)



当省略时间参数时，在显式指定参数之前的参数会被设定为*，之后的参数会被设定为最小值，
week 和day_of_week的最小值为*。比如，设定day=1, minute=20等同于设定year='*', month='*', day=1, 
week='*', day_of_week='*', hour='*', minute=20, second=0，即每个月的第一天，且当分钟到达20时就触发。
"""

from apscheduler.schedulers.blocking import BlockingScheduler

def job_function():
    print "Hello World"

sched = BlockingScheduler()

# 任务会在6月、7月、8月、11月和12月的第三个周五，00:00、01:00、02:00和03:00触发
# sched.add_job(job_function, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')


# 在2020-05-30 00:00:00前，每周一到每周五 5:30运行
sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2020-05-30')





sched.start()