from utils import limpiar_consola

def interfaz() -> None:
    limpiar_consola()
    print("################################")
    print("SISTEMA. GESTION DE TRABAJADORES")
    print("################################")

    print("\nMenú de Opciones:\n")
    print("0. Salir")
    print("1. Componente. Registrar trabajador")
    print("2. Componente. Listar trabajadores")
    print("3. Componente. Consultar trabajador")
    print("4. Componente. Eliminar trabajador")
    print("5. Componente. Modificar trabajador")

    opcion = int(input("\nIngrese una opción vía su código numérico: "))
    return opcion