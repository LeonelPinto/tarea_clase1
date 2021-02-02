edad = int(input(f'Indicar la edad: '))
if edad >= 18:
    print('Es mayor de edad')    
elif edad < 18 and edad >= 0: 
#no tendrá un año entero pero si meses
    print('Es menor de edad')
else:
    print('Valor incorrecto') 