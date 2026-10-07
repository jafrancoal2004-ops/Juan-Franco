class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion 

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.duracion} min)"


class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
        print(f"Añadida: {cancion.titulo} a la lista '{self.nombre}'")

    def calcular_duracion_total(self):
        total = 0
        for cancion in self.canciones:
            total += cancion.duracion
        return total

    def mostrar_lista(self):
        print(f"\n Lista de Reproducción: {self.nombre}")
        print("-" * 45)
        for i, cancion in enumerate(self.canciones, start=1):
            print(f"{i}. {cancion}")
        print("-" * 45)
        print(f"Duración Total: {self.calcular_duracion_total()} minutos")


if __name__ == "__main__":
    print("=== SIMULADOR DE REPRODUCTOR DE MÚSICA ===\n")
    
    tema1 = Cancion("Recuerdos de Ypacaraí", "Berta Rojas", 4.2)
    tema2 = Cancion("Blank Space", "Taylor Swift", 3.5)
    tema3 = Cancion("Bohemian Rhapsody", "Queen", 5.9)
    
    mi_playlist = ListaReproduccion("Mis Favoritas 2026")

    mi_playlist.agregar_cancion(tema1)
    mi_playlist.agregar_cancion(tema2)
    mi_playlist.agregar_cancion(tema3)
    
    mi_playlist.mostrar_lista()
