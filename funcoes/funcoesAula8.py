#funçoes

def car(lis):
    return lis[0]

def cdr(lis):
    return lis[1:]

def cons(x, lis):
    return [x]+lis

def ehLista(x):
    return isinstance(x, list)

def ehAtomo(x):
    return not ehLista(x)