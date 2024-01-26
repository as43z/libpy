# Getting started

This is the documentation for the `libpy` codebase.

## `strutils`

`strutils` provides some comfort operations for using strings.

What is inside `strutils`?

* `tokenizer`: A module that generates tokens from a string input.

### Tokenizer

```python
class Token:
    value: str
    cursor_range: tuple[int, int]
```
A token is a dataclass that represents a unit of a token.

* `value` is the value of the token, the stream of characters that represent it.
* `cursor_range`is a tuple containing the start and the end index position of that token.

---

```python
def tokenize(seq: str) -> Generator[Token, None, None]:
```

Generates tokens from an input string.

* `seq` is the input string.

