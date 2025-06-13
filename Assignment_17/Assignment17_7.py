import time

import schedule
import datetime
logfile = open("backup_log.txt","w")
logfile.write("This file contains log of file backup")
logfile.close()

def backup():
    t = datetime.datetime.now()
    print("Taking a file backup")
    lf = open("backup_log.txt","a")
    content = str(t) + " : Backup taken \n"
    lf.write(content)
    lf.close()

def main():
    schedule.every(1).seconds.do(backup)
    while True:
        schedule.run_pending()
        time.sleep(1)

main()


