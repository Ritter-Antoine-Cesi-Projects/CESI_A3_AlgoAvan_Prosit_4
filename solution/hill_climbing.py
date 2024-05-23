from utils import valeur_contenu
from voisinage import voisinage

def hill_climbing(solution_initiale, capacite, poids_objets, valeur_objets):
    solution_courante = solution_initiale
    nouveau = True
    nb_iter = 0
    while (nouveau):
        nb_iter += 1
        meilleure_solution = solution_courante
        meilleure_valeur = valeur_contenu(meilleure_solution, valeur_objets)
        for voisin in voisinage(meilleure_solution, capacite, poids_objets):
            valeur = valeur_contenu(voisin, valeur_objets)
            if valeur <= meilleure_valeur:
                continue
            meilleure_solution = voisin
            meilleure_valeur = valeur
        nouveau = (meilleure_solution != solution_courante)
        solution_courante = meilleure_solution
    return solution_courante