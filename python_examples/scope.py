def globglob():
    global x
    x = 100

# no no no
# print(x)
# so we export x to global scope with global keyword?
# yes yes
globglob()
print(x)

# let the variable jump to outer scope of function with nonlocal
def nonloc():
    x = 'yay'
    def inside_nonloc():
        nonlocal x
        x = 'insidethenonlocal'
    inside_nonloc()
    return x

print(nonloc())


# what happen if we
def outer():
    x = "I am from the outside"
    def inside():
        global x
        x = "I come from the depth of despair"
    inside()
    return x

print(x)
# "100"
print(outer())
# "I am from the outside"
print(x)
# "I come from the depth of despair"
outer()
print(x)
# "I come from the depth of despair"
# naruhodo



