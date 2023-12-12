import tkinter as tk

import tkinter as tk


def mostrar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()

    # Establecer la conexión a la base de datos MySQL
    conexion = mysql.connector.connect(
        host="tu_host",
        user="tu_usuario",
        password="tu_contraseña",
        database="tu_base_de_datos"
    )
    
    cursor = conexion.cursor()

    # Crear una tabla si no existe
    cursor.execute("CREATE TABLE IF NOT EXISTS datos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), edad INT)")

    # Insertar datos en la tabla
    cursor.execute("INSERT INTO datos (nombre, edad) VALUES (%s, %s)", (nombre, edad))

    # Confirmar la transacción y cerrar la conexión
    conexion.commit()
    conexion.close()

    print(f"Nombre: {nombre}, Edad: {edad}, almacenado en la base de datos")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario en Python")

# ... (Código del formulario como se proporcionó anteriormente)

# Botón para enviar el formulario
boton_enviar = tk.Button(ventana, text="Enviar", command=mostrar_datos)
boton_enviar.pack(pady=10)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()





def mostrar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    print(f"Nombre: {nombre}, Edad: {edad}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Formulario en Python")

# Etiqueta y campo de entrada para el nombre
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack(pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.pack(pady=5)

# Etiqueta y campo de entrada para la edad
label_edad = tk.Label(ventana, text="Edad:")
label_edad.pack(pady=5)
entry_edad = tk.Entry(ventana)
entry_edad.pack(pady=5)

# Botón para enviar el formulario
boton_enviar = tk.Button(ventana, text="Enviar", command=mostrar_datos)
boton_enviar.pack(pady=10)

# Iniciar el bucle principal de la interfaz gráfica
ventana.mainloop()
