from libpy.ds.result import T, Result, Ok, Error
from typing import Callable, Any

def perform_op(op: Callable[[T, T], Result[T]], *args) -> Result[T]:
    if len(args) < 2:
        return Error("perform_op should always contain more than 1 argument.")
    
    # Unpack
    a = args[0]
    b: tuple[T, ...] = args[1:]

    if len(b) == 1:
        return op(a, b[0])
    
    return op(a, perform_op(op, *b).unwrap()[0])

def add (a: int, b: int) -> Result[int]:
    return Ok(a + b)

def pipeline(a: T, *funcs: Callable[[Any], Result[T]]) -> Result[T]:
    if len(funcs) < 1:
        return Error("pipeline requires more than one function.")
    
    if len(funcs) > 1:
        f = funcs[0]
        fp = funcs[1:]
        return pipeline(f(a).unwrap()[0], *fp)

    f = funcs[0]
    if not callable(f):
        return Error(f.__name__, "is not callable.") 

    return f(a) 

def capitalize(a: str) -> Result[str]:
    return Ok(a.capitalize())

def reverse(a: str) -> Result[str]:
    return Ok(a[::-1])

print(perform_op(add, 1, 2, 3, 4).unwrap())
print(pipeline("hello. world!", capitalize, reverse).unwrap())