class DipShitError(Exception):
    """
    base class all exceptions should derive from
    """
    ...

class InvalidSyntax(DipShitError):
    def __init__(self) -> None:
        super().__init__(f"invalid syntax")

class UnknownChar(DipShitError):
    def __init__(self, char: str) -> None:
        super().__init__(f"Unknown character `{char}`")
