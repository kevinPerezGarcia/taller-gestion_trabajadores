import os

lst_trabajadores = []
dct_trabajador = {
    "dni": "",
    "nombres_apellidos": "",
    "sexo": "",
    "edad": "",
    "anio_ingreso": "",
    "salario": ""    
}
opciones = [0, 1]

while True:
    os.system("cls")
    print("GESTION DE TRABAJADORES")
    print("-----------------------")
    print("Opciones:")
    print("0. Salir")
    print("1. Registrar trabajador")

    while True:
        opcion = int(input("Ingrese una opción vía su código numérico: "))
        try:
            assert (opcion in opciones) is True
            break
        except AssertionError:
            print("¡Opción numérica incorrecta!. Vuelva a intentarlo.")

    if opcion == 0:
        os.system("cls")
        print("¡Usted salió del programa!")
        break
    else:
        while True:
            os.system("cls")
            print("REGISTRO DE TRABAJADORES")
            print("------------------------")
            opcion = input("Ingrese 000 para volver al menú de opciones: ")
            if opcion == '000':
                break
            
