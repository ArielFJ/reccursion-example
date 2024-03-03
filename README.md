# Fibonacci en Python

Este código en Python implementa la secuencia de Fibonacci de manera iterativa y recursiva, proporcionando también una función para medir el tiempo de ejecución de cada enfoque. La secuencia de Fibonacci es una serie matemática en la que cada número es la suma de los dos anteriores. Los primeros números en la secuencia son 0, 1, 1, 2, 3, 5, 8, 13, 21, y así sucesivamente.

## Archivos en el Repositorio:

1. **main.py**: Contiene las implementaciones del cálculo del n-ésimo número de Fibonacci tanto de forma iterativa como recursiva.

## Funciones Principales:

### Iterativa:

```python
def fibonacci(n):
    if n <= 1:
        return n

    fib_sequence = [0, 1]
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

    return fib_sequence[n]
```

### Recursiva:

```python
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
```

### Medición del Tiempo de Ejecución:

```python
def measure_func_time(func):
    start_time = time.time()
    res = func(None)
    end_time = time.time()

    print(f"La función duró {end_time - start_time:2f} segundos")
    return res
```

## Cómo Usar el Programa:

1. Definir el valor de `fib_n` que representa el índice de la secuencia de Fibonacci que se desea calcular.

```python
fib_n = 40
```

2. Ejecutar el programa en la terminal.
```bash
python main.py
```

## Consideraciones:

- La implementación iterativa es generalmente más eficiente para valores grandes de `n` al evitar la sobrecarga de las llamadas a funciones y los cálculos repetidos.
- La implementación recursiva puede ser más simple de entender, pero puede ser menos eficiente para valores grandes de `n` debido a los cálculos repetidos. 
- Es importante aclarar que podemos optimizar estas implementaciones agregando un `Hash Table` para guardar valores ya vistos, y así no calcular los valores en cada iteración o llamada recursiva.

## Ejecuciones de ejemplo:
Debajo tenemos algunas ejecuciones que van doblando el dígito a buscar en la secuencia Fibonacci. Una línea nos dice el tiempo que tardó la función iterativa, mientras que la otra nos dice cuánto duró la función recursiva. Sabiendo que la recursión no se caracteriza por ser muy eficiente, creo que es claro cuál es la función recursiva.

```bash
$ python3 main.py
Buscando dígito #5
La función duró 0.000005 segundos
La función duró 0.000004 segundos

$ python3 main.py
Buscando dígito #10
La función duró 0.000006 segundos
La función duró 0.000064 segundos

$ python3 main.py
Buscando dígito #20
La función duró 0.000009 segundos
La función duró 0.001956 segundos

$ python3 main.py
Buscando dígito #40
La función duró 0.000012 segundos
La función duró 29.948735 segundos
```