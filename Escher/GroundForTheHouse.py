def house(plan):

    x = plan.split()

    def cut_zero(x):
        for i in list(x):
            if '#' in i:
                break
            else:
                if i.count('0') == len(i):
                    x.remove(i)

        for i in reversed(list(x)):
            if '#' in i:
                break
            else:
                if i.count('0') == len(i):
                    x.remove(i)

    def rotation(arr):
        return list(zip(*arr[::-1]))

    cut_zero(x)
    rot = rotation(x)
    cut_zero(rot)

    if len(rot) != 0:
        width = len(rot)
        height = len(rot[0])

        result = width*height
    else:
        result = 0

    return result

if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
