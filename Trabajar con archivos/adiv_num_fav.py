import json




with open("num_fav.json") as f:
    num_fav = json.load(f)

print(f"¡Lo sé, tu número favorito es {num_fav}!")