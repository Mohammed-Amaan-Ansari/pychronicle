from pathlib import Path
import ast


def parse_python_file(file_path: Path):
    """
    Reads a Python file and returns its AST.
    """
    source = file_path.read_text(encoding="utf-8")

    tree = ast.parse(source)

    return tree


if __name__ == "__main__":
    sample = Path(__file__).resolve().parents[2] / "examples" / "sample.py"

    tree = parse_python_file(sample)

    print(ast.dump(tree, indent=4, include_attributes=True))