#funcion para añadir un cliente, que recibe por parametro un diccionario
def añadir_cliente(clientes):
    nif = input("Ingrese el NIF del cliente: ")
    if len(nif) != 9 or not nif[:8].isdigit(): #verificamos que tenga el largo apropiado y que los primeros 8 sean digitos
        print("El NIF debe contener 9 caracteres, los 8 primeros numéricos.")
        return
    if nif in clientes:
        print("El cliente ya existe.")
        return

    apellidos_nombre = input("Ingrese los apellidos y nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    codigo_postal = input("Ingrese codigo postal: ")
    if len(codigo_postal) != 5 or not codigo_postal.isdigit():
        print("El codigo postal debe contener 5 digitos")
    telefono = input("Ingrese el teléfono del cliente: ")
    if len(telefono) != 9 or not telefono.isdigit(): #verificacion del len y ademas que sean digitos
        print("El teléfono debe contener 9 dígitos.")
        return

    correo = input("Ingrese el correo electrónico del cliente: ")
    cliente_habitual = input("¿Es cliente habitual? (si/no): ").lower() == "si"
    fecha_operacion = input("Ingrese la fecha de la operación (en formato dd/mm/yyyy): ")
    #aqui creamos un diccionario con los datos que hemos introducido previamente
    cliente = {
        "apellidos_nombre": apellidos_nombre,
        "direccion": direccion,
        "telefono": telefono,
        "codigo_postal": codigo_postal,
        "correo": correo,
        "cliente_habitual": cliente_habitual,
        "fecha_operacion": fecha_operacion
    }

    clientes[nif] = cliente
    print("Cliente añadido correctamente.\n")

#uso basico de la operacion del para eliminar un cliente
def eliminar_cliente(clientes):
    nif = input("Ingrese el NIF del cliente que desea eliminar: ")
    if nif in clientes:
        del clientes[nif]
        print("Cliente eliminado correctamente.")
    else:
        print("El cliente no existe.")

#chequeamos que exista el cliente previamente luego de ello, mostramos todos los datos almacenados de dicho cliente
def mostrar_cliente(clientes):
    nif = input("Ingrese el NIF del cliente que desea mostrar: ")
    if nif in clientes:
        cliente = clientes[nif]
        print("Datos del cliente:")
        print("NIF:", nif)
        print("Apellidos y nombre:", cliente["apellidos_nombre"])
        print("Dirección:", cliente["direccion"])
        print("Codigo Postal:", cliente["codigo_postal"])
        print("Teléfono:", cliente["telefono"])
        print("Correo electrónico:", cliente["correo"])
        print("Cliente habitual:", cliente["cliente_habitual"])
        print("Fecha de la operación:", cliente["fecha_operacion"])
    else:
        print("El cliente no existe.")

#simplemente ensenamos los clientes con un bucle for en el diccionario
def listar_clientes(clientes):
    print("Lista de clientes:")
    for nif, cliente in clientes.items():
        print("NIF:", nif)
        print("Nombre:", cliente["apellidos_nombre"])
        print("---")

#lo mismo que la funciona anterior pero chequeando quienes son clientes habituales
def listar_clientes_habituales(clientes):
    print("Lista de clientes habituales:")
    for nif, cliente in clientes.items():
        if cliente["cliente_habitual"]:
            print("NIF:", nif)
            print("Nombre:", cliente["apellidos_nombre"])
            print("---")

#menu hace llamado a todas las funciones anteriores basado en la opcion que elija el usuario
#iniciamos un diccionario vacio, en el cual vamos introduciendo los datos poco a poco. asociando
#el nif a los datos
def menu():
    clientes = {}
    while True:
        print("Menú:")
        print("(1) Añadir cliente")
        print("(2) Eliminar cliente")
        print("(3) Mostrar cliente")
        print("(4) Listar todos los clientes")
        print("(5) Listar clientes habituales")
        print("(6) Salir\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            añadir_cliente(clientes)
        elif opcion == "2":
            eliminar_cliente(clientes)
        elif opcion == "3":
            mostrar_cliente(clientes)
        elif opcion == "4":
            listar_clientes(clientes)
        elif opcion == "5":
            listar_clientes_habituales(clientes)
        elif opcion == "6":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()