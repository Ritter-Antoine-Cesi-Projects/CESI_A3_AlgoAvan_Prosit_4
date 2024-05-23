import random

def begin():
    print("")
    print("Running tests:")
    print("")

def start_test(test_name):
    print("Starting test: " + test_name)
    print("")

def separators():
    print("")
    print("--------------------------------------------------")
    print("")
    
def random_objets(nb_objets, poids_max, val_max):
    poids_objets = {i: random.randint(1, poids_max) for i in range(nb_objets)}
    valeur_objets = {i: random.randint(1, val_max) for i in range(nb_objets)}
    return poids_objets, valeur_objets

def poids_contenu(sac, poids_objets):
    if len(sac) != len(poids_objets):
        raise ValueError("sac and poids_objets must have the same number of elements")
    return sum([poids_objets[k] for k, v in enumerate(sac) if v])

def valeur_contenu(sac, valeur_objets):
    if len(sac) != len(valeur_objets):
        raise ValueError("sac and valeur_objets must have the same number of elements")
    return sum([valeur_objets[k] for k, v in enumerate(sac) if v])

def random_solution(nb_objets, capacite, poids_objets):
    sac = tuple(random.choice([False, True]) for _ in range(nb_objets))
    while (poids_contenu(sac, poids_objets) > capacite):
        objets_presents = tuple(
            i for i, val in enumerate(sac) if val)
        objet_supprime =random.choice(objets_presents)
        sac =sac[:objet_supprime] + (False,) + sac[objet_supprime+1:]                           
    return sac