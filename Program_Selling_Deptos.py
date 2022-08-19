# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	cv = int()
	vv = int()
	ca = int()
	pd = int()
	i = int()
	j = int()
	cont = int()
	sum = int()
	posmax = int()
	max = int()
	posmax2 = int()
	max2 = int()
	comision = int()
	valor_ambientes = int()
	piso = int()
	ambientes = int()
	aux = int()
	vaux = int()
	porcentaje = float()
	porcentaje_vendedor = float()
	vendedor = float()
	prom = float()
	vendedor = [float() for ind0 in range(10)]
	piso = [int() for ind0 in range(15)]
	ambientes = [int() for ind0 in range(4)]
	comision = [int() for ind0 in range(10)]
	valor_ambientes = [int() for ind0 in range(4)]
	vaux = [int() for ind0 in range(10)]
	porcentaje_vendedor = 0.015
	for i in range(1,11):
		vendedor[i-1] = 0
		comision[i-1] = 0
	for i in range(1,5):
		ambientes[i-1] = 0
		valor_ambientes[i-1] = 0
		vaux[i-1] = i
	for i in range(1,16):
		piso[i-1] = 0
	print("ingrese la carga de datos")
	print("Se realizaran 104 cargas aleatorias")
	cont = 0
	for i in range(1,105):
		cv = ALEATORIO(1,10)
		vv = ALEATORIO(10000,40000)
		ca = ALEATORIO(1,4)
		pd = ALEATORIO(1,15)
		vendedor[cv-1] = vendedor[cv-1]+1
		ambientes[ca-1] = ambientes[ca-1]+1
		piso[pd-1] = piso[pd-1]+1
		comision[cv-1] = comision[cv-1]+vv
		valor_ambientes[ca-1] = valor_ambientes[ca-1]+vv
		if cv==6 and ca==1:
			cont = cont+1
	for cv in range(1,11):
		print("El vendedor ",cv," realizo: ",vendedor[cv-1]," ventas")
	print("-----------------------------")
	print("Punto 1")
	posmax = 1
	max = vendedor[0]
	for i in range(1,11):
		if max<vendedor[i-1]:
			max = vendedor[i-1]
			posmax = i
	print("El vendedor que realizo mas ventas fue el numero ",posmax," con ",max," ventas")
	print("------------------------")
	print("Punto 2")
	for ca in range(1,5):
		print("Departamentos vendidos de ",ca," ambiente/s: ",ambientes[ca-1])
	print("---------------------")
	print("Punto 3")
	posmax2 = 1
	max2 = piso[0]
	for i in range(2,16):
		if max2<piso[i-1]:
			max2 = piso[i-1]
			posmax2 = i
	print("EL piso ",posmax2," tiene a mayor cantidad de Dptos con ",max2," departamentos")
	print("---------------------------")
	print("Punto 4")
	for cv in range(1,11):
		print("Vendedor ",cv," vendio una cantidad de: ",comision[cv-1]," $")
	print("--------------------------------")
	max = comision[0]
	posmax = 1
	for i in range(2,11):
		if max<comision[i-1]:
			max = comision[i-1]
			posmax = i
	porcentaje = max*porcentaje_vendedor
	print("El vendedor ",posmax," obtuvo mayor comision con ",porcentaje," $ obtenido por ventas")
	print("--------------------------")
	print("Punto 5")
	for ca in range(1,5):
		prom = valor_ambientes[ca-1]/ambientes[ca-1]
		print("Dpto de: ",ca," ambiente/s  Valor promedio de venta: ",prom)
	print("-----------------------------")
	print("Punto 6")
	print("El vendedor 6 vendio ",cont," Deptos de 1 ambiente")
	print("----------------------------")
	print("Punto 7")
	for j in range(1,4):
		for i in range(1,5-j):
			if valor_ambientes[i-1]<valor_ambientes[i]:
				aux = valor_ambientes[i-1]
				valor_ambientes[i-1] = valor_ambientes[i]
				valor_ambientes[i] = aux
				aux = vaux[i-1]
				vaux[i-1] = vaux[i]
				vaux[i] = aux
	for i in range(1,5):
		print("Dpto de ",vaux[i-1]," ambientes con ingresos: ",valor_ambientes[i-1])

