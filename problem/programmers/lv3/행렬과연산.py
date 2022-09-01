import collections

def solution(rc, operations):
    def ShiftRow():
        rc.rotate()
        side_left.rotate()
        side_right.rotate()
    
    def Rotate():
        rc[-1].append(side_right.pop())
        rc[0].appendleft(side_left.popleft())
        side_right.appendleft(rc[0].pop())
        side_left.append(rc[-1].popleft())
    
    rc = collections.deque(map(collections.deque, rc))
    side_left = collections.deque()
    side_right = collections.deque()
    for l in rc:
        side_left.append(l.popleft())
        side_right.append(l.pop())
    for c in operations:
        if c[0] == "R":
            Rotate()
        else:
            ShiftRow()

    for l in rc:
        l.appendleft(side_left.popleft())
        l.append(side_right.popleft())
    return list(map(list, rc))
    