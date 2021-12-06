from typing import List, Callable, Dict, Tuple, Union

class SatSolver:
    """
    variable à initialiser    heuristique: fonction
    nb_lit = Int                     nombre de litéraux positifs et négatifs en commencant à 0
    nb_clauses = Int
    clause_to_lit = List[List[Int]]
    lit_to_clause = List[List[Int]]

    variable interne
    etat_clauses = List[Int]
    etat_lit = List[Bool or None]
    pile Traitement = List[(Int, Bool)]
    Len_clause = List[Int]
    profondeur = 0                   profondeur actuelle dans l'arbre de recherche
    nb_noeud = 0                     nombre de noeud parcouru lors de l'algorithme
    Stop = Bool                      Bool condition d'arret du programme si on ne trouve pas de modèle aprés un parcours complet
    """

    def __init__(self, list_clauses, heuristique = "base"):

        self.heuristique = heuristique
        self.nb_lit = 0

        # On cherche le nombre de littéraux
        for clause in list_clauses:
            if max(clause) > self.nb_lit:
                self.nb_lit = max(clause)
        # Le nombre de littéraux doit être pair (+ et -)
        if self.nb_lit % 2 == 0:
            self.nb_lit += 1

        self.nb_clauses = len(list_clauses)
        self.clause_to_lit = list_clauses

        # On crée la matrice littéraux->clauses
        self.lit_to_clause = [[]]*self.nb_lit
        for iclause in range(len(list_clauses)):
            for lit in list_clauses[iclause]:
                self.lit_to_clause[lit].append(iclause)

        # liste de la profondeur où la clause i a été vrai
        self.etat_clauses = [0]*self.nb_clauses

        # état les littéraux actuels
        self.etat_lit = [None]*self.nb_lit

        # longueurs des clauses
        self.len_clauses = [len(clause) for clause in self.clause_to_lit]

        # pile des noeuds à traiter (n°lit, autre côté à faire (bool) )
        self.pile_traitement = []

        # profondeur actuel
        self.profondeur = 0

        # nombre de noeud parcouru
        self.nb_noeud = 0

        # condition d'arrêt du programme
        self.stop = False

    def solve(self):
        #Lance la solution du problème
        self.stop = False
        print("début")
        while not self.stop:
            if not self.verif():
                self.backtrack()
                continue
            self.search()
        print("fin")

    def verif(self):
        #cherche des erreur pour backtrack si besoin
        if 0 in self.len_clauses:
            return False
        return True

    def backtrack(self):
        # On réinitialise les clauses validées à la profondeur précédente
        for i in self.lit_to_clause:
            if self.etat_clauses[i] == self.profondeur:
                self.etat_clauses[i] = 0

        self.profondeur -= 1

        #annule le dernier changement de littéral
        last_change = self.pile_traitement.pop()
        self.etat_lit[last_change[0]] = None

        if last_change[0] % 2 == 0:
            self.etat_lit[last_change[0]+1] = None
            for i in self.lit_to_clause:
                self.len_clauses[i] += 1
        else:
            self.etat_lit[last_change[0]-1] = None
            for i in self.lit_to_clause:
                self.len_clauses[i] += 1

        #fait un nouveau changement si nécessaire
        if last_change[1]:
            self.lit_set(last_change[0], False)
        elif not last_change[2]:
            # s' arrête si racine de l' arbre
            if self.profondeur == 0:
                self.stop = True
                return
            self.backtrack()

    def lit_set(self, lit, first_try):
        #met lit à positif son opposé a négatif et update les tables
        self.profondeur += 1
        self.pile_traitement.append((lit, first_try))
        self.etat_lit[lit] = True
        for i in self.lit_to_clause:
            if self.etat_clauses[i] == 0:
                self.etat_clauses[i] = self.profondeur
        if lit % 2 == 0:
            self.etat_lit[lit+1] = False
            for i in self.lit_to_clause:
                self.len_clauses[i] -= 1
        else:
            self.etat_lit[lit-1] = False
            for i in self.lit_to_clause:
                self.len_clauses[i] -= 1

    def search(self):
        for lit in range(self.nb_lit):
            if self.etat_lit[lit] is None:
                self.lit_set(lit, True)
                return
        print("réussite")