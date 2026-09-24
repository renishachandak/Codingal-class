pizza =("Neapolitan Pizza", "Italian", "01:00", "Medium To Hard")
Icecreame = ("Vanilla Icecreame", "Romeian","03:00", "Hard")
print("Recipe 2:",Icecreame)
print("Name:",Icecreame[0])
print("Cuisine:",Icecreame[1])
print("Difficulty:",Icecreame[-1])

all_recipes = (pizza,Icecreame)
print("First Recipe Name:",all_recipes[0][0])
print("First Recipe Cuisine:",all_recipes[0][1])
print("First Recipe Time:",all_recipes[0][2])

print("Ice Creame Recipes Details:")
for detail in Icecreame:
    print(" - ",detail)

pizza_ingrediants = {"Tomato", "Cheese", "Wheat", "Oil", "Basil"}
Icecreame_ingrediants = {"Milk","Vanilla Essence","Condenced Milk","Sugar","Salt","Milk"}
print("Pizza ingrediants:", pizza_ingrediants)
print("Icecreame ingrediants:", Icecreame_ingrediants)
print("Total Icecreame ingrediants:", len(Icecreame_ingrediants))

pizza_ingrediants.add("Milk")
pizza_ingrediants.discard("Oil")
print("Updated Pizza ingrediants:",pizza_ingrediants)

all_ingrediants = pizza_ingrediants.union(Icecreame_ingrediants)
common = pizza_ingrediants.intersection(Icecreame_ingrediants)
only_pizza = pizza_ingrediants.difference(Icecreame_ingrediants)
unique = pizza_ingrediants.symmetric_difference(Icecreame_ingrediants)

print("All ingrediants:",all_ingrediants)
print("Common Ingrediants:",common)
print("Only In Pizza:",only_pizza)
print("Unique:",unique)