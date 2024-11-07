import random as rnd
x = rnd.randint(0,100)
print(x)
guess = int(input("Entrez une valeur : "))
while guess < x :
    print("Le guess eest trop petit")
    guess = int(input("Entrez une valeur : "))
else :
    print("Le guess est trop grand")
    guess = int(input("Entrez une valeur : "))
if guess == x :
    print("Le guess est correct")

