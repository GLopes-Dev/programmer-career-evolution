#Challenge 024 - Create a program that reads a city name and says if it name starts with "SANTO" or not

print("=" * 10, "[Challenge 024]", "=" * 10)
city = input("City name: ").strip()
if 'SANTO' in city.upper().split()[0]:
    print("Starts with Santo? Yes")
else:
    print("Starts with Santo? No")


#True or False Version
print("=" * 10, "[Challenge 024]", "=" * 10)
city = input("City Name: ").strip()
city1 = city.upper()
print('SANTO' in city1.split()[0])