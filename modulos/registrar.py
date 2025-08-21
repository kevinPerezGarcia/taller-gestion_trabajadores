from utils import limpiar_consola

def registrar_trabajador(lst_trabajadores: list) -> None:

        dct_trabajador = {}

        while True:
            limpiar_consola()
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