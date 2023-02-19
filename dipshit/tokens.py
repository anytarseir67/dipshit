from .exceptions import UnknownChar, InvalidSyntax
from typing import List

def find_match(s: str, start: str, end: str):
    toret = {}
    pstack = []

    for i, c in enumerate(s):
        if c == start:
            pstack.append(i)
        elif c == end:
            if len(pstack) == 0:
                return
            toret[pstack.pop()] = i

    if len(pstack) > 0:
        return

    return toret

class Token:
    """base class all tokens should derive from
    """
    def __init__(self) -> None:
        pass

class NextBank(Token):
    ...

class PreviousBank(Token):
    ...

class MoveLeft(Token):
    ...

class MoveRight(Token):
    ...

class Add(Token):
    ...

class Subtract(Token):
    ...

class Origin(Token):
    ...

class PrintCell(Token):
    ...

class ZeroBank(Token):
    ...

class InvertBank(Token):
    ...

class PrintBank(Token):
    ...

class CallBank(Token):
    ...

class IncrementBank(Token):
    ...

class DecrementBank(Token):
    ...

class Loop(Token):
    def __init__(self, tokens: List[Token]) -> None:
        self.tokens = tokens

class Multiply(Token):
    ...

class ZeroCell(Token):
    ...

class PrintCellAsNum(Token):
    ...

class PrintBankAsNums(Token):
    ...

class Copy(Token):
    ...

class Paste(Token):
    ...

class Conditional(Token):
    def __init__(self, tokens: List[Token]) -> None:
        self.tokens = tokens

class Break(Token):
    ...

class Pointer(Token):
    ...

class Nop(Token):
    ...

class Tokenizer:
    def __init__(self) -> None:
        self.tokens_to_skip = 0
        self.comment_len = 0

    def tokenize(self, code: str) -> List[Token]:
        tokens = []
        for i, char in enumerate(code):
            if self.tokens_to_skip > 0:
                self.tokens_to_skip -= 1
                continue

            if self.comment_len > 0:
                self.comment_len -= 1
                continue

            match char:
                case '`':
                    tokens.append(NextBank())
                case '~':
                    tokens.append(PreviousBank())
                case '<':
                    tokens.append(MoveLeft())
                case '>':
                    tokens.append(MoveRight())
                case '+':
                    tokens.append(Add())
                case '-':
                    tokens.append(Subtract())
                case '|':
                    tokens.append(Origin())
                case '#':
                    tokens.append(PrintCell())
                case '%':
                    tokens.append(ZeroBank())
                case '!':
                    tokens.append(InvertBank())
                case '@':
                    tokens.append(PrintBank())
                case '^':
                    tokens.append(CallBank())
                case '*':
                    tokens.append(IncrementBank())
                case '$':
                    tokens.append(DecrementBank())
                case '[':
                    end = find_match(code[i:], '[', ']')[0]
                    _cloop = code[i+1:i+end]
                    tokens.append(Loop(self.tokenize(_cloop)))
                    self.tokens_to_skip = end
                case '?':
                    tokens.append(Multiply())
                case '.':
                    tokens.append(ZeroCell())
                case '\'':
                    tokens.append(PrintCellAsNum())
                case '"':
                    tokens.append(PrintBankAsNums())
                case '=':
                    tokens.append(Copy())
                case ':':
                    tokens.append(Paste())
                case '_':
                    tokens.append(Nop())
                case ';':
                    self.comment_len = code[i:].index('\n')
                case '{':
                    end = find_match(code[i:], '{', '}')[0]
                    _cloop = code[i+1:i+end]
                    tokens.append(Conditional(self.tokenize(_cloop)))
                    self.tokens_to_skip = end
                case '&':
                    tokens.append(Break())
                case '\\':
                    tokens.append(Pointer())
                case ' ':
                    continue
                case '\n':
                    continue
                case _:
                    raise UnknownChar(char)
        return tokens