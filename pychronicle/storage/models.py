from dataclasses import dataclass


@dataclass
class VariableState:

    timestamp: float

    line_number: int

    variable_name: str

    serialized_value: str



@dataclass
class ExecutionTrace:
    timestamp: float
    event_type: str
    line_number: int
    function_name: str
    locals_snapshot: str