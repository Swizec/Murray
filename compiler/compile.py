
import sys, os

import parsers

TRANSLATIONS = {'.': 'dot'}

def parse(code):
    arguments = []
    string = []
    in_string = False
    dont_pass = False
    lines = []

    def _parse(element):
        try:
            parser = getattr(parsers, element)
            return [parser.main(arguments)]
        except AttributeError:
            try:
                return _parse(TRANSLATIONS[element])
            except KeyError:
                return arguments+[element]

    for element in code:
        if element == '':
            lines += arguments
            arguments = []
            continue

        if element[-1:] in TRANSLATIONS.keys() and not in_string:
            arguments = _parse(element[-1:])
            element = element[:-1]

        if element[-1:] == '"':
            in_string = True
        
        if not in_string:
            arguments = _parse(element)
        else:
            string.append(element)
            if element[0] == '"':
                in_string = False
                arguments.append(' '.join([word for word in reversed(string)]))
                string = []

    lines += arguments
        
    return reversed(lines)

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
