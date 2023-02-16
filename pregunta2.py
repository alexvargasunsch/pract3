class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
class ListaDoble:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0

    def vacia(self):
        return self.primero == None
    def agregarInicio (self,dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = Nodo(dato)
            aux.siguiente = self.primero
            self.primero.primero  = self.primero
            self.primero = aux
        self.size += 1
    def eliminarFinal (self):
        if self.vacia():
            print("No hay elementos, lista vacia")
        elif self.primero.primero.siguiente == None:
            self.primero = self.ultimo = Nodo
            self.size = 0
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.siguiente = None
            self.size -=1
    def recorrerFinal (self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux=aux.anterior 
            aux= aux.dato 
    def recorrerInicioFinal(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente

    def cantidad(self):
        cantidad = self.size
        
        print('Las tareas pendientes es:  ', cantidad, ' y son: ', )        
        
print('Tareas Pendientes')
try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaDoble()
        
        while opcion !=5:
            print("\n 1.Agregar agregar la tarea  al inicio \n 2.Eliminar la tarea del final \n 3.Mostar las tareas en orden Inverso \n 4.Contar la cantidad de tareas pendientes \n 5.Salir")
            opcion = int(input("Ingrese opcion: "))

            if opcion == 1:
                dato = input("Ingrese un nombre de la tarea: ")
                lista.agregarInicio(dato)
            elif opcion == 2:
                lista.eliminarFinal()
            elif opcion == 3:
                lista.recorrerFinal()
            elif opcion == 4:
                lista.cantidad()
            elif opcion == 5:
                print("FIN")
            else:
                print("Ingrese un dato correcto")

except Exception as e:
    print(e)    