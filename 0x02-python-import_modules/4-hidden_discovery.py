#!/usr/bin/python3
import dis
import types
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./4-hidden_discovery.py <compiled_module.pyc>")

    filename = sys.argv[1]

    with open(filename, 'rb') as file:
        code = compile(file.read(), filename, 'exec')

    names = set()
    for instr in dis.get_instructions(code):
        if instr.opcode == dis.opmap['STORE_NAME']:
            name = instr.argval
            if not name.startswith('__'):
                names.add(name)

    for name in sorted(names):
        print(name)
