
import sys

import parsers

def parse(code):
    arguments = []
    string = []
    in_string = False
    for element in code:
        if not in_string:
            try:
                parser = getattr(parsers, element)
                arguments = [parser(arguments)]
            except AttributeError:
                arguments.append(element)
        else:
            string.append(element)
        
    print arguments
            

def compile(source, target=None):
    f = file(source, 'r')

    code = reversed(reduce(lambda a,b: a+b.strip().split(' '), f, []))
    result = parse(code)        

    f.close()


if __name__=='__main__':
    compile(sys.argv[1])
