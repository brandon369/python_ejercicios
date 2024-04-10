class BaseDatos:
    def __init__(self, name_bd):
        self.name_db = name_bd
        self.statusConnect = False

    def conectar(self):
        print(f"Conectando a la base de datos {self.name_db}")
        self.statusConnect = True

    def desconectar(self):
        print(f"Desconectando de la base de datos {self.name_db}")
        self.statusConnect = False

    def insertar(self, data):
        pass

    def eliminar(self, id):
        pass

bd = BaseDatos("mi_bd")
bd.conectar()
bd.insertar({"id": 1, "nombre": "Ejemplo"})
bd.eliminar({"id": 1})
bd.desconectar()
