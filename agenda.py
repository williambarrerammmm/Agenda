import amigo

class agenda:
	
	miLista=[]
	nombre=[]
		
	def __init__(self,nombreAgenda,apellidoAgenda):               
		self.nombreAgenda=nombreAgenda
		self.apellidoAgenda=apellidoAgenda 
	
	def agregarAmigos(self,amigos):
		self.miLista.append(amigos)
		
	def eliminarAmigos(self,eliminarAmig):
		for u in self.miLista:
			self.nombre.append(u.nombres())
			if eliminarAmig in self.nombre:
				self.miLista.remove(u)
				print("Se elimino a "+eliminarAmig+" de la agenda")
		
	def imprimir(self):
		print("Agenda de: "+self.nombreAgenda+" "+self.apellidoAgenda)
		print("contactos: ")
		for i in self.miLista:
			i.imprimirAmigo()
