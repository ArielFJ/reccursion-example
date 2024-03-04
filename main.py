import time

def iterative_fibonacci(n):
    """
    Bsuca el dígito N en la secuencia Fibonacci usando ciclos
    """
    if n <= 1:
        return n

    fib_sequence = [0, 1]
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    return fib_sequence[n]

def recursive_fibonacci(n):
    """
    Utiliza recursión (una función que se llama a sí misma) para hallar el dígito N en la secuencia Fibonacci
    """
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def measure_func_time(func):
    """
    Mide el tiempo que tarda una función desde su inicio hasta su final
    """
    start_time = time.time()
    res = func(None)
    end_time = time.time()

    print(f"La función duró {end_time - start_time:2f} segundos")
    return res

fib_n = 10

print('Buscando dígito #', fib_n, sep='')
measure_func_time(lambda _: iterative_fibonacci(fib_n))
measure_func_time(lambda _: recursive_fibonacci(fib_n))

""""
Cómo funciona la recursión en la memoria?

call(40)
    call(39)
        call(38) -> 38 + call(37)
            ...
                call(1) -> 1

"""