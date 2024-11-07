from time import sleep
nombre = int(input("entrer un chiffre plus grand que 0 : "))
while nombre > 0:
    print(nombre)
    nombre = nombre - 1
    sleep(1)
print("Le temps est écoulé")