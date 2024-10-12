# Printing simple args
toup = (1, 2, 3)
def print_args(*args):
    print(args)

print_args(toup)


# How to unpack touples
def sum_args(*args):
    return sum(args)

s = sum_args(*toup)
print(s)

# more unpack test
def iterable_test(*a):
    return [ord(char) for char in a if isinstance(char, str) and len(char) == 1]

print(iterable_test('a', 'b', 'c'))


# more readable
def iterable_again(*a):
    res = []
    for char in a:
        if isinstance(char, str) and len(char) == 1:
            res.append(ord(char))
    return res

print(iterable_again('a', 'b'))


# iterate chars
def iterate_chars(start_char, n):
    if isinstance(start_char, str) and len(start_char) == 1:
        res = []
        start_ascii = ord(start_char)

        for char in range(start_ascii, start_ascii + n):
            res.append(char)
        return res
    else:
        return []
    
s = iterate_chars('a', 3)
k = map(chr,s)
print(list(k))


# kwargin 
def kwarging(**kwargs):
    print(kwargs)

k = {"name":"abc", "age":300}
a = kwarging(**k)


# or
def kwargingkwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    return '\n'

a = kwargingkwargs(**k)
print(a)

# kwargs args
def kwargargs(*args, **kwargs):
    print(f'pos: {args}')
    print(f'keys: {kwargs}')

    pos = args[0] if args else None

    kl = list(kwargs.items())

    if pos is not None and 0 <= pos < len(kl):
        key, value = kl[pos]
        return key, value
    else:
        return None, None

combining = kwargargs(1, 4, 2, 5,'c',"a word", name="abc", age=444)
print(combining)

# finally class examples
class Kwargor:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def display_the_kwargs(self):
        print(self.kwargs)

kwargor = Kwargor(something="nothing", job="engine", age=-100)
kwargor.display_the_kwargs()


# good job kwargor
class KwargoArgo:
    def __init__(self, *argo, **kwargo):
        print("Parent argo", argo)
        print("Parent kwargo", kwargo)


class MiniKargo(KwargoArgo):
    def __init__(self, *argo, **kwargo):
        super().__init__(*argo, **kwargo)
        print("Child starting")


child = MiniKargo(10, 30, name="notbob", age=22)

