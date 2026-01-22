# comidas_favs = ["Camarones con arroz", "Fideos en salsa blanca", "Costilla de cerdo"]
# for comida in comidas_favs:
#     print(f"¡Me encanta comer {comida}!")
# print("Podría comer esos platos sin parar d:")

# felinos = ["Guepardo", "Lince", "Puma"]
# for felino in felinos:
#     print(f"El {felino.lower()}, un animal majestruoso")
# print("Todos estos animales son felinos :)")

# for numero in range(1, 21):
#     print(numero)

# un_millon = list(range(1, 1_000_001))
# for n in un_millon:
#     print(n)

# un_millon = list(range(1, 1_000_001))
# print(min(un_millon))
# print(max(un_millon))
# print(sum(un_millon))

# impares = list(range(1,21,2))
# for impar in impares:
#     print(impar)

# multiplos_3 = [n * 3 for n in range (1, 11)]
# for multiplo in multiplos_3:
#     print(multiplo)

cubos = [n ** 3 for n in range(1, 11)]
print("The first three items in the list are:")
print(cubos[:3])
print("Three items form the middle of the list are:")
print(cubos[3:6])
print("The last three items in my list are:")
print(cubos[-3:])
print(cubos)