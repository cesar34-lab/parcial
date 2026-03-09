
PIECES  = set('KQRBNkqrbn')
COLS    = set('abcdefghpP')
ROWS    = set('12345678')
ARROWS  = {'-'}
GT      = {'>'}
CAPTURE = {'X', 'x'}

def classify(ch):
    if ch in PIECES:  return 'PIECE'
    if ch in COLS:    return 'COL'
    if ch in ROWS:    return 'ROW'
    if ch in ARROWS:  return 'DASH'
    if ch in GT:      return 'GT'
    if ch in CAPTURE: return 'CAP'
    return 'OTHER'

TRANSITIONS = {
    ('q0', 'PIECE'): 'q1',
    ('q0', 'COL'):   'q1',
    ('q1', 'COL'):   'q2',
    ('q1', 'ROW'):   'q3',
    ('q1', 'DASH'):  'q4',
    ('q1', 'CAP'):   'q5',
    ('q2', 'ROW'):   'q3',
    ('q2', 'DASH'):  'q4',
    ('q2', 'CAP'):   'q5',
    ('q3', 'DASH'):  'q4',
    ('q3', 'CAP'):   'q5',
    ('q4', 'GT'):    'q5',
    ('q5', 'PIECE'): 'q6',
    ('q5', 'COL'):   'q7',
    ('q6', 'COL'):   'q7',
    ('q7', 'ROW'):   'q8',
}

ACCEPT_STATE = 'q8'

def run_afd(token):
    """
    Ejecuta el AFD sobre los movimiento de ajedrez.
    Retorna (estado_final, traza_de_estados).
    """
    token = token.strip()
    token = token.replace(' X ', 'X').replace(' x ', 'x')

    state = 'q0'
    trace = [state]

    for ch in token:
        if ch == ' ':
            continue
        cls = classify(ch)
        key = (state, cls)
        state = TRANSITIONS.get(key, 'qE')
        trace.append(state)
        if state == 'qE':
            break

    return state, trace

def validate_moves(moves):
    #Valida una lista de movimientos e imprime resultados.

    for move in moves:
        final, trace = run_afd(move)
        accepted = final == ACCEPT_STATE
        status   = " ACEPTA" if accepted else " RECHAZA"
        print(f"  {move:<20} → {status}  (traza: {' → '.join(trace)})")
    print("=" * 60)


test_moves = [
    "p->k4",
    "kbpXqn",
    "kbp X qn",
    "Ke2->e4",
    "Qd1Xd7",
    "e4",
    "->k4",
    "p--k4",
    "zz->k9",
]

validate_moves(test_moves)
