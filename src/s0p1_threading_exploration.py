import threading 
import time 

### PART 1 ####

def print_epoch(nameOfThread, delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(nameOfThread, "------", time.time())


def print_cube(x):
    print(f"Cube is {x*x*x}")

def print_square(x):
    print(f"Square is {x*x}")

### PART 2 ###

class MyThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print(f"start {self.name} thread")
        print_epoch(self.name, self.delay)
        print(f"end {self.name} thread")


if __name__=="__main__":
    # ### PART 1 ###
    # # create threads
    # # t1 = threading.Thread(target=print_epoch,args=("thread 1",1))
    # # t2 = threading.Thread(target=print_epoch,args=("thread 2",2))
    # t1 = threading.Thread(target=print_cube,args=(2,))
    # t2 = threading.Thread(target=print_square,args=(2,))
    # # start threads
    # t1.start()
    # t2.start()
    # # wait until threads are done
    # t1.join()
    # t2.join()
    ### PART 2 ###
    t1 = MyThread("thread-1", 1)
    t2 = MyThread("thread-2", 2)
    t1.start()
    t2.start()
    print(t1.name)
    print(t2.name)
    print(threading.active_count())
    print(threading.current_thread())
    print(threading.enumerate())
    t1.join()
    t2.join()
    # print done!
    print("All done!")