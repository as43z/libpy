from __future__ import annotations
from typing import Iterable, Callable 
from queue import Queue
# import operator # Unused but maybe will be used later


class LazyBuffer: 
    __slots__ = ('shape', 'dtype', 'ops', '_initial_state')
    def __init__(self):
        self.shape = (0,)
        self.dtype = None
        self.ops = Queue()
        self._initial_state = None

    """
    Return lazy buffer from an initial state (a list) perhaps.
    """
    @classmethod
    def from_iter(cls, iter: Iterable):
        x = cls()
        x._initial_state = iter
        return x

    def op(self, f: Callable, args = None):
        self.ops.put((f, args))

    """
    'Collects' or rather, evaluates the operations in the operation queue.
    """
    def collect(self):
        if self._initial_state == None:
            raise Exception("LazyBuffer has no initial state. Before collecting please add an initial state.")
        x = self._initial_state
        while not self.ops.empty():
            f, args = self.ops.get()
            if args:
                x = f(x, args)
            else:
                x = f(x)
        return x
    
    @property
    def size(self):
        s = 1
        for l in self.shape:
            s *= l
        return s

