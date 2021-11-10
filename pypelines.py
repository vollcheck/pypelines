from pprint import pprint
from types import FunctionType
from typing import Callable, TypeVar

from bytecode import Bytecode, Instr

T = TypeVar("T")


def pypeline(debug: bool = False) -> Callable:
    def wrapper(where: Callable[..., T]) -> Callable[..., T]:
        assert isinstance(
            where, FunctionType
        ), "Pypelines works best with the functions ;)"
        where.__code__ = patch_code(where.__code__, debug)
        return where

    return wrapper


def patch_code(code: T, debug: bool = False) -> Bytecode:
    # Interestingly enough, code is evaluated immediately
    # in the decorator, just like a macro :P

    bytecode = Bytecode.from_code(code)
    new_bytecode = []

    if debug:
        print("Received bytecode: ")
        pprint(bytecode)

    for instr in bytecode:
        if isinstance(instr, Instr) and instr.name == "BINARY_OR":
            new_instrs = [
                Instr("ROT_TWO", lineno=instr.lineno),
                Instr("CALL_FUNCTION", 1, lineno=instr.lineno),
            ]
            new_bytecode += new_instrs

            # Prettier but slower way:
            # new_bytecode.append(Instr("ROT_TWO", lineno=instr.lineno))
            # new_bytecode.append(Instr("CALL_FUNCTION", 1, lineno=instr.lineno))
        else:
            new_bytecode.append(instr)

    bytecode.clear()
    bytecode.extend(new_bytecode)

    if debug:
        print("\nChanged bytecode: ")
        pprint(bytecode)

    return bytecode.to_code()
