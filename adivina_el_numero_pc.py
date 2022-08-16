import random


def adivina_el_numero_pc(x):

    print("******************")
    print("Bienvenido al Juego e Pc Mas Epico")
    print("******************")
    print(f"Selecciona un numero entre 1 y {x} y la pc adivinara")

    limite_inferior = 1
    limite_superior = x

    respuesta = ""
    while respuesta != "c":
        #Generar una prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)  # [1, 10]
        else:
            prediccion = limite_inferior

            #obtener una respuesta del usuario
        respuesta = input(f"Mi predicccion es {prediccion}. Si es muy alta, ingresa (A): . Si es muy baja, ingresa (B): . Si es corecta, ingresa (C): ").lower()

        if respuesta == "a":
            limite_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1

    print(f"Felcitaciones!! La pc adivino tu numero tontito: {prediccion}")


adivina_el_numero_pc(10)



        # Intervalo inicial: [1, 10]
        # Prediccion: 6
        # Respuesta : "a"
        # Itervalo: [1, 5]

