def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    
    def sum_term(i):
        if i == 0 or i == n: 
            return f(a + i * h) / 2
        else:
            return f(a + i * h)
    
    def recursive_sum(i):
        if i > n:
            return 0
        return sum_term(i) + recursive_sum(i + 1)
    
    return recursive_sum(0) * h


def f(x):
    return x**2

res = trapezoidal_rule(f, 2, 3, 100)

print(res)
