def navigation(seaside):
    y = [0, 0]
    c = [0, 0]
    m = [0, 0]
    s = [0, 0]

    for i in range(len(seaside)):
        for j in range(len(seaside[i])):
            if seaside[i][j] == 'Y':
                y = [i, j]
            elif seaside[i][j] == 'C':
                c = [i, j]
            elif seaside[i][j] == 'M':
                m = [i, j]
            elif seaside[i][j] == 'S':
                s = [i, j]

    def dist(a, b):
        return max(abs(a[0]-b[0]), abs(a[1]-b[1]))

    y_c = dist(y, c)
    y_s = dist(y, s)
    y_m = dist(y, m)

    return y_c + y_s + y_m

if __name__ == '__main__':
    print("Example:")
    print(navigation([['Y', 0, 0, 0, 'C'],
                      [ 0,  0, 0, 0,  0],
                      [ 0,  0, 0, 0,  0],
                      ['M', 0, 0, 0, 'S']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert navigation([['Y', 0, 0, 0, 'C'],
                       [ 0,  0, 0, 0,  0],
                       [ 0,  0, 0, 0,  0],
                       ['M', 0, 0, 0, 'S']]) == 11

    assert navigation([[ 0,  0, 'C'],
                       [ 0, 'S', 0],
                       ['M','Y', 0]]) == 4

    assert navigation([[ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'M', 0, 'S', 0],
                       [ 0,  0, 0,  0,  0,  0,  0],
                       [ 0,  0, 0, 'C', 0,  0,  0],
                       [ 0, 'Y',0,  0,  0,  0,  0],
                       [ 0,  0, 0,  0,  0,  0,  0]]) == 9
    print("Coding complete? Click 'Check' to earn cool rewards!")
