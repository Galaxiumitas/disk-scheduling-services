def clook(requests, start):
    """
    C-LOOK Implementation

    requests: Lista de solicitudes de cilindros.
    start: Posición inicial del cabezal del disco.
    return: Orden de procesamiento y tiempo total de búsqueda.
    """
    requests.sort()  # Ordenamos las solicitudes de menor a mayor
    total_seek_time = 0
    current_position = start
    order = []

    # Dividimos las solicitudes en función de la posición actual del cabezal
    right = [r for r in requests if r >= current_position]
    left = [r for r in requests if r < current_position]

    # Procesa las solicitudes hacia la derecha y luego salta al inicio de las solicitudes más pequeñas
    order = right + left

    # Calcula el tiempo total de búsqueda
    for pos in order:
        total_seek_time += abs(pos - current_position)
        current_position = pos

    return order, total_seek_time
