mon = int(input("Enter month number (1-12): "))

seas = ("winter", "spring", "summer", "autumn")

if mon in (12, 1, 2):
    s = seas[0]  # Winter
elif mon in (3, 4, 5):
    s = seas[1]  # Spring
elif mon in (6, 7, 8):
    s = seas[2]  # Summer
elif mon in (9, 10, 11):
    s = seas[3]  # Autumn
else:
    s = "Invalid month number"

print("The corresponding season is:",s)