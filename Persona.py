class Persona:
    
    def __init__(self) -> None:
        self._nombre = ''
        self._edad = 0 
        self._telefono = ''
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono


    