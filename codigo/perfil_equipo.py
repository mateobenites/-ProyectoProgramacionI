def generar_sigla(nombre):
    palabras = nombre.split()
    sigla = ""

    for palabra in palabras:
        sigla += palabra[0].upper()

    return sigla

def contiene_digitos(texto):
    val = False

    for caracter in texto:
        if caracter.isdigit():
            val = True

    return val

equipo = input("Nombre del equipo: ").upper()
comision = input("Comisión: ")

integrante1 = input("Nombre del primer integrante: ")
integrante2 = input("Nombre del segundo integrante: ")

sigla = generar_sigla(equipo)
cantidad_caracteres = len(equipo)
tiene_digitos = contiene_digitos(equipo)

#FALTA AGREGAR PRINTS