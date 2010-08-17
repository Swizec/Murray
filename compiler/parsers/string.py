
def main(args):
    args = map(lambda arg: arg.strip('"') if arg[-1:] == '"' and arg[0] == '"' else 'str({0})'.format(arg),
               args)
    return '" ".join({0})'.format(str(args))
