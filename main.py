from generators import pigeonProblem
from View import ViewConsole
from satSolver import SatSolver

def main():

    clauses = pigeonProblem.generate_clauses(3)
    SATsolv = SatSolver(clauses)
    SATsolv.solve()

if __name__ == '__main__':
    main()

