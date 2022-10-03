from .interp import Interpreter
from . import __version__

class Repl(Interpreter):
    def run(self, code: str=None) -> None:
        super().run(code)
        print(f'\nbank `{self.state.bank_index}`, cell `{self.state.cell_index}` = '+str(self.state.banks[self.state.bank_index][self.state.cell_index]))

def main():
    interp = Repl()
    print(f"DipShit v{__version__}")
    while True:
        try:
            line = input('|>    ')
            if line == "exit":
                break
            while True:
                n = input('...  ')
                if n == '':
                    break
                line += n
            if "exit" in line:
                break
            interp.run(line)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()