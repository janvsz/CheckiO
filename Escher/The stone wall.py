def stone_wall(wall):

    def rotation(arr):
        return list(zip(*arr[::-1]))

    splitarr = wall.split()
    arr = rotation(splitarr)
    result = min(arr, key=lambda x: x.count('#'))
    return arr.index(result)

if __name__ == '__main__':
    print("Example:")
    print(stone_wall('''
##########
####0##0##
00##0###00
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert stone_wall('''
##########
####0##0##
00##0###00
''') == 4

    assert stone_wall('''
#00#######
#######0##
00######00
''') == 1

    assert stone_wall('''
#####
#####
#####
''') == 0

    print("Coding complete? Click 'Check' to earn cool rewards!")
