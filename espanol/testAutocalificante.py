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

# 2. Quien fue el maestro de Obi-Wan Kenobi?
# A. Yoda.
# B. Qui-Gon Jinn.
# C. Mace Windu.

res2 = "B"

print("2. Quien fue el maestro de Obi-Wan Kenobi?")
print("A. Yoda.")
print("B. Qui-Gon Jinn.")
print("C. Mace Windu.")

user2 = input("Cual es tu eleccion?")

if user2 == res2:
    print("respuesta correcta")
else:
    print("te equivocaste")


# 3. Que necesita un Jedi para construir un sable de luz?
# A. Un cristal kyber.
# B. Una piedra de la Estrella de la Muerte.
# C. Un motor de nave espacial.

res3 = "A"

print("3. Que necesita un Jedi para construir un sable de luz?")
print("A. Un cristal kyber.")
print("B. Una piedra de la Estrella de la Muerte.")
print("C. Un motor de nave espacial.")

user3 = input("Cual es tu eleccion?")

if user3 == res3:
    print("respuesta correcta")
else:
    print("te equivocaste")


# 4. Quien construyo a C-3PO?
# A. Luke Skywalker.
# B. El emperador Palpatine.
# C. Anakin Skywalker.

res4 = "C"

print("4. Quien construyo a C-3PO?")
print("A. Luke Skywalker.")
print("B. El emperador Palpatine.")
print("C. Anakin Skywalker.")

user4 = input("Cual es tu eleccion?")

if user4 == res4:
    print("respuesta correcta")
else:
    print("te equivocaste")


# 5. Cual es el planeta natal de Chewbacca?
# A. Kashyyyk.
# B. Tatooine.
# C. Naboo.

res5 = "A"

print("5. Cual es el planeta natal de Chewbacca?")
print("A. Kashyyyk.")
print("B. Tatooine.")
print("C. Naboo.")

user5 = input("Cual es tu eleccion?")

if user5 == res5:
    print("respuesta correcta")
else:
    print("te equivocaste")


# 6. Como se llama la nave de Han Solo?
# A. La Tantive IV.
# B. El Halcon Milenario.
# C. El Destructor Estelar.

res6 = "B"

print("6. Como se llama la nave de Han Solo?")
print("A. La Tantive IV.")
print("B. El Halcon Milenario.")
print("C. El Destructor Estelar.")

user6 = input("Cual es tu eleccion?")

if user6 == res6:
    print("respuesta correcta")
else:
    print("te equivocaste")


# 7. Quien es la madre de Luke Skywalker?
# A. Leia Organa.
# B. Padme Amidala.
# C. Shmi Skywalker.

res7 = "B"

print("7. Quien es la madre de Luke Skywalker?")
print("A. Leia Organa.")
print("B. Padme Amidala.")
print("C. Shmi Skywalker.")

user7 = input("Cual es tu eleccion?")

if user7 == res7:
    print("respuesta correcta")
else:
    print("te equivocaste")