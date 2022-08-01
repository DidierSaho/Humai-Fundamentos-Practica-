titulo = 'Volver al Futuro'
titulo = titulo.title()
lista = titulo.split()
#print(lista[0][0])
acronimo = " "

for n in lista:
	acronimo = acronimo + n[0]
	#print(acronimo)
print(acronimo)
