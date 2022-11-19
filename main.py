import re
def solution(buildings):
    result = []

    for i in buildings:
        i = re.sub('[^nak]', '', i)
        nak_in_string = len(re.findall('nak', i))
        if nak_in_string == 2:
            result.append('O')
        else:
            result.append('X')
    return result
