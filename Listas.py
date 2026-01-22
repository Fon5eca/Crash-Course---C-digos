carros = ["Ferrari", "Volkswagen", "Mercedes-Benz"]
print(f"Mi marca de carro favorita es {carros[2]}")
print(f"A los bochos se les dice '{carros[1]}'")
print(f"{carros[0]} es una marca cara de autos.")
carros_2 = carros[:]
carros.append("Toyota")
carros_2.append("GMC")
print(carros)
print(carros_2)

print("Mis carros favoritos son:")
for car in carros:
    print(car)

print("Los carros favoritos de mi amigo son:")
for carro_amigo in carros_2:
    print(carro_amigo)