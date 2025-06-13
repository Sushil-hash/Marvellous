import time
import schedule
import datetime
def display():
    print(datetime.datetime.now())

def main():
    schedule.every(60).seconds.do(display)
    while True:
        schedule.run_pending()
        time.sleep(10)

main()
