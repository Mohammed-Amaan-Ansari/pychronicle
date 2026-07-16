from pathlib import Path

from pychronicle.ast_engine.parser import parse_python_file


def test_parser():

    tree = parse_python_file(
        Path("examples/sample.py")
    )

    assert tree is not None