import time

def fibonacci(n):
    if n <= 1:
        return n

    fib_sequence = [0, 1]
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    return fib_sequence[n]

def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def measure_func_time(func):
    start_time = time.time()
    res = func(None)
    end_time = time.time()

    print(f"La función duró {end_time - start_time:2f} segundos")
    return res

fib_n = 40

print('Buscando dígito #', fib_n, sep='')
measure_func_time(lambda _: fibonacci(fib_n))
measure_func_time(lambda _: recursive_fibonacci(fib_n))

