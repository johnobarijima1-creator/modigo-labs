def count_unique_coordinates(coordinates):
    unique = []
    for coord in coordinates:
        if coord not in unique:
            unique.append(coord)
    return len(unique)
print(count_unique_coordinates([(0,0), (1,1), (0,0),]))