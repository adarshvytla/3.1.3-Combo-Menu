cost = 0.0
sandwich = input("What type of sandwhich would you like(chicken $5.25, beef $6.25, tofu $5.75)")
if sandwich == "chicken":
    cost = 5.25
if sandwich == "beef" : 
    cost = 6.25
if sandwich == "tofu" :
    cost = 5.75

print("You have selected a", sandwich, "sandwhich, and it costs", cost, ".")