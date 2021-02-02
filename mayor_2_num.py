num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))
if num1 < num2:
    print('El número ' +  str(num2) + ' es mayor a ' + str(num1))
elif num1 > num2:
    print('El número ' + str(num1) + ' es mayor a ' + str(num2))
else:
    print('Los dos números son iguales.')
