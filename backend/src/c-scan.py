def c_scan(requests, start, disk_size):
    """
    C-SCAN Implementation

    requests: Lista de solicitudes de cilindros.
    start: Posición inicial del cabezal del disco.
    disk_size: Tamaño del disco.
    return: Orden de procesamiento y tiempo total de búsqueda.
    """
    requests.sort()  # Ordenamos las solicitudes de menor a mayor
    total_seek_time = 0
    current_position = start
    order = []

    # Dividimos las solicitudes en las que están a la derecha e izquierda del cabezal
    right = [r for r in requests if r >= current_position]
    left = [r for r in requests if r < current_position]

    # Procesa las solicitudes en dirección ascendente y luego regresa al inicio
    order = right + [disk_size - 1, 0] + left

    # Calcula el tiempo total de búsqueda
    for pos in order:
        total_seek_time += abs(pos - current_position)
        current_position = pos

    return order, total_seek_time
