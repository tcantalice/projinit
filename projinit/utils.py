import os


def makedirs(path, *dirs):
    path = os.path.abspath(path)
    for dir in dirs:
        dir = os.path.join(path, dir)
        os.mkdir(dir)


def name_normalizer(name: str):
    is_ascii = name.isascii()
    is_empty = len(name) == 0

    if not is_ascii or is_empty:
        return False

    return name.strip().replace(' ', '_').lower()
