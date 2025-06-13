import time

import schedule

def lunch():
    print("Lunch Time")

def wrap():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(lunch)
    schedule.every().day.at("18:00").do(wrap)
    while True:
        schedule.run_pending()
        time.sleep(1)

main()
