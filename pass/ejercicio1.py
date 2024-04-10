from abc import ABC, abstractmethod

class BaseClase(ABC):
    @abstractmethod
    def metodo_abstracto(self):
        pass

class SubClase(BaseClase):
    def metodo_abstracto(self):
        print("Implementación del método abstracto en la subclase")


objeto_subclase = SubClase()
objeto_subclase.metodo_abstracto()
