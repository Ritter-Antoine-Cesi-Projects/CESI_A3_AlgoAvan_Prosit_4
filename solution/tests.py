import random
from collections import deque
import time

from hill_climbing import hill_climbing
from utils import begin, start_test, separators, random_objets, random_solution, valeur_contenu, poids_contenu
from voisinage import voisinage
from recherche_tabou import recherche_tabou, recherche_tabou_multistart

def test_random_objets():
    random.seed(a=3)
    nb_objets = 10
    poids_objets, valeur_objets = random_objets(nb_objets, 10, 10)
    print('Poids: ' + str(poids_objets) + "\nValeurs: " + str(valeur_objets))
    sac = (True, False, True)
    objets = [k for k, v in enumerate(sac) if v]
    print(objets)

def test_poids_valeur():
    nb_objets = 10
    sac = (True, True, False, False, False, False, False, False, False, False)
    poids_objets, valeur_objets = random_objets(nb_objets, 10, 10)
    print('Poids:', poids_contenu(sac, poids_objets))
    print('Valeur:', valeur_contenu(sac, valeur_objets))

def test_voisinage():
    nb_objets = 3
    test = (True, False, True)
    poids_objets, valeur_objets = random_objets(nb_objets, 10, 10)
    print (test, "\nvoisins :")
    for voisin in voisinage(test, 10, poids_objets):
        print(voisin)

def test_hill_climbing():
    random.seed(a=3)
    capacite = 20
    nb_objets = 100
    poids_objets, valeur_objets=random_objets(nb_objets, 10, 10)
    sac = (False,)*nb_objets
    print("optimisation locale")
    sol = hill_climbing(sac, capacite, poids_objets, valeur_objets)
    print("valeur finale = " + str(valeur_contenu(sol, valeur_objets)) + ", capacite=" + str(poids_contenu(sol, poids_objets)) + "/" + str(capacite))
    print([i for i, val in enumerate(sol) if val])

def test_random_solution():
    val_max = 0
    random.seed(a=3)
    nb_objets = 10
    poids_objets, valeur_objets = random_objets(nb_objets, 10, 10)
    capacite = 20
    for _ in range(5):
      sac = random_solution(10, capacite, poids_objets)                    
      sol_courante = hill_climbing(sac, capacite, poids_objets, valeur_objets)          
      val_courante = valeur_contenu(sol_courante, valeur_objets)
      print("valeur = %d, capacite=%d/%d"        
              %(valeur_contenu(sol_courante, valeur_objets),      
                poids_contenu(sol_courante, poids_objets),       
                capacite))
      if (val_courante > val_max):               
        val_max = val_courante                 
        sol_max = sol_courante     

def test_recherche_tabou():
    nb_objets = 100
    capacite = 20
    random.seed(a=3)
    poids_objets, valeur_objets = random_objets(nb_objets, 10, 10)
    sac = (False,)*nb_objets
    taille_tabou=5
    iter_max=30
    print("tabou de taille 5")
    sol=recherche_tabou(sac, taille_tabou, iter_max, capacite, poids_objets, valeur_objets)
    print("valeur finale = " + str(valeur_contenu(sol, valeur_objets)) + ", capacite="+str(poids_contenu(sol, poids_objets)) + "/" + str(capacite))

def test_recherche_tabou_multistart():
    nb_objets = 100
    capacite = 20
    print("multistart tabou")
    sol, valeur_objets, poids_objets = recherche_tabou_multistart(nb_objets, capacite)
    print("valeur finale = " + str(valeur_contenu(sol, valeur_objets)) + ", capacite="+str(poids_contenu(sol, poids_objets)) + "/" + str(capacite))

def main():
    begin()
    list_tests = [test_random_objets, test_poids_valeur, test_voisinage, test_hill_climbing, test_random_solution, test_recherche_tabou, test_recherche_tabou_multistart]
    for test in list_tests:
        start_test(test.__name__)
        test()
        separators()

if __name__ == '__main__':
    main()