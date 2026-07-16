import ast

from pychronicle.tracer.recorder import record_state


def execute(tree):
    """
    Compiles and executes
    an instrumented AST.
    """

    ast.fix_missing_locations(tree)

    namespace = {
        "record_state": record_state
    }

    code = compile(
        tree,
        filename="<ast>",
        mode="exec",
    )

    exec(code, namespace)