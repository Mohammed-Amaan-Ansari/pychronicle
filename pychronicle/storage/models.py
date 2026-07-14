from dataclasses import dataclass


@dataclass
class VariableState:

    timestamp: float

    line_number: int

    variable_name: str

    serialized_value: str