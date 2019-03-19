selector = 0
unit1 = 0
unit2 = 0
ans = 0

print("Welcome to my file convertor")
selector = input("Which category would you like to convert? we support (l)ength and (W)eight:  ")

# If Length is selected

if selector == "l":

  print("We can convert using the units; mm, cm, m, km")
  unit1 = input("Which unit would you like to convert from: ")

  unit2 = input("Which unit would you like to convert to: ")

  num1 = input("Enter your value: " )

# Conversion for length

  if unit1 == "cm" and unit2 == "m":
    ans = float(num1) / 100
  elif unit1 == "mm" and unit2 == "cm":
    ans = float(num1) / 10
  elif unit1 == "m" and unit2 == "cm":
    ans = float(num1) * 100
  elif unit1 == "cm" and unit2 == "mm":
    ans = float(num1) * 10
  elif unit1 == "mm" and unit2 == "m":
    ans = float(num1) / 1000
  elif unit1 == "m" and unit2 == "mm":
    ans = float(num1) * 1000  
  elif unit1 == "km" and unit2 == "m":
    ans = float(num1) * 1000
  elif unit1 == "m" and unit2 == "km":
    ans = float(num1) / 1000
  elif unit1 == "mm" and unit2 == "km":
    ans = float(num1) / 1000000
  elif unit1 == unit2:
    ans = num1

# If unit2 is length

if unit2 == "m":
  print(str(ans) + " Metres")
elif unit2 == "cm":
  print(str(ans) + " Centimetres")
elif unit2 == "mm":
  print(str(ans) + " Millimetres")
elif unit2 == "km":
  print(str(ans) + " Kilometres")

if selector == "w":
  print("We can convert using the units; lbs, tn, g, kg, ug, mg / imperial-ton, us-ton, st, oz")
  unit1 = input("Which unit would you like to convert from: ")
  unit2 = input("Which unit would you like to convert to: ")
  num1 = input("Enter your value: " )

  if unit1 == "g" and unit2 == "kg":
    ans = float(num1)/1000
  elif unit1 == "g" and unit2 == "ug":
    ans = float(num1) * 1000000
  elif unit1 == "g" and unit2 == "lbs":
    ans = float(num1)/453.592
  elif unit1 == "g" and unit2 == "tn":
    ans = float(num1)/1000000
  elif unit1 == "kg" and unit2 == "g":
    ans = float(num1)/1000
  elif unit1 == "kg" and unit2 == "ug":
    ans = float(num1) * 1000000000
  elif unit1 == "kg" and unit2 == "tn":
    ans = float(num1)/1000
  elif unit1 == "kg" and unit2 == "lbs":
    ans = float(num1)*2.205
  elif unit1 == "tn" and unit2 == "g":
    ans = float(num1)*1000000
  elif unit1 == "tn" and unit2 == "kg":
    ans = float(num1)*1000
  elif unit1 == "tn" and unit2 == "lbs":
    ans = float(num1)*2204.623
  elif unit1 == "ug" and unit2 == "tn":
    ans = float(num1) * 1000000000000
  elif unit1 == "ug" and unit2 == "g":
    ans = float(num1) / 1000000
  elif unit1 == "ug" and unit2 == "kg":
    ans = float(num1) / 1000000000
  elif unit1 == "ug" and unit2 == "tn":
    ans = float(num1) / 1000000000000
  elif unit1 == "ug" and unit2 == "tn":
    ans = float(num1) / 1000000000000
  elif unit1 == "ug" and unit2 == "lbs":
    ans = float(num1) / 453600000
  elif unit1 == "ug" and unit2 == "mg":
    ans = float(num1) / 1000
  elif unit1 == "mg" and unit2 == "ug":
    ans = float(num1) * 1000
  elif unit1 == "mg" and unit2 == "kg":
    ans = float(num1) / 1000000
  elif unit1 == "mg" and unit2 == "kg":
    ans = float(num1) / 1000
  elif unit1 == "mg" and unit2 == "tn":
    ans = float(num1) / 1000000000
  elif unit1 == "mg" and unit2 == "lbs":
    ans = float(num1) / 453592.37
  elif unit1 == "lbs" and unit2 == "tn":
    ans = float(num1) / 2204.623
  elif unit1 == "lbs" and unit2 == "g":
    ans = float(num1) * 453.592
  elif unit1 == "lbs" and unit2 == "kg":
    ans = float(num1) / 2.205
  elif unit1 == "lbs" and unit2 == "ug":
    ans = float(num1) * 453600000
  elif unit1 == "lbs" and unit2 == "mg":
    ans = float(num1) * 453592.37
  elif unit1 == "imperial-ton" and unit2 == "":
  elif unit1 == unit2: 
    ans = num1


if unit2 == "lbs":
  print(str(ans) + " Pounds")
elif unit2 == "tn":
  print(str(ans) + " Tonnes")
elif unit2 == "g":
  print(str(ans) + " Grammes")
elif unit2 == "kg":
  print(str(ans) + " Kilogrammes")
elif unit2 == "ug":
  print(str(ans) + " Microgrammes")
elif unit2 == "mg":
  print(str(ans) + " Microgrammes")
