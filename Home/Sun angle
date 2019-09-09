def sun_angle(time):
    hour = int(time[:2])
    minute = int(time[3:])
    second = (hour * 3600) + (minute * 60)
    if second >= 21600 and second <= 64800:
        hours = (hour - 6) * 15
        minutes = minute * 0.25
        result = hours+minutes
        return result
    else:
        result = "I don't see the sun!"
        return result

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
