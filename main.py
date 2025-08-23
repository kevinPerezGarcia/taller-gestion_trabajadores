import sqlite3
import os

conn = sqlite3.connect('gestion_trabajadores.db')
cursor = conn.cursor()

# Crear registro - C
def crear_usuario(dni: str, nombres_apellidos: str, sexo: str, edad: int, anio_ingreso: int, salario: float):
    
    cursor.execute(
        """
        INSERT INTO trabajadores
        VALUES
        (?, ?, ?, ?, ?, ?)
        """,
        (dni, nombres_apellidos, sexo, edad, anio_ingreso, salario)
    )
    
    conn.commit()

# Obtener registros - R
def obtener_registros():
    
    cursor.execute("SELECT * FROM trabajadores")
    trabajadores = cursor.fetchall()
    
    lst_trabajadores = []
    for trabajador in trabajadores:
        lst_trabajadores.append(trabajador)
    
    print(lst_trabajadores)

if __name__ == "__main__":

    os.system("cls")

    #crear_usuario("2345", "Fulanito Fulanón", "M", 35, 2025, 2000)
    obtener_registros()