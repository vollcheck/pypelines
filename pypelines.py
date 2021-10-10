from pprint import pprint
from types import FunctionType

from bytecode import Bytecode, Instr, SetLineno


REPLACEMENT = {
    'BINARY_OR': 'CALL_FUNCTION'
}


def pypeline(where):
    if isinstance(where, FunctionType):
        where.__code__ = patch_code(where.__code__)
        return where


def patch_code(code):
    bytecode = Bytecode.from_code(code)

    # set line other way
    new_bytecode = []

    # ROT_TWO simulation
    new_bytecode.append(bytecode.pop(0))
    new_bytecode.insert(0, bytecode.pop(0))

    for instr in bytecode:
        if instr.name in REPLACEMENT:
            new_bytecode.append(Instr(REPLACEMENT.get(instr.name), 1, lineno=instr.lineno))
        else:
            new_bytecode.append(instr)

    bytecode.clear()
    bytecode.extend(new_bytecode)

    pprint(bytecode)

    return bytecode.to_code()


def add_two(x):
    return x + 2


@pypeline
def test_desired(x):
    return x | add_two


# @pipeline
def test_current(x):
    return add_two(x)


print(test_desired(5))

# [<LOAD_FAST arg='x' lineno=25>,
#  <LOAD_GLOBAL arg='add_two' lineno=25>,
#  <BINARY_OR lineno=25>,
#  <RETURN_VALUE lineno=25>]

# [<LOAD_GLOBAL arg='add_two' lineno=30>,
#  <LOAD_FAST arg='x' lineno=30>,
#  <CALL_FUNCTION arg=1 lineno=30>,
#  <RETURN_VALUE lineno=30>]

# Needed steps:
# 1. ROT_TWO - we need to rotate top two elements on stack
# 2. replace BINARY_OR with CALL_FUNCTION
