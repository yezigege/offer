import time
from pymongo import MongoClient
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.mongodb import MongoDBJobStore

def job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    
if __name__ == '__main__':
    # mongodb存储job
    scheduler = BlockingScheduler()
    client = MongoClient(host='127.0.0.1', port=27017)
    store = MongoDBJobStore(collection='job', database='test', client=client)
    scheduler.add_jobstore(store)
    scheduler.add_job(job, 'interval', second=5)
    scheduler.start()