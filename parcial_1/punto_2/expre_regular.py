# AFD para identificadores
# Expresion regular: [A-Za-z][A-Za-z0-9]*

def clasificar(ch):
    if ch.isalpha():
        return 'LETRA'
    if ch.isdigit():
        return 'DIGITO'
    return 'OTRO'

transiciones = {
    ('q0', 'LETRA'):  'q1',
    ('q0', 'DIGITO'): 'qE',
    ('q0', 'OTRO'):   'qE',

    ('q1', 'LETRA'):  'q1',
    ('q1', 'DIGITO'): 'q1',
    ('q1', 'OTRO'):   'qE',

    ('qE', 'LETRA'):  'qE',
    ('qE', 'DIGITO'): 'qE',
    ('qE', 'OTRO'):   'qE',
}

def correr_afd(token):
    estado = 'q0'

    if not token:
        return False

    for ch in token:
        clase = clasificar(ch)
        estado = transiciones[(estado, clase)]
        if estado == 'qE':
            break

    return estado == 'q1'

# pruebas: 3 acepta, 2 rechaza
casos = [
    "miVariable",
    "Var99",
    "A",
    "1abc",
    "",
]

for token in casos:
    aceptado = correr_afd(token)
    resultado = "ACEPTA" if aceptado else "RECHAZA"
    print(f"Token: '{token}' -> {resultado}")
