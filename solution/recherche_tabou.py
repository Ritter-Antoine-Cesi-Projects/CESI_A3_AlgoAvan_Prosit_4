import random
from collections import deque
import time
from utils import random_objets, random_solution, valeur_contenu, poids_contenu
from voisinage import voisinage

def recherche_tabou(solution_initiale, taille_tabou, iter_max, capacite, poids_objets, valeur_objets):
    nb_iter = 0
    liste_tabou = deque(maxlen=taille_tabou)
    solution_courante = solution_initiale
    meilleure = solution_initiale
    meilleure_globale = solution_initiale
    valeur_meilleure = valeur_contenu(solution_initiale, valeur_objets)
    valeur_meilleure_globale = valeur_meilleure
    while (nb_iter < iter_max):
        valeur_meilleure = -1
        for voisin in voisinage(solution_courante, capacite, poids_objets):
            if voisin not in liste_tabou:
                valeur_voisin = valeur_contenu(voisin, valeur_objets)
                if valeur_voisin > valeur_meilleure:
                    meilleure = voisin
                    valeur_meilleure = valeur_voisin
        if valeur_meilleure > valeur_meilleure_globale:
            meilleure_globale = meilleure
            valeur_meilleure_globale = valeur_meilleure
            nb_iter = 0
        else:
            nb_iter += 1
        solution_courante = meilleure
        liste_tabou.append(meilleure)
    return meilleure_globale

def recherche_tabou_multistart(nb_objets, capacite):
    random.seed(a=3)
    poids_objets, valeur_objets = random_objets(nb_objets, 10, 10)
    sol_max = None
    val_max =-1
    start = time.process_time()
    for _ in range(500):
        sac = random_solution(nb_objets, capacite, poids_objets)
        sol_courante = recherche_tabou(sac, 5, 30, capacite, poids_objets, valeur_objets)
        val_courante = valeur_contenu(sol_courante, valeur_objets)
        if val_courante > val_max:
            val_max = val_courante
            sol_max = sol_courante
    stop = time.process_time()
    print("valeur finale = " + str(valeur_contenu(sol_max, valeur_objets)))
    print("calculé en ", stop-start, 's')
    return sol_max, valeur_objets, poids_objets