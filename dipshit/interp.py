from .state import State
from .tokens import Tokenizer, Token
from .tokens import NextBank, PreviousBank, MoveLeft, MoveRight, Add, Subtract, Origin, PrintCell, ZeroBank, InvertBank, PrintBank, CallBank, IncrementBank, DecrementBank, Loop, Multiply, ZeroCell, PrintCellAsNum, PrintBankAsNums, Nop
from .exceptions import InvalidSyntax
from typing import List

class Interpreter:
    def __init__(self, code: str=None) -> None:
        self.state = State()
        self.tokenizer = Tokenizer()
        self.code = code

    def run(self, code: str=None) -> None:
        if not code:
            code = self.code
        tokens = self.tokenizer.tokenize(code)
        self.loop(tokens)

    def loop(self, code: List[Token]):
        for char in code:
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
                    for _ in range(self.state.get_arg()):
                        self.loop(char.tokens)
                case Multiply():
                    self.state.mul_cel()
                case ZeroCell():
                    self.state.zero_cell()
                case PrintCellAsNum():
                    self.state.print_cell_num()
                case PrintBankAsNums():
                    self.state.print_bank_nums()
                case Nop():
                    continue
                case '\n':
                    continue
                case _:
                    raise InvalidSyntax()