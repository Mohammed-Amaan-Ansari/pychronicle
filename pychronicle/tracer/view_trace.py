from pychronicle.storage.database import get_execution_trace


rows = get_execution_trace()

for row in rows:
    print(row)