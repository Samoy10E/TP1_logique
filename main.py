from generators import pigeonProblem, queenProblem
import satSolver2
import time

def main():
    # clause = pigeonProblem.generate_clauses(8)
    clause = queenProblem.generate_clauses(8)
    # print(clause)
    # clause = [[0,2],[1],[5,1],[7,2]]
    toutmodel = True

    t = time.time()
    SS2 = satSolver2.SatSolver(clause, toutmodel, satSolver2.firstSatisfy)
    sol = SS2.solve()
    print(len(sol),SS2.nb_noeud, time.time()-t)

    t = time.time()
    SS2 = satSolver2.SatSolver(clause, toutmodel, satSolver2.firstFail)
    sol = SS2.solve()
    print(len(sol),SS2.nb_noeud, time.time()-t)

    t = time.time()
    SS2 = satSolver2.SatSolver(clause, toutmodel, satSolver2.base)
    sol = SS2.solve()
    print(len(sol),SS2.nb_noeud, time.time()-t)

if __name__ == '__main__':
    main()

