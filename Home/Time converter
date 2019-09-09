def time_converter(time):
    text1 = time.split(':')
    if int(text1[0]) <= 24 and int(text1[1]) < 60:
        if int(text1[0]) >= 1 and int(text1[0]) < 12:
            if text1[0].startswith('0'):
                text1[0] = text1[0][1:]
            else:
                text1[0] = text1[0]
            time = ("%s:%s a.m." % (text1[0], text1[1]))
        elif text1[0] == '00':
            text1[0] = '12'
            time = ("%s:%s a.m." % (text1[0], text1[1]))
        elif int(text1[0]) > 12 and int(text1[0]) < 24:
            text1[0] = int(text1[0]) - 12
            time = ("%s:%s p.m." % (text1[0], text1[1]))
        elif text1[0] == '12':
            time = ("%s:%s p.m." % (text1[0], text1[1]))
        elif text1[0] == '24':
            text1[0] = '0'
            time = ("%s:%s p.m." % (text1[0], text1[1]))
        return time
    else:
        print('Error')


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
