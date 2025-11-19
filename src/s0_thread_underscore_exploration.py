import _thread
import time

def print_epoch(nameOfThread, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "------", time.time())