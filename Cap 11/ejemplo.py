def nombre(nombre, apellido, s_nombre=None):
    if s_nombre == None:
        return f"{nombre} {apellido}".title()
    else:
        return f"{nombre} {s_nombre} {apellido}".title()

print(nombre("deisler", "fonseca"))