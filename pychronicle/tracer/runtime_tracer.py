import json
import sys
import time

from pychronicle.storage.database import insert_execution_trace
from pychronicle.storage.models import ExecutionTrace


def trace_function(frame, event, arg):

    if frame.f_code.co_filename == __file__:
        return trace_function

    trace = ExecutionTrace(
        timestamp=time.time(),
        event_type=event,
        line_number=frame.f_lineno,
        function_name=frame.f_code.co_name,
        locals_snapshot=json.dumps(
            frame.f_locals,
            default=str
        ),
    )

    insert_execution_trace(trace)

    return trace_function


def start_tracing():

    sys.settrace(trace_function)


def stop_tracing():

    sys.settrace(None)