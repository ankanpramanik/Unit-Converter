# Degrees Converter
print("          Degrees Converter")
print(" ===================================")
# ℃ to ℉
celcius = float(input("℃ » ℉: "))

fahrenheit = (celcius * 1.8 ) + 32

print('%0.1f ℉' %(fahrenheit))

# ℉ to ℃
fahrenheit = float(input("℉ » ℃: "))

celcius = (fahrenheit - 32) / 1.8

print('%0.1f ℃' %(celcius))

# ℃ to °K
celcius = float(input("℃ » °K: "))

kelvin = celcius + 273.15

print('%0.2f °K' %(kelvin))

# °K to ℃
kelvin = float(input("°K » ℃: "))

celcius = kelvin - 273.15

print('%0.1d ℃' %(celcius))