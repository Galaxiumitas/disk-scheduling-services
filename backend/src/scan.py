def scan(requests, start, direction, disk_size):
    """
    SCAN Implementation
    
    requests: Lista de solicitudes de cilindros.
    start: Posición inicial del cabezal del disco.
    direction: Dirección inicial del movimiento .
    disk_size: Tamaño del disco.
    return: Orden de procesamiento y tiempo total de búsqueda.
    """
    requests.sort()
    total_seek_time = 0
    current_position = start
    order = []

    if direction == "izquierda":
        left = [r for r in requests if r < current_position]
        right = [r for r in requests if r >= current_position]
        order = left[::-1] + right
      
    elif direction == "derecha":
        left = [r for r in requests if r < current_position]
        right = [r for r in requests if r >= current_position]
        order = right + left[::-1]

    for pos in order:
        total_seek_time += abs(pos - current_position)
        current_position = pos

    return order, total_seek_time
