import random
import pyautogui as pg
import time
animals = ('monke', 'donkey', 'dog')
time.sleep(8)

for i in range(69):
    a = random.choice(animals)
    pg.write("you are a"+a)
    pg.press('enter')

# Now open chat in your web browser and run the code
