import os
import json

#Mostrando Menu a elegir
def mostrar_menu():
    print("\n=== CRUD de Empresas ===")
    print("1. Registrar ")
    print("2. Mostrar ")
    print("3. Actualizar ")
    print("4. Eliminar ")
    print("5. Guardar en archivo de texto")
    print("6. Salir")
    
    
#Cargar Datos en formato txt
def cargar_datos():
    if os.path.exists("empresas.txt"):
        with open("empresas.txt", "r") as archivo:
            return json.load(archivo)
    return []
#Guardar datos de empresa
def guardar_datos(empresas):
    with open("empresas.txt", "w") as archivo:
        json.dump(empresas, archivo, indent=4)

#Registrar empresa
def registrar_empresa(empresas):
    nombre = input("Ingrese el nombre de la empresa: ")
    direccion = input("Ingrese la dirección de la empresa: ")
    telefono = input("Ingrese el teléfono de la empresa: ")
    empresa = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono
    }
    empresas.append(empresa)
    print("Empresa registrada con éxito.")

#Mostrar empresas registradas
def mostrar_empresas(empresas):
    if not empresas:
        print("No hay empresas registradas.")
        return
    for i, empresa in enumerate(empresas):
        print(f"{i + 1}. {empresa['nombre']} - {empresa['direccion']} - {empresa['telefono']}")

#Actualizar empresas registradas
def actualizar_empresa(empresas):
    mostrar_empresas(empresas)
    try:
        indice = int(input("Ingrese el número de la empresa a actualizar: ")) - 1
        if indice < 0 or indice >= len(empresas):
            print("Índice inválido.")
            return
        nombre = input("Ingrese el nuevo nombre (deje en blanco para mantener actual): ")
        direccion = input("Ingrese la nueva dirección (deje en blanco para mantener actual): ")
        telefono = input("Ingrese el nuevo teléfono (deje en blanco para mantener actual): ")

        if nombre:
            empresas[indice]['nombre'] = nombre
        if direccion:
            empresas[indice]['direccion'] = direccion
        if telefono:
            empresas[indice]['telefono'] = telefono

        print("Empresa actualizada con éxito.")
    except ValueError:
        print("Entrada inválida.")

#Eliminar empresas registradas

def eliminar_empresa(empresas):
    mostrar_empresas(empresas)
    try:
        indice = int(input("Ingrese el número de la empresa a eliminar: ")) - 1
        if indice < 0 or indice >= len(empresas):
            print("Índice inválido.")
            return
        empresas.pop(indice)
        print("Empresa eliminada con éxito.")
    except ValueError:
        print("Entrada inválida.")

def main():
    empresas = cargar_datos()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_empresa(empresas)
        elif opcion == "2":
            mostrar_empresas(empresas)
        elif opcion == "3":
            actualizar_empresa(empresas)
        elif opcion == "4":
            eliminar_empresa(empresas)
        elif opcion == "5":
            guardar_datos(empresas)
            print("Datos guardados con éxito.")
        elif opcion == "6":
            guardar_datos(empresas)
            print("Saliendo del programa. Datos guardados.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

#Volver a la selección inicial6

if __name__ == "__main__":
    main()
