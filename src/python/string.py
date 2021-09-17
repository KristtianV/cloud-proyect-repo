nombre='juan'
apellidos="perez"

print(nombre,"",apellidos)

frase="I don't know"
frase2='I don\' know'
print(frase)

#RAW (crudo)
ruta=r"c:\documentos\nomina.xls"

#Acceso a caracteres
palabra="Telecomunicaciones"
primero=palabra[0]
ultimo=palabra[-1]
print(primero)
print(palabra[1:4])
print(len(palabra))

comienza=palabra.startswith('co')
print(comienza)

termina=palabra.endswith('es')
print(termina)

contiene='comunica'in palabra
print(contiene)

posicion=palabra.find('comunica')
print(posicion)

puntaje=50
nombre="catalina"
materia="nube"

fraseFinal="La estudiante "+nombre+" obtuvo "+str(puntaje)+" puntos en "+materia
print(fraseFinal)

fraseFinal2=f'La estudiante {nombre} obtuvo {puntaje-2} puntos en {materia}'
print(fraseFinal2)