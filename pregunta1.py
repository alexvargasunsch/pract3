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

    def agregarFinal(self, dato):
        if self.vacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)
            self.ultimo.anterior = aux
        self.size += 1
    def recorrerInicioFinal(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente

    def eliminarInicio(self):
        if self.vacia():
            print("Su lista se encuentra vacia")
        elif self.primero.siguiente == None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size -= 1    
    
print('Lista de compras')
try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaDoble()
        
        while opcion !=5:
            print("\n 1.Agregar productos a la lista \n 2.Eliminar el producto del inicio de la lista \n 3.Mostrar mostrar a lista de compras \n 4.Salir")
            opcion = int(input("Ingrese opcion: "))

            if opcion == 1:
                dato = input("Ingrese un nombre del producto: ")
                lista.agregarFinal(dato)
            elif opcion == 2:
                lista.eliminarInicio()
            elif opcion == 3:
                lista.recorrerInicioFinal()
            elif opcion == 4:
                print("FIN")
            else:
                print("Ingrese un dato correcto")

except Exception as e:
    print(e)