from pathlib import Path
import ast

from pychronicle.ast_engine.parser import parse_python_file


class ASTVisitor(ast.NodeVisitor):
    """Visits AST nodes and prints information about the source code."""

    def visit_Assign(self, node: ast.Assign):
        """Handle variable assignments."""

        for target in node.targets:
            if isinstance(target, ast.Name):
                print(
                    f"[Line {node.lineno}] Assignment -> {target.id}"
                )

        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """Handle function definitions."""

        print(
            f"[Line {node.lineno}] Function -> {node.name}"
        )

        self.generic_visit(node)

    def visit_If(self, node: ast.If):
        """Handle if statements."""

        print(
            f"[Line {node.lineno}] If Statement"
        )

        self.generic_visit(node)

    def visit_For(self, node: ast.For):
        """Handle for loops."""

        print(
            f"[Line {node.lineno}] For Loop"
        )

        self.generic_visit(node)

    def visit_While(self, node: ast.While):
        """Handle while loops."""

        print(
            f"[Line {node.lineno}] While Loop"
        )

        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        """Handle function calls."""

        if isinstance(node.func, ast.Name):
            print(
                f"[Line {node.lineno}] Function Call -> {node.func.id}"
            )

        self.generic_visit(node)


def main():

    sample = (
        Path(__file__).resolve().parents[2]
        / "examples"
        / "sample.py"
    )

    tree = parse_python_file(sample)

    visitor = ASTVisitor()

    visitor.visit(tree)


if __name__ == "__main__":
    main()