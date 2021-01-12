class Usuario:
    
    id = 0

    def __init__(self):
        Usuario.id += 1

    def setName(self, name):
        self.name = name

usuario = Usuario()
nombre = input("Nombre: ")
usuario.setName(nombre)
print(usuario.id)

usuario2 = Usuario()
print(usuario2.id)

usuario3 = Usuario()
print(usuario3.id)