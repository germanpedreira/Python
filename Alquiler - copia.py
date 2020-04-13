#This program calculates the total of a rental contract


print('Hola Lares')

print ('Cuanto sale el primer mes de alquiler?')
rental= input()

print( 'De que % es la actualizacion')
porcentaje = (int(input()))/100

actualizacion = ''
while not (actualizacion == '1' or actualizacion == '2'):
#while actualizacion != '1' and actualizacion !='2':
    print ('Si la actualización es anual introduzca 1, su la actualizacion es semestral introduzca 2')
    actualizacion= input()

contrato_anual= str(int((int(rental) * 12 + (int(rental)) * (1 + float(porcentaje)) *12)))
año2anual= str (int(int(rental) * (1 + float(porcentaje))))
contrato_semestral= str(int(((int(rental) * 6 + (int(rental)) * (1 + float(porcentaje)) *6) + (int(rental) * ((1 + float(porcentaje))**2)) * 6 + (int(rental) * ((1 + float(porcentaje))**3)) * 6)))
semestre2= str (int(int(rental) * (1 + float(porcentaje))))
semestre3= str (int(int(rental) * (((1 + float(porcentaje)) **2))))
semestre4= str (int(int(rental) * (((1 + float(porcentaje)) **3))))


if actualizacion== '1':
    print('El contrato sera de $' + contrato_anual)
    print('El alquiler durante el primer ano sera de $' + rental)
    print('El alquiler durante el segundo ano sera de $' + año2anual)

else:
    print('El contrato sera de ' + contrato_semestral)
    print('El alquiler durante el primer semestre sera de $' + rental)
    print('El alquiler durante el segundo semestre sera de $' + semestre2)
    print('El alquiler durante el tercer semestre sera de $' + semestre3)
    print('El alquiler durante el cuarto semestre sera de $' + semestre4)

print('Presiona Enter para cerrar el programa')
input()
