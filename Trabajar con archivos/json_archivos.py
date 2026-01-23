import json

nums = [1,3,5,7,9] # Aunque lo ponga así, por convención aparecerá con espacios entre elem.

with open("nums.json", "w") as f:
    json.dump(nums, f)