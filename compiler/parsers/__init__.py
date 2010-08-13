
def say(args):
    print string(args)
    return 'meow'

def string(args):
    return ' '.join([word.strip('"') for word in reversed(args)])
