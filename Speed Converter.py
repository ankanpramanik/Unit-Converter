# Speed Converter
print("            Speed Coverter")
print(" ===================================")
# km/h to mph
kilometers = float(input("km/h » mph: "))

conv_fac = 0.621371192

miles = kilometers * conv_fac

print("%d km/h equal to %f mph" %(kilometers,miles))

# mph to km/h
miles = float(input("mph » km/h: "))

conv_fac = 1.609344

kilometers = miles * conv_fac

print("%d mph equal to %f km/h" %(miles,kilometers))

# km/h to m/s
kilometers = float(input("km/h » m/s: "))

conv_fac = 0.277777778

meters = kilometers * conv_fac

print("%d km/h equal to %f m/s" %(kilometers,meters))

# m/h to km/h
meters = float(input("m/s » km/h: "))

conv_fac = 3.6

kilometers = meters * conv_fac

print("%d m/s equal to %0.2f km/h" %(meters,kilometers))

# km/h to kn
meters = float(input("km/h » kn: "))

conv_fac = 0.5399568034557235

centimeters = meters * conv_fac

print("%d km/h equal to %f kn" %(meters,centimeters))

# kn to km/h
cm = float(input("kn » km/h: "))

conv_fac = 1.852

meters = cm * conv_fac

print("%d kn equal to %0.3f km/h" %(cm,meters))

# km/h to Mach
cm = float(input("km/h » Mach: "))

conv_fac = 0.0008376893

meters = cm * conv_fac

print("%d km/h equal to %0.10f Mach" %(cm,meters))

# Mach to km/h
cm = float(input("Mach » km/h: "))

conv_fac = 1193.76

meters = cm * conv_fac

print("%d Mach equal to %0.2f km/h" %(cm,meters))