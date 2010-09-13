
N_ARGS = 1
STACK = True

def main(stack, args):
    #(arg1, arg2) = args
    arg1 = args[0]
    return "%s if (%s) else None" % (arg1, stack[0])
