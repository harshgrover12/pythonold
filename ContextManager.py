# Using class
import os


class OpenFile:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile('sample.txt', 'w') as f:
    f.write('testing')

print(f.closed)  # Returned True as context manager has run successfully

# Using function

from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close()


with open_file('sample.txt', 'w') as f:
    f.write('retesting')

print(f.closed)  # True


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('OOPS'):
    print(os.listdir())  # ['ClassesAndInstances.py', 'ClassStaticInstanceMethods.py', 'ClassVariables.py',
    # 'Inharitance.py', 'MagicMethods.py', 'PropertyDecorator.py']
print(os.getcwd())  # C:\D-Drive\learning\Corey-Schafer
