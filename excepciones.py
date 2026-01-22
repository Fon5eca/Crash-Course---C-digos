while True:
    try:
        num1 = input("Ingresa el primer número (s para salir): ")
        if num1 == "s":
            break
        else:
            num1 = int(num1)

        num2 = input("Ingresa el otro número (s para salir): ")
        if num2 == "s":
            break
        else:
            num2 = int(num2)

    except ValueError:
        pass

    else:
        print(num1 + num2)



with open("abril_encantado.txt", encoding="utf-8") as f:
    texto = f.read()

print(texto.lower().count("boat "))



try:
    with open("dogs.txt") as f2:
        print(f2.read())

except FileNotFoundError:
    print("Archivo no encontrado")


try:
    with open("cats.txt") as f1:
        print(f1.read())

except FileNotFoundError:
    print("Archivo no encontrado")