nombreinfdix = 0
nombresupdix = 0
nombresup15 = 0
n = -1
i = 0

for i in range(3):
    n = float(input("Entrez un nombre entre 0 et 20 : "))
    while n < 0 or n > 20 :
        print("Le chiffre n est pas entre 0 ou 20")
        n = float(input("Entrez a nouveau la valeur : "))
    if n < 10 :
        nombreinfdix += 1
    elif n >= 15:
        nombresup15 +=1
    else :
         nombresupdix +=1
print("Il y a ",nombreinfdix,"de nombre inferieur a 10, superieur a dix", nombresupdix," superieur a 15",nombresup15)