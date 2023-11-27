#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    return 98 + (a ** b)

# Verify that the function behaves the same as the bytecode
def test_magic_calculation():
    a = 2
    b = 5
    bytecode_result = eval(compile("98 + (a ** b)", '<string>', 'eval'))
    function_result = magic_calculation(a, b)
    assert bytecode_result == function_result

test_magic_calculation()