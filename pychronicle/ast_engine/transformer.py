from pathlib import Path
import ast

from pychronicle.ast_engine.parser import parse_python_file


def create_record_call(variable_name: str, line_number: int) -> ast.Expr:
    """
    Creates:

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
    Inject record_state() after every assignment.
    """

    def visit_Assign(self, node: ast.Assign):

        self.generic_visit(node)

        new_nodes = [node]

        for target in node.targets:

            if isinstance(target, ast.Name):

                new_nodes.append(
                    create_record_call(
                        target.id,
                        node.lineno,
                    )
                )

        return new_nodes


def transform_file(file_path: Path) -> ast.AST:
    """
    Parse and transform a Python source file.
    """

    tree = parse_python_file(file_path)

    transformer = ASTTransformer()

    transformed_tree = transformer.visit(tree)

    ast.fix_missing_locations(transformed_tree)

    return transformed_tree