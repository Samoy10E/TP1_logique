from pathlib import Path
"""
Generate clauses from the pigeons problem
"""

def generate_clauses(holes: int, pigeons: int):
    """
    Give conditions to the pigeons problem:
        -each pigeons have one hole
        -each holes have one or no pigeon

    x_p,h, if true, there is the pigeon p in the hole h
    x_p,h = x_k : k = 2*(h*pigeons + p)
    -x_k : k = 2*(h*pigeons+ p) + 1
    """
    clauses = []

    # Each pigeons have an hole.

    clauses_pigeons = [[2*(h*pigeons+p) for h in range(holes)] for p in range(pigeons)]

    clauses = clauses + clauses_pigeons

    # Each hole have one or no pigeon in.

    clauses_holes = []

    for h in range(holes):
        clause_hole = [[2*(h*pigeons+p)+1 for p in range(pigeons)]]
        for chosen_p in range(pigeons):
            clause_hole = clause_hole + [[2*(h*pigeons+chosen_p)+1] + [2*(h*pigeons+p) for p in range(pigeons) if p!=chosen_p]]
        clauses_holes = clauses_holes + clause_hole

    clauses = clauses + clauses_holes
    return clauses

def generate_file(holes: int, pigeons: int):

    #If the problem has not been already generate, generate it and st

    fileName = r"formula/pigeonProblem_"+str(holes)+"H"+str(pigeons)+"P.txt"
    fileObj = Path(fileName)
    if not fileObj.is_file():
        clauses = generate_clauses(holes, pigeons)
        file = open(fileName, "w")
        commentary = "c pigeon problem with " + str(holes) + " holes and " + str(pigeons) + " pigeons\n"
        file.write(commentary)
        parameters = "p cnf " + str(2*holes*pigeons) + " " + str(len(clauses)) + "\n"
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


