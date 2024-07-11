import random

def jouer_jeu():
    print("Bienvenue dans le jeu de 'deviner le nombre !'")
    print("Je vais choisir un nombre entre 1 et 100. A vous de deviner")

    nombre_a_deviner = random.randint(1,100)
    tentative = 0

    while True :
        tentative += 1
        guess = int(input("Entrer votre devinette : "))

        if guess < nombre_a_deviner :
            print ("Trop bas !  Essayez encore")
        elif guess > nombre_a_deviner :
            print("Trop haut ! Essayez encore")
        else:
            print("Bravo vous avez deviné le nombre")
            break

def main():
    jouer_jeu()
    rejouer = input ("Voulez-vous jouer à nouveau ? (oui/non)").lower()
    if rejouer == "oui" :
        jouer_jeu()
    else :
        print("Merci bye bye !")


if __name__ == "__main__":
    main()
