clientes = {}

while True: 
  nombre_cliente = input("Ingrese el nombre del cliente (o 'salir' para terminar): ")

  if nombre_cliente.lower() == 'salir':
    break

varita_elegida = int(input("Seleccione la varita comprada (1. Varita de Saúco, 2.Varita de Espino, 3.Varita de Sauce, 4.Varita de Acebo): "))

if varita_elegida < 1 or varita_elegida > 4:
  print("Opción de varita no válida. Inténtelo de nuevo.")
  continue

varitas = {
  1: "Varita de Saúco",
  2: "Varita de Espino",
  3: "Varita de Sauce",
  4: "Varita de Acebo"
}

if nombre_cliente in clientes:
  clientes[nombre_cliente].append(varitas[varita_elegida])
else:
  clientes[nombre_cliente] = [varitas[varita_elegida]]

print("\nRegistro de clientes y varitas compradas:")

for cliente, varitas_compradas in clientes.items():

print(f"{cliente}: {', '.join(varitas_compradas)}") 
