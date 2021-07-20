#Realizar una clase que administre una agenda. Se debe almacenar
#para cada contacto el nombre, el teléfono y el email.
    # Además deberá mostrar un menú con las siguientes opciones.
        #Agregar contacto
        #Lista de contactos
        #Buscar contacto
        #Editar contacto
        #Cerrar agenda

class Agenda():
    def __init__(self):
        self.contactos=[]

    def menu(self):
        print("1.Agregar contacto \n2.Lista de Contactos \n3.Buscar contacto \n4.Editar contacto \n5.Eliminar contacto \n6.Cerrar agemda ")
        print("----------")
        while (True):
            try:
                self.opcion_elegir = int(input("Ingresar opcion: "))
                while 0 == self.opcion_elegir or self.opcion_elegir >= 7:
                    self.opcion_elegir = int(input("Ingresar opcion (1 al 6): "))
                break
            except:
                print("Ingrese una opcion valida")
        print()
        if(self.opcion_elegir == 1):
            self.agregar_contactos()
        elif(self.opcion_elegir == 2):
            self.lista_contactos()
        elif (self.opcion_elegir == 3):
            self.buscar_contactos()
        elif (self.opcion_elegir == 4):
            self.editar_contactos()
        elif (self.opcion_elegir == 5):
            self.eliminar_contacto()
        elif (self.opcion_elegir == 6):
            self.cerrar_agenda()

        self.menu()

    def agregar_contactos(self):
        print("Agregar contacto")
        apell = input("Ingresar apellido: ").capitalize()
        nomb=input("Ingresar nombre: ").capitalize()
        while (True):
            try:
                tel=int(input("Ingresar un numero de telefono/celular: "))
                break
            except:
                print("Ingrese un numero valido")
        dir=input("Ingresar direccion: ").capitalize()
        self.contactos.append({"Apellido":apell,"Nombre":nomb,"Numero de contacto":tel,"Direccion":dir})
        print()

    def lista_contactos(self):
        print("Lista de contactos")
        if len(self.contactos)==0:
            print("No hay contactos agregados en la agenda")
        else:
            print(self.contactos)
        print()

    def buscar_contactos(self):
        print("Buscar contacto")
        apell = input("Apellido a buscar: ").capitalize()
        print("----------")
        for i in range(len(self.contactos)):
            if apell == self.contactos[i]["Apellido"]:
                print("Datos del Contacto")
                print("Apellido: ", self.contactos[i]["Apellido"])
                print("Nombre: ",self.contactos[i]["Nombre"])
                print("Numero de contacto: ",self.contactos[i]["Numero de contacto"])
                print("Direccion: ", self.contactos[i]["Direccion"])
                print("Posicion en la lista: ", i+1) #Se suma el 1 para omitir que se visualice una posicion 0
        print()

    def posicion_contacto(self): #Sirve para identificar la posicion de un contacto de la lista
        while True:
            try:
                self.posicion = int(input("Ingrese una posicion en la lista del contacto (buscar contacto): "))
                while self.posicion > len(self.contactos):
                    self.posicion = int(input("Ingrese una posicion en la lista del contacto valida: "))
                break
            except:
                print("Ingrese una posicion valida (caracteres numericos)")
        self.posicion_real = self.posicion - 1 #self.posicion es el numero dado al usuario, la real es la usada por la logica de python en la lista

    def editar_contactos(self): #Para editar un contacto es necesario saber su posicion en la lista, mediante buscar contacto
        print("Editar contacto")
        self.posicion_contacto()
        print("Contacto: ", self.contactos[self.posicion_real])
        print("----------")
        print("Que desea editar?")
        print("1.Apellido \n2.Nombre \n3.Numero de contacto \n4.Direccion \n5.Salir")
        while (True):
            try:
                opcion = int(input("Ingresar opcion: "))
                while 0 == opcion or opcion >= 6:
                    opcion = int(input("Ingresar una opcion correcta: "))
                break
            except:
                print("Ingrese una opcion valida")
        if opcion == 1:
            print("Apellido actual: ", self.contactos[self.posicion_real]["Apellido"])
            apell_nuevo = input("Ingresar nuevo apellido: ").capitalize()
            self.contactos[self.posicion_real]["Apellido"] = apell_nuevo
            print("Datos modificados: ", self.contactos[self.posicion_real]["Apellido"])
        elif opcion == 2:
            print("Nombre actual: ", self.contactos[self.posicion_real]["Nombre"])
            nomb_nuevo = input("Ingresar nuevo nombre: ").capitalize()
            self.contactos[self.posicion_real]["Nombre"] = nomb_nuevo
            print("Datos modificados: ", self.contactos[self.posicion_real]["Nombre"])
        elif opcion == 3:
            print("Numero de contacto actual: ", self.contactos[self.posicion_real]["Numero de contacto"])
            tel_nuevo = input("Ingresar nuevo numero de contactoo: ")
            self.contactos[self.posicion_real]["Numero de contacto"] = tel_nuevo
            print("Datos modificados: ", self.contactos[self.posicion_real]["Numero de contacto"])
        elif opcion == 4:
            print("Direccion actual: ", self.contactos[self.posicion_real]["Direccion"])
            dir_nuevo = input("Ingresar nueva direccion: ").capitalize()
            self.contactos[self.posicion_real]["Direccion"] = dir_nuevo
            print("Datos modificados: ", self.contactos[self.posicion_real]["Direccion"])
        print()

    def eliminar_contacto(self): #Para eliminar un contacto es necesario saber su posicion en la lista, mediante buscar contacto
        print("Eliminar contacto")
        self.posicion_contacto()
        del self.contactos[self.posicion_real]
        self.lista_contactos()

    def cerrar_agenda(self):
        quit()

Agenda2021=Agenda()
Agenda2021.menu()