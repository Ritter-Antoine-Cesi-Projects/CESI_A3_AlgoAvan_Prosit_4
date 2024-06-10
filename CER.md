# Prendre connaissance de la situation et la clarifier

## Contexte

Suite à notre modélisation nous souhaitons utiliser une métaheuristique,
il nous reste à déterminer laquelle.

## Mots Clefs

- Étape d’intensification
- Algorithme génétique
- Métaheuristique
- Hill climbing
- Méthode à voisinages
- Optimum local
- Diversification
- Algo tabou
- Rugosité du voisinage
- GRASP
- Métaheuristique par trajectoire/par population
- VRP géométrique
- Méthodes perturbatives
- Recuit simulé
- Test statistique
- Borne inférieure
- Modélisation de voisinage
- Plan d’expérience
- Instance
- Colonie de fourmis

# **Analyse du Besoin**

## **Problème(s)**

- Quelle métaheuristique utiliser ?
- Comment réaliser des tests statistiques ?
- Comment évaluer nos résultats ?

## **Contraintes**

- Utilisation des métaheuristiques
- VRP
- Le temps de résolution doit être raisonnable (bien que le
problème soit NP-complet)

## **Livrables**

- Choix de la métaheuristique
- Recommandations de paramétrage de la métaheuristique
- Générations d’instances
- Tests statistiques

# **Généralisation du problème**

- Métaheuristiques

# Pistes de solutions

- Les algorithmes génétiques sont des métaheuristiques (Antoine
Faure)
- Les solutions des algorithmes génétiques peuvent subir des
mutations (Léo Rouas)
- Les métaheuristiques ont deux phases :
o Intensification, se rapprocher d’une bonne solution
o Diversification, apporter de nouvelles solutions pour éviter de
rester bloquer dans un optimum local (Julien Wolff)
- L’algorithme génétique que nous allons utiliser va générer un
grand nombre de solutions (Matthis Pinheiro-Cruz)
- Le principe de l’algorithme de recuit simulé serait de tester une
solution en faisant varier une variable au cours du temps pour
trouver la solution attendue (Gabriel Anciaux)
- Pour ce problème de VRP, une méthode de métaheuristique par
population sera plus adaptée que par trajectoire (Antonin
Bourrel)
- Dans notre cas le VRP géométrique serait plus adapté que le VRP
simple (Raphaël Denni)

# **Plan d’action**

- Se renseigner sur le plan d’expérience
- Se renseigner sur les algorithmes génétiques et les colonies de
fourmis

# **Notion de cours**

## Mots clefs

### **Étape d’intensification**

Processus dans les algorithmes de recherche heuristique où l'exploration est concentrée autour des solutions prometteuses déjà découvertes, dans le but de trouver des solutions optimales locales ou d'améliorer les solutions existantes.

### **Algorithme génétique**

Algorithme de recherche inspiré du processus de sélection naturelle. Il utilise des opérations telles que la sélection, le croisement et la mutation pour évoluer une population de solutions candidates vers des solutions optimales.

### **Métaheuristique**

Stratégie générale de résolution de problèmes d'optimisation qui guide d'autres heuristiques pour explorer efficacement l'espace de recherche et trouver des solutions proches de l'optimum global.

### **Hill climbing**

Algorithme de recherche locale qui commence par une solution arbitraire et fait des modifications incrémentales pour améliorer la solution, en se déplaçant toujours vers des solutions voisines meilleures.

### **Méthode à voisinages**

Approche où la solution est améliorée par des modifications locales dans un ensemble de solutions voisines. Les méthodes incluent souvent des algorithmes comme hill climbing et les algorithmes de recherche tabou.

### **Optimum local**

Solution qui est meilleure que toutes les solutions voisines, mais qui peut ne pas être la meilleure solution possible dans l'ensemble de l'espace de recherche (optimum global).

### **Diversification**

Stratégie dans les algorithmes de recherche qui vise à explorer de nouvelles régions de l'espace de recherche pour éviter de se bloquer dans des optima locaux et améliorer la probabilité de trouver l'optimum global.

### **Algo tabou**

Algorithme de recherche qui utilise une mémoire pour éviter les cycles et guider la recherche loin des solutions précédemment explorées, en marquant certaines solutions comme "taboues" pour une période de temps.

### **Rugosité du voisinage**

Concept qui décrit la variabilité ou l'irrégularité de l'espace de recherche autour d'une solution donnée, influençant la difficulté de trouver un optimum local ou global.

### **GRASP (Greedy Randomized Adaptive Search Procedure)**

Méthode métaheuristique qui combine des techniques gloutonnes (greedy) avec des éléments aléatoires pour construire des solutions initiales, suivie d'une phase de recherche locale pour améliorer ces solutions.

### **Métaheuristique par trajectoire/par population**

- **Par trajectoire** : Algorithmes qui explorent l'espace de recherche en suivant un chemin continu de solutions, comme hill climbing ou recuit simulé.
- **Par population** : Algorithmes qui maintiennent et évoluent une population de solutions simultanément, comme les algorithmes génétiques et les colonies de fourmis.

### **VRP géométrique (Vehicle Routing Problem)**

Problème d'optimisation où l'objectif est de trouver les routes optimales pour une flotte de véhicules afin de desservir un ensemble de clients avec des contraintes géométriques spécifiques.

### **Méthodes perturbatives**

Méthodes qui améliorent les solutions en apportant des modifications perturbatrices contrôlées aux solutions actuelles, souvent utilisées pour échapper aux optima locaux.

### **Recuit simulé**

Algorithme inspiré du processus de recuit métallurgique. Il utilise une température décroissante pour contrôler l'acceptation de solutions pires dans le but d'échapper aux optima locaux et trouver un optimum global.

### **Test statistique**

Méthode utilisée pour déterminer si une hypothèse sur un ensemble de données est statistiquement significative, souvent utilisée pour valider des résultats expérimentaux.

### **Borne inférieure**

Estimation ou calcul du plus bas niveau possible qu'une solution optimale peut atteindre, souvent utilisé pour évaluer la performance d'algorithmes d'approximation.

### **Modélisation de voisinage**

Processus de définition des règles ou méthodes par lesquelles les solutions voisines sont générées ou explorées à partir d'une solution courante dans les algorithmes de recherche locale.

### **Plan d’expérience**

Stratégie expérimentale utilisée pour planifier, réaliser et analyser des expériences de manière à optimiser les ressources et obtenir des données fiables et significatives.

### **Instance**

Représentation spécifique d'un problème d'optimisation, avec des paramètres et des données spécifiques, utilisée pour tester et évaluer des algorithmes.

### **Colonie de fourmis**

Algorithme inspiré du comportement des colonies de fourmis dans la nature, utilisant des agents autonomes (fourmis) pour explorer l'espace de recherche et construire des solutions basées sur la communication indirecte via des phéromones.

# Solutions

# Ressources

[Précis de recherche opérationnelle  : Méthodes et exercices d'application Ed. 6 - ScholarVox Université](https://univ.scholarvox.com/reader/docid/45006309/page/420)

[Recherche opérationnelle : Méthodes d'optimisation en gestion Ed. 1 - ScholarVox Université](https://univ.scholarvox.com/reader/docid/88829335/page/182)

[Métaheuristiques : Recuits simulé, recherche avec tabous, recherche à voisinages variables, méthodes GRASP, algorithmes évolutionnaires, fourmis artificielles, essaims particulaires et autres méthodes d'optimisation Ed. 2 - ScholarVox Université](https://univ.scholarvox.com/reader/docid/88818856)