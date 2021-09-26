# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 10:32:48 2021

@author: ACER PC
"""
valor = 0
cantidad = 0
agregar = "no"
ganancias = []
gastos = []
impuesto = "Pagar impuesto"
noimpuesto = "No pagar impuestos"
mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
estado = []
agregar = input("Bienvenido a la Administracion de Ganancias y Gastos \n\n ¿Desea agregar informacion mensual?")

while (agregar == "si"):
    valor = float(input("¿Cual fue la ganancia mensual de este mes?"))
    ganancias.append(valor)
    valorg = float(input("¿Cual fue el gasto mensual de este mes?"))
    gastos.append(valorg)
    if (valor > valorg):
        estado.append(impuesto)
        print(impuesto)
    else:
        estado.append(noimpuesto)
        print(noimpuesto)
    cantidad = cantidad +1
    agregar = input("¿Desea agregar mas informacion?")

for i in range(cantidad):
    print(f'Mes : {mes[i]} Ganancias : {ganancias[i]} Gastos: {gastos[i]} Estado: {estado[i]}')
        
