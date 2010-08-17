
import os, importlib, sys

path = os.path.abspath(__file__).rsplit('/', 1)[0]

sys.path.append(path)

for executor in os.listdir(os.path.abspath(__file__).rsplit('/', 1)[0]):
    (module, extension) = executor.split('.')
    if extension == 'py' and module != '__init__':
        setattr(sys.modules[__name__], module, importlib.import_module(module))

