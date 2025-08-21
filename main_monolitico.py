lst_trabajadores = []
dct_trabajador = {
    "dni": "",
    "nombres_apellidos": "",
    "sexo": "",
    "edad": "",
    "anio_ingreso": "",
    "salario": ""    
}


def registrar_trabajador() -> None:
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


def listar_trabajadores() -> None:
    while True:
        limpiar_consola()
        print("=================================")
        print("COMPONENTE. LISTA DE TRABAJADORES")
        print("=================================")
        print("\nOpciones:\n")
        print("0. Volver")
        print("1. Acción. Listar trabajadores")
        
        opcion = int(input("\nIngrese una opción vía su código numérico: "))

        if opcion == 0:
            break
        elif opcion == 1:
            limpiar_consola()
            print("---------------------")
            print("LISTA DE TRABAJADORES")
            print("---------------------\n")
            print("DNI    Nombres y Apellidos Sexo   Edad   Año de Ingreso Salario")
            print("...... ................... ...... ...... .............. .......")
            for trabajador in lst_trabajadores:
                print(f"{trabajador["dni"]:<6}", end=" ")
                print(f"{trabajador["nombres_apellidos"]:<19}", end=" ")
                print(f"{trabajador["sexo"]:<6}", end= " ")
                print(f"{trabajador["edad"]:<6}", end=" ")
                print(f"{trabajador["anio_ingreso"]:<14}", end=" ")
                print(f"{trabajador["salario"]:<7}")
            input("\nPulse la tecla 'ENTER' para continuar.")


def consultar_trabajador() -> None:
    while True:
        limpiar_consola()
        print("==================================")
        print("COMPONENTE. CONSULTA DE TRABAJADOR")
        print("==================================")
        print("\nOpciones:\n")
        print("0. Salir")
        print("1. Acción. Consultar trabajador")

        opcion = int(input("\nIngrese una opción vía su código numérico: "))
        if opcion == 0:
            break
        elif opcion == 1:
            limpiar_consola()
            print("----------------------------")
            print("ACCION. CONSULTAR TRABAJADOR")
            print("----------------------------")
            dni_a_buscar = input("\nIngrese el DNI del trabajador a consultar: ")

            for ind, trabajador in enumerate(lst_trabajadores):
                if trabajador["dni"] == dni_a_buscar:
                    tpl_consulta = (True, ind, trabajador)
                else:
                    tpl_consulta = (False, None)

            if tpl_consulta[0]:
                dct_trabajador_consultado = tpl_consulta[2]
                print("")
                print(f"DNI:                 {dct_trabajador_consultado["dni"]}")
                print(f"Nombres y apellidos: {dct_trabajador_consultado["nombres_apellidos"]}")
                print(f"Sexo:                {dct_trabajador_consultado["sexo"]}")
                print(f"Edad:                {dct_trabajador_consultado["edad"]}")
                print(f"Año de ingreso:      {dct_trabajador_consultado["anio_ingreso"]}")
                print(f"Salario:             {dct_trabajador_consultado["salario"]}")
            else:
                print(f"\n¡Trabajador, con DNI: {dni_a_buscar}, no registrado!")
            
            input("\nPulse la tecla 'ENTER' para continuar.")


def eliminar_trabajador() -> None:
    while True:
        limpiar_consola()
        print("=====================================")
        print("COMPONENTE. ELIMINACION DE TRABAJADOR")
        print("=====================================")
        print("\nOpciones:\n")
        print("0. Volver")
        print("1. Acción. Eliminar trabajador")
        opcion = int(input("\nIngrese una opción vía su código numérico: "))
        if opcion == 0:
            break
        elif opcion == 1:
            limpiar_consola()
            print("---------------------------")
            print("ACCION. ELIMINAR TRABAJADOR")
            print("---------------------------")

            dni_a_eliminar = input("\nIngrese el DNI del trabajador a eliminar: ")

            for ind, trabajador in enumerate(lst_trabajadores):
                if trabajador["dni"] == dni_a_eliminar:
                    tpl_eliminacion = (True, ind, trabajador)
                else:
                    tpl_eliminacion = (False, None)

            if tpl_eliminacion[0]:
                confirmacion_de_eliminacion = input(f"\n¿Está seguro que desea eliminar el registro del trabajador cuyo DNI es {dni_a_eliminar}? (S/N): ").upper()
                if confirmacion_de_eliminacion == 'N':
                    continue
                else:
                    indice = tpl_eliminacion[1]
                    del lst_trabajadores[indice]
                    print(f"\n¡Registro del trabajador con DNI '{dni_a_eliminar}' eliminado!")
                    input("\nPresione la tecla 'ENTER' para continuar.")
            else:
                print(f"\n¡Trabajador, con DNI: {dni_a_eliminar}, no registrado!")


def modificar_trabajador() -> None:
    while True:
        limpiar_consola()
        print("======================================")
        print("COMPONENTE. MODIFICACION DE TRABAJADOR")
        print("======================================")
        print("\nOpciones:\n")
        print("0. Volver")
        print("1. Acción. Modificar trabajador")

        opcion = int(input("\nIngrese una opción vía su código numérico: "))

        if opcion == 0:
            break
        elif opcion == 1:
            limpiar_consola()
            print("----------------------------------")
            print("ACCION. MODIFICACION DE TRABAJADOR")
            print("----------------------------------")
            dni_a_modificar = input("\nIngrese el DNI del trabajador a modificar: ")
            for ind, trabajador in enumerate(lst_trabajadores):
                if trabajador["dni"] == dni_a_modificar:
                    tpl_modificacion = (True, ind, trabajador)
                else:
                    tpl_modificacion = (False, None)
            
            if tpl_modificacion[0]:
                confirmacion_modificacion = input(f"\n¿Está seguro que desea modificar el registro del trabajador cuyo DNI es '{dni_a_modificar}'? (S/N): ").upper()
                if confirmacion_modificacion == "N":
                    continue
                else:
                    indice = tpl_modificacion[1]
                    print("")
                    dct_trabajador["dni"] = dni_a_modificar
                    dct_trabajador["nombres_apellidos"] = input("Nombres y apellidos: ")
                    dct_trabajador["sexo"] = input("Sexo: ")
                    dct_trabajador["edad"] = input("Edad: ")
                    dct_trabajador["anio_ingreso"] = input("Año de ingreso: ")
                    dct_trabajador["salario"] = input("Salario: ")
                    lst_trabajadores[indice] = dct_trabajador

                    print(f"\n¡Registro del trabajador con DNI '{dni_a_modificar}', modificado!")
                    input("\nPresione la tecla 'ENTER' para continuar.")
            else:
                print(f"\n¡Trabajador, con DNI: {dni_a_modificar}, no registrado!")


