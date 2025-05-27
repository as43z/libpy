from abc import abstractmethod
from typing import (
    Generic,
    TypeVar,
    Union,
    Tuple,
    Protocol,
    runtime_checkable
)

from libpy.generics import T

@runtime_checkable
class Unwrappable(Protocol[T]):
    """
    Unwrappables are objects that implement the .unwrap() function. This
    function is part of the lazy evaluation of the Result chain.
    """
    @abstractmethod
    def unwrap(self) -> T: ...

class Error(Unwrappable):
    """
    Represents an error in the execution of a program.

    :params args: Variadic arguments for printing during raise.
    """
    def __init__(self, *args):
        self.container = args
    
    def unwrap(self):
        """
        Raise an error with the arguments supplied during creation.
        """
        raise Exception(*self.container)

class Ok(Unwrappable, Generic[T]):
    """
    Represents an error in the execution of a program.

    :params args : Variadic arguments that are part of the executable pipeline.
    """
    def __init__(self, *args):
        super().__init__()
        self.container: Tuple[T] = args
    
    def unwrap(self) -> Tuple[T, ...]:
        """
        Unwraps the execution of the program.
        :returns: a Tuple[T, ...] of arguments of the operation.
        """
        return self.container

"""
Result unions the Error or the Ok of an execution.
"""
Result = Union[Error, Ok[T]]