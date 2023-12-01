#!/usr/bin/python3
import importlib.util

def get_names_from_pyc_file(file_path):
    spec = importlib.util.spec_from_file_location("hidden_module", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return [name for name in dir(module) if not name.startswith('__')]

if __name__ == "__main__":
    file_path = "hidden_4.pyc"
    names = get_names_from_pyc_file(file_path)
    names.sort()

    for name in names:
        print(name)
