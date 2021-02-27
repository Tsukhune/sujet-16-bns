def moyenne(tab):
    somme = 0
    for chiffre in tab:
        somme += chiffre
    moyenne = chiffre / len(tab)
    return moyenne
