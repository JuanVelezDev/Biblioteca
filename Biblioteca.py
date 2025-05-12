# Biblioteca para gestionar libros

# Inicializamos un diccionario para almacenar los libros
library = {
    "Cien años de soledad": ("Gabriel García Márquez", "Realismo Mágico", 1967, 5, 10.50),
    "1984": ("George Orwell", "Distopía", 1949, 3, 12.00),
    "El principito": ("Antoine de Saint-Exupéry", "Fábula", 1943, 7, 8.75),
    "Don Quijote de la Mancha": ("Miguel de Cervantes", "Novela", 1605, 2, 20.00),
    "Orgullo y prejuicio": ("Jane Austen", "Romántico", 1813, 4, 9.99)
}

# Función para solicitar un número entero de forma segura
def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Por favor ingrese un número positivo.")
            else:
                return value
        except ValueError:
            print("Por favor ingrese un número entero válido.")

# Función para solicitar un número flotante de forma segura
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Por favor ingrese un número positivo.")
            else:
                return value
        except ValueError:
            print("Por favor ingrese un número válido.")

# Función para registrar un nuevo libro
def add_book(title, author, genre, year, quantity, replacement_cost):
    if title in library:
        print(f"Libro '{title}' ya existe en la biblioteca.")
    else:
        library[title] = (author, genre, year, quantity, replacement_cost)
        print(f"Libro '{title}' agregado correctamente.")

# Función para buscar un libro en el catálogo
def search_book(title):
    if title in library:
        author, genre, year, quantity, replacement_cost = library[title]
        print(f"\nDetalles del libro '{title}':")
        print(f"Autor: {author}")
        print(f"Género: {genre}")
        print(f"Año de publicación: {year}")
        print(f"Cantidad disponible: {quantity}")
        print(f"Precio de reposición: ${replacement_cost}")
    else:
        print(f"Libro no encontrado. ¿Desea registrarlo?")

# Función para actualizar la cantidad o el precio de reposición de un libro
def update_book_info(title):
    if title in library:
        author, genre, year, quantity, replacement_cost = library[title]
        
        print(f"\nInformación actual del libro '{title}':")
        print(f"Cantidad disponible: {quantity}")
        print(f"Precio de reposición: ${replacement_cost}")
        
        new_quantity = get_int_input("Ingrese la nueva cantidad disponible: ")
        new_replacement_cost = get_float_input("Ingrese el nuevo precio de reposición: $")
        
        library[title] = (author, genre, year, new_quantity, new_replacement_cost)
        print(f"Información del libro '{title}' actualizada correctamente.")
    else:
        print(f"Libro '{title}' no encontrado.")

# Función para eliminar un libro
def delete_book(title):
    if title in library:
        confirmation = input(f"¿Está seguro que desea eliminar '{title}'? (s/n): ").lower()
        if confirmation == 's':
            del library[title]
            print(f"Libro '{title}' eliminado correctamente.")
        else:
            print(f"Eliminación de '{title}' cancelada.")
    else:
        print(f"Libro '{title}' no encontrado.")

# Función para calcular el valor total de reposición del inventario
def calculate_inventory_value():
    total_value = sum(quantity * replacement_cost for _, (_, _, _, quantity, replacement_cost) in library.items())
    print(f"\nValor total del inventario: ${total_value:.2f}")

# Función para obtener el libro más antiguo y el más reciente por género
def oldest_and_newest_books_by_genre():
    genre_books = {}
    
    for title, (author, genre, year, quantity, replacement_cost) in library.items():
        if genre not in genre_books:
            genre_books[genre] = (title, year)
        else:
            _, existing_year = genre_books[genre]
            if year < existing_year:
                genre_books[genre] = (title, year)
    
    for genre, (oldest_book, _) in genre_books.items():
        print(f"El libro más antiguo en el género '{genre}' es '{oldest_book}'.")

# Menú principal
def main():
    while True:
        print("\n=== Sistema de Gestión de Biblioteca ===")
        print("1. Agregar un nuevo libro")
        print("2. Buscar un libro")
        print("3. Actualizar información del libro")
        print("4. Eliminar un libro")
        print("5. Calcular valor total del inventario")
        print("6. Ver libro más antiguo por género")
        print("7. Salir")
        
        choice = input("Elija una opción (1-7): ")
        
        if choice == "1":
            title = input("Ingrese el título del libro: ").strip()
            author = input("Ingrese el autor del libro: ").strip()
            genre = input("Ingrese el género del libro: ").strip()
            
            while True:
                year = input("Ingrese el año de publicación: ")
                if year.isdigit() and int(year) <= 2024:
                    year = int(year)
                    break
                else:
                    print("Año inválido. Ingrese un valor entre 1800 y 2024.")
            
            quantity = get_int_input("Ingrese la cantidad disponible: ")
            replacement_cost = get_float_input("Ingrese el precio de reposición: $")
            
            add_book(title, author, genre, year, quantity, replacement_cost)
        
        elif choice == "2":
            title = input("Ingrese el título del libro para buscar: ").strip()
            search_book(title)
        
        elif choice == "3":
            title = input("Ingrese el título del libro a actualizar: ").strip()
            update_book_info(title)
        
        elif choice == "4":
            title = input("Ingrese el título del libro a eliminar: ").strip()
            delete_book(title)
        
        elif choice == "5":
            calculate_inventory_value()
        
        elif choice == "6":
            oldest_and_newest_books_by_genre()
        
        elif choice == "7":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 7.")

# Ejecutar el sistema
main()
