from utils import poids_contenu

def voisinage(sac, capacite, poids_objets):
    for k in range(len(sac)):
        tempo_sac = list(sac)
        tempo_sac[k] = not tempo_sac[k]
        if poids_contenu(tempo_sac, poids_objets) <= capacite:
            yield tempo_sac