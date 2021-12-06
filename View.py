from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Callable, Dict, Tuple, Union

import generators

"""
Abstract class, manage views and controls
"""
class View(ABC):

    nomProblemeCourant: str
    problemeCourant: List[List[int]]

    nomHeuristiqueCourante: str
    heuristiqueCourante: Callable

    problemeAnalyse: Dict[str, Tuple[int, int, Union[bool, List[List[int]]]]] #{nomProbleme_nomHeuristiqe_taille : (temps_exec, nombre_noeud,model)}
    #Le modèle est un bool si on choisi l'option estSatifiable, non?

    def __init__(self):
        self.ProblemeCrourant = []
        self.nomProblemeCourant = ""

    def select_fichier(self,nomFichier: str) -> List[List[int]]:
        fileName = r"formula/" + nomFichier + ".txt"
        fileObj = Path(fileName)
        if not fileObj.is_file():
            raise NameError(fileName)
        file = open(fileName)
        texte = file.readlines()
        clauses = []
        for ligne in texte:
            if ligne[0] != "c" and ligne[0] != "p":
                prop = ligne.split(" ")
                clause = []
                for p in prop:
                    p = int(p)*2
                    if p<0:
                        p = -p+1
                    clause.append(p)
                clauses.append(clause)
        self.ProblemeCrourant = clauses
        self.nomProblemeCourant = nomFichier

    def select_generateur(self, nomGenerateur: str) -> List[List[int]]:
        self.ProblemeCrourant = listeGenerateur(nomGenerateur)
        self.nomProblemeCourant = nomGenerateur

    def select_heuristique(self,heuristique : Callable):
        self.heuristiqueCourante = heuristique

    def lance_solveur(self, satisfiableOuSolution : bool) -> Union[bool, List[List[int]]]:
        #TODO méthode commune
        return

    def analyse(self, taille: int):
        temps_exec = 0
        nombre_noeud = 0
        model = []

        #TODO mesurer temps d'éxécution
        model = lanceSolveur(True)
        #TODO récupérer nombre de noeud

        self.problemeAnalyse[self.nomProblemeCourant+"_"+self.nomHeuristiqueCourante+"_"+str(taille)] = (temps_exec,nombre_noeud,model)

    def ecrire(self):
        #TODO écrire les models sur un fichier txt
        #peut etre qu'il faut déplacer cette méthode ailleur
        return

    @abstractmethod
    def affiche(self,nomProbleme_nomHeuristiqe_taille: str):
        #TODO en fonction de model (bool ou non) affiche:
        #TODO affiche temps d'execution
        #TODO affiche nombre de noeud
        pass

    @abstractmethod
    def compare(self):
        #TODO plot plusieurs analyse
        pass

class ViewConsole(View):

    def action(self):
        print(">")
        entre = input()
        print(entre)
        if entre in ["sortie","-s","exit"]:
            return False
        elif entre in ["aide","help"]:
            print("Pour sortir taper 'sortie'")
        elif entre in ["generateur","g?"]:
            noms = liste_generateur()
            print(noms)
        else:
            commande = entre.split(" ")
            if commande[0] in ["solve", "-s"]:
                satifaisable = bool(commande[1])
                if commande[2] in ["fichier","-f"]:
                    self.select_fichier(commande[3])
                    i = 4
                elif commande[2] in ["generateur","-g"]:
                    self.select_generateur(commande[3],commande[4])
                    i = 5

                if i<len(commande) and commande[i] in ["heuristique","-h"]:
                    self.select_heuristique(commande[i+1])

            print(self.nomProblemeCourant)




        return True

    def affiche(self,nomProbleme_nomHeuristiqe_taille: str):
        # TODO en fonction de model (bool ou non) affiche:
        # TODO affiche temps d'execution
        # TODO affiche nombre de noeud
        pass

    def compare(self):
        # TODO plot plusieurs analyse
        pass
