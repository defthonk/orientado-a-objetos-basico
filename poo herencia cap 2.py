class Persona: #Esta es la super clase
    def __init__(self, nombre, edad, DNI): 
        self.nombre = nombre
        self.edad = edad 
        self.DNI = DNI

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años y mi DNI es {self.DNI}")

juan = Persona("Oscar", 23, "34567890")
juan.presentarse()
print(juan.DNI) 

class Trabajador(Persona): #Subclase, en esta tenemos que poner el nombre de la clase a la cual estamos heredando, en este caso seria a la clase Persona, que es nuestra super clase 
    def __init__(self, nombre, edad, DNI, sueldo, cargo, empresa): #El constructori __init__ necesita recibir los valores de la clase padre, pero tambien los nuevos valores de la sub clase 
        super().__init__(nombre, edad, DNI) #Super hace referencia a la super clase, aca solo colocamos los valores que traemos de la super clase
        self.sueldo = sueldo 
        self.cargo = cargo 
        self.empresa = empresa
    
    def calcularSueldoAnual(self):
        return 12*self.sueldo + 2000
    
    def present(self):
        print(f"Mi sueldo actual es de {self.sueldo}, mi cargo en la empresa es el {self.cargo} y la empresa para la cual trabajo es {self.empresa}")

trabajador =  Trabajador("Juan", 33, "223456789", 1500, "jefe", "Chevrolet")
trabajador.presentarse()
print(trabajador.DNI)
print(trabajador.calcularSueldoAnual())
trabajador.present()

class Estudiante(Persona): 
    def __init__(self, nombre, edad, DNI, universidad, curso, asignaturas):
        super().__init__(nombre, edad, DNI)
        self.universidad = universidad
        self.curso = curso 
        self.asignaturas = asignaturas

    def describirse(self):
        print(f"Hola soy {self.nombre}, tengo {self.edad} años, y estudio en la universidad {self.universidad}, estoy en el curso {self.curso} de ingenieria en sistemas")

estudiante = Estudiante("Maria",20, "23456789", "Universidad libre", 4,["Programacion", "Calculo", "Fisica"])
estudiante.describirse() #Para mostrar por pantalla los def, los que quiero mostrar, coloco la variable que encierra toda mi lista(creo), pero la variable tiene que tener el nombre de la subclase
print(f"en el curso de ingenieria en sistemas veo las siguientes materias {estudiante.asignaturas}") #Y para mostrar por pantalla algo de mi lista como tal, tengo que colocar print y adentro colocar el nombre de mi variable, le coloco punto, mas al pedazo de la lista que quiero entrar

#Otra cosa, cuando hago un def __init__(self):, el por defecto abajo me muestra pass, esto debido que abajo del def tiene que ir algo, pero el pass no sirve para nada 

