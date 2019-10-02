from itertools import combinations
from math import sqrt, hypot

def wild_dogs(coords):

    def same_line(p1, p2, p3):

        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3

        return abs((x1 - x2) * (y1 - y3)) == abs((x1 - x3) * (y1 - y2))

    def distance(group):

        x0, y0 = group[0]
        x1, y1 = group[1]

        # the line passing through p0 and p1 : a*x + b*y == c

        a = y1 - y0
        b = x0 - x1
        c = b * y0 + a * x0

        # distance from (0, 0) to the line
        return abs(c) / hypot(a, b)

    # make group of point on same line.

    groups = []
    for p1, p2 in combinations(coords, 2):

        groups.append([p for p in coords if same_line(p1, p2, p)])

    # return nearest distance with max dogs.
    return round(min((-len(g), distance(g)) for g in groups)[1], 2)



if __name__ == '__main__':
    print("Example:")
    print(wild_dogs([(7, 122), (8, 139), (9, 156),
                     (10, 173), (11, 190), (-100, 1)]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert wild_dogs([(7, 122), (8, 139), (9, 156),
                      (10, 173), (11, 190), (-100, 1)]) == 0.18

    assert wild_dogs([(6, -0.5), (3, -5), (1, -20)]) == 3.63

    assert wild_dogs([(10, 10), (13, 13), (21, 18)]) == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
