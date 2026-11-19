import json

with open ('data.json') as f:
    data = json.load(f)

# TOTAL FACTURADO

total = 0

for producto in data["ventas"]:
    ingresos = producto["precio_unitario"] * producto["cantidad"]
    total += ingresos

print(f"Total facturado:{total:.2f} €")

# VENTAS POR CATEGORIA

totales = {}

for venta in data["ventas"]:
    categ = venta["categoria"]
    totales[categ] = totales.get(categ,0) + venta["cantidad"] * venta["precio_unitario"]

print(dict(totales))

# PRODUCTO MÁS VENDIDO

unidades = {}

for venta in data["ventas"]:
    prod = venta["producto"]
    unidades[prod] = unidades.get(prod, 0) + venta["cantidad"]

mas_vendido = max(unidades, key=unidades.get)
print(mas_vendido, unidades[mas_vendido])