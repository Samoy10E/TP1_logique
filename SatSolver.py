class SatSolver:

    #Variable à initialiser
    clauseToInt: List[List]
    heuristique: Fonction
    satisfiableOuSolution: bool

    #Variable interne
    nombreNoeud: int
    etatClause: List[List[bool]]
    pileLit: Pile[tuple]
    etatLit: List[bool]
    lenClause: List[List[int]]

    def __init__(self,clauseToInt : List[List], heuristique : Fonction, satisfiableOuSolution : bool):
        self.clauseToInt = clauseToInt
        self.heuristique = heuristique
        self.satisfiableOuSolution = satisfiableOuSolution


    def solveur(self):
        if self.satisfiableOuSolution:
            return #vrai ou faux
        else:
            return #model