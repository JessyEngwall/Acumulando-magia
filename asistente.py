def detectar_alexa(texto):
  palabras = texto.split()
  contador_alexa = palabras.count('Alexa')

  if contador_alexa == 1:
      return "¡Hola, soy Alexa!"
  elif contador_alexa > 1:
      return "Tranquilo, solo di mi nombre una vez"
  else:
      return "No mencionaste Alexa en el texto"

# Ejemplo de uso
texto_usuario = input("Escribe un texto: ")
respuesta = detectar_alexa(texto_usuario)
print(respuesta)
