def long_repeat(line):
    if len(line) == 0:
        return len(line)
    elif len(line) == 1:
        return len(line)
    else:
        length = len(line)
        count = 1
        result = []
        for i in range(0, length - 1):
            if line[i+1] == line[i]:
                count += 1
                result.append(count)
            else:
                count = 1
        if len(result) == 0:
            return 1
        else:
            return max(result)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
