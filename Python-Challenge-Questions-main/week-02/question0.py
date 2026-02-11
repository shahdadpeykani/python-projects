# Write a Python program that receives distance in miles and converts it into kilometers using the following
# conversion.
# 1 mile = 1.609344 kilometers

distance_in_miles = float(input("Please enter distance in miles: "))

distance_in_kilometers = round(distance_in_miles * 1.609344)

print(f"{distance_in_miles} miles is equal to {distance_in_kilometers} kilometers.")