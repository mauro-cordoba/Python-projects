# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


import random

if __name__ == '__main__':

	unidades_falladas_operario = ["","","","","",""]
	kg_producto = ["","","","","",""]
	kg_operario = ["","","","","",""]
	unidades_producto = ["","","",""]
	unidades_operario = ["","","","","",""]
	prom1 = ["","","","","",""]
	prom = ["","","","","",""]
	vaux = ["","","",""]
	for i in range(1,5):
		kg_producto[i-1] = 0
		unidades_producto[i-1] = 0
		vaux[i-1] = i
	for i in range(1,7):
		kg_operario[i-1] = 0
		unidades_falladas_operario[i-1] = 0
		unidades_operario[i-1] = 0
	print("Codigo de operario:")
	co = int(input())
	while co!=0:
		cp = random.randint(1,4)
		cm = random.randint(1,5)
		uf = random.randint(5,20)
		up = random.randint(5,40)
		kg = random.randint(1,20)
		unidades_falladas_operario[co-1] = unidades_falladas_operario[co-1]+uf
		unidades_operario[co-1] = unidades_operario[co-1]+1
		kg_producto[cp-1] = kg_producto[cp-1]+kg
		kg_operario[co-1] = kg_operario[co-1]+kg
		unidades_producto[cp-1] = unidades_producto[cp-1]+1
		print("Codigo de operario:")
		co = int(input())
	print("------------------------")
	print("Punto 1: Promedio de Unidades Falladas por lote para cada operario:")
	print("---------------------------------")
	for co in range(1,7):
		if unidades_operario[co-1]!=0:
			prom1[co-1] = unidades_falladas_operario[co-1]/unidades_operario[co-1]
		else:
			prom1[co-1] = 0
		print("Operario ",co," --> Unidades falladas: ",prom1[co-1])
	print("-----------------------------")
	for i in range(1,7):
		print(i,") ",prom1[i-1])
	print("---------------------------")
	print("Punto 2: La menor cantidad de KG utilizada por producto")
	print("----------------------------")
	for cp in range(1,5):
		print(co,") ",kg_producto[cp-1],"Kg")
	min = kg_producto[0]
	posmin = 1
	for i in range(2,5):
		if min>kg_producto[i-1]:
			min = kg_producto[i-1]
			posmin = i
	print("El producto ",posmin," es el que consume menor cantidad: ",min," Kg")
	print("--------------------------")
	print("Punto 3: operarios que sueran el promedio de Kg utilizada por cada operario")
	sum = 0
	for co in range(1,7):
		if unidades_operario[co-1]!=0:
			prom[co-1] = kg_operario[co-1]/unidades_operario[co-1]
		else:
			prom[co-1] = 0
		print("Operario: ",co," --> Kg prom: ",prom[co-1])
		sum = sum+prom[co-1]
	print("------------------------------")
	prom_total = sum/6
	print("El promedio total es: ",prom_total," Kg x Opeario")
	print("--------------------------------")
	max = prom[0]
	posmax = 1
	for i in range(1,6):
		if prom[i-1]>prom_total:
			max = prom[i-1]
			posmax = i
			print("El operario: ",posmax," supera el promedio con: ",max)
	print("------------------------------")
	cont = 0
	for i in range(1,7):
		if prom[i-1]>prom_total:
			cont = cont+1
	print("Un total de ",cont," operarios superan el promedio")
	print("----------------------------")
	print("Punto  4: Vector de menor a mayor con unidades producidas por producto")
	print("----------------------------")
	for j in range(1,4):
		for i in range(1,5-j):
			if unidades_producto[i-1]>unidades_producto[i]:
				aux = unidades_producto[i-1]
				unidades_producto[i-1] = unidades_producto[i]
				unidades_producto[i] = aux
				aux = vaux[i-1]
				vaux[i-1] = vaux[i]
				vaux[i] = aux
	for i in range(1,5):
		print("Producto: ",vaux[i-1]," Unidades producidas: ",unidades_producto[i-1])
	print("--------------------------------------")
	print("Punto 5:")

