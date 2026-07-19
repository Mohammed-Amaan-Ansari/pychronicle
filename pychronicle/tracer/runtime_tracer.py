import sys
from pprint import pprint


def trace_function(frame, event, arg):
    """
    Runtime tracing callback.
    """

    # Ignore tracing inside the tracer itself
    if frame.f_code.co_filename == __file__:
        return trace_function

    print("=" * 60)

    print(f"Event      : {event}")
    print(f"Function   : {frame.f_code.co_name}")
    print(f"Line       : {frame.f_lineno}")
    print(f"File       : {frame.f_code.co_filename}")

    print("\nLocal Variables")

    pprint(frame.f_locals)

    print("=" * 60)

    return trace_function


def start_tracing():
    sys.settrace(trace_function)


def stop_tracing():
    sys.settrace(None)