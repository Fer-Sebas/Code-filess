# PROYECTO
# Hacer un test, un cuestionario que guarde las respuestas, 
# y al final, le de un puntaje al usuario.
# Tema abierto
# Al menos 7 preguntas
# al final, debe decir cuantas se contestaron bien
# debe pedirle el nombre al usuario
# Preguntas de multiples opciones

# TEMA: Star Wars

res1 = "B" # Le decimos al computador cual es la respuesta correcta 
# de la primera pregunta

# 1. Cual fue la razon de la redencion de Darth Vader?
# A. El emperador era una diva.
# B. Su hijo iba a morir.
# C. Luke tenia el terreno alto.

print("1. Cual fue la razon de la redencion de Darth Vader?")
print("A. El emperador era una diva.")
print("B. Su hijo iba a morir.")
print("C. Luke tenia el terreno alto.")

user1 = input("Cual es tu eleccion?")

if user1 == res1:
    print("respuesta correcta")
else:
    print("te equivocaste")