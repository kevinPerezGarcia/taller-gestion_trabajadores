import os

while True:
    os.system("cls")
    print("GESTION DE TRABAJADORES")
    print("-----------------------")
    print("Opciones:")
    print("0. Salir")

    while True:
        opcion = int(input("Ingrese una opción vía su código numérico: "))
        try:
            assert (opcion in [0]) is True
            break
        except AssertionError:
            print("¡Opción numérica incorrecta!. Vuelva a intentarlo.")

    if opcion == 0:
        break