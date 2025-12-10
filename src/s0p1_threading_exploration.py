import threading 
import time 


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


if __name__=="__main__":
    # create threads
    # t1 = threading.Thread(target=print_epoch,args=("thread 1",1))
    # t2 = threading.Thread(target=print_epoch,args=("thread 2",2))
    t1 = threading.Thread(target=print_cube,args=(2,))
    t2 = threading.Thread(target=print_square,args=(2,))
    # start threads
    t1.start()
    t2.start()
    # wait until threads are done
    t1.join()
    t2.join()
    # print done!
    print("All done!")