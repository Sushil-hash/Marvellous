import time

import schedule
def display():
    print("Namskar")

def main():
    schedule.every().day.at("09:00").do(display)
    while True:
        schedule.run_pending()
        time.sleep(1)

main()
