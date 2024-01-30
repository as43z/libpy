from libpy.array.lazybuffer import LazyBuffer
from typing import Iterator
import numbers
import time

def add(x, off):
    if not getattr(x, '__iter__'):
        raise Exception("Received %s not an Iterator." % type(x).__name__)

    nm = [0]*len(x)
    for i, el in enumerate(x):
        if isinstance(el, numbers.Number):
          nm[i] = el+off  
    return nm

def mult(x):
    if not getattr(x, '__iter__'):
        raise Exception("Received %s not an Iterator." % type(x).__name__)

    y = 1
    for el in x:
        if isinstance(el, numbers.Number):
            # For some reason my pyright is complaining about this line below.
            # I don't understand why. Typing is hard I guess.
            y *= el
    return y

n = [x**2 for x in range(100_000)] 
buff = LazyBuffer().from_iter(n)

t1 = time.time()
n = add(n, 5)
z = mult(n)
t2 = time.time()
print("Non lazy:", t2-t1)

t1 = time.time()
buff.op(add, 5)
buff.op(mult)

a = buff.collect()
t2 =time.time()
print("lazy:", t2-t1)
