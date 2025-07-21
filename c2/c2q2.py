print(" *** Wind classification ***")
inp = float(input("Enter wind speed (km/h) : "))

print("Wind classification is ",end='')
if inp < 52:
    print("Breeze.")
elif inp < 55:
    print("Depression.")
elif inp < 102:
    print("Tropical Storm.")
elif inp < 209:
    print("Typhoon.")
else:
    print("Super Typhoon.")