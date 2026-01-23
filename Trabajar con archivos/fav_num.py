import json




fav_num = input("Por favor, ingresa tu número favorito. ")
with open("num_fav.json", "a") as f:
    json.dump(fav_num, f)

