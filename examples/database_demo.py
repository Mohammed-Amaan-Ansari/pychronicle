import time

from pychronicle.storage.schema import initialize_database
from pychronicle.storage.database import insert_variable_state
from pychronicle.storage.models import VariableState


initialize_database()

state = VariableState(
    timestamp=time.time(),
    line_number=1,
    variable_name="x",
    serialized_value="10",
)

insert_variable_state(state)

print("Inserted successfully.")