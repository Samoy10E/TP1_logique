from typing import List, Callable, Dict, Tuple, Union

def firstSatisfy(Solveur):
    litMax = 0
    for lit in range(Solveur.nb_lit):
        if Solveur.rep_lit[lit]>Solveur.rep_lit[lit] and Solveur.etat_prop[lit//2] is None:
            litMax = lit
    return litMax

def firstFail(Solveur):
    return Solveur.rep_lit.index(min(Solveur.rep_lit))

def base(Solveur):
    for i,n in enumarate(Solveur.rep_lit):
        if not n and Solveur.etat_prop[i//2] is not None:
            return i

class SatSolver:
    """
    variable à initialiser    heuristique: fonction
    nb_lit = Int                     nombre de litéraux positifs et négatifs en commencant à 0
    nb_clauses = Int
    clause_to_lit = List[List[Int]]
    lit_to_clause = List[List[Int]]

    variable interne
    etat_clauses = List[Int]
    etat_prop = List[Bool or None]
    pile Traitement = List[(Int, Bool)]
    Len_clause = List[Int]
    profondeur = 0                   profondeur actuelle dans l'arbre de recherche
    nb_noeud = 0                     nombre de noeud parcouru lors de l'algorithme
    Stop = Bool                      Bool condition d'arret du programme si on ne trouve pas de modèle aprés un parcours complet
    """

    def __init__(self, list_clauses, toutModels = True, heuristique = base):

        self.toutModels = toutModels
        self.model = []

        self.heuristique = heuristique
        self.nb_lit = 0

        # On cherche le nombre de littéraux
        for clause in list_clauses:
            if max(clause)+1 > self.nb_lit:
                self.nb_lit = max(clause)+1

        # Le nombre de littéraux doit être pair (+ et -)
        if self.nb_lit % 2 == 1:
            self.nb_lit += 1

        self.nb_clauses = len(list_clauses)
        self.clause_to_lit = list_clauses

        # Nombre de fois qu' apparaît un littéral dans toute les clauses
        self.rep_lit = [0]*self.nb_lit

        # On crée la matrice littéraux->clauses
        self.lit_to_clause = []*self.nb_lit
        for i in range(self.nb_lit):
            self.lit_to_clause.append([])

        for iclause in range(len(list_clauses)):
            for lit in list_clauses[iclause]:
                self.lit_to_clause[lit].append(iclause)
                self.rep_lit[lit] += 1

        # liste de la profondeur où la clause i a été vrai
        self.etat_clauses = [0]*self.nb_clauses

        # état les littéraux actuels
        self.etat_prop = [None] * (self.nb_lit // 2)

        # longueurs des clauses
        self.len_clauses = [len(clause) for clause in self.clause_to_lit]

        # pile des noeuds à traiter (n°lit, autre côté à faire (bool) )
        self.pile_traitement = []

        # profondeur actuel
        self.profondeur = 0

        # nombre de noeud parcouru
        self.nb_noeud = 0

        # condition d' arrêt
        self.stop = False

    def solve(self):

        while not self.stop:
            """Itération"""
            # Si il y a une solution on retourne la solution et/ou on backtrack pour continuer
            if 0 not in self.etat_clauses:
                self.ajouteModel()
                if self.toutModels:
                    self.backtrack()
                else:
                    # On a fini, on retourne le modèle
                    return self.model[0]

            # Si on arrive à un cul de sac on backtrack
            elif 0 in self.len_clauses:
                self.backtrack()

            else:
                # On descant dans l' arbre
                self.profondeur += 1

                # On cherche le prochain littéraux à évaluer
                lit = self.heuristiqueGlobale()

                # On ajoute l' opération à effectuer la prochaine fois qu' on passera sur ce noeud

                self.pile_traitement.append((lit, True))

                # Mise à jour des clauses

                self.etat_prop[lit//2] = lit%2==0
                self.majClause(lit, False)

                # Sinon on continue à itérer

        # On a fini, on retourne le(s) modèle(s)
        return self.model



    def backtrack(self):
        """On remonte"""
        # On remonte dans l' arbre
        self.profondeur -= 1

        lit, op = self.pile_traitement.pop()

        # Si on revient à la racine et que c'est la deuxième fois
        if self.profondeur == 0 and not op:
            self.stop = True
            return

        # Tant que on tombe sur des opérations déjà-vu
        while not op:
            # On annule la proposition
            self.etat_prop[lit // 2] = None

            # On annules les changements
            self.majClause(lit, True)

            """On remonte"""
            # On remonte dans l' arbre
            self.profondeur -= 1

            # On backtrack
            lit, op = self.pile_traitement.pop()

            # Si on revient à la racine et que c'est la deuxième fois
            if self.profondeur == 0 and not op:
                self.stop = True
                return

        # Sinon on prend l' autre chemin

        # On annules les changements
        self.majClause(lit, True)

        litbis = lit + 1 - 2 * int(lit%2 == 1)

        self.profondeur += 1

        # On affecte une valuation au littérale l
        self.etat_prop[lit // 2] = not self.etat_prop[lit // 2]

        # On met à jour les clauses
        self.majClause(litbis, False)

        # Ajout à la pile d' opération
        self.pile_traitement.append((litbis,False))

        # On reprend l' itération

    def majClause(self, lit, backtrack):
        # On met à jour l' état des clauses
        for iClause in self.lit_to_clause[lit]:
            self.etat_clauses[iClause] = self.profondeur*(1-backtrack)
            for l in self.clause_to_lit[iClause]:
                if self.etat_prop[l//2] is None:
                    self.rep_lit[l] -= 1 + 2*backtrack

        # On met à jour la longueur des clauses
        litbis = int(lit + 1 - 2 * lit%2==0)

        for iClause in self.lit_to_clause[litbis]:
            self.len_clauses[iClause] -= (1 - 2*int(backtrack))
            for l in self.clause_to_lit[iClause]:
                if self.etat_prop[l//2] is None:
                    self.rep_lit[l] -= 1 + 2*backtrack


    def heuristiqueGlobale(self) -> int:
        # Littéraux pur ou mono littoraux
        for i, lenClause in enumerate(self.len_clauses):
            # Si il y a une clause de longueur 1
            if lenClause == 1:
                # On cherche le littéral par encore évalué
                for lit in self.clause_to_lit[i]:
                    if self.etat_prop[lit//2] is None:
                        return lit

        for lit, nLit in enumerate(self.rep_lit):
            # Si il y a une clause de longueur 1
            if nLit == 0 and self.etat_prop[lit//2] is None:
                # On retourne le littérale opposé
                return lit + 1 - 2*(lit%2==1)

        # retourne heuristique
        return self.heuristique(self)

    def ajouteModel(self):
        if not self.toutModels:
            for i,lit in enumerate(self.etat_prop):
                if lit is None:
                    self.etat_prop[i] = True
            self.model.append(self.etat_prop)
        else:
            self.completeModele(self.etat_prop.copy())


    def completeModele(self, elit, iDebut=0):
        i = iDebut
        while i<len(elit) and elit[i] is not None:
            i += 1

        if i<len(elit) and self.etat_prop[i] is None:
            elit1, elit2 = elit.copy(), elit.copy()

            elit1[i] = True
            self.completeModele(elit1, i+1)

            elit2[i] = False
            self.completeModele(elit2, i + 1)
        else:
            self.model.append(elit)

