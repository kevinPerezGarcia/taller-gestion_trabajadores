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
    print("################################")
    print("SISTEMA. GESTION DE TRABAJADORES")
    print("################################")

    print("\nMenú de Opciones:\n")
    print("0. Salir")
    print("1. Componente. Registrar trabajador")

    opcion = int(input("\nIngrese una opción vía su código numérico: "))

    if opcion == 0:
        os.system("cls")
        print("¡Usted salió del programa!\n")
        break
    else:
        while True:
            os.system("cls")
            print("====================================")
            print("COMPONENTE. REGISTRO DE TRABAJADORES")
            print("====================================")

            print("\nOpciones:\n")
            print("0. Volver")
            print("1. Acción. Registrar trabajador")

            opcion = int(input("\nIngrese una opción vía su código numérico: "))
            if opcion == 0:
                break
            else:
                print("\nIngrese la siguiente información del trabajador a registrar:\n")
                dct_trabajador['dni'] = input("DNI: ")
                dct_trabajador['nombres_apellidos'] = input("Nombres y apellidos: ")
                dct_trabajador['sexo'] = input("Sexo: ")
                dct_trabajador['edad'] = input("Edad: ")
                dct_trabajador['anio_ingreso'] = input("Año de ingreso: ")
                dct_trabajador['salario'] = input("Salario: ")

                lst_trabajadores.append(dct_trabajador.copy())

                input("\n¡Trabajador registrado! Presione cualquier tecla para continuar.")