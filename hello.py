from memory_profiler import profile

@profile
def funct(n):
    for i in range(n**n):
        pass
    return

@profile
def funct2(n):
    for i in range(n**n):
        yield i
    return

funct2(6)