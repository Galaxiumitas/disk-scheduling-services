def look(requests, start, direction):
    """
    LOOK Implementation

    requests: Lista de solicitudes de cilindros.
    start: Posición inicial del cabezal del disco.
    direction: Dirección inicial del movimiento.
    return: Orden de procesamiento y tiempo total de búsqueda.
    """
    requests.sort()
    total_seek_time = 0
    current_position = start
    order = []

    left = [r for r in requests if r < current_position]
    right = [r for r in requests if r >= current_position]

    if direction == "derecha":
        order = right + left[::-1]
      
    elif direction == "izquierda":
        order = left[::-1] + right

    for pos in order:
        total_seek_time += abs(pos - current_position)
        current_position = pos

    return order, total_seek_time
