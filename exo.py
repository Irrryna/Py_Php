# nombre1 = input("Entrez un nombre : ")
# print("Le nombre est : ", nombre1)

# nombre1 = int(input("Entrez un nombre entier : "))
# print("Le nombre entier est : ", nombre1)

# nombre2 = float(input("Entrez un nombre à virgule : "))
# print("Le nombre à virgule est : ", nombre2)

# notes = [15, 17, 20]
# somme = sum(notes) # Calcule la somme des notes
# print("La somme des notes est : ", somme)

# moyenne = somme / len(notes) # Calcule la moyenne des notes
# print("La moyenne des notes est : ", moyenne)

# nombre_notes = len(notes) # Retourne le nombre d'éléments dans la liste 'notes'
# print("Le nombre de notes est : ", nombre_notes)

# notes.append(12) # Ajoute une note à la liste
# print("La nouvelle liste des notes est : ", notes)

# max_nombre = max([3, 58, 11, 21]) # Retourne 58
# print("Le nombre maximum est : ", max_nombre)

# notes = [15, 17, 20]
# somme = 0

# for note in notes:
#     somme += note

# print("Somme des notes :", somme)

# compteur = 1

# while compteur <= 5:
#     print("Valeur actuelle :", compteur)
#     compteur += 1  # on ajoute 1 à chaque tour

# reponse = ""

# while reponse != "ok":
#     reponse = input("Tape 'ok' pour continuer : ")

# print("Merci, tu as compris !")

# phrase = "Le test logiciel est essentiel"
# mots = phrase.split(' ') # Divise la phrase en mots
# print("Liste des mots :", mots)

# def addition(a, b):
#     return a + b
#     resultat = addition(5, 3)
#     print("Le résultat de l'addition est :", resultat)

for i in range(1, 6):
    print(i) # Affiche les nombres de 1 à 5

def inverser_chaine(chaine):
    chaine_inversee = ''
    size = len(chaine)
    for i in range(size):
        char = chaine[i]
        chaine_inversee = char + chaine_inversee
    return chaine_inversee

mot = "Bonjour"
mot_inverse = inverser_chaine(mot)    
print("Le mot inversé est :", mot_inverse)


def somme_liste(liste):
    somme = 0
    for i in liste:
        somme += i
    return somme

print(somme_liste([1, 2, 3, 4])) # Affiche 10

def plus_grand_nombre(liste):
    max_nombre = liste[0]
    for i in liste:
        if i > max_nombre:
            max_nombre = i
    return max_nombre
print(plus_grand_nombre([3, 58, 11, 21])) # Affiche 58

def factorielle(n):
 resultat = n
 for i in range(1, n):
    resultat *= i
 return resultat
print(factorielle(5)) # Affiche 120

def est_palindrome(mot):
 longueur = len(mot)
 for i in range(longueur // 2):
    if mot[i] != mot[longueur - i - 1]:
        return False
        return True
print(est_palindrome("radar")) # Affiche True