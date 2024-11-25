import random
import os
import unicodedata
import nltk
from nltk.corpus import words

nltk.download("words")


class Joueur:
    def __init__(self, nom):
        """
        Initialise un joueur avec son nom.
        :param nom: Le nom du joueur
        """
        self.nom = nom

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères.
        :return: Le nom du joueur
        """

        return f"Le nom du joueur est: {self.nom}"


def initialiser_liste():
    # Créer une instance du correcteur orthographique pour le français

    mots = words.words()

    return mots


def choisir_mot_aleatoire(liste_mots):
    """
    Choisit un mot aléatoire dans la liste de mots.
    :param liste_mots: La liste des mots à partir de laquelle choisir
    :return: Le mot choisi aléatoirement
    """
    # Choisir un mot aléatoire dans la liste
    mot_inconnu = random.choice(liste_mots)

    return mot_inconnu


def afficher_pendu(i):
    # Fonction qui affiche l'état du pendu en fonction du nombre d'erreurs (i)
    etats_pendu = [
        """
        """,
        """
               |
               |
               |
        =========
        """,
        """
               |
               |
               |
               |
               |
        =========
        """,
        """
           -----
               |
               |
               |
               |
               |
        =========
        """,
        """
           -----
          |    |
               |
               |
               |
               |
        =========
        """,
        """
           -----
          |    |
          O    |
               |
               |
               |
        =========
        """,
        """
           -----
          |    |
          O    |
          |    |
               |
               |
        =========
        """,
        """
           -----
          |    |
          O    |
         /|    |
               |
               |
        =========
        """,
        """
           -----
          |    |
          O    |
         /|\\   |
               |
               |
        =========
        """,
        """
           -----
          |    |
          O    |
         /|\\   |
         /     |
               |
        =========
        """,
        """
           -----
          |    |
          O    |
         /|\\   |
         /\\    |
               |
        =========
        """,
    ]

    print(etats_pendu[i])


def Jouer(mots):
    # Normalise les mots sans accents
    mots = "".join(
        c for c in unicodedata.normalize("NFD", mots)
        if unicodedata.category(c) != "Mn"
    )

    mot_cache = ["_"] * len(mots)
    # La première et dernière lettre sont visibles
    mot_cache[0] = mots[0]
    mot_cache[-1] = mots[-1]

    lettres_du_mot = list(mots)

    print("\nVoici le mot à deviner:", " ".join(mot_cache))

    tentatives = 10  # Nombre de tentatives
    i = 0  # Compteur de tentatives incorrectes

    while i < tentatives:
        if "_" not in mot_cache:
            break
        else:
            proposition = input("Proposez une lettre : ").lower()

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

            os.system("clear")
            # Afficher l'état actuel du mot caché
            afficher_pendu(i)
            print("\nMot à deviner : ", " ".join(mot_cache))
            print(f"Il vous reste {tentatives-i} tentatives.")

    # Vérifier la fin du jeu
    if "_" not in mot_cache:
        print("Félicitations ! Vous avez deviné le mot.")
        resultat = 1

    else:
        print(f"Game Over ! Le mot était : {mots}")
        resultat = 0

    return resultat


def Afficher_classement(liste_joueur, resultat):
    # Affichage du titre du classement
    print("\n" + "-" * 10 + " CLASSEMENT " + "-" * 10)

    if resultat == 1:
        liste_joueur[0] = (liste_joueur[0][0], liste_joueur[0][1] + 1)
    else:
        liste_joueur[0] = (liste_joueur[0][0], liste_joueur[0][1])

    print("")
    # Affichage du nom du joueur et de son score
    print(f"Joueur: {liste_joueur[0][0]}\t\t\tScore: {liste_joueur[0][1]}")
    # Ligne de séparation après l'affichage
    print("" + "-" * 30)

    return


if __name__ == "__main__":
    # Demander le nom du joueur
    liste_joueur = []
    choix = 1
    nom_du_joueur = input("Entrez votre nom: ")
    joueur = Joueur(nom_du_joueur)
    liste_joueur.append((joueur.nom, 0))
    liste_mots = initialiser_liste()

    while choix == 1:
        mot_inconnu = choisir_mot_aleatoire(liste_mots)
        resultat = Jouer(mot_inconnu)
        Afficher_classement(liste_joueur, resultat)
        print("\nVoulez-vous continuer à jouer? (oui = 1 / non = 0)")
        choix = int(input("Réponse:"))
        os.system("clear")
