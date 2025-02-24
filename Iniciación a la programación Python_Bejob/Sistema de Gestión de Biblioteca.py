# CREACIÓN DE LA CLASE
class Libro:
    def __init__(self, titulo, autor, isbn):
        # Declaración de atributos
        # Inicializa un nuevo libro con título, autor, ISBN y estado disponible
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    # Declaración de métodos
    def agregar(self):
        # Método agregar() que permite introducir un nuevo libro con sus características.
        print(f"Libro '{self.titulo}' agregado con éxito.")

    def prestar(self):
        # Presta el libro si está disponible
        if self.disponible:
            self.disponible = False
            print(f"Libro '{self.titulo}' prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        # Devuelve el libro si estaba prestado
        if not self.disponible:
            self.disponible = True
            print(f"Libro '{self.titulo}' devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    def mostrar(self):
        # Devuelve una cadena con la información del libro y su estado
        estado = "Diponible: Sí" if self.disponible else "Diponible: No"
        return f"{self.titulo} ({self.autor}) - ISBN: {self.isbn} - {estado}"

    def buscar(self, isbn):
        # Busca un libro por su ISBN y muestra su información si lo encuentra
        if self.isbn == isbn:
            estado = "Diponible: Sí" if self.disponible else "Diponible: No"
            print(f"{self.titulo} ({self.autor}) - ISBN: {self.isbn} - {estado}")
            return True
        return False

def menu():
    # Muestra el menú principal y devuelve la opción seleccionada por el usuario
    print("\n--- Sistema de Gestión de Biblioteca ---")
    print("1. Agregar un nuevo libro")
    print("2. Prestar un libro")
    print("3. Devolver un libro")
    print("4. Mostrar todos los libros")
    print("5. Buscar un libro por ISBN")
    print("6. Salir del programa")
    # Si el usuario ingresa una opción inválida en el menú, muestra un mensaje de error y vuelve a pedir una opción
    try:
        return int(input("Seleccione una opción: ").strip())
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")
        return -1

def agregarLibro(inventario):
    # Solicita al usuario los datos del libro y lo agrega al inventario
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    isbn = input("Ingrese el ISBN del libro: ")

    if any(libro.isbn == isbn for libro in inventario):
        print("Error: Ya existe un libro con este ISBN.")
    else:
        libro = Libro(titulo, autor, isbn)
        libro.agregar()
        inventario.append(libro)

def prestarLibro(inventario):
    # Solicita al usuario el ISBN del libro a prestar y lo presta si está disponible
    isbn = input("Ingrese el ISBN del libro que desea prestar: ")
    for libro in inventario:
        if libro.buscar(isbn):
            libro.prestar()
            return
    print("Libro no encontrado.")

def devolverLibro(inventario):
    # Solicita al usuario el ISBN del libro a devolver y lo devuelve si está prestado
    isbn = input("Ingrese el ISBN del libro que desea devolver: ")
    for libro in inventario:
        if libro.buscar(isbn):
            libro.devolver()
            return
    print("Libro no encontrado.")

def mostrarLibros(inventario):
    # Muestra todos los libros en el inventario
    if not inventario:
        print("No hay libros en el inventario.")
    else:
        for libro in inventario:
            print(libro.mostrar())

def buscarLibro(inventario):
    # Busca un libro por su ISBN y muestra su información si lo encuentra
    isbn = input("Ingrese el ISBN del libro que desea buscar: ")
    for libro in inventario:
        if libro.buscar(isbn):
            return
    print("Libro no encontrado.")

def main():
    # Función principal que controla el flujo del programa
    inventario = []
    while True:
        opcion = menu()
        if opcion == 1:
            agregarLibro(inventario)
        elif opcion == 2:
            prestarLibro(inventario)
        elif opcion == 3:
            devolverLibro(inventario)
        elif opcion == 4:
            mostrarLibros(inventario)
        elif opcion == 5:
            buscarLibro(inventario)
        elif opcion == 6:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()