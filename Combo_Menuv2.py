cost = 0.0
sandwich = input("What type of sandwhich would you like(chicken, beef, tofu)")
if sandwich == "chicken":
    cost += 5.25
if sandwich == "beef" : 
    cost += 6.25
if sandwich == "tofu" :
    cost += 5.75

print("You a selected a", sandwich, "sandwhich, and it costs", cost, ".")

beverage_choice = input("Would you like a beverage(yes or no)")
beverage_size = "none"

if beverage_choice == "yes" :
    beverage_size = input("What size would you like your beverage(small, medium, large)")
    if beverage_size == "small" :
        cost += 1.00
    elif beverage_size == "medium" :
        cost += 1.75
    elif beverage_size == "large" :
        cost += 2.25
    print("You have selected a", beverage_size, "beverage.")
else:
    print("You did not selected a beverage.")

print("Your total cost is", cost, ".")




