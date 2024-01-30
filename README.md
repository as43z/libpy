# libpy

**libpy** is a custom library developed for testing and custom purposes.
All of the code present in this codebase is not recomended for production,
and under no circumstance I make myself accountable for nefarious nor
missuse of this code.

## What does this codebase include?

- `strutils` is utility code for string related utility. It comes with a 
    tokenizer.
- `ds` is utility code for generating data structures. It comes with a tree
module.
- `array` is utility code for array related utility. It comes with a LazyBuffer.

More to come.

## How to use?

Refer to each module to understand how to use it. Consult the [docs](docs/)

## TODO

- [ ] Better GTNode representation. Should return a string containing the node
minimum representation: the hash, the parent's hash and the hashes of the
children nodes.

- [ ] LazyBuffer is somewhat faster (right now only 1.005x LOL). This structure
is incredible simple at the moment. Quite stupid to be fair.

- [ ] LazyBuffer compatible with Numpy or any type of Iterable that can be used
i operations such as `__add__`, `__sub__`, ... .

