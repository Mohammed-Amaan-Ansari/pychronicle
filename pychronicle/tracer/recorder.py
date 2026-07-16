import time

from pychronicle.storage.database import insert_variable_state
from pychronicle.storage.models import VariableState

def record_state(
    variable_name,
    value,
    line_number,
):
    """
    Stores the variable state into SQLite.
    """

    state = VariableState(
        timestamp=time.time(),
        line_number=line_number,
        variable_name=variable_name,
        serialized_value=repr(value),
    )

    insert_variable_state(state)

