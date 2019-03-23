
a = ['birb','doggo','seeb']
c = ['birb','doggo','seebdddd']

def foo(*args, **kwargs):
    for idx, element in enumerate(args):
        print('args ', idx, args[idx])
    for element in args:
        print('args ', element)
    for key in kwargs: # kwargs is like dictionary,
                       # so what is 'in' kwargs is not list, it's idx
        print('Keyword ', key)
        print('kwargs ', kwargs[key][2])

foo(a, c, d = a, s = c) # a, c are args
                        # d, s are kwargs
'''
args  0 ['birb', 'doggo', 'seeb']
args  1 ['birb', 'doggo', 'seebdddd']
args  ['birb', 'doggo', 'seeb']
args  ['birb', 'doggo', 'seebdddd']
Keyword  d
kwargs  seeb
Keyword  s
kwargs  seebdddd
'''