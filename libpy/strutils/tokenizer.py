"""
    Tokenizer, a string tokenizer processor
    
    Copyright (c) 2024 Albert Sáez
"""
from dataclasses import dataclass
from typing import Generator
import string

TOKENIZER_DEBUG=True

def __tokenizer_debug(*args, **kwargs):
    if not TOKENIZER_DEBUG: return
    prefix = kwargs['prefix'] if 'prefix' in kwargs else ''
    print(prefix, *args, end=kwargs['end'] if 'end' in kwargs else '\n') 

@dataclass
class Token:
    """
    A token is a sequence of one or more characters (string) that is found in a parent sequence of characters
    i.e. "I was driving a car" --> Token: I, Token: was, Token: driving ...
    
    value: str -- is the value of the token (the token itself)
    cursor_range: (int, int) -- is the index of the cursor in the parent line that is associated with the 
                                start and the end of the token. (start, end). 
    """
    value: str = ''
    cursor_range: tuple[int, int] = (0, 0) 

def tokenize_iter(seq: str) ->Generator[Token, None, None]:
    """
    Returns a generator of tokens that have been retrieved from the input sequence.
    
    seq: str -- The input sequence of characters
    """
    __tokenizer_debug(f'Got sequence: {seq}', prefix='[TOKENIZER_DEBUG]')
    n = len(seq)
    tmp = Token()
    for i, ch in enumerate(seq):
        if ch.isspace(): continue
        elif ch in string.punctuation: yield Token(ch, (i, i))
        elif ch in string.ascii_letters or ch in string.digits:
            if tmp.cursor_range == (0, 0): tmp.cursor_range = (i, 0)
            tmp.value += ch
            if i < n-1 and not seq[i+1].isspace() and not seq[i+1] in string.punctuation:
                continue
            tmp.cursor_range = (tmp.cursor_range[0], i)
            tk = tmp
            tmp = Token()
            yield tk
        else: yield Token()

def tokenize(seq: str) -> list[Token]:
    """
    Returns a list of tokens from an input string.
    
    seq: str -- The input sequence of characters
    """
    tokens = []
    for token in tokenize_iter(seq):
        tokens.append(token)

    return tokens
   
    
