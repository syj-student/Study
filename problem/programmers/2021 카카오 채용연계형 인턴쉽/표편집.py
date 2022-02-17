def solution(n, k, cmd):
    ogn = n
    ex = [i for i in range(n)]
    tmp = list()

    def move(loc, dx, sign):
        while dx:
            new_loc = loc + sign
            if 0 <= new_loc < len(ex):
                loc = new_loc
                dx -= 1
            elif new_loc < 0:
                return 0
            elif len(ex) <= new_loc:
                return n - 1
        return new_loc

    def delete(loc):
        new_loc = loc + 1
        tmp.append(ex.pop(loc))
        return new_loc if new_loc < len(ex) else 0

    def redo(loc):
        a = tmp.pop()
        ex.insert(a, a)
        return loc if loc < a else loc + 1

    for l in cmd:
        c = l[0]
        if c == "U":
            k = move(k, int(l[2]), 1)
        elif c == "D":
            k = move(k, int(l[2]), -1)
        elif c == "C":
            k = delete(k)
        else:
            k = redo(k)
        print(k, ex, tmp)
    answer = ''
    for x in range(ogn):
        answer += 'O' if x in ex else 'X'
    return answer


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
