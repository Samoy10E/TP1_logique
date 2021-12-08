from pathlib import Path
"""
Generate clauses from the pigeons problem
"""

def generate_clauses(n: int):
    """
    Give conditions to the queens problem:
        -one queen on rows
        -one queen on columns
        -one queen on diagonals

    There is a queen on the l,c tile <=> C = (n*c+l)*2
    There is not a queen on the lc, tile <=> C = (n*c+l)*2+1
    """

    clauses = []

    # There is at least one queen on each row/column
    clauses_least_oneQueen = [[((n*c)+l)*2 for l in range(n)] for c in range(n)]

    clauses += clauses_least_oneQueen
    # There is no more than one queen on each column
    clauses_only_oneQueen_column = [[((n*c1)+l)*2+1,((n*c2)+l)*2+1]
                                  for c1 in range(n) for c2 in range(c1+1,n) for l in range(n)]

    clauses += clauses_only_oneQueen_column
    # There is no more than one queen on each row
    clauses_only_oneQueen_row = [[((n*c)+l1)*2+1,((n*c)+l2)*2+1]
                                  for l1 in range(n) for l2 in range(l1+1,n) for c in range(n)]

    clauses += clauses_only_oneQueen_row
    # SUD-EAST diagonal
    clauses_only_oneQueen_SE = [[((n*(k+i1))+n-1-i1)*2+1,((n*(k+i2))+n-1-i2)*2+1]
                                  for k in range(n) for i1 in range(n-k) for i2 in range(i1+1,n-k)]

    clauses += clauses_only_oneQueen_SE
    # NORTH-WEST diagonal
    clauses_only_oneQueen_NW = [[((n*i1)+k-i1)*2+1,((n*i2)+k-i2)*2+1]
                                  for k in range(n-1) for i1 in range(k+1) for i2 in range(i1+1,k+1)]

    clauses += clauses_only_oneQueen_NW
    # SUD-WEST diagonal
    clauses_only_oneQueen_SW = [[((n*(n-1-k+i1))+i1)*2+1,((n*(n-1-k+i2))+i2)*2+1]
                                  for k in range(n) for i1 in range(k+1) for i2 in range(i1+1,k+1)]

    clauses += clauses_only_oneQueen_SW
    # NORTH-EAST diagonal
    clauses_only_oneQueen_NE = [[((n*i1)+n-1-k+i1)*2+1,((n*i2)+n-1-k+i2)*2+1]
                                  for k in range(n-1) for i1 in range(k+1) for i2 in range(i1+1,k+1)]

    clauses += clauses_only_oneQueen_NE
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