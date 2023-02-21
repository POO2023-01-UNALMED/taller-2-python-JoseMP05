class Auto:
    cantidadCreados = 0
    def __init__ (self, modelo, asientos, marca, motor, registro): #__init__ funciona como constructor
        self.modelo = modelo
        self.asientos = asientos
        self.marca = marca
        self.motor = motor 
        self.registro = registro

    def cantidadAsientos (self):
        contador = 0
        for i in range(len(asientos)):
            if asientos[i] is not None:
                contador += 1
        return contador

    def verificarIntegridad (self):
        registroAuto =  self.registro
        registroMotor = motor.registro
		
        if registroAuto == registroMotor:
            for i in range(len(asientos)):
                registroasiento = asientos[i].registro
                if registroasiento == 0:
                    continue
                elif registroasiento == registroAuto:
                    continue    
                elif registroasiento != registroAuto:
                    return "Las piezas no son originales"
            return "Auto original"
        return "Las piezas no son originales"


class Asiento:
    def __init__ (self, color, precio, registro):
        self.color = color
        self.precio =  precio
        self.registro = registro

    def cambiarColor (self, color):
        colores = ("rojo", "verde", 'amarillo', "negro", "blanco")
        if color in colores:
            self.color = color

class Motor:
    def __init__ (self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro (self, registro):
        self.registro = registro

    def asignarTipo (self, tipo):
        if tipo == "electrico":
            self.tipo = tipo
        elif tipo == "gasolina":
            self.tipo = tipo

if __name__ == "__main__":
    asientos = (
        Asiento("rojo", 5000, 3),
        Asiento("negro", 5000, 3),
        Asiento("verde", 5000, 3),
    )

    asientos[1].cambiarColor("blanco")
    print(asientos[1].color)
    motor = Motor(4, "ni idea", 3)
    print(asientos[1].registro)
    auto = Auto("Atos", "Hyunday", asientos, motor, 3)
    print(auto.cantidadAsientos())
    print(auto.verificarIntegridad())
