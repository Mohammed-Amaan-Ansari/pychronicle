import sys


def trace_function(frame, event, arg):
    """
    Trace function called by Python for each execution event.
    """

    print(
        f"Event: {event:8} | "
        f"Function: {frame.f_code.co_name:15} | "
        f"Line: {frame.f_lineno}"
    )

    return trace_function


def start_tracing():
    """
    Enable Python tracing.
    """
    sys.settrace(trace_function)


def stop_tracing():
    """
    Disable tracing.
    """
    sys.settrace(None)