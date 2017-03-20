

class amigo:
	
	def __init__(self,nombre,apellido,telefonos):
		self.nombre=nombre
		self.apellido=apellido
		self.telefonos=telefonos             #constructor 
		
	def agregarTelefono(self,telefono):
		self.telefonos.append(telefono)
		
	def agregarNombre(self,nombrea):
		self.nombre.append(nombrea)
		
	def agregarApellido(self,apellidoa):
		self.apellido.append(apellidoa)

	def nombres(self):
		return self.nombre
	
	def imprimirAmigo(self):
		print(self.nombre+" "+self.apellido+" ")
		print(self.telefonos)
