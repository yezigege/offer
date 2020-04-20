import time
from apscheduler.schedulers.blocking import BlockingScheduler

scheduler = BlockingScheduler()

@scheduler.scheduled_job('cron', second='*/5')
def request_update_status():
    print('当前时间===>', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print('Doing job')

scheduler.start()