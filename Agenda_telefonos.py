#En caso de necesitar una agenda vacía borrar estos datos
#Viktor L.
agenda = {"Viktor": "321654987", "Viktor2": "321654987"}

run = True


def nuevo_clave_valor():
    formato_numero = "666666666"
    tu_nombre = str(input("¿Cuál es tu nombre? \n")).title()
    tu_num = str(input("¿Cuál es tu número de teléfono? \n"))
    if len(tu_num) != len(formato_numero):
        print("Solo acepto numeros en formato de España.(9 dígitos)")
        print("Comprueba que tu número este correctamete añadido.")
    else:
        agenda[tu_nombre] = tu_num
        print("Añadido correctamente.")


def ver_agenda():
    if bool(agenda) == False:
        print("Vaya, al parecer no tienes contactos en la agenda.")
    else:
        print(agenda)


def borrar_clave_valor():
    if bool(agenda) == False:
        print("Vaya, al parecer no tienes contactos en la agenda.")
    else:
        print(f"Estos son los contactos que tienes en la agenda\n")
        for k in agenda.keys():
            print(f"---> {k}.")

        nombre_a_borrar = input(
            "Escribe el nombre de la persona que deseas borrar de tu agenda.\n").title()
        agenda.pop(nombre_a_borrar, None)
        print(f"Borrado {nombre_a_borrar} correctamente.")


def buscar_por_numero():

    if bool(agenda) == False:
        print("Vaya, al parecer no tienes contactos en la agenda.")
    else:
        print(f"Estos son los números que tienes en la agenda\n")
        for k in agenda.keys():
            print(f"---> {k}.")
        nombre_a_buscar = str(input(
            "Introduce el nombre de la persona que deseas conocer el número.\n")).title()
        for nombre, numero in agenda.items():
            if nombre == nombre_a_buscar:
                print(f"El número de {nombre}: {numero}.")


def agenda_funcion():
    flag = True
    while flag:
        print("_____________________________")
        print("¿Qué quieres hacer en la agenda?")
        decision = int(input(
            ("|1. Añadir a alguien \n|2. Ver tus contactos. \n|3. Borrar a alguien de la agenda. "
             "\n|4. Borrar toda la agenda. \n|5. Encontrar un número.\n|6. Salir de la agenda. \n")))

        if decision == 1:
            nuevo_clave_valor()

        elif decision == 2:
            ver_agenda()

        elif decision == 3:
            borrar_clave_valor()

        elif decision == 4:
            print("¿Seguro que quieres borrar todos los contactos?")
            seguro = int(
                input("Presiona 1 para confirmar, otra tecla para abortar.\n"))
            if seguro == 1:
                agenda.clear()
                print("Los contactos han sido borrados correctamente.")
            else:
                print("La operación ha sido cancelada correctamente.")
        elif decision == 5:
            buscar_por_numero()
        elif decision == 6:
            flag = False
            break
        else:
            print("Debes presionar una de las teclas mencionadas.")


while run:
    try:
        inicio = int(input("Presiona 1 para abrir la agenda. \n"))
        if inicio == 1:
            agenda_funcion()
        else:
            print("La tecla para iniciar la agenda es el 1")

        # En caso de no introducir ningún caracter para iniciar.
    except ValueError:
        print("Debes de presionar la tecla 1.")
