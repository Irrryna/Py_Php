import unicodedata

def nettoyer(texte):
    # Met tout en minuscules
    texte = texte.lower()
    # Enlève les accents
    texte = ''.join(
        c for c in unicodedata.normalize('NFD', texte) #décompose les caractères accentués
        if unicodedata.category(c) != 'Mn'   #Mark Nonspacing → on supprime accents
    )
    # Garde uniquement les lettres (pas d’espaces, pas de ponctuation)
    texte = ''.join(c for c in texte if c.isalpha()) #ne garde que les lettres
    return texte

def est_palindrome(phrase):
    propre = nettoyer(phrase)
    longueur = len(propre)
    for i in range(longueur // 2):
        if propre[i] != propre[longueur - i - 1]:
            return False
    return True

print(est_palindrome("Ésope reste ici et se repose"))  # Affiche True
