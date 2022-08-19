# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	cs = float()
	cp = float()
	fp = float()
	i = float()
	j = float()
	cont = float()
	aux = float()
	max = float()
	posmax = float()
	max2 = float()
	posmax2 = float()
	dinero_tp = float()
	prom = float()
	promedio = float()
	prom_total = float()
	prom_prod = float()
	producto = float()
	dinero_suc = float()
	un_pr = float()
	sum = float()
	precio = float()
	met_pago = float()
	un_suc = float()
	vaux = float()
	un_pr = [float() for ind0 in range(5)]
	prom_prod = [float() for ind0 in range(5)]
	producto = [float() for ind0 in range(5)]
	dinero_tp = [float() for ind0 in range(5)]
	dinero_suc = [float() for ind0 in range(15)]
	met_pago = [float() for ind0 in range(4)]
	un_suc = [float() for ind0 in range(15)]
	vaux = [float() for ind0 in range(15)]
	producto[0] = 300
	producto[1] = 550
	producto[2] = 600
	producto[3] = 650
	producto[4] = 900
	for i in range(1,5):
		met_pago[i-1] = 0
	for i in range(1,6):
		un_pr[i-1] = 0
		dinero_tp[i-1] = 0
	for i in range(1,16):
		un_suc[i-1] = 0
		dinero_suc[i-1] = 0
		vaux[i-1] = i
	sum = 0
	cs = ALEATORIO(1,15)
	while cs!=0:
		cp = ALEATORIO(1,5)
		fp = ALEATORIO(1,4)
		if fp==4:
			producto[cp-1] = producto[cp-1]*1.05
		un_pr[cp-1] = un_pr[cp-1]+1
		dinero_tp[cp-1] = dinero_tp[cp-1]+producto[cp-1]
		dinero_suc[cs-1] = dinero_suc[cs-1]+producto[cp-1]
		met_pago[fp-1] = met_pago[fp-1]+1
		un_suc[cs-1] = un_suc[cs-1]+1
		sum = sum+producto[cp-1]
		print("Ingrese codigo de sucursal: ")
		cs = int(input())
	print("Punto 1")
	print("Unidades vendidas por cada producto")
	for i in range(1,6):
		print(i,") ",un_pr[i-1]," unidades vendidas")
	print("--------------------------")
	print("Punto 2")
	print("Dinero Ingresado por tipo de Producto")
	for i in range(1,6):
		print(i,") ",dinero_tp[i-1]," $")
	print("------------------------")
	print("Punto 3")
	print("Promedio por cada tipo de producto")
	print("---------------------------")
	sum = 0
	for i in range(1,6):
		if un_pr[i-1]!=0:
			prom_prod[i-1] = dinero_tp[i-1]/un_pr[i-1]
		print("Producto ",i," promedio de: ",prom_prod[i-1]," $ en ventas")
		sum = sum+prom_prod[i-1]
	prom_total = sum/5
	print("--------------------------------")
	print("Punto 4")
	print("Producto que supera el pPromedio Total: >>",prom_total,"<<")
	cont = 0
	for i in range(1,6):
		if prom_prod[i-1]>prom_total:
			cont = cont+1
			print("El producto ",i," supera el promedio: ",prom_prod[i-1])
	print("------------------------")
	print("En total ",cont," productos superan el promedio")
	print("---------------------------")
	print("Punto 5")
	print("La sucursal que mas dinero recaudo")
	max = dinero_suc[0]
	posmax = 1
	for i in range(1,15):
		if max>dinero_suc[i-1]:
			max = dinero_suc[i-1]
			posmax = i
	print("La sucurasl ",posmax," tuvo mas ingresos con ",max," $ en ventas")
	print("--------------------------")
	print("Punto 6")
	print("El metodo de pago mas utilizado")
	max = met_pago[0]
	posmax = 1
	for i in range(1,4):
		if max>met_pago[i-1]:
			max = met_pago[i-1]
			posmax = i
	print("El metodo de pago mas utilizado es el ",posmax," con ",max," usos")
	print("--------------------------")
	print("Punto 7")
	print("Sucursales ordenadas segun ingresos: ")
	print("-------------------------------")
	for j in range(1,15):
		for i in range(1,16-j):
			if un_suc[i-1]<un_suc[i]:
				aux = un_suc[i-1]
				un_suc[i-1] = un_suc[i]
				un_suc[i] = aux
				aux = vaux[i-1]
				vaux[i-1] = vaux[i]
				vaux[i] = aux
	for i in range(1,16):
		print(") ",un_suc[i-1]," unidades de la Sucursal: ",vaux[i-1])

