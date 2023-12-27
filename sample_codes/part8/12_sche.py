import schedule
import time

def job():
    print("執行一次"+time.ctime())

schedule.every().seconds.do(job)
# schedule.every(5).seconds.do(job)
# schedule.every().minutes.do(job)
# schedule.every().hours.do(job)
# schedule.every().days.do(job)
# schedule.every().weeks.do(job)

while(True):
    schedule.run_pending()
    
schedule.clear()  # 將排程移除 