from pychronicle.tracer.runtime_tracer import (
    start_tracing,
    stop_tracing,
)


def add(a, b):

    result = a + b

    return result


def multiply(x, y):

    value = x * y

    return value


start_tracing()

num1 = 10

num2 = 20

sum_result = add(num1, num2)

final = multiply(sum_result, 5)

print(final)

stop_tracing()