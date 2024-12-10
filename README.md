# Jeu du Pendu

Un jeu du pendu simple et amusant développé en Python.

## Documentation 

- La documentation explicitant les classes et fonctions employées dans ce programme est accessible au format HTML via la commande :
  `start _build\html\index.html`

## Fonctionnalités

- Devinez un mot choisi aléatoirement en proposant des lettres.
- Gestion du nombre de tentatives limitées.
- Affichage graphique du pendu à chaque tentative incorrecte.
- Classement des scores pour suivre vos réussites.

## Installation

1. Clonez le dépôt :  
   `git clone https://github.com/<AntoG24>/jeu-du-pendu.git`
   OU `git clone https://github.com/AntoG24/Jeu-du-pendu-.git`
   `cd jeu-du-pendu`  

3. Installez les dépendances nécessaires :  
   `pip install -r requirements.txt`

## Utilisation

Pour lancer le jeu, exécutez le fichier principal :  
`python main.py`  
OU `python src/jeu_du_pendu.py`

Lors de l'exécution, le programme :  
1. Demande votre nom.  
2. Choisit un mot à deviner aléatoirement.  
3. Vous invite à proposer des lettres jusqu'à deviner le mot ou épuiser vos tentatives.  

Exemple d'affichage en cours de partie :  
`Mot à deviner : p _ _ _ a`  
`Il vous reste 7 tentatives.`  

## Structure du projet

- `src/` : dossier principal contenant le jeu.  
- `tests/` : dossier contenant les tests unitaires pour vérifier le bon fonctionnement du jeu.  
- `requirements.txt` : liste des dépendances Python nécessaires au projet.  

## Tests

Pour exécuter les tests unitaires et vérifier que tout fonctionne correctement :  
`pytest`

## Contribution

Contributions bienvenues ! Suivez ces étapes pour contribuer :  
1. Forkez ce dépôt.  
2. Créez une branche pour vos modifications (`git checkout -b ma-nouvelle-fonctionnalité`).  
3. Committez vos changements (`git commit -m "Ajout d'une nouvelle fonctionnalité"`).  
4. Poussez sur votre branche (`git push origin ma-nouvelle-fonctionnalité`).  
5. Ouvrez une Pull Request.  

## Licence

Ce projet n'a pas encore de licence spécifiée.

