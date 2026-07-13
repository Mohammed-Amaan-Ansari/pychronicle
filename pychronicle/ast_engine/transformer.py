from pathlib import Path
import ast

from pychronicle.ast_engine.parser import parse_python_file


def record_state(variable_name):
    """Temporary function that prints the variable name."""

    print(f"Recording variable: {variable_name}")
class ASTTransformer(ast.NodeTransformer):

    def visit_Assign(self, node):

        new_nodes = [node]

        for target in node.targets:

            if isinstance(target, ast.Name):

                record_call = ast.Expr(

                    value=ast.Call(

                        func=ast.Name(

                            id="record_state",

                            ctx=ast.Load()

                        ),

                        args=[

                            ast.Constant(target.id)

                        ],

                        keywords=[]
                    )
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

    tree = transformer.visit(tree)

    ast.fix_missing_locations(tree)

    namespace = {

        "record_state": record_state

    }

    compiled = compile(

        tree,

        filename="<ast>",

        mode="exec"

    )

    exec(compiled, namespace)

if __name__ == "__main__":
    main()