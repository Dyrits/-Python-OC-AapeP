def mise_en_forme(mot):
    return [lettre for lettre in list(mot)]

def mise_en_forme_mystere(mot):
    return ["_" for lettre in list(mot)]

def affichage_mystere(liste):
    print(" | ".join(liste))

def afficher_score(dictionnaire_scores):
    print("\nListe et score des joueurs :")
    for nom, score in dictionnaire_scores.items():
        print(f"{nom} : {score} points")
