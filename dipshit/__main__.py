import sys
import os
from .interp import Interpreter
from .repl import main as repl_main

def main():
    if len(sys.argv) > 1:
        if os.path.isfile(sys.argv[1]):
            with open(sys.argv[1], 'r') as f:
                Interpreter().run(f.read())
        return
    repl_main()

if __name__ == "__main__":
    main()
    