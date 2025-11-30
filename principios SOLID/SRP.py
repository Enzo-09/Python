"""
* EJERCICIO:
 * Explora el "Principio SOLID de Responsabilidad Única (Single Responsibility
 * Principle, SRP)" y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""
"""
#incorrecto
class usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    def guardar_usuario(self):
        pass
    def enviar_email(self):
        pass

#correcto
class usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email        

class servicio_usuario:
    def guardar_usuario(self, usuario):
        pass
class servicio_email:
    def enviar_email(self, usuario):
        pass
"""
"""
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un sistema de gestión para una biblioteca. El sistema necesita
 * manejar diferentes aspectos como el registro de libros, la gestión de usuarios
 * y el procesamiento de préstamos de libros.
 * Requisitos:
 * 1. Registrar libros: El sistema debe permitir agregar nuevos libros con
 * información básica como título, autor y número de copias disponibles.
 * 2. Registrar usuarios: El sistema debe permitir agregar nuevos usuarios con
 * información básica como nombre, número de identificación y correo electrónico.
 * 3. Procesar préstamos de libros: El sistema debe permitir a los usuarios
 * tomar prestados y devolver libros.
 * Instrucciones:
 * 1. Diseña una clase que no cumple el SRP: Crea una clase Library que maneje
 * los tres aspectos mencionados anteriormente (registro de libros, registro de
 * usuarios y procesamiento de préstamos).
 * 2. Refactoriza el código: Separa las responsabilidades en diferentes clases
 * siguiendo el Principio de Responsabilidad Única.
 """
"""
#extra
class biblioteca:
    def __init__(self) -> None:
        self.libros = []
        self.usuarios = []
        self.prestamos = []
    
    def registrar_libros(self, titulo: str , autor: str, copias: int):
        self.libros.append({"titulo": titulo, "autor": autor, "copias": copias})
    
    def registrar_usuario(self, id:int, nombre:str, email:str):
        self.usuarios.append({"id": id, "nombre": nombre, "email": email})
    
    def registrar_prestamos(self, id, titulo):
        for libros in self.libros:
            if libros["titulo"] == titulo and libros["copias"] > 0:
                libros[copias] -= 1
                self.prestamos.append({"user id": id, "titulo": titulo})
                return True
            return False
    
    def devolver_libros(self, id, titulo):
        for prestamos in self.prestamos:
            if prestamos["id"] == id and prestamos["titulo"] ==  titulo:
                self.prestamos.remove(prestamos)
                for libro in self.libros:
                    if libro["titulo"] == titulo:
                        libro["copias"] += 1
                    return True
        return False
"""

class Usuario:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

class Libro:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias

class ServicioPrestamos:
    def __init__(self):
        self.prestamos = []

    def prestar_libro(self, usuario, libro):
        if libro.copias > 0:
            libro.copias -= 1
            self.prestamos.append({"id": usuario.id, "titulo": libro.titulo})
            return True
        return False
    
    def devolver_libro(self, usuario, libro):
        for prestamo in self.prestamos:
            if prestamo["id"] == usuario.id and prestamo["titulo"] == libro.titulo:
                self.prestamos.remove(prestamo)
                libro.copias += 1
                return True
        return False
    
class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.servicios_prestamos = ServicioPrestamos()

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
    
    def prestamo_libro(self, id, titulo):
        usuario = next((u for u in self.usuarios if u.id == id), None)
        libro = next((l for l in self.libros if l.titulo == titulo), None)
        if usuario and libro:
            return self.servicios_prestamos.prestar_libro(usuario, libro)
        return False
    
    def devolver_libro(self, id, titulo):
        usuario = next((u for u in self.usuarios if u.id == id), None)
        libro = next((l for l in self.libros if l.titulo == titulo), None)
        if usuario and libro:
            return self.servicios_prestamos.devolver_libro(usuario, libro)
        return False