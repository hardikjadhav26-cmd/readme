def calculate_calories(carbs, fats, proteins):
    total = (carbs * 4) + (fats * 9) + (proteins * 4)
    return total

carbs = float(input("Enter grams of carbohydrates: "))
fats = float(input("Enter grams of fats: "))
proteins = float(input("Enter grams of proteins: "))

calories = calculate_calories(carbs, fats, proteins)

print("Total caloric intake =", calories, "calories")
