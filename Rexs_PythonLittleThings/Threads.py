Proces a wątek, IO bound/CPU bound, GIL

from concurrent.futures import ThreadPoolExecutor
from threading import Barrier, Condition, Event, Thread, Timer, RLock, Semaphore
import logging
from time import sleep, time


# klasa Thread, dziedziczenie, a klasowy i funkcyjny argument konstruktora

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s %(message)s')


class MySleepingThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self) -> None:
        logging.debug("ODPALAM SIĘ!")
        sleep(2)
        logging.debug("OBUDZIŁEM SIĘ!")
        logging.debug(f"args: {self.args}")



for i in range(10):
    thread = MySleepingThread(args=(f"Odpalony jako {i}",))
    thread.start()
print("SKOŃCZYŁEM WYKONYWAĆ GŁÓWNY KOD PROGRAMU")
 
 
class MyCustomClass:
    def __init__(self, delay: int):
        self.delay = delay

    def __call__(self):
        logging.debug("Idę spać, narka!")
        sleep(self.delay)
        logging.debug("Pobudka!")

def go_to_sleep_for(delay_time):
    logging.debug("Idę spać, narka!")
    sleep(delay_time)
    logging.debug("Pobudka!")


# metody join(), is_alive()

thread = Thread(target=go_to_sleep_for, args=(3,))
thread.start()
thread_2 = Thread(target=go_to_sleep_for, args=(2,))
thread_2.start()

while True:
    sleep(1)
    if thread.is_alive():
        print("thread wciąż sobie pracuje")
    if thread_2.is_alive():
        print("thread_2 wciąż sobie pracuje")

# klasa TIMER

def say_hi():
    logging.debug("Hi!")

timers = [Timer(i+1, say_hi) for i in range(10)]

logging.debug("Odpalam tajmery!")
for timer in timers:
    timer.start()

timers[6].cancel()

print("koniec programu!")


# klasa Lock/RLock

def do_something(lock, delay):
    print("Zacząłem!")
    sleep(2)
    print("ale pospałem!")
    start_time = time()
    with lock:
        sleep(delay)
    logging.debug(f"Done in {time() - start_time}")


lock = RLock()
threads = [Thread(target=do_something, args=(lock, 2)) for _ in range(10)]
for thread in threads:
    thread.start()
logging.debug("Started")


# klasa Semaphore

def do_something(semaphore, delay):
    print("Zacząłem!")
    sleep(2)
    print("ale pospałem!")
    start_time = time()
    with semaphore:
        sleep(delay)
    logging.debug(f"Done in {time() - start_time}")


semaphore = Semaphore(5)
threads = [Thread(target=do_something, args=(semaphore, 2)) for _ in range(10)]
for thread in threads:
    thread.start()
logging.debug("Started")


# klasa Condition

def worker(condition: Condition):
    logging.debug('Worker ready to work')
    with condition:
        condition.wait()
        logging.debug('The worker can do the work')


def boss(condition: Condition, wielding_job_condition: Condition):
    logging.debug("Boss is ready, but drinking coffee")
    sleep(2)
    with (condition, wielding_job_condition):
        logging.debug("Boss is ordering his workers to do work!")
        wielding_job_condition.notify()
        sleep(2)
        condition.notify(n=2)
        sleep(2)
        condition.notify()


condition = Condition()
wielding_job_condition = Condition()

worker_one = Thread(name='worker_one', target=worker, args=(condition,))
worker_two = Thread(name='worker_two', target=worker, args=(condition,))
worker_three = Thread(name='worker_three', target=worker, args=(wielding_job_condition,))
worker_four = Thread(name='worker_four', target=worker, args=(condition,))
boss = Thread(name="boss", target=boss, args=(condition, wielding_job_condition))
worker_one.start()
worker_two.start()

worker_three.start()

worker_four.start()
boss.start()


# klasa Event

def worker(event: Event):
    logging.debug('Worker ready to work')
    event.wait()
    logging.debug('The worker can do the work')


def boss(event: Event):
    logging.debug("Boss is ready, but drinking coffee")
    sleep(2)
    logging.debug("Boss is ordering his workers to do work!")
    event.set()

event = Event()
worker_one = Thread(name='worker_one', target=worker, args=(event,))
worker_two = Thread(name='worker_two', target=worker, args=(event,))
boss = Thread(name="boss", target=boss, args=(event,))
boss.start()
worker_one.start()
worker_two.start()

# klasa Barrier

def worker(barrier: Barrier, delay: int):
    logging.debug('Worker ready to work')
    sleep(delay)
    logging.debug("jestem gotowy wykonać zadanie!")
    barrier.wait()
    logging.debug('The worker can do the work')

barrier = Barrier(2)

worker_one = Thread(name='worker_one', target=worker, args=(barrier, 1))
worker_two = Thread(name='worker_two', target=worker, args=(barrier, 3))
worker_three = Thread(name='worker_three', target=worker, args=(barrier, 2))
worker_four = Thread(name='worker_four', target=worker, args=(barrier, 4))
worker_one.start()
worker_two.start()
worker_three.start()
worker_four.start()

# thread pools

def worker(number: int):
    logging.debug('Worker ready to work')
    sleep(2)
    logging.debug('The worker can do the work')
    return f"I was a worker number {number}!"


with ThreadPoolExecutor(max_workers=20) as executor:
    results = list(executor.map(worker, list(range(100))))
logging.debug(results)