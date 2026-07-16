from pathlib import Path

from pychronicle.ast_engine.parser import parse_python_file
from pychronicle.ast_engine.transformer import ASTTransformer

from pychronicle.storage.schema import initialize_database
from pychronicle.tracer.executor import execute


initialize_database()

sample = (
    Path(__file__).resolve().parents[1]
    / "examples"
    / "sample.py"
)

tree = parse_python_file(sample)

transformer = ASTTransformer()

tree = transformer.visit(tree)

execute(tree)