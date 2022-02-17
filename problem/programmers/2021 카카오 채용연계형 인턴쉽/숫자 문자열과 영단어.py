def solution(s):
    info = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    for a, b in info.items():
        if a in s:
            s = s.replace(a, b)
    return int(s)
