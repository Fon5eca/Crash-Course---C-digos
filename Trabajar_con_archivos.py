with open("digitos_Pi.txt") as file_object:
    contenido = file_object.read()
print(contenido)

with open("digitos_Pi.txt") as i:
    for linea in i:
        print(linea.rstrip())



# Almacenar dígitos de pi en un string
with open("digitos_Pi.txt") as acceso_archivo:
    lista_lineas = acceso_archivo.readlines()     #Guardar cada linea como elemento en una lista. Siempre, cada linea se guarda como string.

digitos_pi = ""
for linea in lista_lineas:
    digitos_pi += linea.strip()     #El archivo original tiene espacios, y Python los toma en cuenta, entonces por eso hay que agregar .strip()

print(digitos_pi)

if "415" in digitos_pi:
    print("Sí está!")

print([1, 4, 5] in [8, 3, 24, 1, 4, 5])



# Leer archivo de lo que aprendí en Python
with open("python_learning.txt") as python_archivo:
    lineas = python_archivo.readlines()

for linea in lineas:
    print(linea.replace("Python", "Java Script").rstrip())