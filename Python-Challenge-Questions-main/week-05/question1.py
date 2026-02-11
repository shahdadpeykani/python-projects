
print("Welcome to Real Steel Calculator!")
hardness = int(input("Enter the value of hardness: "))
carbon = float(input("Enter the value of carbon content: "))
tensile_strength = int(input("Enter the value of tensile strength: "))

if hardness > 50 and carbon < 0.7 and tensile_strength > 5600:
    print("This is grade 10 steel.")
elif hardness > 50 and carbon < 0.7:
    print("This is grade 9 steel.")
elif carbon < 0.7 and tensile_strength > 5600:
    print("This is grade 8 steel.")
elif hardness > 50 and tensile_strength > 5600:
    print("This is grade 7 steel.")
elif hardness > 50 or carbon < 0.7 or tensile_strength > 5600:
    print("This is grade 6 steel.")
else:
    print("This is grade 5 steel.")
