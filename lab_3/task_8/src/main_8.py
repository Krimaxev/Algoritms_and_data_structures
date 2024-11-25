'''import heapq

def find_k_closest(points, k):
    if not points:
        return []

    closest_points = []
    for x, y in points:
        distance_squared = x ** 2 + y ** 2
        heapq.heappush(closest_points, (-distance_squared, (x, y)))
        if len(closest_points) > k:
            heapq.heappop(closest_points)

    result = [point for _, point in closest_points]
    return result


if __name__=="__main__":'''

