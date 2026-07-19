from pychronicle.tracer.runtime_tracer import (
    start_tracing,
    stop_tracing,
)


def add(a, b):
    result = a + b
    return result


start_tracing()

x = 10
y = 20

z = add(x, y)

print(z)

stop_tracing()