
def main(args):
    args = map(lambda arg: arg if arg[-1:] == '"' and arg[0] == '"' else 'str({0})'.format(arg),
               args)
    return '"".join([{0}])'.format(','.join(args))
