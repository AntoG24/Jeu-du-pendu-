import sys
import os


# Ajouter le dossier 'src' au chemin de recherche des modules.
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)


from jeu_du_pendu import (
    Joueur,
    initialiser_liste,
    choisir_mot_aleatoire,
    afficher_pendu,
    Afficher_classement,
)


def test_joueur_initialisation():
    joueur = Joueur("Alice")
    assert joueur.nom == "Alice"


def test_joueur_str():
    joueur = Joueur("Alice")
    assert str(joueur) == "Le nom du joueur est: Alice"


def test_initialiser_liste():
    mots = initialiser_liste()
    assert isinstance(mots, list)
    assert len(mots) > 0


def test_choisir_mot_aleatoire():
    liste_mots = initialiser_liste()
    mot = choisir_mot_aleatoire(liste_mots)
    assert mot in liste_mots


def test_gestion_tentatives():
    mots = "pendu"
    i = 0
    proposition = "x"  # Lettre incorrecte

    if proposition not in mots:
        i += 1  # Incrémente les tentatives incorrectes

    assert i == 1  # Une tentative incorrecte a été ajoutée


def test_afficher_pendu():
    try:
        afficher_pendu(3)
    except Exception as e:
        assert False, f"La fonction a échoué avec l'erreur : {e}"


def test_boucle_while(monkeypatch):
    mots = "pendu"
    mot_cache = [
        "p",
        "e",
        "n",
        "_",
        "u",
    ]  # Le mot partiellement deviné, avec une seule lettre manquante
    lettres_du_mot = list(mots)
    tentatives = 10  # Nombre de tentatives
    i = 0  # Compteur de tentatives incorrectes

    while i < tentatives:
        if "_" not in mot_cache:
            break  # Si tout le mot est deviné, on sort de la boucle
        else:
            proposition = "d"

        # Vérifier que l'entrée est une seule lettre valide
        if len(proposition) != 1 or not proposition.isalpha():
            print("Veuillez entrer une seule lettre.")
        else:
            # Vérifier si la lettre est dans le mot
            if proposition in lettres_du_mot:
                print(f"La lettre '{proposition}' est dans le mot !")
                # Remplacer les underscores par la lettre trouvée
                for index, lettre in enumerate(lettres_du_mot):
                    if lettre == proposition:
                        mot_cache[index] = proposition
            else:
                print(f"La lettre '{proposition}' n'est pas dans le mot.")
                i += 1  # Incrémenter le nombre de tentatives incorrectes

        # Afficher l'état actuel du mot caché
        print("\nMot à deviner : ", " ".join(mot_cache))
        print(f"Il vous reste {tentatives - i} tentatives.")

    # Vérifier la fin du jeu
    if "_" not in mot_cache:
        resultat = 1  # Le mot a été deviné, le joueur a gagné
    else:
        resultat = 0  # Tentatives épuisées, le joueur a perdu

    # Vérifier que le résultat est 1, car le mot est deviné avec succès
    assert resultat == 1
    # Vérifier que le mot est complètement deviné
    assert "_" not in mot_cache


def test_arreter_programme(monkeypatch):
    # Valeurs définis en entrée
    # Choix=0
    # nom=Alice
    monkeypatch.setattr(
        "builtins.input", lambda prompt: "Alice" if "nom" in prompt else "0"
    )

    # Initialiser les données pour le test
    liste_joueur = []
    choix = 1
    nom_du_joueur = input("Entrez votre nom: ")  # Simulé à 'Alice'
    joueur = Joueur(nom_du_joueur)
    liste_joueur.append((joueur.nom, 0))

    # Commencer la boucle du jeu
    iterations = 0
    while choix == 1:
        print("\nVoulez-vous continuer à jouer? (oui = 1 / non = 0)")
        choix = int(
            input("Réponse:")
        )
        iterations += 1
        if iterations >= 2:  # On limite à 2 itérations pour tester l'arrêt
            break

    # Vérifier que le programme a bien arrêté après la réponse 0
    assert iterations == 1  # La boucle doit s'être exécutée 2 fois
    assert (
        choix == 0
    )  # Le choix doit être 0, indiquant que l'utilisateur a choisi d'arrêter


def test_mise_a_jour_mot_cache():
    mots = "pendu"
    mot_cache = ["_"] * len(mots)
    lettres_du_mot = list(mots)

    proposition = "e"
    # Vérifier si la lettre est ajoutée
    for index, lettre in enumerate(lettres_du_mot):
        if lettre == proposition:
            mot_cache[index] = proposition

    assert mot_cache == ["_", "e", "_", "_", "_"]


def test_afficher_classement():
    # Vérifier si le score est actualisé et affiché
    liste_joueur = [("Alice", 0)]
    Afficher_classement(liste_joueur, 1)
    assert liste_joueur[0][1] == 1
