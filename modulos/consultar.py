from utils import limpiar_consola

def consultar_trabajador(lst_trabajadores: list) -> None:
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
