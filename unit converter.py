print("Welcome to Unit Converter")
print("For converting temperature units enter T\nFor converting distance units enter D\nFor converting speed units enter S\n")
unit=input("What do you want to convert?")
if unit=="T":
    print("          Degrees Converter")
    print(" ===================================")
    print("For converting ℃ to ℉  enter 1 \n For converting ℉ to ℃  enter 2 \n For converting ℃ to °K  enter 3 \n For converting °K to ℃  enter 4\n ")
    val=int(input("What do you want to convert?\n"))
    if val==1:
        # ℃ to ℉
        celcius = float(input("℃ » ℉: "))
        fahrenheit = (celcius * 1.8 ) + 32
        print('%0.1f ℉' %(fahrenheit))
    elif val==2:
        # ℉ to ℃
        fahrenheit = float(input("℉ » ℃: "))
        celcius = (fahrenheit - 32) / 1.8
        print('%0.1f ℃' %(celcius))
    elif val==3:
        # ℃ to °K
        celcius = float(input("℃ » °K: "))
        kelvin = celcius + 273.15
        print('%0.2f °K' %(kelvin))
    elif val==4:
        # °K to ℃
        kelvin = float(input("°K » ℃: "))
        celcius = kelvin - 273.15
        print('%0.1d ℃' %(celcius))
elif unit=="D":
    # Distance Converter
    print("        Distance Coverter")
    print("===================================")
    print("For converting Km to Miles  enter 1 \n For converting Miles to Km  enter 2 \n For converting Km to metre  enter 3 \n For converting metres to Km  enter 4\n For converting metres to cm  enter 5\n For converting cm to metres  enter 4\n ")
    val=int(input("What do you want to convert?"))
    if val==1:
        # Kilometers to Miles
        kilometers = float(input("km » mi: "))
        conv_fac = 0.621371
        miles = kilometers * conv_fac
        print("%0.2f km equal to %0.2f mi" %(kilometers,miles))
    if val==2:
        # Miles to Kilometers
        miles = float(input("mi » km:"))
        conv_fac = 0.621371
        kilometers = miles / conv_fac
        print("%0.2f mi equal to %0.2f km" %(miles,kilometers))
    if val==3:
        # Kilometers to Meters
        kilometers = float(input("km » m: "))
        conv_fac = 1000
        meters = kilometers * conv_fac
        print("%0.2f km equal to %0.2f m" %(kilometers,meters))
    if val==4:
        # Meters to Kilometers
        meters = float(input("m » km: "))
        conv_fac = 1000
        kilometers = meters / conv_fac
        print("%0.2f m equal to %0.2f km" %(meters,kilometers))
    if val==5:
        # Meters to Centimeters
        meters = float(input("m » cm: "))
        conv_fac = 100
        centimeters = meters * conv_fac
        print("%0.1d m equal to %0.2d cm" %(meters,centimeters))
    if val==6:
        # Cm to Meters
        cm = float(input("cm » m: "))
        conv_fac = 100
        meters = cm / conv_fac
        print("%0.1d cm equal to %0.1d m" %(cm,meters))
elif unit=="S":
    # Speed Converter
    print("            Speed Coverter")
    print(" ===================================")
    print("For converting km/h to mph enter 1 \nFor converting mph to km/h enter 2 \nFor converting km/h to m/s enter 3 \nFor converting m/h to km/h enter 4\nFor converting km/h to kn enter 5\nFor converting kn to km/h enter 6\nFor converting km/h to Mach enter 7\nFor converting Mach to km/h enter 8\n")
    val=int(input("What do you want to convert?\n"))
    if val==1:
        # km/h to mph
        kilometers = float(input("km/h » mph: "))
        conv_fac = 0.621371192
        miles = kilometers * conv_fac
        print("%d km/h equal to %f mph" %(kilometers,miles))
    if val==2:
        # mph to km/h
        miles = float(input("mph » km/h: "))
        conv_fac = 1.609344
        kilometers = miles * conv_fac
        print("%d mph equal to %f km/h" %(miles,kilometers))
    if val==3:
        # km/h to m/s
        kilometers = float(input("km/h » m/s: "))
        conv_fac = 0.277777778
        meters = kilometers * conv_fac
        print("%d km/h equal to %f m/s" %(kilometers,meters))
    if val==4:
        # m/h to km/h
        meters = float(input("m/s » km/h: "))
        conv_fac = 3.6
        kilometers = meters * conv_fac
        print("%d m/s equal to %0.2f km/h" %(meters,kilometers))
    if val==5:
        # km/h to kn
        meters = float(input("km/h » kn: "))
        conv_fac = 0.5399568034557235
        centimeters = meters * conv_fac
        print("%d km/h equal to %f kn" %(meters,centimeters))
    if val==6:
        # kn to km/h
        cm = float(input("kn » km/h: "))
        conv_fac = 1.852
        meters = cm * conv_fac
        print("%d kn equal to %0.3f km/h" %(cm,meters))
    if val==7:
        # km/h to Mach
        cm = float(input("km/h » Mach: "))
        conv_fac = 0.0008376893
        meters = cm * conv_fac
        print("%d km/h equal to %0.10f Mach" %(cm,meters))
    if val==8:
        # Mach to km/h
        cm = float(input("Mach » km/h: "))
        conv_fac = 1193.76
        meters = cm * conv_fac
        print("%d Mach equal to %0.2f km/h" %(cm,meters))
