def distance_between_points(points1:tuple,points2:tuple):
    x1 ,y1 =  points1
    x2 ,y2 =  points2
    distance = ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)
    return distance
print(distance_between_points((0,0),(4,3)))
