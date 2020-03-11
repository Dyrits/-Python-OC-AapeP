import random
import os
from donnees import *
from fonctions import *

# Le nombre de joueurs est défini. On limite cependant cela à 6:
nombre_de_joueurs = None
while not nombre_de_joueurs:
    try:
        nombre_de_joueurs = int(input("Entrez le nombre de joueurs : "))
        if nombre_de_joueurs > 6 or nombre_de_joueurs < 1:
            print("Le nombre de joueurs minimum est de 1 et le maximum est 6. Veuillez saisir une autre valeur.")
            nombre_de_joueurs = None
    except:
        print("Veuillez saisir un nombre entre 1 et 6.")
        nombre_de_joueurs = None

# Le nom des joueurs est défini:
while len(dictionnaire_scores) != nombre_de_joueurs:
    for index in range(nombre_de_joueurs):
        dictionnaire_scores.update(
            {input(f"Quel est le nom du joueur {index + 1} ? "): 0})
    if len(dictionnaire_scores) != nombre_de_joueurs:
        print("Deux joueurs ont le même nom ? Veuillez recommencer et leur donner des noms différents.")

# Les noms des joueurs et scores sont affichés :
afficher_score(dictionnaire_scores)

fin_du_jeu = False
while fin_du_jeu == False:

    # Le mot à deviner est choisi aléatoirement et mise en forme dans de listes qui pourront être comparée et mise à jour facilement :
    mot_cible = random.choice(list(dictionnaire_mots.keys()))
    liste_cible = mise_en_forme(mot_cible)
    liste_mystere = mise_en_forme_mystere(mot_cible)

    # Le mot mystère est affiché :
    print(f"\nDevinez le mot en moins de {dictionnaire_mots[mot_cible]} tentatives.\n")
    affichage_mystere(liste_mystere)

    # Chaque mot a un nombre de points différents associé :
    points = dictionnaire_mots[mot_cible]

    # Le premier joueur est défini :
    joueur_actif = 0

    while not liste_cible == liste_mystere:

        nom_du_joueur = list(dictionnaire_scores.keys())[joueur_actif]
        print(f"\nC'est au tour de {nom_du_joueur} !")

        # Le joueur peut choisir une lettre ou directement essayer de deviner le mot :
        choix_joueur = input("Veuillez choisir une lettre ou essayez de deviner le mot: ")

        # Si le joueur trouve le bon mot :
        if choix_joueur.upper() == mot_cible:
            liste_cible = liste_mystere
            print(f"Bravo! Vous avez deviné le mot : {mot_cible} ! Vous remportez {points} points !")
            dictionnaire_scores[nom_du_joueur] += points
            afficher_score(dictionnaire_scores)
            break

        # Si le joueur trouve une lettre correcte :
        elif choix_joueur.upper() in liste_mystere:
            print("Cette lettre a déjà été révélée ! Tant pis pour vous, vous avez gaspillé un tour...")

        elif choix_joueur.upper() in mot_cible:
            print(f"Bravo, la lettre {choix_joueur.upper()} est bien présente dans le mot !\n")
            for index, lettre in enumerate(liste_cible):
                if choix_joueur.upper() == lettre:
                    liste_mystere[index] = liste_cible[index]
            affichage_mystere(liste_mystere)
            if liste_cible == liste_mystere:
                print(f"Bravo! Vous avez deviné le mot : {mot_cible} ! Vous remportez {points} points !")
                dictionnaire_scores[nom_du_joueur] += points
                afficher_score(dictionnaire_scores)
                break
        else:
            print("Non, pas une bonne lettre, pas un bon mot...\n")
            affichage_mystere(liste_mystere)

        # Le tour du joueur est terminé. C'est au tour du joueur suivant.
        if joueur_actif + 1 < nombre_de_joueurs:
            joueur_actif += 1
        else:
            joueur_actif = 0

        points -= 1
        print(f"\nIl vous reste {points} tour(s) pour deviner le mot.")
        if points == 0:
            print("Cette manche est perdue !")
            break

    # Le mot est retiré du dictionnaire :
    del dictionnaire_mots[mot_cible]
    if dictionnaire_mots == {}:
        print("Il n'y a plus de mot à deviner. La partie est terminée.")
        break

    # Les joueurs peuvent continuer à jouer ou non :
    fin_du_jeu = None
    while fin_du_jeu == None:
        fin_du_jeu = str(input("Voulez-vous continuer ? (O/N)").lower())
        if fin_du_jeu != "o" and fin_du_jeu != "n":
            print("Entrez O pour OUI or N pour NON.")
            fin_du_jeu = None
    if fin_du_jeu == "n":
        fin_du_jeu = True
        print("La partie est terminée !")
    else: 
        fin_du_jeu = False
        print("La partie continue !")

os.system("Pause")
