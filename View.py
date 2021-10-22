from abc import ABC, abstractmethod

class View(ABC):

    nomProblemeCourant: string
    problemeCourant: clauseToLit

    nomHeuristiqueCourante: string
    heuristiqueCourante: fonction

    problemeAnalyse: dictionnary #{nomProbleme_nomHeuristiqe_taille : (temps_exec, nombre_noeud,model)}
    #Le modèle est un bool si on choisi l'option estSatifiable, non?

    def __init__(self):
        return

    def select_fichier(self,nomFichier: string) -> clauseToInt:
        #TODO méthode commune
        return

    def select_generateur(self, nomGenerateur: fonction, *args) -> clauseToInt:
        #TODO méthode commune
        return

    def select_heuristique(self,heuristique : fonction):
        self.heuristiqueCourante = heuristique

    def lanceSolveur(self, satisfiableOuSolution : bool) -> bool_ou_model:
        #TODO méthode commune
        return

    def analyse(self, taille):
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
    def affiche(self,nomProbleme_nomHeuristiqe_taille: string):
        #TODO en fonction de model (bool ou non) affiche:
        #TODO affiche temps d'execution
        #TODO affiche nombre de noeud
        pass

    @abstractmethod
    def compare(self):
        #TODO plot plusieurs analyse
        pass

class ViewConsole(View):

    def affiche(self,nomProbleme_nomHeuristiqe_taille: string):
        # TODO en fonction de model (bool ou non) affiche:
        # TODO affiche temps d'execution
        # TODO affiche nombre de noeud
        pass

    def compare(self):
        # TODO plot plusieurs analyse
        pass
