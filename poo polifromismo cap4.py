#El poliformismo es una herrammienta que nos va a permitir redefinir metodos que heredemos de una clase padre, osea que si definimos un metodo de una super clase y de esa super clase se heredan 3 subclases mas, en cada una de esas subclases bajo el mismo nombre voy a poder modificar y definir de nuevo el codigo que se ejecuta en esos metodos, por tanto en la subclase 1, si yo tengo un metodo que se llame saludar, puede ser distinto que en la subclase 2, que el mismo metodo que se llama saluda, pero teniendo un codigo diferente

class Empleado:
    
    def __init__(self, nombre, sueldoMensual):
        self.nombre = nombre
        self.sueldoMensual = sueldoMensual

    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual*(1 + 1/100)
        print(f"El sueldo anual de {self.nombre}, empleado normal, es de {sueldo}")

class Contable(Empleado):

    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)

    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual*(1 +4/100)
        print(f"El sueldo anual de {self.nombre}, Contable es de {sueldo}")

class Publicista(Empleado):

    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)

    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual*(1 + 5/100)
        print(f"El sueldo anual de {self.nombre}, Publicista, es de {sueldo}")

class Becario(Empleado):

    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)

    def calcularSueldoAnual(self):
        sueldo = 12*self.sueldoMensual
        print(f"El sueldo anual de {self.nombre}, Becario, es de {sueldo}")

empleados = [
    Empleado("Bless", 1000),
    Contable("Jh de la cruz", 1100),
    Publicista("Ryan castro", 1200),
    Becario("Que chimba sog", 750)
]

for empleado in empleados:
    empleado.calcularSueldoAnual()