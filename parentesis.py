abrir_lista = ["[", "{", "("]
cerrar_lista = ["]", "}", ")"]


def verificarParentesis(cadena):
    lista = []
    for i in cadena:
        if i in abrir_lista:
            lista.append(i)
        elif i in cerrar_lista:
            pos = cerrar_lista.index(i)
            if ((len(lista) > 0) and
                    (abrir_lista[pos] == lista[len(lista) - 1])):
                lista.pop()
            else:
                return "Incorrecto"
    if len(lista) == 0:
        return "Correcto"
    else:
        return "Incorrecto"


cadena = "[{((())())}]{[]}"
print(cadena, "-", verificarParentesis(cadena))

cadena = "(({}))[]"
print(cadena, "-", verificarParentesis(cadena))

cadena = ")([])("
print(cadena, "-", verificarParentesis(cadena))

cadena = "(){[]([]"
print(cadena, "-", verificarParentesis(cadena))
