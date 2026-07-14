import ast

node = ast.Expr(
    value=ast.Call(
        func=ast.Name(
            id="print",
            ctx=ast.Load()
        ),
        args=[
            ast.Constant("Hello AST!")
        ],
        keywords=[]
    )
)

print(ast.dump(node, indent=4))