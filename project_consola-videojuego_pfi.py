#modulo para bd
import sqlite3
#modulo para ver fecha y hora cuando fueron agregados los productos
from datetime import datetime

# Conectar a la base de datos (se crea si no existe)
conexion = sqlite3.connect("/home/saul/Phython_Class/TT-24212-Python/TT-24212-Python/preentrega-saul0412/inventraio.db")
cursor = conexion.cursor()

# Crear la tabla 'productos' si no existe (incluyendo id_producto autoincremental)
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE,  -- El nombre debe ser único
    cantidad INTEGER NOT NULL,
    fecha_agregado TEXT
)
''')

# Función principal del sistema de inventario
while True:
    print("=" * 43)
    #Python es totalmente compatible con Unicode, lo que incluye los emojis.emojipedia.org 
    print("🎮 🖥️ 🐧  Sistema de Consolas y Videojuegos 🎮 🕹️ 💾")
    print("=" * 43)
   # print("1️⃣  ➤ Agregar Producto")
   # print("2. Mostrar Productos")
   # print("3. Consultar Stock de un Producto")
   # print("4. Eliminar Producto")
   # print("5. Modificar Producto")
   # print("6. Salir")
    print("1️⃣  ➤ Agregar Producto")
    print("2️⃣  ➤ Mostrar Productos")
    print("3️⃣  ➤ Consultar Stock de un Producto")
    print("4️⃣  ➤ Eliminar Producto")
    print("5️⃣  ➤ Modificar Producto")
    print("6️⃣  ➤ Salir")
    print("🕹️" * 15)

    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        producto = input("Ingrese el nombre del producto: ").lower()

        # Verificar si el producto ya existe en la base de datos por su nombre
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (producto,))
        resultado = cursor.fetchone()

        if resultado:
            print(f"El producto '{producto}' ya existe en el inventario.")
        else:
            cantidad = int(input("Ingrese la cantidad: "))
            fecha_agregado = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                cursor.execute("INSERT INTO productos (nombre, cantidad, fecha_agregado) VALUES (?, ?, ?)", 
                               (producto, cantidad, fecha_agregado))
                conexion.commit()
                print("Producto agregado exitosamente.")
            except sqlite3.IntegrityError:
                print(f"Error: Ya existe un producto con el nombre '{producto}'.")

    elif opcion == '2':
        # Mostrar todos los productos del inventario
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

        if len(productos) == 0:
            print("No hay productos en el inventario.")
        else:
            print("\nProductos en el inventario:")
            print("#" * 29)
            for producto in productos:
                fecha_agregado = producto[3] if len(producto) > 3 else "Desconocida"
                print(f"#  > ID: {producto[0]} - {producto[1]} : {producto[2]} Unidades (Agregado: {fecha_agregado})")
            print("#" * 29)

    elif opcion == '3':
        consulta_producto = input("Ingrese el nombre del producto a consultar: ").lower()

        # Consultar si el producto existe en la base de datos
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", (consulta_producto,))
        producto = cursor.fetchone()

        if producto:
            print(f"Producto '{consulta_producto}' está en stock con {producto[2]} Unidades.")
        else:
            print(f"El producto '{consulta_producto}' no está en stock.")

    elif opcion == '4':
        # Eliminar Producto
        id_producto = input("Ingrese el ID del producto a eliminar: ")

        try:
            cursor.execute("DELETE FROM productos WHERE id_producto = ?", (id_producto,))
            if cursor.rowcount == 0:
                print(f"No se encontró el producto con ID {id_producto}.")
            else:
                conexion.commit()
                print(f"Producto con ID {id_producto} eliminado exitosamente.")
        except Exception as e:
            print(f"Error al eliminar el producto: {e}")

    elif opcion == '5':
        # Modificar Producto (solo cantidad o ambos)
        id_producto = input("Ingrese el ID del producto a modificar: ")

        # Verificar si el producto existe
        cursor.execute("SELECT * FROM productos WHERE id_producto = ?", (id_producto,))
        producto = cursor.fetchone()

        if producto:
            print(f"Producto encontrado: {producto[1]} con {producto[2]} unidades.")
            
            #una subopción para modificar cantidad o ambos
            print("\n¿Qué deseas modificar?")
            print("1. Solo la cantidad")
            print("2. Nombre y cantidad")
            sub_opcion = input("Selecciona una opción: ")

            if sub_opcion == '1':
                nueva_cantidad = int(input(f"Ingrese la nueva cantidad para el producto '{producto[1]}': "))
                try:
                    cursor.execute("UPDATE productos SET cantidad = ? WHERE id_producto = ?", 
                                   (nueva_cantidad, id_producto))
                    conexion.commit()
                    print(f"Cantidad del producto '{producto[1]}' actualizada exitosamente.")
                except Exception as e:
                    print(f"Error al actualizar la cantidad: {e}")
            elif sub_opcion == '2':
                nuevo_nombre = input(f"Ingrese el nuevo nombre para el producto '{producto[1]}': ").lower()
                nueva_cantidad = int(input(f"Ingrese la nueva cantidad para el producto '{producto[1]}': "))
                try:
                    cursor.execute("UPDATE productos SET nombre = ?, cantidad = ? WHERE id_producto = ?", 
                                   (nuevo_nombre, nueva_cantidad, id_producto))
                    conexion.commit()
                    print(f"Producto con ID {id_producto} modificado exitosamente.")
                except Exception as e:
                    print(f"Error al modificar el producto: {e}")
            else:
                print("Opción inválida.")
        else:
            print(f"No se encontró el producto con ID {id_producto}.")
    #El bucle cierra
    elif opcion == '6':
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. \nPor favor, elige una opción del menú.")

# Cerrar la conexión a la base de datos
conexion.close()
