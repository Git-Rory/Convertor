#----------//Variables\\----------#

import tkinter
import webbrowser

selector1 = 0
selector = 0
unit1 = 0
unit2 = 0
ans = 0
num1 = 0

# Speed of light in air (Speed of light in a vacuum is 300000000 Kilometres per second)
c = 299792458 # Kilometres Per Second

#----------//Functions\\----------#

def length():
	
	unit1 = 0
	unit2 = 0
	ans = 0
	num1 = 0

	print("We can convert using the units; km, m, cm, mm, um, nm, mi, yd, ft, in, nmi")
	unit1 = input("Which unit would you like to convert from: ")
	unit2 = input("Which unit would you like to convert to: ")
	num1 = input("Enter your value: " )
	lengthcalc(unit1, unit2, num1)

def lengthcalc(unit1, unit2, num1):

#----------//Kilometres\\----------#
	if unit1 == "km" and unit2 == "m":
		ans = float(num1) * 1000
	elif unit1 == "km" and unit2 == "cm":
		ans = float(num1) * 100000
	elif unit1 == "km" and unit2 == "mm":
		ans = float(num1) * (1*(10**6))
	elif unit1 == "km" and unit2 == "um":
		ans = float(num1) * (1*(10**9))
	elif unit1 == "km" and unit2 == "nm":
		ans = float(num1) * (1*(10**12))
	elif unit1 == "km" and unit2 == "mi":
		ans = float(num1) / 1.609
	elif unit1 == "km" and unit2 == "yd":
		ans = float(num1) * 1093.613
	elif unit1 == "km" and unit2 == "ft":
		ans = float(num1) * 3280.84
	elif unit1 == "km" and unit2 == "in":
		ans = float(num1) * 39370.079
	elif unit1 == "km" and unit2 == "nmi":
		ans = float(num1) / 1.852
		
#----------//Metres\\-----------#
	elif unit1 == "m" and unit2 == "km":
		ans = float(num1) / 1000
	elif unit1 == "m" and unit2 == "cm":
		ans = float(num1) * 100
	elif unit1 == "m" and unit2 == "mm":
		ans = float(num1) * 1000
	elif unit1 == "m" and unit2 == "um":
		ans = float(num1) * (1*(10**6))
	elif unit1 == "m" and unit2 == "nm":
		ans = float(num1) * (1*(10**9))
	elif unit1 == "m" and unit2 == "mi":
		ans = float(num1) / 1609.344
	elif unit1 == "m" and unit2 == "yd":
		ans = float(num1) * 1.094
	elif unit1 == "m" and unit2 == "ft":
		ans = float(num1) * 3.281
	elif unit1 == "m" and unit2 == "in":
		ans = float(num1) * 39.37
	elif unit1 == "m" and unit2 == "nmi":
		ans = float(num1) / 1852
		
#----------//Centimetres\\----------#
	elif unit1 == "cm" and unit2 == "km":
		ans = float(num1) / 100000
	elif unit1 == "cm" and unit2 == "m":
		ans = float(num1) / 100
	elif unit1 == "cm" and unit2 == "mm":
		ans = float(num1) * 10
	elif unit1 == "cm" and unit2 == "um":
		ans = float(num1) * 10000
	elif unit1 == "cm" and unit2 == "nm":
		ans = float(num1) * (1*(10**7))
	elif unit1 == "cm" and unit2 == "mi":
		ans = float(num1) / 160934.4
	elif unit1 == "cm" and unit2 == "yd":
		ans = float(num1) / 91.44
	elif unit1 == "cm" and unit2 == "ft":
		ans = float(num1) / 30.48
	elif unit1 == "cm" and unit2 == "in":
		ans = float(num1) / 2.54
	elif unit1 == "cm" and unit2 == "nmi":
		ans = float(num1) / 185200
		
#----------//Millimetres\\----------#
	elif unit1 == "mm" and unit2 == "km":
		ans = float(num1) / (1*(10**6))
	elif unit1 == "mm" and unit2 == "m":
		ans = float(num1) / 1000
	elif unit1 == "mm" and unit2 == "cm":
		ans = float(num1) / 10
	elif unit1 == "mm" and unit2 == "um":
		ans = float(num1) * 1000
	elif unit1 == "mm" and unit2 == "nm":
		ans = float(num1) * (1*(10**6))
	elif unit1 == "mm" and unit2 == "mi":
		ans = float(num1) * (1.609*(10**6))
	elif unit1 == "mm" and unit2 == "yd":
		ans = float(num1) / 914.4
	elif unit1 == "mm" and unit2 == "ft":
		ans = float(num1) / 304.8
	elif unit1 == "mm" and unit2 == "in":
		ans = float(num1) / 25.4
	elif unit1 == "mm" and unit2 == "nmi":
		ans = float(num1) / (1.852*(10**6))
		
#----------//Micrometres\\----------#
	elif unit1 == "um" and unit2 == "km":
		ans = float(num1) / (1*(10**9))
	elif unit1 == "um" and unit2 == "m":
		ans = float(num1) / (1*(10**6))
	elif unit1 == "um" and unit2 == "cm":
		ans = float(num1) / 10000
	elif unit1 == "um" and unit2 == "mm":
		ans = float(num1) / 1000
	elif unit1 == "um" and unit2 == "nm":
		ans = float(num1) * 1000
	elif unit1 == "um" and unit2 == "mi":
		ans = float(num1) / (1.609*(10**9))
	elif unit1 == "um" and unit2 == "yd":
		ans = float(num1) / 914400
	elif unit1 == "um" and unit2 == "ft":
		ans = float(num1) / 304800
	elif unit1 == "um" and unit2 == "in":
		ans = float(num1) / 25400
	elif unit1 == "um" and unit2 == "nmi":
		ans = float(num1) / (1.852*(10**9))
		
#----------//Nanometres\\----------#
	elif unit1 == "nm" and unit2 == "km":
		ans = float(num1) / (1*(10**12))
	elif unit1 == "nm" and unit2 == "m":
		ans = float(num1) / (1*(10**9))
	elif unit1 == "nm" and unit2 == "cm":
		ans = float(num1) / (1*(10**7))
	elif unit1 == "nm" and unit2 == "mm":
		ans = float(num1) / (1*(10**6))
	elif unit1 == "nm" and unit2 == "um":
		ans = float(num1) / 1000
	elif unit1 == "nm" and unit2 == "mi":
		ans = float(num1) / (1.609*(10**12))
	elif unit1 == "nm" and unit2 == "yd":
		ans = float(num1) / (9.144*(10**8))
	elif unit1 == "nm" and unit2 == "ft":
		ans = float(num1) / (3.048*(10**8))
	elif unit1 == "nm" and unit2 == "in":
		ans = float(num1) / (2.54*(10**7))
	elif unit1 == "nm" and unit2 == "nmi":
		ans = float(num1) / (1.852*(10**12))

#----------//Miles\\----------#
	elif unit1 == "mi" and unit2 == "km":
		ans = float(num1) * 1.609
	elif unit1 == "mi" and unit2 == "m":
		ans = float(num1) * 1609.344
	elif unit1 == "mi" and unit2 == "cm":
		ans = float(num1) * 160934.4
	elif unit1 == "mi" and unit2 == "mm":
		ans = float(num1) * (1.609*(10**6))
	elif unit1 == "mi" and unit2 == "nm":
		ans = float(num1) * (1.609*(10**12))
	elif unit1 == "mi" and unit2 == "um":
		ans = float(num1) * (1.609*(10**9))
	elif unit1 == "mi" and unit2 == "yd":
		ans = float(num1) * 1760
	elif unit1 == "mi" and unit2 == "ft":
		ans = float(num1) * 5280
	elif unit1 == "mi" and unit2 == "in":
		ans = float(num1) * 63360
	elif unit1 == "mi" and unit2 == "nmi":
		ans = float(num1) / 1.151

#----------//Yards\\----------#
	elif unit1 == "yd" and unit2 == "km":
		ans = float(num1) / 1093.613
	elif unit1 == "yd" and unit2 == "m":
		ans = float(num1) / 1.094
	elif unit1 == "yd" and unit2 == "cm":
		ans = float(num1) * 91.44
	elif unit1 == "yd" and unit2 == "mm":
		ans = float(num1) * 914.4
	elif unit1 == "yd" and unit2 == "nm":
		ans = float(num1) * (9.144*(10**8))
	elif unit1 == "yd" and unit2 == "um":
		ans = float(num1) * 914400
	elif unit1 == "yd" and unit2 == "ft":
		ans = float(num1) * 3
	elif unit1 == "yd" and unit2 == "in":
		ans = float(num1) * 36
	elif unit1 == "yd" and unit2 == "nmi":
		ans = float(num1) / 2025.372
	elif unit1 == "yd" and unit2 == "mi":
		ans = float(num1) / 1760

#----------//Feet\\----------#
	elif unit1 == "ft" and unit2 == "km":
		ans = float(num1) * 3280.84
	elif unit1 == "ft" and unit2 == "m":
		ans = float(num1) / 3.281
	elif unit1 == "ft" and unit2 == "cm":
		ans = float(num1) * 30.48
	elif unit1 == "ft" and unit2 == "mm":
		ans = float(num1) * 304.8
	elif unit1 == "ft" and unit2 == "nm":
		ans = float(num1) * (3.048*(10**8))
	elif unit1 == "ft" and unit2 == "um":
		ans = float(num1) * 304800
	elif unit1 == "ft" and unit2 == "yd":
		ans = float(num1) / 3
	elif unit1 == "ft" and unit2 == "in":
		ans = float(num1) * 12
	elif unit1 == "ft" and unit2 == "nmi":
		ans = float(num1) / 6076.115
	elif unit1 == "ft" and unit2 == "mi":
		ans = float(num1) / 5280

#----------//Inches\\----------#
	elif unit1 == "in" and unit2 == "km":
		ans = float(num1) / 39370.079
	elif unit1 == "in" and unit2 == "m":
		ans = float(num1) / 39.37
	elif unit1 == "in" and unit2 == "cm":
		ans = float(num1) * 2.54
	elif unit1 == "in" and unit2 == "mm":
		ans = float(num1) * 25.4
	elif unit1 == "in" and unit2 == "nm":
		ans = float(num1) * (2.54*(10**7))
	elif unit1 == "in" and unit2 == "um":
		ans = float(num1) * 25400
	elif unit1 == "in" and unit2 == "yd":
		ans = float(num1) / 36
	elif unit1 == "in" and unit2 == "ft":
		ans = float(num1) / 12
	elif unit1 == "in" and unit2 == "nmi":
		ans = float(num1) / 72913.386
	elif unit1 == "in" and unit2 == "mi":
		ans = float(num1) / 63360

#----------//Nautical Miles\\----------#
	elif unit1 == "nmi" and unit2 == "km":
		ans = float(num1) * 1.852
	elif unit1 == "nmi" and unit2 == "m":
		ans = float(num1) * 1852
	elif unit1 == "nmi" and unit2 == "cm":
		ans = float(num1) * 185200
	elif unit1 == "nmi" and unit2 == "mm":
		ans = float(num1) * (1.852*(10**6))
	elif unit1 == "nmi" and unit2 == "nm":
		ans = float(num1) * (1.852*(10**12))
	elif unit1 == "nmi" and unit2 == "um":
		ans = float(num1) * (1.852*(10**9))
	elif unit1 == "nmi" and unit2 == "yd":
		ans = float(num1) * 2025.372
	elif unit1 == "nmi" and unit2 == "in":
		ans = float(num1) * 72913.386
	elif unit1 == "nmi" and unit2 == "ft":
		ans = float(num1) * 6076.115
	elif unit1 == "nmi" and unit2 == "mi":
		ans = float(num1) * 1.151

#----------//Input Validation\\----------#
	elif unit1 == unit2: 
		ans = num1
		
#----------//Suffixes\\----------#
	if unit2 == "km":
	  print(str(ans) + " Kilometres\n")
	elif unit2 == "m":
	  print(str(ans) + " Miles\n")
	elif unit2 == "cm":
	  print(str(ans) + " Centimetres\n")
	elif unit2 == "mm":
	  print(str(ans) + " Millimetres\n")
	elif unit2 == "um":
	  print(str(ans) + " Micrometres\n")
	elif unit2 == "nm":
	  print(str(ans) + " Nanometres\n")
	elif unit2 == "mi":
	  print(str(ans) + " Miles\n")
	elif unit2 == "yd":
	  print(str(ans) + " Yards\n")
	elif unit2 == "ft":
	  print(str(ans) + " Feet\n")
	elif unit2 == "in":
	  print(str(ans) + " Inches\n")
	elif unit2 == "nmi":
	  print(str(ans) + " Nautical Miles\n")

def weight():
	
	unit1 = 0
	unit2 = 0
	ans = 0
	num1 = 0

	print("We can convert these weights; lbs, tn, g, kg, ug, mg, imperial-ton, us-ton, st, oz")
	unit1 = input("Which unit would you like to convert from: ")
	unit2 = input("Which unit would you like to convert to: ")
	num1 = input("Enter your value: " )
	weightcalc(unit1, unit2, num1)

def weightcalc(unit1, unit2, num1):

#----------//Grammes\\----------#
	if unit1 == "g" and unit2 == "kg":
		ans = float(num1) / 1000
	elif unit1 == "g" and unit2 == "ug":
		ans = float(num1) * 1000000
	elif unit1 == "g" and unit2 == "lbs":
		ans = float(num1) / 453.592
	elif unit1 == "g" and unit2 == "tn":
		ans = float(num1) / 1000000
	elif unit1 == "g" and unit2 == "mg":
		ans = float(num1) * 1000
	elif unit1 == "g" and unit2 == "imperial-ton":
		ans = float(num1) / 1016000000
	elif unit1 == "g" and unit2 == "us-ton":
		ans = float(num1) / 907184.74
	elif unit1 == "g" and unit2 == "st":
		ans = float(num1) / 6350.293
	elif unit1 == "g" and unit2 == "oz":
		ans = float(num1) / 28.35
		
#----------//Kilograumes\\-----------#
	elif unit1 == "kg" and unit2 == "g":
		ans = float(num1) / 1000
	elif unit1 == "kg" and unit2 == "ug":
		ans = float(num1) * 1000000000
	elif unit1 == "kg" and unit2 == "tn":
		ans = float(num1) / 1000
	elif unit1 == "kg" and unit2 == "lbs":
		ans = float(num1) * 2.205
	elif unit1 == "kg" and unit2 == "mg":
		ans = float(num1) * 1000000
	elif unit1 == "kg" and unit2 == "imperial-ton":
		ans = float(num1) / 1016.047
	elif unit1 == "kg" and unit2 == "us-ton":
		ans = float(num1) / 907.185
	elif unit1 == "kg" and unit2 == "st":
		ans = float(num1) * 6.35
	elif unit1 == "kg" and unit2 == "oz":
		ans = float(num1) * 35.274
		
#----------//Tonnes\\----------#
	elif unit1 == "tn" and unit2 == "g":
		ans = float(num1) * 1000000
	elif unit1 == "tn" and unit2 == "kg":
		ans = float(num1) * 1000
	elif unit1 == "tn" and unit2 == "lbs":
		ans = float(num1) * 2204.623
	elif unit1 == "tn" and unit2 == "ug":
		ans = float(num1) * 1000000000000
	elif unit1 == "tn" and unit2 == "mg":
		ans = float(num1) * 1000000000
	elif unit1 == "tn" and unit2 == "imperial-ton":
		ans = float(num1) / 1.016
	elif unit1 == "tn" and unit2 == "us-ton":
		ans = float(num1) * 1.102
	elif unit1 == "tn" and unit2 == "st":
		ans = float(num1) * 157.473
	elif unit1 == "tn" and unit2 == "oz":
		ans = float(num1) * 35273.962
		
#----------//Micrograumes\\----------#
	elif unit1 == "ug" and unit2 == "g":
		ans = float(num1) / 1000000
	elif unit1 == "ug" and unit2 == "kg":
		ans = float(num1) / 1000000000
	elif unit1 == "ug" and unit2 == "tn":
		ans = float(num1) / 1000000000000
	elif unit1 == "ug" and unit2 == "lbs":
		ans = float(num1) / 453600000
	elif unit1 == "ug" and unit2 == "mg":
		ans = float(num1) / 1000
	elif unit1 == "ug" and unit2 == "imperial-ton":
		ans = float(num1) / 1016000000000
	elif unit1 == "ug" and unit2 == "us-ton":
		ans = float(num1) / ((9.072*10)**11)
	elif unit1 == "ug" and unit2 == "st":
		ans = float(num1) / ((6.35*10)**9)
	elif unit1 == "ug" and unit2 == "oz":
		ans = float(num1) * ((2.835*10)**7)
		
#----------//Milligraumes\\----------#
	elif unit1 == "mg" and unit2 == "ug":
		ans = float(num1) * 1000
	elif unit1 == "mg" and unit2 == "kg":
		ans = float(num1) / 1000000
	elif unit1 == "mg" and unit2 == "tn":
		ans = float(num1) / 1000000000
	elif unit1 == "mg" and unit2 == "lbs":
		ans = float(num1) / 453592.37
	elif unit1 == "mg" and unit2 == "g":
		ans = float(num1) / 1000
	elif unit1 == "mg" and unit2 == "imperial-ton":
		ans = float(num1) / 1016000000
	elif unit1 == "mg" and unit2 == "us-ton":
		ans = float(num1) * ((9.072*10)**8)
	elif unit1 == "mg" and unit2 == "st":
		ans = float(num1) / ((6.35*10)**6)
	elif unit1 == "mg" and unit2 == "oz":
		ans = float(num1) / 28349.523
		
#----------//Pounds\\----------#
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
	elif unit1 == "lbs" and unit2 == "imperial-ton":
		ans = float(num1) / 2240
	elif unit1 == "lbs" and unit2 == "us-ton":
		ans = float(num1) / 2000
	elif unit1 == "lbs" and unit2 == "st":
		ans = float(num1) / 14
	elif unit1 == "lbs" and unit2 == "oz":
		ans = float(num1) * 16
		
#----------//Imperial Tonne\\----------#
	elif unit1 == "imperial-ton" and unit2 == "lbs":
		ans = float(num1) * 2240
	elif unit1 == "imperial-ton" and unit2 == "tn":
		ans = float(num1) * 1.016
	elif unit1 == "imperial-ton" and unit2 == "g":
		ans = float(num1) * 1016000000
	elif unit1 == "imperial-ton" and unit2 == "kg":
		ans = float(num1) * 1016.047
	elif unit1 == "imperial-ton" and unit2 == "ug":
		ans = float(num1) * 1016000000000000
	elif unit1 == "imperial-ton" and unit2 == "mg":
		ans = float(num1) * 1016000000000
	elif unit1 == "imperial-ton" and unit2 == "us-ton":
		ans = float(num1) * ((1.016*10)**12)
	elif unit1 == "imperial-ton" and unit2 == "st":
		ans = float(num1) * 160
	elif unit1 == "imperial-ton" and unit2 == "oz":
		ans = float(num1) * 35840
		
#----------//US-Ton\\----------#
	elif unit1 == "us-ton" and unit2 == "lbs":
		ans = float(num1) * 2000
	elif unit1 == "us-ton" and unit2 == "tn":
		ans = float(num1) / 1.102
	elif unit1 == "us-ton" and unit2 == "g":
		ans = float(num1) * 907184.74
	elif unit1 == "us-ton" and unit2 == "kg":
		ans = float(num1) * 907.185
	elif unit1 == "us-ton" and unit2 == "ug":
		ans = float(num1) * ((9.072*10)**11)
	elif unit1 == "us-ton" and unit2 == "mg":
		ans = float(num1) * ((9.072*10)**8)
	elif unit1 == "us-ton" and unit2 == "imperial-ton":
		ans = float(num1) / 1.12
	elif unit1 == "us-ton" and unit2 == "st":
		ans = float(num1) * 142.857
	elif unit1 == "us-ton" and unit2 == "oz":
		ans = float(num1) * 32000
		
#----------//Stone\\----------#
	elif unit1 == "st" and unit2 == "lbs":
		ans = float(num1) * 14
	elif unit1 == "st" and unit2 == "tn":
		ans = float(num1) / 157.473
	elif unit1 == "st" and unit2 == "g":
		ans = float(num1) * 6350.293
	elif unit1 == "st" and unit2 == "kg":
		ans = float(num1) * 6.35
	elif unit1 == "st" and unit2 == "ug":
		ans = float(num1) * (6.35*10**9)
	elif unit1 == "st" and unit2 == "mg":
		ans = float(num1) * ((6.35*10)**6)
	elif unit1 == "st" and unit2 == "imperial-ton":
		ans = float(num1) / 160
	elif unit1 == "st" and unit2 == "oz":
		ans = float(num1) * 224
	elif unit1 == "st" and unit2 == "us-ton":
		ans = float(num1) / 142.857

#----------//Ounces\\----------#
	elif unit1 == "oz" and unit2 == "lbs":
		ans = float(num1) / 16
	elif unit1 == "oz" and unit2 == "tn":
		ans = float(num1) / 35273.962
	elif unit1 == "oz" and unit2 == "g":
		ans = float(num1) * 28.35
	elif unit1 == "oz" and unit2 == "kg":
		ans = float(num1) / 35.274
	elif unit1 == "oz" and unit2 == "ug":
		ans = float(num1) * ((2.835*10)**7)
	elif unit1 == "oz" and unit2 == "mg":
		ans = float(num1) * 28349.523
	elif unit1 == "oz" and unit2 == "imperial-ton":
		ans = float(num1) / 35840
	elif unit1 == "oz" and unit2 == "us-ton":
		ans = float(num1) / 32000
	elif unit1 == "oz" and unit2 == "st":
		ans = float(num1) / 224
		
#----------//Input Validation\\----------#
	elif unit1 == unit2: 
		ans = num1
		
#----------//Suffixes\\----------#
	if unit2 == "lbs":
	  print(str(ans) + " Pounds\n")
	elif unit2 == "tn":
	  print(str(ans) + " Tonnes\n")
	elif unit2 == "g":
	  print(str(ans) + " Grammes\n")
	elif unit2 == "kg":
	  print(str(ans) + " Kilogrammes\n")
	elif unit2 == "ug":
	  print(str(ans) + " Microgrammes\n")
	elif unit2 == "mg":
	  print(str(ans) + " Milligrammes\n")
	elif unit2 == "imperial-ton":
	  print(str(ans) + " Imperial Tonnes\n")
	elif unit2 == "us-ton":
	  print(str(ans) + " US Tonnes\n")
	elif unit2 == "st":
	  print(str(ans) + " Stones\n")
	elif unit2 == "oz":
	  print(str(ans) + " Ounces\n")
	  
def radio_calculation_calculator(selector1, c):
	print("radioconv1", selector1, c)
	selector1 = input("Which category would you like to convert? we support any of these topics, just type the number shown\n\n(1) dBm To Watt Calculator\n(2) Frequency to Wavelength\n(3) Noise Factor to Noise Figure Calculator\n(4) Noise Figure to Noise Temperature Calculator\n(5) Noise Temperature to Noise Figure Converter\n(6) PPM to Hz Calculator\n(7) SINAD to ENOB Calculator\n(8) Watt To dBm Calculator\n(9) Wavelength to Frequency\n")
	print("radioconv2", selector1, c)
	radio_calculation_calculatorcalc(selector1, c)

def radio_calculation_calculatorcalc(selector1, c):
        print(selector, selector1, "ree")
        if selector1 == 1:
                print("2")
                input1 = input("enter dBm value to convert it to Watts")
                ans = ((10**(float(input1)/10))/ 1000)
                print("With a dBm value of", input, "dBm, your expected wattage would be", ans, "Watts")
        elif selector1 == 2:
                unit = input("What unit of frequency are you entering your input in?\n\n (1) Hz\n (2) kHz\n (3) MHz\n (4) GHz")
                if unit == 1:
                        unit1 == "Hz"
                elif unit == 2:
                        unit1 == "kHz"
                elif unit == 3:
                        unit1 == "MHz"
                elif unit == 4:
                        unit1 == "GHz"

                input1 = input("Please enter frequency in order to convert it to wavelength")

                ans = ((c) / input1)
                print("With a frequency of", input1, unit1, "This frequency's wavelength in air is", ans, "Metres")
	#elif selector == 3:

	#elif selector == 4:

	#elif selector == 5:

	#elif selector == 6:

	#elif selector == 7:

	#elif selector == 8:

	#elif selector == 9:

# def antenna_calculator():
# def antenna_calculatorcalc():
# def attenuator_calculator():
# def attenuator_calculatorcalc():
# def microstrip_calculator():
# def microstrip_calculatorcalc():
# def radar_calculator():
# def radar_calculatorcalc():
# def rf_calculator():
# def rf_calculatorcalc():
# def waveguide_calculator():
# def waveguide_calculatorcalc():

#----------//Main\\----------#
print("Welcome to my convertor, please follow me on GitHub if it's useful! :)")

selector = input("Which category would you like to convert? we support any of these topics, just type the number shown to see all subjects within it > \n\n(1) Length\n(2) Weight\n(3) Radio conversion calculators\n(4) Antenna Calculators\n(5) Attenuator Calculators\n(6) Microstrip Calculators\n(7) Radar Calculators\n(8) RF Calculators\n(9) Waveguide Calculators\n(10)My Github\n(11) Exit Programme\n")
print(selector)

if ((float(selector)) == (1)):
	length()
elif ((float(selector)) == (2)):
	weight()
elif ((float(selector)) == (3)):
	radio_calculation_calculator(selector1, c)
elif ((float(selector)) == (4)):
	antenna_calculator()
elif ((float(selector)) == (5)):
	attenuator_calculator()
elif ((float(selector)) == (6)):
	microstrip_calculator()
elif ((float(selector)) == (7)):
	radar_calculator()
elif ((float(selector)) == (8)):
	rf_calculator()
elif ((float(selector)) == (9)):
	waveguide_calculator()
elif ((float(selector)) == (10)):
	webbrowser.open("https://github.com/AxiomYT/")
elif ((float(selector)) == (11)):
	raise SystemExit

#----------//\\----------#
