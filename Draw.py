# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def SAT_solve(list_clauses):
    
    index_lit = []
    for clause in list_clauses:
        for lit in clause:
            if lit[0] == "-":
               lit = lit[1:]
            if lit not in index_lit:
                index_lit.append(lit)
                   
    nb_clauses = len(list_clauses)
    nb_lit = len(index_lit)
    etat_clauses = [0 for i in range(nb_clauses)]
    etat_lit = [None for i in range(nb_lit)]
    len_clauses = [len(clause) for clause in list_clauses]
    pile_lit = []
    list_lit = [[]for i in range(2*nb_lit)]
    for i in range(nb_lit):
        for j in range(nb_clauses):
            if index_lit[i] in list_clauses[j] and "-" + index_lit[i] in list_clauses[j]:
                return("Error")
            elif index_lit[2*i] in list_clauses[j]:
                list_lit[i].append([j])
            elif "-" + index_lit[i] in list_clauses[j]:
                list_lit[2*i+1].append([j])
                
                

