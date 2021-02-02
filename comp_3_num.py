num1 = int(input('Ingresar el primer número: '))
num2 = int(input('Ingresar el segundo número: '))
num3 = int(input('Ingresar el tercero número: '))
if num1 == num2 or num1 == num3 or num2 == num3:
    print('Error: números iguales.')
else:
    if num1 > num2 and num1 > num3:
        mayor = num1
        if num2 > num3:
            menor = num3
            #print('El número ' + str(num1) + ' es el mayor.')
            #print('Y el número ' + str(num3) + ' es el menor')
        else:
            menor = num2
            #print('El número ' + str(num1) + ' es el mayor.')
            #print('Y el número ' + str(num2) + ' es el menor')
    
    elif num2 > num1 and num2 > num3:
        mayor = num2
        if num1 > num3:
            menor = num3
            #print('El número ' + str(num2) + ' es el mayor.')
            #print('Y el número ' + str(num3) + ' es el menor')
        else:
            menor = num1
            #print('El número ' + str(num2) + ' es el mayor.')
            #print('Y el número ' + str(num1) + ' es el menor')
    else:
        mayor = num3
        if num1 > num2:
            menor = num2
            #print('El número ' + str(num3) + ' es el mayor.')
            #print('Y el número ' + str(num2) + ' es el menor.')
        else:
            menor = num1
            #print('El número ' + str(num3) + ' es el mayor.')
            #print('Y el número ' + str(num1) + ' es el menor.')

    print('El número ' + str(mayor) + ' es el mayor y el número ' + str(menor) + ' es el menor.')