import agenda
import amigo

def pedirContacto():
	nombreContacto=input("Nombre del nuevo contacto: ")
	apellidoContacto=input("Apellido del nuevo contacto: " )
	telefonoContacto=pedirTelefonos()
	nuevoContacto=amigo.amigo(nombreContacto,apellidoContacto,telefonoContacto)
	return nuevoContacto

def pedirTelefonos():
	telefonoContacto=[]
	telefonoContacto.append(input("Telefono del nuevo contacto: "))
	i=1;
	while i==1:
		contTelefono=input("¿Agregar mas numeros de este contacto? s/n : ")
		if contTelefono == "s":
			telefonoContacto.append(input("Otro Telefono del nuevo contacto: "))
		if contTelefono == "n":
			i=0;
	return telefonoContacto

nombreAgenda=input("Ingrese el nombre del dueño de la agenda ")
apellidoAgenda=input("Ingrese el apellido del dueño de la agenda ")
agen=agenda.agenda(nombreAgenda,apellidoAgenda)
agen.imprimir()
opcion="" 

while(opcion!="SALIR" and opcion!="salir"):
	print("MENU:")
	print(" Agregar amigo [Agregar]")
	print(" Eliminar amigo [Eliminar]")
	print(" Imprimir agenda [Imprimir]")
	print(" Salir [salir]")
	opcion=input("Ingrese la opcion: ")
	if opcion == "Agregar":
		agen.agregarAmigos(pedirContacto())
	if opcion ==  "Eliminar":
		agen.eliminarAmigos(input("Ingrese el nombre del amigo a eliminar: "))
	if opcion == "Imprimir":
		agen.imprimir()
