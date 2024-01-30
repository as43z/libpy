# Getting started

This is the documentation for the `libpy` codebase.

## `array`

TODO

## `ds`

`ds` provides some datastructures right available to use.

What is inside `ds`?

* `tree`: A module that has tools and classes for creating trees.

### Tree

```python
class GTNode:
    parent: GTNode | None
    children: list[GTNode]
    hash: in
```

* `parent` is the parent node of that corresponding GTNode. In case it is None, then it means it is the root of a General Tree.
* `children` is the list containing the spanning GTNodes from that tree. 
* `hash` is the hash of the object (perhaps can work as an ID).


```python
def repr_gt_node(node: GTNode, indent_level: int = 0, span: bool = True):
```

Represent a node in the Generic Tree.

* `node`: GTNode -- Generic Tree Node to represent. (It will also represent the children nodes)
* `indent_level`: int -- For representing in a prettier way.
* `span`: bool -- Represent the children of the node.

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

