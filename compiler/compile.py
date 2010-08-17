
import sys, os

import parsers

def parse(code):
    arguments = []
    string = []
    in_string = False
    for element in code:
        if element[-1:] == '"':
            in_string = True
        
        if not in_string:
            try:
                parser = getattr(parsers, element)
                arguments = [parser.main(arguments)]
            except AttributeError:
                arguments.append(element)
        else:
            string.append(element)
            if element[0] == '"':
                in_string = False
                arguments.append(' '.join([word for word in reversed(string)]))
                string = []
        
    return arguments

def compile(source, target=None):
    f = file(source, 'r')

    code = reversed(reduce(lambda a,b: a+b.strip().split(' '), f, []))
    result = parse(code)

    f.close()

    if target == None:
        target = '/'.join([os.getcwd(), '.'.join([source.rsplit('/', 1)[1], 'py'])])


    save(result, target)

def save(result, target):
    f = file(target, 'w')

    f.write("import Murray.executors as ex\n")
    f.writelines([''.join([line, "\n"]) for line in result])

    f.close()


if __name__=='__main__':
    compile(sys.argv[1])
