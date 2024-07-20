import sys
from multiprocessing import Process, Value, current_process, RLock, Manager, Pipe, Queue, JoinableQueue, Pool
import logging
from random import randint
from time import sleep
​
logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)
​


# MULTIPROCESSING PACKAGE


class MyProcess(Process):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=None, target=None, name=None, daemon=None)
        self.args = args

    def run(self) -> None:
        logger.debug(self.args)


def worker(params):
    sleep(1)
    logger.debug(params)


if __name__ == '__main__':
    process_1 = MyProcess(args=("Pierwsze", "argumenty!"))
    process_2 = MyProcess(args=("Drugie", "argumenty!"))

    func_proc_1 = Process(target=worker, args=("Pierwsze argumenty funkcyjnie",))
    func_proc_2 = Process(target=worker, args=("Drugie argumenty funkcyjnie",))
    func_proc_3 = Process(target=worker, args=("Trzecie argumenty funkcyjnie",))

    process_1.start()
    process_2.start()

    func_proc_1.start()
    func_proc_2.start()
    func_proc_3.start()

    process_1.join()
    process_2.join()

    func_proc_1.join()
    func_proc_2.join()
    func_proc_3.join()

    logger.debug("End program")
    logger.debug(process_1.exitcode)
    logger.debug(func_proc_2.exitcode)
​



# SHARED MEMORY


from multiprocessing import Process, Value, RLock, current_process
from time import sleep
import logging
import sys

logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

def worker(val: Value):
    logger.debug(f"Started {current_process().name}")
    sleep(1)
    with val.get_lock():
        val.value += 1
    logger.debug(f"Done {current_process().name}")
    sys.exit(0)

if __name__ == '__main__':
    lock = RLock()
    value = Value('d', 10, lock=lock)
    pr1 = Process(target=worker, args=(value,))
    pr1.start()
    pr2 = Process(target=worker, args=(value,))
    pr2.start()

    pr1.join()
    pr2.join()

    print(value.value)
​

from multiprocessing.sharedctypes import Value, Array
from ctypes import Structure, c_double
​

class Point(Structure):
    _fields_ = [("x", c_double), ("y", c_double)]


def modify(num: Value, string: Array, points: Array):
    logger.debug(f"Started {current_process().name}")
    logger.debug(f"Change number: {num.value}")
    with num.get_lock():
        num.value **= 2
    logger.debug(f"Number changed to: {num.value}")
    logger.debug(f"Change string: {string.value}")
    with string.get_lock():
        string.value = string.value.upper()
    logger.debug(f"String changed to: {string.value}")
    with points.get_lock():
        for point in points:
            point.x **= 2
            point.y **= 2
    logger.debug(f"Done {current_process().name}")
​
​
if __name__ == '__main__':
    lock = RLock()
    number = Value(c_double, 1.5, lock=lock)
    string = Array('c', b'hello world', lock=lock)
    points = Array(Point, [(2, 5), (-10, -12), (-10, 10)], lock=lock)

    p1 = Process(target=modify, args=(number, string, points))
    p2 = Process(target=modify, args=(number, string, points))
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(number.value)
    print(string.value)
    print([(point.x, point.y) for point in points])
​



# RESOURCE MANAGER


from multiprocessing import Process, Manager, current_process
from random import randint
from time import sleep
import logging

def worker(delay, manager: Manager):
    name = current_process().name
    logger.debug(f"Started: {name}")
    sleep(delay)
    manager[name] = current_process().pid
    logger.debug(f"Done: {name}")


if __name__ == "__main__":
    with Manager() as manager:
        man_dict = manager.dict()
        processes = []
        for i in range(5):
            pr = Process(target=worker, args=(randint(1,5), man_dict))
            pr.start()
            processes.append(pr)

        for process in processes:
            process.join()
        print(man_dict)
​
​


# PIPE

from multiprocessing import Pipe, Process, current_process
from time import sleep
import sys
import logging


def worker(pipe: Pipe):
    name = current_process().name
    logger.debug(f"Started: {name}")
    val = pipe.recv()
    logger.debug(f" {name} received: {val}")
    sys.exit(0)

recipient1, sender1 = Pipe()
recipient2, sender2 = Pipe()

if __name__ == '__main__':
    worker_1 = Process(target=worker, args=(recipient1, ))
    worker_2 = Process(target=worker, args=(recipient2, ))

    worker_1.start()
    worker_2.start()

    sleep(3)

    sender1.send(100)
    sleep(1)
    sender2.send(200)

def worker(queue: Queue):
    name = current_process().name
    logger.debug(f"Started: {name}")
    while True:
        val = queue.get()
        logger.debug(f" {name} received: {val}")
        sleep(2)



# TASK QUEUE

from multiprocessing import Queue, Process, current_process
from time import sleep
import sys
import logging

q = Queue()

if __name__ == "__main__":
    worker_1 = Process(target=worker, args=(q,))
    worker_2 = Process(target=worker, args=(q,))

    worker_1.start()
    worker_2.start()

    sleep(1)

    q.put(4)
    sleep(1)
    q.put(8)
    q.put(16)
    sleep(1)
    q.put(32)

​
# JoinableQueue

def worker(queue: JoinableQueue):
    name = current_process().name
    logger.debug(f"Started: {name}")
    val = queue.get()
    logger.debug(f" {name} received: {val}")
    queue.task_done()
    sys.exit(0)

q = JoinableQueue()

if __name__ == "__main__":
    worker_1 = Process(target=worker, args=(q,))
    worker_2 = Process(target=worker, args=(q,))
    worker_3 = Process(target=worker, args=(q,))

    worker_1.start()
    worker_2.start()
    worker_3.start()

    sleep(1)

    q.put(4)
    sleep(1)
    q.put(8)
    sleep(1)
    q.put(16)
    q.join()
    logger.debug("Queue processed")
​



# concurrent.futures

from multiprocessing import Pool, current_process
import logging


def worker(value):
    logger.debug(f"Odpalam: {current_process().name} z wartością: {value}")
    sleep(1)
    return value ** 2


if __name__ == "__main__":
    with Pool(processes=10) as pool:
        logger.debug(pool.map(worker, range(10)))
​


from concurrent.futures import ProcessPoolExecutor
import math
​
​
POTENTIAL_PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]
​
​
def check_if_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
​
    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True
​
​
if __name__ == '__main__':
    with ProcessPoolExecutor(6) as executor:
        prime_statuses = executor.map(check_if_prime, POTENTIAL_PRIMES)
        for number, is_prime in zip(POTENTIAL_PRIMES, prime_statuses):
            if is_prime:
                logger.debug(f"{number} is prime")
            else:
                logger.debug(f"{number} is not prime")
​