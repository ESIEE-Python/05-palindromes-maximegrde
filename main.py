#### Fonction secondaire
"""Programme qui vérifie si une liste de caractères est
 un palindrome à l'aide d'une fonction auxiliaire"""
def ispalindrome(p):
    """Test si la chaine de caractère p est un palindrome"""
    p = p.lower()
    table = str.maketrans("éèêëàîïçûüùôö","eeeeaiicuuuoo"," '-_:;?!,&")
    p = p.translate(table)
    if p == p[::-1]:
        return True
    return False
#### Fonction principale


def main():
    """Teste si les mots de la liste de caractères sont des palindromes"""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
