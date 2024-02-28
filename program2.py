nimi_set = set()

while True:
    na = input("Enter a name (press Enter to finish): ")
    if na == "":
        break
    elif na in nimi_set:
        print("Existing name")
    else:
        print("New name")
        nimi_set.add(na)

print("\nList of names:")
for na in nimi_set:
 print(na)