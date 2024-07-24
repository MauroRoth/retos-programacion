
def rgb_to_hexa(r,g,b):
    return f"#{r:02x}{b:02x}{b:02x}"

def hexa_to_rgb(hexa):
    return (int(hexa[0:2], 16), int(hexa[2:4], 16), int(hexa[4:6], 16))

r,g,b = 255, 255, 255
prueba = rgb_to_hexa(r,g,b)
print(prueba)


hexa = "FFAA00"
prueba1 = hexa_to_rgb(hexa)
print(prueba1)
