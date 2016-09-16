import time
from threading import Thread
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)

t = Thread(target=countdown, args=(10, ), daemon = True)
t.start()
# t.join()
if t.is_alive():
    print('Still running')
    time.sleep(2)
else:
    print('Comleted')

if t.is_alive():
    print('Still running')
    time.sleep(2)
else:
    print('Comleted')