import subprocess
import schedule
import time

def run_script():
    subprocess.call(['python', './feitjesapicalls.py'])

# Plan het script om dagelijks om 9:10 uur uitgevoerd te worden
schedule.every().day.at("09:25").do(run_script)

while True:
    print("Heartbeat")
    schedule.run_pending()
    time.sleep(60)
