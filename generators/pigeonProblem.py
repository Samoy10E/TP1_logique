"""
Generate clauses from the pigeons problem
"""

def generate(holes: int, pigeons: int):
    """
    Give conditions to the pigeons problem:
        -each pigeons have one hole
        -each holes have one or no pigeon

    x_p,h, if true, there is the pigeon p in the hole h
    x_p,h = x_k : k = 2*(h*pigeons + p)
    -x_k : k = 2*(h*pigeons+ p) + 1
    """
    Clauses = []

    Nlit = holes*pigeons*2

    # Each pigeons have an hole.

    Cp = [[2*(h*pigeons+p) for h in range(holes)] for p in range(pigeons)]

