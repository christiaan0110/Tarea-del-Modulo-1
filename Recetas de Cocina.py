import sqlite3

conn = sqlite3.connect('recetas.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS recetas
             (id INTEGER PRIMARY KEY, nombre TEXT, ingredientes TEXT, pasos TEXT)''')


def agregar_receta():
    nombre = input("Nombre de la receta: ")
    ingredientes = input("Ingredientes (separados por comas): ")
    pasos = input("Pasos: ")
    c.execute("INSERT INTO recetas (nombre, ingredientes, pasos) VALUES (?, ?, ?)", (nombre, ingredientes, pasos))
    conn.commit()
    print("Receta agregada con éxito.")


def actualizar_receta():
    id_receta = input("ID de la receta a actualizar: ")
    nombre = input("Nuevo nombre de la receta: ")
    ingredientes = input("Nuevos ingredientes (separados por comas): ")
    pasos = input("Nuevos pasos: ")
    c.execute("UPDATE recetas SET nombre = ?, ingredientes = ?, pasos = ? WHERE id = ?",
              (nombre, ingredientes, pasos, id_receta))
    conn.commit()
    print("Receta actualizada con éxito.")


def eliminar_receta():
    id_receta = input("ID de la receta a eliminar: ")
    c.execute("DELETE FROM recetas WHERE id = ?", (id_receta,))
    conn.commit()
    print("Receta eliminada con éxito.")


def ver_recetas():
    c.execute("SELECT * FROM recetas")
    recetas = c.fetchall()
    for receta in recetas:
        print(f"ID: {receta[0]}, Nombre: {receta[1]}, Ingredientes: {receta[2]}, Pasos: {receta[3]}")


def buscar_receta():
    nombre = input("Nombre de la receta a buscar: ")
    c.execute("SELECT * FROM recetas WHERE nombre LIKE ?", ('%' + nombre + '%',))
    recetas = c.fetchall()
    for receta in recetas:
        print(f"ID: {receta[0]}, Nombre: {receta[1]}, Ingredientes: {receta[2]}, Pasos: {receta[3]}")


def menu():
    while True:
        print("\nOpciones:")
        print("a) Agregar nueva receta")
        print("b) Actualizar receta existente")
        print("c) Eliminar receta existente")
        print("d) Ver listado de recetas")
        print("e) Buscar ingredientes y pasos de receta")
        print("f) Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == 'a':
            agregar_receta()
        elif opcion == 'b':
            actualizar_receta()
        elif opcion == 'c':
            eliminar_receta()
        elif opcion == 'd':
            ver_recetas()
        elif opcion == 'e':
            buscar_receta()
        elif opcion == 'f':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


menu()
conn.close()
