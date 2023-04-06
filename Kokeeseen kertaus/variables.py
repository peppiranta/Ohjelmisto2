weight = float(input("Enter your weight here: "))
kg_or_lbs = input("(K)g or (L)bs: ")
kg = float(weight)
lbs = float(kg) * 2.2

weight_kg = (kg)
weight_lbs = (lbs)

if kg_or_lbs == "K" or kg_or_lbs == "k":
    print("Your weight in kg is:", weight_kg)
elif kg_or_lbs == "L" or kg_or_lbs == "l":
    print("Your weight in lbs is:", weight_lbs)