import os
import sys

def _build_array():
    return [0 for _ in range(0, 1000)]

class State:
    def __init__(self) -> None:
        self.banks = [_build_array(), _build_array(), _build_array(), _build_array(), _build_array()]
        if len(sys.argv) > 2:
            for i, char in enumerate(' '.join(sys.argv[1:])):
                self.banks[0][i] = ord(char)
            self.banks[0][i+1] = -1
        self.bank_index = 2
        self.cell_index = 0
        self.copied = None

    def __getitem__(self, i):
        return self.banks[self.bank_index][i]

    def copy(self) -> None:
        self.copied = self.banks[self.bank_index][self.cell_index]
    
    def paste(self) -> None:
        self.banks[self.bank_index][self.cell_index] = self.copied

    def inc_bank(self) -> None:
        self.bank_index += 1
    
    def dec_bank(self) -> None:
        self.bank_index -= 1

    def move_right(self) -> None:
        self.cell_index += 1

    def move_left(self) -> None:
        self.cell_index -= 1

    def inc(self) -> None:
        self.banks[self.bank_index][self.cell_index] += 1

    def dec(self) -> None:
        self.banks[self.bank_index][self.cell_index] -= 1 

    def origin_cell(self) -> None:
        self.cell_index = 0

    def zero_bank(self) -> None:
        self.banks[self.bank_index] = _build_array()

    def bank_stdout(self) -> None:
        out = ""
        for char in self.banks[self.bank_index]:
            if char == -1:
                break
            out += chr(char)
        sys.stdout.write(out)

    def call_bank(self) -> None:
        cmd = ""
        for char in self.banks[self.bank_index]:
            if char == -1:
                break
            cmd += chr(char)
        cmd = cmd.rstrip('\x00')
        os.system(cmd)

    def inc_current_bank(self) -> None:
        for _ in range(0, 1000):
            self.banks[self.bank_index][_] += 1

    def dec_current_bank(self) -> None:
        for _ in range(0, 1000):
            self.banks[self.bank_index][_] -= 1

    def inv_bank(self) -> None:
        for i, b in enumerate(self.banks[self.bank_index]):
            f = 0 - b
            self.banks[self.bank_index][i] = f

    def get_arg(self, index: int=0) -> int:
        index = self.cell_index + index
        return self.banks[1][index]

    def mul_cel(self) -> None:
        m = self.get_arg()
        self.banks[self.bank_index][self.cell_index] *= m

    def zero_cell(self) -> None:
        self.banks[self.bank_index][self.cell_index] = 0

    def stdout(self) -> None:
        sys.stdout.write(chr(self.banks[self.bank_index][self.cell_index]))

    def print_cell_num(self):
        sys.stdout.write(str(self.banks[self.bank_index][self.cell_index]))

    def print_bank_nums(self):
        sys.stdout.write(', '.join([str(x) for x in self.banks[self.bank_index]]))