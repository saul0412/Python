# Python
Python Class:
Funcionalidades de la aplicación
###########################################
# Sistema de Gestión de Consolas y Videojuegos

Este sistema permite gestionar el inventario de consolas y videojuegos de manera eficiente, ofreciendo funcionalidades para agregar, consultar, modificar y eliminar productos, todo integrado con una base de datos SQLite.

---

##  **Características**
1. **Agregar Productos:**
   - Permite añadir nuevos productos al inventario.
   - Cada producto incluye:
     - Nombre único.
     - Descripción breve.
     - Cantidad disponible.
     - Fecha de registro automática.

2. **Mostrar Productos:**
   - Lista todos los productos en el inventario.
   - Muestra detalles como:
     - ID del producto.
     - Nombre.
     - Descripción.
     - Cantidad en stock.
     - Fecha de agregado.

3. **Consultar Stock de un Producto:**
   - Permite buscar un producto específico por su nombre.
   - Muestra la cantidad disponible del producto en stock.

4. **Eliminar Productos:**
   - Elimina productos del inventario mediante su ID.
   - Incluye validación para evitar errores si el producto no existe.

5. **Modificar Productos:**
   - Permite actualizar:
     - Cantidad disponible.
     - Nombre del producto.
     - Descripción del producto.

6. **Base de Datos:**
   - Implementada con SQLite.
   - Se crea automáticamente si no existe.
   - Tabla de productos diseñada para almacenar:
     - ID del producto (autoincremental).
     - Nombre (único).
     - Descripción.
     - Cantidad.
     - Fecha de agregado.

7. **Interfaz de Usuario:**
   - Basada en texto.
   - Utiliza emojis para hacer la experiencia más visual y atractiva.
   - Menú interactivo con opciones claras.

---

## **Requisitos del Sistema**
- **Python**: Versión 3.7 o superior.
- **Librerías**: Todas incluidas en la biblioteca estándar de Python:
  - `sqlite3` para la base de datos.
  - `datetime` para la gestión de fechas.

---

## **Cómo Usar el Sistema**
1. Clona el repositorio o descarga los archivos del proyecto.
2. Ejecuta el archivo principal con:
   ```bash
   python sistema_consolas.py
---
   proyecto/
inventario.db   # Base de datos SQLite (se genera automáticamente).
sistema_consolas.py  # Archivo principal con el código del sistema.
README.md       # Archivo de documentación.
---

