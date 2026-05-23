class Nodo:
    def __init__(self, libro):
            self.libro = libro
            self.izq = None
            self.der = None

"""
Clase Arbol: Es definida para el usarla al momento de 
 organizar y buscar elementos, en ese caso libros y usuarios,
mediante su atributo clave, en este caso el id.
"""
class Arbol:

    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        """
        Inserta un nuevo dato en el árbol.
        Si el árbol está vacío, el dato se convierte en la raíz.
        De lo contrario, se llama al método recursivo _insertar.
        """
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(self.raiz, dato)

    def _insertar(self, nodo, libro):
        """
        Inserta ordenadamente un nuevo libro o usuario en el árbol.
        Esto mantiene el árbol ordenado y permite búsquedas rápidas.
        """
        if libro.id < nodo.libro.id:
            if nodo.izq is None:
                nodo.izq = Nodo(libro)
            else:
                self._insertar(nodo.izq, libro)
        else:
            if nodo.der is None:
                nodo.der = Nodo(libro)
            else:
                self._insertar(nodo.der, libro)

    def buscar(self, llave):
        """
        Busca un elemento por su id en el árbol.
        Retorna el libro o usuario encontrado o None si no existe.
        """
        return self._buscar(self.raiz, llave)

    def _buscar(self, nodo, llave):
        """
        Búsqueda recursiva en el árbol.
        Comparación de la llave con el id almacenado en cada nodo.
        """
        if nodo is None:
            return None
        if llave == nodo.libro.id:
            return nodo.libro
        
        if llave < nodo.libro.id:
            return self._buscar(nodo.izq, llave)
        
        return self._buscar(nodo.der, llave)
    
    def listar_libros(self):
        """
        Retorna una lista de libros ordenados por id.
        """
        return list(self._listar_libros(self.raiz))

    def _listar_libros(self, nodo):
        if nodo:
            yield from self._listar_libros(nodo.izq)
            yield nodo.libro
            yield from self._listar_libros(nodo.der)
    
    def listar_usuarios(self):
        """
        Retorna una lista de usuarios ordenados por id.
        """
        return list(self._listar_usuarios(self.raiz))

    def _listar_usuarios(self, nodo):
        if nodo:
            yield from self._listar_usuarios(nodo.izq)
            yield nodo.libro
            yield from self._listar_usuarios(nodo.der)

    def buscar_libro_titulo(self, titulo):
        for libro in self.libros.listar_libros():
            if libro.titulo.lower() == titulo.lower():
                print(libro)
                return
        print("Libro no encontrado")

class Libro:
    def __init__(self, id,titulo,autor):
        """
            Inicializa un objeto Libro.

            Parámetros:
            id (int): Identificador único del libro.
            titulo (str): Título del libro.
            autor (str): Autor del libro.
        """
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.prestado = False
        self.usuario = None

    def __str__(self):
        """
            Retorna una representación en texto del libro, indicando si está disponible o prestado.
        """
        prestado = f"(Prestado a {self.usuario.nombre})" if self.prestado else "(Disponible)"
        return f"{self.titulo} {prestado}"


class Usuario:
    def __init__(self, id,nombre):
        """
            Inicializa un objeto Usuario.

            Parámetros:
            id (int): Identificador único del usuario.
            nombre (str): Nombre del usuario.
        """
        self.id = id
        self.nombre = nombre

    def __str__(self):
        """
            Retorna el nombre del usuario como representación en texto.
        """
        return self.nombre


class Biblioteca:
    def __init__(self):
        """
            Inicializa la biblioteca con listas vacías de libros y usuarios,
            y agrega libros y usuarios iniciales.
        """
        self.libros = Arbol()
        self.usuarios = Arbol()
        # Libros iniciales

        self.libros.insertar(Libro(1, "Cien años de soledad", "Gabriel García Márquez"))
        self.libros.insertar(Libro(2, "El principito", "Antoine de Saint-Exupéry"))
        self.libros.insertar(Libro(3, "La Odisea", "Homero"))
        self.libros.insertar(Libro(4, "Don Quijote", "Miguel de Cervantes"))
        self.libros.insertar(Libro(5, "El coronel no tiene quien le escriba", "Gabriel García Márquez"))

        # Agregar usuarios iniciales
        self.usuarios.insertar(Usuario(1, "Gabriel Bernal"))
        self.usuarios.insertar(Usuario(2, "Luis Bernal"))
        self.usuarios.insertar(Usuario(3, "María Gómez"))
        self.usuarios.insertar(Usuario(4, "Carlos Ruiz"))
        self.usuarios.insertar(Usuario(5, "Pasion Ramírez"))

    def agregar_libro(self,titulo, autor):
        """
        Agrega un nuevo libro a la biblioteca.

        Parámetros:
        titulo (str): Título del libro.
        autor (str): Autor del libro.
        """
        id = len(self.libros.listar_libros()) + 1
        libro = Libro(id, titulo, autor)
        self.libros.insertar(libro)
        print(f"\nLibro '{titulo}' agregado correctamente.")

    def agregar_usuario(self,nombre):
        """
        Agrega un nuevo usuario a la biblioteca.

        Parámetros:
        nombre (str): Nombre del usuario.
        """    
        id = len(self.usuarios.listar_usuarios()) + 1
        usuario = Usuario(id, nombre)
        self.usuarios.insertar(usuario)
        print(f"\nUsuario '{nombre}' agregado correctamente.")

    def listar_libros(self):
        """
        Muestra la lista de libros registrados en la biblioteca,˜
        incluyendo su estado (disponible o prestado).
        """
        print("\nLista de Libros:")
        for libro in self.libros.listar_libros():
            estado = "Prestado" if libro.prestado else "Disponible"
            print(f"{libro.id} - {libro.titulo} - {libro.autor} - {estado}")

    def listar_usuarios(self):
        """
        Muestra la lista de usuarios registrados en la biblioteca.
        """   
        if self.usuarios.listar_usuarios():
            print("\nLista de usuarios:")
            for usuario in self.usuarios.listar_usuarios():
                print(f"ID: {usuario.id}. Usuario: {usuario.nombre}")
        else:
            print("No hay usuarios registrados.")
        print()

    def prestar_libro(self, id_libro, id_usuario):
        """
        Presta un libro a un usuario si ambos existen y el libro está disponible.

        Parámetros:
        id_titulo (int): ID del libro a prestar.
        id_usuario (int): ID del usuario que recibe el libro.
        """
        libro = self.libros.buscar(id_libro)
        usuario = self.usuarios.buscar(id_usuario)
        print(libro)
        if libro is None or usuario is None:
            print("Error: libro o usuario no encontrado.")
            return
        if libro.prestado:
            print("El libro ya está prestado.")
            return

        libro.prestado = True
        libro.usuario = usuario

        print(f"\nLibro '{libro.titulo}' prestado a {usuario.nombre}.")

    def devolver_libro(self, id_libro):
        """
        Devuelve un libro prestado a la biblioteca.

        Parámetros:
        id_titulo (int): ID del libro a devolver.
        """    
        libro = self.libros.buscar(id_libro)
        if libro is None:
            print("Libro no encontrado.")
            return
        if not libro.prestado:
            print("El libro no está prestado.")
            return

        libro.prestado = False
        libro.usuario = None
        print(f"\nLibro '{libro.titulo}'.")


# Menu principal

def menu():
    """
    Muestra el menú principal del sistema y gestiona la interacción con el usuario.
    """
    biblioteca = Biblioteca()

    while True:
        print("\nMenú de Biblioteca")
        print("1. Agregar libro")
        print("2. Agregar usuario")
        print("3. Listar libros")
        print("4. Listar usuarios")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            biblioteca.agregar_libro(titulo,autor)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del usuario: ")
            biblioteca.agregar_usuario(nombre)
        elif opcion == "3":
            biblioteca.listar_libros()
        elif opcion == "4":
            biblioteca.listar_usuarios()
        elif opcion == "5":
            biblioteca.listar_libros()
            titulo = input("Ingrese el ID del libro a seleccionar: ")
            biblioteca.listar_usuarios()
            usuario = input("Ingrese ID del usuario a seleccionar: ")
            biblioteca.prestar_libro(int(titulo), int(usuario))
        elif opcion == "6":
            biblioteca.listar_libros()
            titulo = input("Ingrese el título del libro a devolver: ")
            biblioteca.devolver_libro(int(titulo))
        elif opcion == "7":
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida, intente nuevamente.")


# Ejecutar el menú
menu()