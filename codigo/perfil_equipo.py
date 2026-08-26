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
comision = input("Comision: ")

integrante1 = input("Nombre del primer integrante: ").title()
rol1 = input("Rol del primer integrante: ")

integrante2 = input("Nombre del segundo integrante: ").title()
rol2 = input("Rol del segundo integrante: ")

integrante3 = input("Nombre del tercer integrante: ").title()
rol3 = input("Rol del tercer integrante: ")

integrante4 = input("Nombre del cuarto integrante: ").title()
rol4 = input("Rol del cuarto integrante: ")


sigla = generar_sigla(equipo)
cantidad_caracteres = len(equipo)
tiene_digitos = contiene_digitos(equipo)

print(" ")
print("Perfil del Equipo:")
print(f"Equipo: {equipo} (Sigla: {sigla})")
print(f"Comisión: {comision}")
print(f"Cantidad de caracteres del nombre: {cantidad_caracteres}")
print(f"¿El nombre del equipo tiene dígitos?: {tiene_digitos}")
print(" ")
print(f"Integrantes:")
print(f"- {integrante1} | Rol: {rol1}")
print(f"- {integrante2} | Rol: {rol2}")
print(f"- {integrante3} | Rol: {rol3}")
print(f"- {integrante4} | Rol: {rol4}")