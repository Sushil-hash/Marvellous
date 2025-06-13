import time
import schedule
def display():
    print("Do Coding")

def main():
    schedule.every(30).minutes.do(display)
    while True:
        schedule.run_pending()
        time.sleep(60)

main()