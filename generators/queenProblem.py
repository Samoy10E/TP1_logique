from pathlib import Path
"""
Generate clauses from the pigeons problem
"""

def generate_clauses(n: int):
    """
    Give conditions to the queens problem:
        -each pigeons have one hole
        -each holes have one or no pigeon

    x_p,h, if true, there is the pigeon p in the hole h
    x_p,h = x_k : k = 2*(h*pigeons + p)
    -x_k : k = 2*(h*pigeons+ p) + 1
    """
    pigeons = n
    holes = n-1

    clauses = []

    # Each hole have one pigeon.

    clauses_at_the_most_one_pigeon = [[2*(h*pigeons+p1)+1,2*(h*pigeons+p2)+1]   for p1 in range(pigeons-1)
                                                                                for p2 in range(p1+1,pigeons)
                                                                                for h in range(holes)]

    clauses = clauses + clauses_at_the_most_one_pigeon

    # Each pigeons have an hole.

    clauses_at_least_one_hole = [[2 * (h * pigeons + p) for h in range(holes)] for p in range(pigeons)]

    clauses_at_the_most_one_hole = [[2*(h1*pigeons+p)+1,2*(h2*pigeons+p)+1] for h1 in range(holes-1)
                                                                            for h2 in range(h1 + 1, holes)
                                                                            for p in range(pigeons)]

    clauses = clauses + clauses_at_least_one_hole + clauses_at_the_most_one_hole
    return clauses

def generate_file(n: int):

    #If the problem has not been already generate, generate it and st

    fileName = r"formula/queenProblem_"+str(n)+".txt"
    fileObj = Path(fileName)
    if not fileObj.is_file():
        clauses = generate_clauses(n)
        file = open(fileName, "w")
        commentary = "c queen problem with " + str(n)+"\n"
        file.write(commentary)
        parameters = "p cnf " + str(2*n) + " " + str(len(clauses)) + "\n"
        file.write(parameters)
        for clause in clauses:
            line = ""
            for lit in clause:
                if lit%2==1:
                    line += "-"
                line += str(lit//2) + " "
            line = line[:-1] + "\n"
            file.write(line)
        file.close()