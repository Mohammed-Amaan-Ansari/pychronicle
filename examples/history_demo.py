from pychronicle.storage.database import get_all_variable_states

rows = get_all_variable_states()

for row in rows:
    print(row)