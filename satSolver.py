class SatSolver:

    #Variable à initialiser
    clauseToLit: List[List]
    heuristique: Fonction
    satisfiableOuSolution: bool

    #Variable interne
    nombreNoeud: int
    etatClause: List[int]
    pileLit: Pile[tuple]
    etatLit: List[bool]
    lenClause: List[List[int]]

    def __init__(self,clauseToLit : List[List],heuristique : Fonction,satisfiableOuSolution : bool):
        self.clauseToLit = clauseToLit
        self.heuristique = heuristique
        self.satisfiableOuSolution = satisfiableOuSolution

    def solveur(self):
        # TODO Ecrire le solveur
        if self.satisfiableOuSolution:
            return #vrai ou faux
        else:
            return #model