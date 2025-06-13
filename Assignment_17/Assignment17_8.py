import time

import schedule

def mail_checking():
    print("Checking email")

def main():
    schedule.every(10).seconds.do(mail_checking)
    while True:
        schedule.run_pending()
        time.sleep(1)

main()