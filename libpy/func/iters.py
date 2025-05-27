import itertools
from typing import (
  Iterable,
  Callable,
  Optional,
  Any,
)

from libpy.generics import T

IterResult = tuple[Optional[Exception], Optional[T]]

def first(
  i: Iterable[T],
  cond: Callable[[T], bool] = lambda x: True
) -> IterResult[T]:
  """Returns the first item of the iterable that matches the conditional,
    otherwise returns the first element"""
  try:
    return None, next(filter(cond, i))
  except StopIteration:
    return None, None
  except Exception as e:
    return e, None

def apply(
  i: Iterable[T],
  fs: Iterable[Callable[[T], Any]] | Callable[[T], Any]
) -> IterResult[Iterable[Any]]:
  """Wrap over map() and return the exception and the resulting iterable."""
  fs = iter(fs if isinstance(fs, Iterable) else [fs])
  try:
    return None, map(lambda x: pipe(x, fs), fs)
  except Exception as e:
    return e, None

def pipe(
  x : Any,
  fs: Iterable[Callable[[Any], Any]] | Callable[[Any], Any]
) -> Any:
  """For an input X, apply all possible F's and return the final computation or an error."""
  fs = iter(fs if isinstance(fs, Iterable) else [fs])
  try:
    f = next(fs)
  except StopIteration:
    return x

  return pipe(f(x), fs)

def drop(
  i: Iterable[T],
  cond: Callable[[T], bool] = lambda x: False
) -> Iterable[T]:
  """Drop those items for which condition is true."""
  return filter(lambda x: not cond(x), i)