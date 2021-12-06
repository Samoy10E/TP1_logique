from generators import pigeonProblem
import satSolver2

def main():
    clause = pigeonProblem.pigeons_generate_clauses(10)
    # clause = [[0,2],[1],[5,1],[7,2]]
    SS2 = satSolver2.SatSolver(clause, True, satSolver2.firstSatisfy)
    print(SS2.solve())


if __name__ == '__main__':
    main()

