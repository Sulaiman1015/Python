nom = input("quel est votre nom?")
age = 0
while age == 0:
    age_str = input("quel age avez vous?")
    try:
        age = int(age_str)

    except:
        print("Entrez numero uniquement pour l'age")
# print("fin de la boucle")
print("mon nom est " + nom + "," + "j'ai " + str(age) + " ans.")
print("l'age prochain est "+str(age+1)+" ans.")


# boucle while-->tant que
# n = 0
# while n < 5:
#     n = n+1
#     print(n)

# mot_de_pass = ""
# while not mot_de_pass == "toto":
#     mot_de_pass = input("entre votre mot de pass correctement:")
#     while mot_de_pass == "toto":
#         print("bon code")
#         break

