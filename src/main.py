def menu():
    while True:
        print("\n=== SISTEMA DE VENTAS ===")
        print("1. Gestionar productos")
        print("2. Gestionar clientes")
        print("3. Registrar venta")
        print("4. Reportes")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            print(">> Aquí irá la gestión de productos")
        elif opcion == "2":
            print(">> Aquí irá la gestión de clientes")
        elif opcion == "3":
            print(">> Aquí irá el registro de ventas")
        elif opcion == "4":
            print(">> Aquí irán los reportes")
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu()
