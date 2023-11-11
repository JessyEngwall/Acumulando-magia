def porcentaje_error(lecturas):
  lecturas_fuera_rango = [lectura for lectura in lecturas if lectura < 10 or lectura > 40]
  porcentaje = (len(lecturas_fuera_rango) / len(lecturas)) * 100 if len(lecturas) > 0 else 0
  return porcentaje

# Ejemplo de uso
lecturas_sensor = []

while True:
  lectura_str = input("Ingrese lectura del sensor (o 'fin' para terminar): ")

  if lectura_str.lower() == 'fin':
      break

  try:
      lectura = float(lectura_str)
      lecturas_sensor.append(lectura)
  except ValueError:
      print("Ingrese un valor numérico válido.")

porcentaje_error_sensor = porcentaje_error(lecturas_sensor)

print(f"\nPorcentaje de lecturas fuera de rango: {porcentaje_error_sensor:.2f}%")
