from re import L


class DipShitError(Exception):
    """
    base class all exceptions should derive from
    """
    ...

class EmptyClipboard(DipShitError):
    def __init__(self) -> None:
        super().__init__("cannot paste when clipboard is empty")

class InvalidSyntax(DipShitError):
    def __init__(self) -> None:
        super().__init__(f"invalid syntax")

class UnknownChar(DipShitError):
    def __init__(self, char: str) -> None:
        super().__init__(f"Unknown character `{char}`")

class UnexpectedArgument(DipShitError):
    def __init__(self, cell, index) -> None:
        super().__init__(f"unexpected argument {cell} at {index}")
