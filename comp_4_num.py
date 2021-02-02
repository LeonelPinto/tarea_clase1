num1 = int(input('Ingresar el primer número: '))
num2 = int(input('Ingresar el segundo número: '))
num3 = int(input('Ingresar el tercero número: '))
num4 = int(input('Ingresar el cuarto número: '))
if num1 == num2 or num1 == num3 or num1 == num4 or num2 == num3 or num2 == num4 or num3 == num4:
    print('Error: números iguales.')
else:
    if num1 > num2 and num1 > num3 and num1 > num4:
        mayor = num1
    else:
        if num2 > num1 and num2 > num3 and num2 > num4:
            mayor = num2
        else:
            if num3 > num1 and num3 > num2 and num3 > num4:
                mayor=num3
            else:
                mayor=num4
    if num1 < num2 and num1 < num3 and num1 < num4 :
        menor = num1
    else:
        if num2 < num1 and num2 < num3 and num2 < num4:
            menor=num2
        else:
            if num3 < num1 and num3 < num2 and num3 < num4:
                menor=num3
            else:
                menor=num4
    print("El número mayor es "+str(mayor)+" y el número menor es "+str(menor))

