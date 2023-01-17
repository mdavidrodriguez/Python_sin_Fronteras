class Usuario:
    def __init__(self,nombre,apellido): 
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print("Hola!, mi nombre es", self.nombre, self.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print('Hola Me llamo', self.nombre, 'y soy administrador')

usuario = Usuario('Felipe', 'Feliz')
usuario2 = Usuario('Chanchito', 'Feliz')

# print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)

# usuario.saludo()
admin = Admin('Super', 'Administrador')
admin.saludo()
admin.superSaludo()


