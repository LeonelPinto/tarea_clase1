def mensaje(opcion):
    print('Hola!')
    print('Como estás?')
    print('Elegiste la opcion: ' + str(opcion))
    print('Adios!')

inf = "Las opciones que puedes elegir son del 1 al 4"

print(inf)
opcion = int(input('Elige la opcion: '))
if (opcion >= 1 and opcion <= 4):
    mensaje(opcion)
else:
    print('Elegisye la opcion incorrecta')