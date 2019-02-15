
def print_args(*args, **kwargs):
    print('Positional:', args)
    print('Keyword:', kwargs)

print_args(1, 2, foo='bar', stuff='meep')
