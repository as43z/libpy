from __future__ import annotations
from typing import Iterable, Callable 
from queue import Queue
# import operator # Unused but maybe will be used later

class LazyBuffer: 
    """
    A lazy evaluated buffer of operations and items.
    """
    __slots__ = ('shape', 'dtype', 'ops', '_initial_state')
    def __init__(self):
        self.shape = (0,)
        self.dtype = None
        self.ops = Queue()
        self._initial_state = None

    @classmethod
    def from_iter(cls, iter: Iterable):
        """
        Return lazy buffer from an initial state (a list) perhaps.
        """
        x = cls()
        x._initial_state = iter
        return x

    def op(self, f: Callable, args = None):
        self.ops.put((f, args))

    def collect(self):
        """
        'Collects' or rather, evaluates the operations in the operation queue.
        """
        if self._initial_state is None:
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

