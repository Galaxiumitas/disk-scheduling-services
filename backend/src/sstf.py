def sstf(requests, start):
    current_position = start
    total_seek_time = 0
    order = []

    while requests:
        closest_request = min(requests, key=lambda x: abs(x - current_position))
        seek_time = abs(closest_request - current_position)
      
        total_seek_time += seek_time
        current_position = closest_request
      
        order.append(closest_request)
        requests.remove(closest_request)

    return order, total_seek_time
