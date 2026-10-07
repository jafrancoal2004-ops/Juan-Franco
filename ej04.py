class Libro:
    def __init__(self, titulo, autor, disponible):
        # Guardamos los datos del libro
        # disponible va a ser True (si está libre) o False (si está prestado)
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self):
        # Cambiamos el True o False por un texto más lindo para el usuario
        if self.disponible:
            estado = "Disponible para préstamo"
        else:
            estado = "Prestado actualmente"
            
        # Devolvemos la ficha armada con f-strings
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Estado: {estado}\n"
            f"-----------------------------------"
        )

# --- Probar el programa ---
if __name__ == "__main__":
    # Creamos un par de libros, uno disponible y otro prestado como pide la pauta
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", True)
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", False)
    
    # Imprimimos las fichas en la consola
    print("=== INVENTARIO DE BIBLIOTECA ===\n")
    print(libro1)
    print(libro2)
