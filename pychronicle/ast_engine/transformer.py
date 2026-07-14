from pathlib import Path
import ast

from pychronicle.ast_engine.parser import parse_python_file


def record_state(variable_name, value, line_number):
    """
    Temporary recorder.

    In Week 2, this function will write the execution
    state into SQLite instead of printing it.
    """
    print(f"[Line {line_number}] {variable_name} = {value}")


def create_record_call(variable_name: str, line_number: int) -> ast.Expr:
    """
    Creates the AST node for:

        record_state("x", x, line_number)
    """

    return ast.Expr(
        value=ast.Call(
            func=ast.Name(
                id="record_state",
                ctx=ast.Load(),
            ),
            args=[
                ast.Constant(variable_name),
                ast.Name(
                    id=variable_name,
                    ctx=ast.Load(),
                ),
                ast.Constant(line_number),
            ],
            keywords=[],
        )
    )


class ASTTransformer(ast.NodeTransformer):
    """
    Injects record_state() after every variable assignment.
    """

    def visit_Assign(self, node: ast.Assign):

        # First transform child nodes
        self.generic_visit(node)

        # Keep original assignment
        new_nodes = [node]

        # Handle assignments like:
        # x = 10
        # a = b = 100
        for target in node.targets:

            if isinstance(target, ast.Name):

                record_call = create_record_call(
                    target.id,
                    node.lineno,
                )

                new_nodes.append(record_call)

        return new_nodes


def main():

    sample = (
        Path(__file__).resolve().parents[2]
        / "examples"
        / "sample.py"
    )

    tree = parse_python_file(sample)

    transformer = ASTTransformer()

    transformed_tree = transformer.visit(tree)

    ast.fix_missing_locations(transformed_tree)

    namespace = {
        "record_state": record_state
    }

    compiled = compile(
        transformed_tree,
        filename="<ast>",
        mode="exec",
    )

    exec(compiled, namespace)


if __name__ == "__main__":
    main()