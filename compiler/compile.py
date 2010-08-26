
import sys, os

import parsers

TRANSLATIONS = {'.': 'dot'}

#def parse(code):
#    arguments = []
#    string = []
#    in_string = False
#    dont_pass = False
#    lines = []

#    def _parse(element):
#        try:
#            parser = getattr(parsers, element)
#            return [parser.main(arguments)]
#        except AttributeError:
#            try:
#                return _parse(TRANSLATIONS[element])
#            except KeyError:
#                return arguments+[element]

#    for element in code:
#        if element == '':
#            lines += arguments
#            arguments = []
#            continue

#        if element[-1:] in TRANSLATIONS.keys() and not in_string:
#            arguments = _parse(element[-1:])
#            element = element[:-1]

#        if element[-1:] == '"':
#            in_string = True
        
#        if not in_string:
#            arguments = _parse(element)
#        else:
#            string.append(element)
#            if element[0] == '"':
#                in_string = False
#                arguments.append(' '.join([word for word in reversed(string)]))
#                string = []

#    lines += arguments
        
#    return reversed(lines)

def parse(code):
    def _string(code):
        s = []
        for word in code:
            s.append(word)
            if word[-1:] == '"':
                return (' '.join(s), len(s))
        raise ParsingError("Unterminated string")

    def _consume(code, n):
        stack = []

        if n == 'Inf':
            n = len(code)

        i = 0
        while i < n:
            element = code[i]

            if element == '':
                return (stack, i)
            
            if element[0] == '"':
                (element, offset) = _string(code[i:])
                i += offset

            try:
                parser = getattr(parsers, element)
            except AttributeError:
                pass
            else:
                (args, offset) = _consume(code[i+1:], parser.N_ARGS)
                i += offset
                element = parser.main(args)

            stack.append(element)
            i += 1

        return (stack, i)
            
    lines = []
    while len(code) > 0:
        (line, offset) = _consume(code, len(code))
        lines += line
        code = code[offset+1:]

    return lines
    

def compile(source, target=None):
    f = file(source, 'r')

    code = reduce(lambda a,b: a+b.strip().split(' ') if b[0] != '#' else a, f, [])
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


class ParsingError(Exception):
    pass


if __name__=='__main__':
    compile(sys.argv[1])
