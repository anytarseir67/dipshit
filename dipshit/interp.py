from .state import State
from .tokens import Tokenizer, Token
from .tokens import NextBank, PreviousBank, MoveLeft, MoveRight, Add, Subtract, Origin, PrintCell, ZeroBank, InvertBank, PrintBank, CallBank, IncrementBank, DecrementBank, Loop, Multiply, ZeroCell, PrintCellAsNum, PrintBankAsNums, Copy, Paste, Conditional, Break, Pointer, Nop
from .exceptions import InvalidSyntax, EmptyClipboard, UnexpectedArgument
from typing import List

class Interpreter:
    def __init__(self, code: str=None) -> None:
        self.state = State()
        self.tokenizer = Tokenizer()
        self.code = code
        self.loop_nest = 0
        self.loop_break = 0

    def run(self, code: str=None) -> None:
        if not code:
            code = self.code
        tokens = self.tokenizer.tokenize(code)
        self.loop(tokens)

    def loop(self, code: List[Token]):
        for char in code:
            if self.loop_break > 0:
                self.loop_break -= 1
                break
            match char:
                case NextBank():
                    self.state.inc_bank()
                case PreviousBank():
                    self.state.dec_bank()
                case MoveLeft():
                    self.state.move_left()
                case MoveRight():
                    self.state.move_right()
                case Add():
                    self.state.inc()
                case Subtract():
                    self.state.dec()
                case Origin():
                    self.state.origin_cell()
                case PrintCell():
                    self.state.stdout()
                case ZeroBank():
                    self.state.zero_bank()
                case InvertBank():
                    self.state.inv_bank()
                case PrintBank():
                    self.state.bank_stdout()
                case CallBank():
                    self.state.call_bank()
                case IncrementBank():
                    self.state.inc_current_bank()
                case DecrementBank():
                    self.state.dec_current_bank()
                case Loop():
                    self.loop_nest += 1
                    arg = self.state.get_arg()
                    if arg == 0:
                        while True:
                            if self.loop_break > 0:
                                self.loop_break -= 1
                            self.loop(char.tokens)
                    elif arg > 0:
                        for _ in range():
                            self.loop(char.tokens)
                    else:
                        raise UnexpectedArgument(arg, self.state.cell_index)
                    self.loop_nest -= 1
                case Multiply():
                    self.state.mul_cel()
                case ZeroCell():
                    self.state.zero_cell()
                case PrintCellAsNum():
                    self.state.print_cell_num()
                case PrintBankAsNums():
                    self.state.print_bank_nums()
                case Copy():
                    self.state.copy()
                case Paste():
                    if self.state.copied == None:
                        raise EmptyClipboard()
                    self.state.paste()
                case Conditional():
                    val = self.state.get_arg()
                    cell = self.state.get_arg(-1)
                    cell = self.state.banks[self.state.bank_index][cell]
                    _type = self.state.get_arg(-2)
                    if _type == 0:
                        if val == cell:
                            self.loop(char.tokens)
                    elif _type == 1:
                        if val != cell:
                            self.loop(char.tokens)
                    elif _type == 2:
                        if val > cell:
                            self.loop(char.tokens)
                    elif _type == 3:
                        if val < cell:
                            self.loop(char.tokens)
                    else:
                        raise UnexpectedArgument(_type, self.state.cell_index-2)
                case Break():
                    #TODO: doesn't work :|
                    arg = self.state.get_arg()
                    if arg != 0:
                        self.loop_break += self.loop_nest
                    else:
                        self.loop_break += 1
                case Pointer():
                    self.state.copied = self.state.cell_index
                case Nop():
                    continue
                case '\n':
                    continue
                case _:
                    raise InvalidSyntax()