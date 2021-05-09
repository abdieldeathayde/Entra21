A = float(input())
B = float(input())
C = float(input())

area_triangulo_retangulo = (A * C) / 2
area_triangulo_retangulo = round(area_triangulo_retangulo, 3)
print("TRIANGULO: " + str(area_triangulo_retangulo))


pi = 3.14159
area_circulo = pi * (C * C)
area_circulo = round(area_circulo, 3)
print("CIRCULO: ", area_circulo)

area_trapezio = ((A + B) * C)/ 2
area_trapezio = round(area_trapezio, 3)
print("TRAPEZIO: ", area_trapezio)

area_quadrado = B * B
area_quadrado = round(area_quadrado,3)
print("QUADRADO: ", area_quadrado)

area_retangulo = A * B
area_retangulo = round(area_retangulo,3)
print("RETANGULO: ", area_retangulo)