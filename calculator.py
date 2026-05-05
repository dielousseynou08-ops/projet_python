#calculatrice

def additioner(a : float, b:float ) ->float:
    sum = a + b
    return f"le résultat de votre opération est de {sum}"

def soustraction(a : float, b:float ) ->float:
    sous = a - b
    return f"le résultat de votre opération est de {sous}"


def multiplier(a : float, b:float ) ->float:
    p = a * b
    return f"le résultat de votre opération est de {p}"

def diviser (a : float, b:float ) ->float:
    if b == 0:
        d = "Opération impossible"
    else:
        d = a / b

    return f" le résultat de votre opération est de {d}"

def nombre():
    a = float(input("Entrer le 1er nombre : "))
    b = float(input("Entrer le 2er nombre : "))
    return a, b



menu = """ Mini calculatrice !
1. Addition
2. Soustraction
3. Multiplication
4. Division \n""" 

print(menu)

while True:
    operation = input("Choissisez une opération à faire : ")
    if operation in ["1","2","3","4"]:
        try:
            if operation == "1":
                a, b = nombre()
                resultat = additioner(a, b)
                print(resultat)

            elif operation == "2":
                a, b = nombre()
                resultat = soustraction(a,b)
                print(resultat)

            elif operation == "3":
                a, b = nombre()
                resultat = multiplier(a, b)
                print(resultat)

            elif operation == "4":
                a, b = nombre()
                resultat = diviser(a, b)
                print(resultat)
                
        except :
            print("Opération impossible !")
    else:
        print("choissisez une opération valide !")
        break
    





